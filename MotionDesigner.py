from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QSlider
from PySide6.QtCore import Qt

from ui_MotionDesigner import Ui_MotionDesigner
import os
import json
import live2d.v3 as live2d

class MotionDesigner(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MotionDesigner()
        self.ui.setupUi(self)

        self.model: None | live2d.Model = None
        self.paramIds = []
        self.cdi: None | dict = None

        self.ui.live2DScene.initialized.connect(self.on_scene_initialized)

        self.ui.scaler.setRange(10, 50)
        self.ui.scaler.valueChanged.connect(lambda value: self.ui.curveEditor.setScale(value))

    def on_scene_initialized(self, model: live2d.Model):
        self.model = model
        self.paramIds = self.model.GetParameterIds()
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
            self.ui.paramTable.setItem(i, 0, QTableWidgetItem(p))
            self.ui.paramTable.setItem(i, 1, QTableWidgetItem(str(self.cdi['Parameters'][i]['Name'])))
            value_item = QTableWidgetItem("%.2f" % self.model.GetParameterDefaultValue(i))
            self.ui.paramTable.setItem(i, 2, value_item)
            value_slider = QSlider(Qt.Horizontal, self.ui.paramTable)
            self.ui.paramTable.setCellWidget(i, 3, value_slider)
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
        self.ui.live2DScene.changedParamValues.append((i, value))

        self.ui.paramTable.item(i, 2).setText("%.2f" % value)





if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    live2d.init()
    app = QApplication(sys.argv)
    window = MotionDesigner()
    window.show()
    sys.exit(app.exec())
    live2d.dispose()

        