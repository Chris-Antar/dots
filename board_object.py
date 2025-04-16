class BoardObject:
    def __init__(self, shape: list, color: tuple):
        self._shape = shape
        self._color = color

    # Getter for shape
    @property
    def shape(self) -> list:
        return self._shape

    # Setter for shape
    @shape.setter
    def shape(self, value: list):
        self._shape = value

    # Getter for color
    @property
    def color(self) -> tuple:
        return self._color

    # Setter for color
    @color.setter
    def color(self, value: tuple):
        self._color = value

    
    