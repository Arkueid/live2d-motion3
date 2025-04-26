import live2d.v3 as live2d
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Signal
import time

class Live2DScene(QOpenGLWidget):
    initialized = Signal(live2d.Model)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = live2d.Model()
        self.model_path = None
        self.lastCt = -1
        self.paramValues = []

    def setModelPath(self, model_path):
        self.model_path = model_path
    
    def initializeGL(self):
        live2d.glInit()
        if self.model_path:
            self.model.LoadModelJson(self.model_path)
        else:
            self.model.LoadModelJson("Mao/Mao.model3.json")
            
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
        for i, v in enumerate(self.paramValues):
            self.model.SetParameterValue(i, v)
        
        self.model.SaveParameters()
        self.model.UpdateDrag(delta)
        self.model.UpdateExpression(delta)
        self.model.UpdatePhysics(delta)

        # 防止参数被物理计算重置
        for i, v in enumerate(self.paramValues):
            self.model.SetParameterValue(i, v)

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