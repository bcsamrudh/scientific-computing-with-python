import math
class Rectangle:

  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __repr__(self):
    repr = f"Rectangle(width={self.width}, height={self.height})"
    return repr

  def set_width(self,width):
    self.width=width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return (self.width)*(self.height)

  def get_perimeter(self):
    return 2*(self.width+self.height)

  def get_diagonal(self):
    diagonal = (self.width)**2 + (self.height)**2
    return diagonal**0.5

  def get_picture(self):
    picture=""
    if self.width >50 or self.height >50:
      return "Too big for picture."
    for i in range(self.height):
      for j in range(self.width):
        picture+="*"
      picture+="\n"
    return picture

  def get_amount_inside(self,shape):
    rect_area = Rectangle.get_area(self)
    shape_area = Rectangle.get_area(shape)
    return round(math.floor(rect_area/shape_area))
    
class Square(Rectangle):

  def __init__(self,side):
    self.width = side
    self.height = side

  def __repr__(self):
     repr = f"Square(side={self.width})"
     return repr

  def set_side(self,side):
    self.width= side
    self.height = side