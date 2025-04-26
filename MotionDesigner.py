from PySide6.QtWidgets import QWidget, QTableWidgetItem, QSlider, QCheckBox, QListWidgetItem, QHeaderView, QFileDialog
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon

from ui_MotionDesigner import Ui_MotionDesigner
import os
import json
import live2d.v3 as live2d
from motion_interpolate import Curve, get_segment_type


class MotionDesigner(QWidget):

    def __init__(self, model_path=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_MotionDesigner()
        self.ui.setupUi(self)

        self.ui.splitter.setStretchFactor(0, 1)
        # self.ui.splitter.setStretchFactor(1, 1)

        self.model_path = model_path

        self.ui.live2DScene.setModelPath(model_path)

        self.model: None | live2d.Model = None
        self.paramIds = []
        self.paramCurves = []
        self.cdi: None | dict = None

        self.currentParamIndex = -1

        self.ui.live2DScene.initialized.connect(self._on_scene_initialized)

        self.ui.scaler.setRange(1, 50)
        self.ui.scaler.setValue(30)
        self.ui.scaler.valueChanged.connect(self.ui.curveEditor.setScale)

        self.ui.curveTypeSelector.setCurrentIndex(1)
        self.ui.curveTypeSelector.currentIndexChanged.connect(self.ui.curveEditor.setSegmentType)

        self.ui.curveEditor.segTypeChanged.connect(self.ui.curveTypeSelector.setCurrentIndex)

        self.ui.frameCount.valueChanged.connect(self.ui.curveEditor.setDuration)

        self.ui.motionParamList.itemClicked.connect(self._on_param_curve_changed)

        self.ui.curveEditor.curveValueChanged.connect(self._on_curve_value_changed)

        self.ui.nextFrameBtn.clicked.connect(self.ui.curveEditor.moveToNextFrame)
        self.ui.preFrameBtn.clicked.connect(self.ui.curveEditor.moveToPrevFrame)
        self.ui.firstFrameBtn.clicked.connect(self.ui.curveEditor.moveToFirstFrame)
        self.ui.lastFrameBtn.clicked.connect(self.ui.curveEditor.moveToLastFrame)

        self.ui.curveEditor.setEnabled(False)
        self.playTimer = QTimer(self)
        self.playTimer.setInterval(1000 // self.ui.curveEditor.fps)
        self.playTimer.setSingleShot(True)
        self.playTimer.timeout.connect(self._on_play_timer_timeout)
        self.ui.playBtn.clicked.connect(self._on_play_btn_clicked)

        self.ui.fpsSpinBox.valueChanged.connect(self._on_fps_spin_box_value_changed)

        self.ui.paramTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.paramTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.paramTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

        self.ui.mixPlayCheckBox.checkStateChanged.connect(lambda v: self.ui.curveEditor.setNoInterpolate(v == Qt.CheckState.Checked))
    

    def _on_fps_spin_box_value_changed(self, value):
        self.ui.curveEditor.setFps(value)
        self.playTimer.setInterval(1000 // value)

    def _on_scene_initialized(self, model: live2d.Model):
        self.model = model
        self.paramIds = self.model.GetParameterIds()
        self.ui.live2DScene.paramValues = [self.model.GetParameterDefaultValue(i) for i in range(len(self.paramIds))]
        self.paramCurves = [Curve.create(p, []) for p in self.paramIds]
        self._load_cdi()
        self._init_param_table()

    def _load_cdi(self):
        files = os.listdir(self.model.GetModelHomeDir())
        for f in files:
            if f.endswith(".cdi3.json"):
                with open(os.path.join(self.model.GetModelHomeDir(), f), 'r', encoding='utf-8') as fp:
                    self.cdi = json.load(fp)
                    return
                
    def _init_param_table(self):
        self.ui.paramTable.setRowCount(len(self.paramIds))
        for i, p in enumerate(self.paramIds):
            check_box = QCheckBox()
            self.ui.paramTable.setCellWidget(i, 0, check_box)
            check_box.checkStateChanged.connect(lambda state, i=i: self._on_param_check_box_state_changed(state, i))
        
            self.ui.paramTable.setItem(i, 1, QTableWidgetItem(p))
            self.ui.paramTable.setItem(i, 2, QTableWidgetItem(str(self.cdi['Parameters'][i]['Name'])))
            value_item = QTableWidgetItem("%.2f" % self.model.GetParameterDefaultValue(i))
            self.ui.paramTable.setItem(i, 3, value_item)
            value_slider = QSlider(Qt.Horizontal, self.ui.paramTable)
            self.ui.paramTable.setCellWidget(i, 4, value_slider)
            value_slider.setFixedWidth(100)
            value_slider.setRange(0, 100)
            minValue = self.model.GetParameterMinimumValue(i)
            maxValue = self.model.GetParameterMaximumValue(i)
            value = self.model.GetParameterValue(i)
            value_slider.setValue(int((value - minValue) / (maxValue - minValue) * 100.0))
            value_slider.valueChanged.connect(lambda value, i=i: self._on_value_slider_changed(value, i ))

    def _on_value_slider_changed(self, value, i):
        min_value = self.model.GetParameterMinimumValue(i)
        max_value = self.model.GetParameterMaximumValue(i)
        value = min_value + (max_value - min_value) * value / 100.0
        self.ui.live2DScene.paramValues[i] = value

        self.ui.paramTable.item(i, 3).setText("%.2f" % value)


    def _on_param_check_box_state_changed(self, state, i):
        if state == Qt.Checked:
            item = QListWidgetItem(self.paramIds[i])
            item.setData(Qt.ItemDataRole.UserRole, self.paramCurves[i])
            item.setData(Qt.ItemDataRole.UserRole + 1, i)
            self.ui.motionParamList.addItem(item)
        else:
            for item in self.ui.motionParamList.findItems(self.paramIds[i], Qt.MatchExactly): 
                self.ui.motionParamList.takeItem(self.ui.motionParamList.row(item))


    def _on_param_curve_changed(self, item: QListWidgetItem):
        if item is None:
            self.ui.curveEditor.setEnabled(False)
            self.ui.curveEditor.setTarget("", [], -30, 30)
            self.ui.currentTargetLabel.setText("目标未选择")
            self.currentParamIndex = -1
            return

        self.ui.curveEditor.setEnabled(True)
        curve: Curve = item.data(Qt.ItemDataRole.UserRole)
        index = item.data(Qt.ItemDataRole.UserRole + 1)
        self.currentParamIndex = index
        self.ui.currentTargetLabel.setText(curve.paramId)
        self.ui.curveEditor.setTarget(curve.paramId, 
                                      curve.segments, 
                                      self.model.GetParameterMaximumValue(index), 
                                      self.model.GetParameterMinimumValue(index))

    def _on_curve_value_changed(self, num_frames, value, valid):
        if self.ui.mixPlayCheckBox.isChecked():
            self._update_all_used_params()
        else:
            if self.currentParamIndex != -1 and valid:
                self.ui.live2DScene.paramValues[self.currentParamIndex] = value

        fps = self.ui.curveEditor.fps
        secs = num_frames // fps
        minutes = (num_frames - secs * fps) // fps * fps
        frames = num_frames % fps 
        self.ui.currentTLabel.setText("%02d:%02d:%02d" % (minutes, secs, frames))

    def _update_all_used_params(self):
        t = self.ui.curveEditor.getT()
        size = self.ui.motionParamList.count()
        for i in range(size):
            item = self.ui.motionParamList.item(i)
            curve: Curve = item.data(Qt.ItemDataRole.UserRole)
            index = item.data(Qt.ItemDataRole.UserRole + 1)
            v = curve.interpolate(t)
            if v is not None:
                pct = self.ui.curveEditor.percentOfY(v)
                maxValue = self.model.GetParameterMaximumValue(index)
                minValue = self.model.GetParameterMinimumValue(index)
                v = pct * (maxValue - minValue) + minValue
                self.ui.live2DScene.paramValues[index] = v
                # print("update param %s to %.2f" % (curve.paramId, v))

    def _on_play_btn_clicked(self):
        if not self.ui.playBtn.isChecked():
            self.playTimer.stop()
            self.ui.playBtn.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        else:
            if self.ui.curveEditor.isEndReached():
                self.ui.curveEditor.moveToFirstFrame()
            self.ui.playBtn.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
            self.playTimer.start()

    def _on_play_timer_timeout(self):
        if self.ui.curveEditor.isEndReached():
            self.playTimer.stop()
            self.ui.playBtn.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
            self.ui.playBtn.setChecked(False)
        else:
            self.ui.curveEditor.moveToNextFrame()
            self.playTimer.start()

    def export_motion(self, save_path):
        filePath, _ = QFileDialog.getSaveFileName(self, "导出动画", save_path, "Live2D 动画 (*.motion3.json)")
        if filePath == "":
            return
        
        curve_count = 0
        fps = self.ui.curveEditor.fps
        duration = self.ui.curveEditor.duration / fps
        segment_count = 0
        point_count = 0
        curves = []
        map_t = lambda x: self.ui.curveEditor.getNumFrames(x) / fps
        
        for i in range(self.ui.motionParamList.count()):
            c = self.ui.motionParamList.item(i).data(Qt.ItemDataRole.UserRole)
            sc = len(c.segments)
            if sc == 0:
                continue
            curve_count += 1
            segment_count += sc
            point_count += 1
            for s in c.segments:
                if get_segment_type(s) == 1:
                    point_count += 3
                else:
                    point_count += 1
            idx = self.ui.motionParamList.item(i).data(Qt.ItemDataRole.UserRole + 1)
            minValue = self.model.GetParameterMinimumValue(idx)
            maxValue = self.model.GetParameterMaximumValue(idx)
            map_value = lambda y, maxValue=maxValue, minValue=minValue: self.ui.curveEditor.percentOfY(y) * (maxValue - minValue) + minValue
            curves.append(c.to_json(map_t, map_value))

        data = {
            "Version": 3,
            "Meta": {
                "Duration": duration,
                "Fps": fps,
                "FadeInTime": 0.5,
                "FadeOutTime": 1.0,
                "Loop": True,
                "AreBeziersRestricted": True,
                "CurveCount": curve_count,
                "TotalSegmentCount": segment_count,
                "TotalPointCount": point_count,
                "UserDataCount": 0,
                "TotalUserDataSize": 0
            },
            "Curves": curves
        }

        with open(filePath, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    live2d.init()
    app = QApplication(sys.argv)
    window = MotionDesigner()
    window.show()
    sys.exit(app.exec())
    live2d.dispose()

        