from motion_interpolate import BezierSegment, Point
import matplotlib.pyplot as plt


segment = BezierSegment(
    Point(0, -30),
    Point(0.01, 20),
    Point(0.8, 0.5),
    Point(1, 30)
)

points = []
for i in range(100):
    points.append((i / 100, segment.interpolate(i / 100)))

plt.plot(*zip(*points))
plt.show()  