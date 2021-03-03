class Color:

    def __init__(self, id, name, hexcode):
        self.id = id
        self.name = name
        self.hexcode = hexcode



class ColorsList:

    def __init__(self):

        self._colors = []

    @property
    def colors(self):
        return self._colors


    def add_color(self, name, hexcode):

        next_color_id = max( [ c.id for c in self._colors ] or [0] ) + 1

        new_color = Color(next_color_id, name, hexcode)

        self._colors.append(new_color)

    def remove_color_by_id(self, color_id):

        for color in self._colors:
            if color.id == color_id:
                self._colors.remove(color)
                break
