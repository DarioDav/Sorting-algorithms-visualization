class Circle():
      def __init__(self, x, y, radius, color=(0, 0, 0)):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
      
      def get_center(self):
            return (self.x, self.y)
      
      def get_radius(self):
            return self.radius
      
      def set_center(self, x, y):
            self.x = x
            self.y = y
      
      def set_radius(self, radius):
            self.radius = radius
      def get_color(self):
            return self.color
      