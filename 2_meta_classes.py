class ComponentValidator(type):
    def __new__(cls, name, bases, attrs):
        if 'defaultColor' not in attrs:
            if name != 'Component':
                raise TypeError(f"The {name} class must define a 'defaultColor' attribute")
        return super().__new__(cls, name, bases, attrs)

class Component(metaclass=ComponentValidator):
    def __init__(self, objectName: str):
        #print(f"Component __init__ for {objectName}")
        self.objectName = objectName

class BicycleWheel(Component):
    defaultColor = 'black'
    def __init__(self, objectName: str, radius: int):
        super().__init__(objectName=objectName)
        self.radius = radius

class BicycleSeat(Component):
    defaultColor = 'black'
    def __init__(self, objectName: str, color: str = None):
        super().__init__(objectName=objectName)
        self.color = color if color is not None else BicycleSeat.defaultColor
    
    def reset_to_default_color(self):
        self.color = BicycleSeat.defaultColor

    def get_info(self) -> str:
        # Maybe mention the default in documentation/info
        return f"Seat '{self.objectName}'. Color: {self.color} (Default is {BicycleSeat.defaultColor})"

wheel1 = BicycleWheel(objectName='w1', radius=27)

seat1 = BicycleSeat(objectName='Seat 1')
print(seat1.get_info())

seat2 = BicycleSeat(objectName='Seat 2', color='blue')
print(seat2.get_info())

seat3 = BicycleSeat(objectName='Seat 3', color='red')
print(seat3.get_info())
seat3.reset_to_default_color()
print(seat3.get_info())

BicycleSeat.defaultColor = 'cyan'
seat4 = BicycleSeat(objectName='Seat 4', color='red')
print(seat4.get_info())
seat3.reset_to_default_color()
print(seat4.get_info())
print(BicycleSeat.defaultColor)

class BicycleHandle(Component):
    # TypeError, DOES NOT HAVE a defaultColor attribute
    def __init__(self, objectName: str):
        super().__init__(objectName=objectName)

handle1 = BicycleHandle(objectName='handle 1')



