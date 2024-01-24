class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
    
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ''
      for i in range(0,self.height):
         picture += '*' * self.width + '\n'
      return picture

  def get_amount_inside(self, shape):
    times = 0
    if (shape.width > self.width) or (shape.height > self.height):
      return times
    else: 
      times += 1
      return times + Rectangle(self.width - shape.width, shape.height).get_amount_inside(shape) +  Rectangle(shape.width, self.height - shape.height).get_amount_inside(shape) +  Rectangle(self.width - shape.width, self.height - shape.height).get_amount_inside(shape)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self,length):
    Rectangle.__init__(self, length, length)

  def set_side(self,length):
    Rectangle.set_width(self,length)
    Rectangle.set_height(self,length)

  def set_width(self,length):
    self.set_side(length)

  def set_height(self,length):
    self.set_side(length)

  def __str__(self):
    return f"Square(side={self.width})"
    
