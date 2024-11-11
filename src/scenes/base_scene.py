"""
Parent class for all game screens (e.g. main menu, game screen, game over screen...).
"""


class BaseScene:
    def __init__(self):
        """Initialize screen resources."""
        pass

    def __str__(self):
        return self.__class__.__name__

    def tick(self):
        """
        Core update logic for the screen.
        This method is called in the main game loop to update game objects.
        Logic only, the drawing should be done in the 'draw' method.
        Override in subclasses.
        """
        raise NotImplementedError(
            "The 'tick' method must be implemented in subclasses."
        )

    def draw(self, screen):
        """
        Render visuals for the screen.
        Rendering only, the logic should be done in the 'tick' method.
        Override in subclasses to draw all necessary elements to the screen.

        :param screen: The pygame display surface to render on.
        """
        raise NotImplementedError(
            "The 'draw' method must be implemented in subclasses."
        )

    def destroy(self):
        """Hook to stop and clean up the screen resources."""
        pass
