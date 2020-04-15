class Cylinder(object):
    
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14
        pass

    def volume(self):
        return self.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return (2 * self.radius ** 2 * self.pi) + (2 * self.pi * self.radius * self.height)

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())