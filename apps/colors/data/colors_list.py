
print(__name__)


def add_color(colors, name, hexcode):

    next_color_id = max( [ c["id"] for c in colors ] or [0] ) + 1

    new_color = {
        "id": next_color_id,
        "name": name,
        "hexcode": hexcode,
    }

    colors.append(new_color)

def remove_color_by_id(colors, color_id):

    for color in colors:
        if color["id"] == color_id:
            colors.remove(color)
            break
