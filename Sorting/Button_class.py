import pygame

class Button:
    """
    A class to create interactive buttons in Pygame.

    Attributes:
        text (str): The text displayed on the button.
        x (int): The x-coordinate of the top-left corner of the button.
        y (int): The y-coordinate of the top-left corner of the button.
        width (int): The width of the button.
        height (int): The height of the button.
        color (tuple): The default background color of the button (RGB).
        hover_color (tuple): The background color when the mouse hovers over the button (RGB).
        text_color (tuple): The color of the text on the button (RGB).
        font_size (int): The size of the font for the button text.
        font (pygame.font.Font): The Pygame font object used for the text.
        rect (pygame.Rect): The Pygame Rect object representing the button's clickable area.
    """

    def __init__(self, text, x, y, width, height, color, hover_color, text_color="Black", font_size=30):
        """
        Initializes a new Button object.

        Args:
            text (str): The text to display on the button.
            x (int): The x-coordinate of the top-left corner.
            y (int): The y-coordinate of the top-left corner.
            width (int): The width of the button.
            height (int): The height of the button.
            color (tuple): The default background color (RGB).
            hover_color (tuple): The background color on hover (RGB).
            text_color (tuple, optional): The color of the text (RGB). Defaults to BLACK.
            font_size (int, optional): The size of the font. Defaults to 30.
        """
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)  # Default font, specify path for custom fonts
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        """
        Draws the button on the given Pygame surface.

        The button's color changes when the mouse hovers over it.

        Args:
            surface (pygame.Surface): The Pygame surface to draw the button on (e.g., the screen).
        """
        # Check if mouse is hovering over the button
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        # Draw the button rectangle
        pygame.draw.rect(surface, current_color, self.rect, border_radius=10) # Added border_radius for rounded corners

        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)
        # Center the text on the button
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        """
        Checks if the button was clicked.

        Args:
            event (pygame.event.Event): A Pygame event object.

        Returns:
            bool: True if the button was clicked, False otherwise.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    return True
        return False