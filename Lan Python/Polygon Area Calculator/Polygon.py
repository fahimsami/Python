import math

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
     
    def set_width(self, value):
        self._width = value
        return self._width
    
    def set_height(self, value):
        self._height = value
        return self._height
     
    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return 2 * (self._width + self._height)
    
    def get_diagonal(self):
        return math.sqrt(self._width ** 2 + self._height ** 2)
    
    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture.."
        picture = ""
        for _ in range(self._height):
            picture += "*" * self._width + "\n"
        return picture

    def get_amount_inside(self, value):
        inner_width = getattr(value, '_width', None)
        inner_height = getattr(value, '_height', None)
        if inner_width is None or inner_height is None:
            raise AttributeError("Passed shape must have '_width' and '_height'")

        fits_across = self._width // inner_width
        fits_down = self._height // inner_height
        return fits_across * fits_down
    
    def __str__(self):
        return f"Rectangle ( Width = {self._width}, Height = {self._height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, value):
        self._width = value
        self._height = value
        return self._width

    def set_height(self, value):
        self._width = value
        self._height = value
        return self._height

    def set_side(self, value):
        self._width = value
        self._height = value
        return self._width

    def get_picture(self):
        return super().get_picture()
        
    def get_amount_inside(self, value):
        return super().get_amount_inside(value)
        
    def __str__(self):
        return f"Square (side = {self._width})"


if __name__ == '__main__':        
        rect = Rectangle(10, 5)
        print(rect.get_area())
        rect.set_height(3)
        print(rect.get_perimeter())
        print(rect)
        print(rect.get_picture())
       
        sq = Square(9)
        print(sq.get_area())
        sq.set_side(4)
        print(sq.get_diagonal())
        print(sq)
        print(sq.get_picture())   

        rect.set_height(8)
        rect.set_width(16)
        print(rect.get_amount_inside(sq))     
        