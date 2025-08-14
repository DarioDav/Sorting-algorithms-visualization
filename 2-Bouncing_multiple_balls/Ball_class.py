class Circle():
      def __init__(self, x, y, radius, color=(0, 0, 0), x_velocity= 10, y_velocity = 10):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.x_velocity = x_velocity
            self.y_velocity = y_velocity
      
      def move(self, WIDTH, HEIGHT):
        self.x += self.x_velocity
        self.y += self.y_velocity

        # Bounce on edges
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.x_velocity *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.y_velocity *= -1
      