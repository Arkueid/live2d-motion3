import live2d.v3 as live2d
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtGui import QOpenGLFunctions
from PySide6.QtCore import Signal
import time

class Live2DScene(QOpenGLWidget):
    initialized = Signal(live2d.Model)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = live2d.Model()
        self.model.LoadModelJson("Mao/Mao.model3.json")
        self.lastCt = -1

        self.changedParamValues = []
    
    def initializeGL(self):
        live2d.glInit()
        self.model.CreateRenderer(2)

        self.lastCt = time.time()
        self.initialized.emit(self.model)
        self.startTimer(int(1000 / 60))
    
    def resizeGL(self, w, h):
        self.model.Resize(w, h)
    
    def paintGL(self):
        live2d.clearBuffer()
        ct = time.time()
        delta = ct - self.lastCt
        self.lastCt = ct

        self.model.LoadParameters(delta)
        for i, v in self.changedParamValues:
            self.model.SetParameterValue(i, v)
        
        self.changedParamValues.clear()
        self.model.SaveParameters()
        self.model.UpdateDrag(delta)
        self.model.UpdateExpression(delta)
        self.model.UpdatePhysics(delta)
        self.model.UpdatePose(delta)
        self.model.Draw()
    
    def timerEvent(self, event):
        self.update()
    


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    live2d.init()
    app = QApplication(sys.argv)
    scene = Live2DScene()
    scene.show()
    sys.exit(app.exec())