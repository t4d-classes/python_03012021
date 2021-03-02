def add_color(colors, name, hexcode):

    next_color_id = max( [ c[0] for c in colors ] or [0] ) + 1

    colors.append((next_color_id, name, hexcode))

def remove_color_by_id(colors, color_id):

    for color in colors:
        if color[0] == color_id:
            colors.remove(color)
            break
