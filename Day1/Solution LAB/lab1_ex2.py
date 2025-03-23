# rectangle class
class Rectangle:

  def __init__(self, height, width):
    self.height = height
    self.width = width

  def calculate_perimeter(self):
    return (self.height + self.width)*2
    
  def calculate_area(self):
    return self.height * self.width


# circle class
class Circle:

  PI = 3.14

  def __init__(self, radius):
    self.radius = radius

  def calculate_perimeter(self):
    return 2 * self.PI * self.radius
    
  def calculate_area(self):
    return self.PI * self.radius**2


# drive code
# get shape
print('Shape (rectangle|circle): ', end='')
shape_name = input()

# get corresponding shape sizes
shape = None
if shape_name == 'rectangle':
  print('Height: ', end='')
  height = float(input())
  print('Width: ', end='')
  width = float(input())
  shape = Rectangle(height, width)
elif shape_name == 'circle':
  print('Radius: ', end='')
  radius = float(input())
  shape = Circle(radius)
else:
  print('\n=> Invalid!')

# output perimeter & area
if shape != None:
  print()
  print('=> Perimeter:', shape.calculate_perimeter())
  print('=> Area:', shape.calculate_area())