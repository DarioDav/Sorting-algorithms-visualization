import pygame
import sys

import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Button Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLUE = (0, 128, 255)
LIGHT_BLUE = (100, 180, 255)

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

    def __init__(self, text, x, y, width, height, color, hover_color, text_color=BLACK, font_size=30):
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

# --- Example Usage ---
def main():
    running = True
    clock = pygame.time.Clock()

    # Create buttons
    button1 = Button("Start Simulation", 50, 50, 200, 60, BLUE, LIGHT_BLUE, WHITE)
    button2 = Button("Reset", 50, 130, 200, 60, GRAY, DARK_GRAY, BLACK)
    button3 = Button("Exit", 50, 210, 200, 60, (200, 50, 50), (255, 100, 100), WHITE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for button clicks
            if button1.is_clicked(event):
                print("Start Simulation button clicked!")
                # Add your simulation start logic here
            if button2.is_clicked(event):
                print("Reset button clicked!")
                # Add your reset logic here
            if button3.is_clicked(event):
                print("Exit button clicked!")
                running = False # Exit the game when Exit button is clicked

        # Fill the background
        screen.fill(WHITE)

        # Draw all buttons
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

