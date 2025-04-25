from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui_MainWindow import Ui_MainWindow
from MotionDesigner import MotionDesigner
import os


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNew.triggered.connect(self._on_new_action_triggered)
        self.ui.actionSave.triggered.connect(self._on_save_action_triggered)

        self.ui.tabs.tabCloseRequested.connect(self.ui.tabs.removeTab)
    def _on_new_action_triggered(self):
        model_path = QFileDialog.getOpenFileName(self, "打开模型", "", "Live2D 模型 (*.model3.json)")[0]
        if model_path:
            motion_designer = MotionDesigner(model_path)
            self.ui.tabs.addTab(motion_designer, os.path.split(os.path.dirname(model_path))[-1])
            self.ui.tabs.setCurrentIndex(self.ui.tabs.count() - 1)

    def _on_save_action_triggered(self):
        designer = self.ui.tabs.currentWidget()
        name = self.ui.tabs.tabText(self.ui.tabs.currentIndex())
        designer.export_motion(f"{name}.motion3.json")
