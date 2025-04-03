class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class BicycleWheel:
    def __init__(self, name: str, center: Point, radius: int):
        self.name = name
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        center = self.center
        return f"Center: {self.center}. Radius: {self.radius}"

    def isAlignedWith(self, other):
        if self.center.y == other.center.y:
            return True
        else:
            return False

point1 = Point(3, 2)
point2 = Point(5, 2)
w1 = BicycleWheel(name='w1', center=point1, radius=27)
w2 = BicycleWheel(name='w2', center=point2, radius=27)

print(f"wheel w1. {repr(w1)}")

if w1.isAlignedWith(w2):
    print(f'Wheels {w1} and {w2} are aligned. Their vertical center is {w1.center.y}')