# 实现读取动作并播放

from abc import ABC, abstractmethod

class Point:

    def __init__(self, t: float, value: float):
        self.t = t
        self.value = value

    def __repr__(self):
        return f"Point({self.t}, {self.value})"


class Segment(ABC):

    @abstractmethod
    def interpolate(self, t: float) -> float: pass

    @abstractmethod
    def contains(self, t: float) -> bool: pass


class LinearSegment(Segment):

    def __init__(self, p0: Point, p1: Point):
        self.p0 = p0
        self.p1 = p1

    def contains(self, t: float) -> bool:
        return self.p0.t < t <= self.p1.t

    def interpolate(self, t: float) -> float:
        return self.p0.value + (self.p1.value - self.p0.value) * (t - self.p0.t) / (self.p1.t - self.p0.t)
    
    def __repr__(self) -> str:
        return f"LinearSegment({self.p0}, {self.p1})"


class BezierSegment(Segment):

    def __init__(self, p0: Point, p1: Point, p2: Point, p3: Point):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def contains(self, t: float) -> bool:
        return self.p0.t< t <= self.p3.t
    
    def interpolate(self, t):
        tt = (t - self.p0.t) / (self.p3.t - self.p0.t)
        return (1 - tt) ** 3 * self.p0.value + \
                3 * (1 - tt) ** 2 * tt * self.p1.value + \
                3 * (1 - tt) * tt ** 2 * self.p2.value + \
                tt ** 3 * self.p3.value
    
    def __repr__(self) -> str:
        return f"BezierSegment(p0={self.p0}, p1={self.p1}, p2={self.p2}, p3={self.p3})"
    

class SteppedSegment(Segment):

    def __init__(self, p0: Point, p1: Point):
        self.p0 = p0
        self.p1 = p1
    
    def contains(self, t):
        return self.p0.t < t <= self.p1.t
    
    def interpolate(self, t):
        return self.p0.value if t < self.p0.t else self.p1.value
    
    def __repr__(self):
        return f"SteppedSegment(p0={self.p0}, p1={self.p1})"


class InverseSteppedSegment(Segment):

    def __init__(self, p0: Point, p1: Point):
        self.p0 = p0
        self.p1 = p1
    
    def contains(self, t):
        return self.p0.t < t <= self.p1.t
    
    def interpolate(self, t):
        return self.p1.value
    
    def __repr__(self):
        return f"InverseSteppedSegment(p0={self.p0}, p1={self.p1})"
    

class Curve:

    def __init__(self, paramId: str):
        self.paramId = paramId
        self.duration = 0
        self.segments = []
    
    def __repr__(self):
        return f"Curve(paramId={self.paramId}, duration={self.duration}, segments={self.segments})"
    
    def interpolate(self, t: float) -> float | None:
        for segment in self.segments:
            if segment.contains(t):
                return segment.interpolate(t)
            
        return None

    @staticmethod
    def create(paramId: str, segments: list[float]) -> 'Curve':
        curve = Curve(paramId)
        idx = 2
        size = len(segments)
        last_point = segments[0:2]

        while idx < size:
            identifier = segments[idx]
            
            if identifier == 0:
                segment = segments[idx+1:idx+3]
                seg = LinearSegment(
                    Point(last_point[0], last_point[1]),
                    Point(segment[0], segment[1])
                )
                idx += 3
            elif identifier == 1:
                segment = segments[idx+1:idx+7]
                seg = BezierSegment(
                    Point(last_point[0], last_point[1]),
                    Point(segment[0], segment[1]),
                    Point(segment[2], segment[3]),
                    Point(segment[4], segment[5])
                )
                idx += 7
            elif identifier == 2:
                segment = segments[idx+1:idx+3]
                seg = SteppedSegment(
                    Point(last_point[0], last_point[1]),
                    Point(segment[0], segment[1])
                )
                idx += 3
            elif identifier == 3:
                segment = segments[idx+1:idx+3]
                seg = InverseSteppedSegment(
                    Point(last_point[0], last_point[1]),
                    Point(segment[0], segment[1])
                )
                idx += 3
            else:
                raise Exception("Invalid identifier")
            last_point = segments[idx-2:idx]

            curve.segments.append(seg)

        curve.duration = last_point[0]
        return curve

if __name__ == "__main__":
    import json
    motion = json.load(open("Mao/motions/"
                            # "mtn_01.motion3.json"
                            "special_01.motion3.json"
                             ))
    import matplotlib.pyplot as plt
    curves: list[Curve] = []
    for curve in motion["Curves"]:
        curve = Curve.create(curve["Id"], curve["Segments"])
        # print(curve)
        
        curves.append(curve)
        # plt.title(curve.paramId)
        # plt.plot([x[0] for x in points], [x[1] for x in points])
        # plt.show()
        # break
    
    import live2d.v3 as live2d
    import pygame
    import time

    pygame.init()
    live2d.init()

    pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
    live2d.glInit()
    model = live2d.LAppModel()
    model.LoadModelJson("Mao/Mao.model3.json")
    model.Resize(800, 600)

    started = False
    lastCt = time.time()
    timeEplased = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                del model
                live2d.dispose()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True
                    timeEplased = 0

        ct = time.time()
        delta = ct - lastCt
        lastCt = ct

        live2d.clearBuffer()
        model.Update()
        if started:

            timeEplased += delta
            c = None
            for c in curves:
                v = c.interpolate(timeEplased)
                if v is None:
                    break

                model.SetParameterValue(c.paramId, v)

            if timeEplased >= c.duration:
                started = False
                timeEplased = 0

        model.Draw()

        pygame.display.flip()
