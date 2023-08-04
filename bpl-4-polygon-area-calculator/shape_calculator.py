class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    
    for dimension in [self.height, self.width]:
      if dimension > 50:
        return 'Too big for picture.'
        
    result = ''
    for y in range(self.height):
      for x in range(self.width):
        result += '*'
      result += '\n'
    return result

  def get_amount_inside(self, other):
    x_fits = self.width // other.width
    y_fits = self.height // other.height
    return x_fits * y_fits
    

class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f'Square(side={self.height})'
  
  def set_side(self, side):
    super().set_height(side)
    super().set_width(side)

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height
