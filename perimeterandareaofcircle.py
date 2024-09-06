class circle:
    def __init__(self, radius):
        self.radius = radius
        area = 3.14 * radius * radius
        perimeter = 2 * 3.14 * radius
        print(area,"sq. cm")
        print(perimeter, "cm")
    
radius = int(input("Enter the radius of the circle: "))
obj = circle(radius)