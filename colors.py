def add_color(colors, name, hexcode):

    next_color_id = max( [ c[0] for c in colors ] or [0] ) + 1

    colors.append((next_color_id, name, hexcode))

def remove_color_by_id(colors, color_id):

    for color in colors:
        if color[0] == color_id:
            colors.remove(color)
            break

def color_table(colors):

    table = []

    table.append("Id     Name     Hexcode")
    table.append("-----------------------")

    if len(colors) < 1:
        table.append("There are no colors")
    else:
        for id, name, hexcode in colors:
            table.append(f"{str(id).rjust(2)} {name.ljust(12)} {hexcode}")

    return "\n".join(table)


colors = []

add_color(colors, "red", "#ff0000")
add_color(colors, "green", "#00ff00")
add_color(colors, "blue", "#0000ff")

print(color_table(colors) + "\n")
remove_color_by_id(colors, 2)
add_color(colors, "purple", "#ff00ff")
print(color_table(colors))
