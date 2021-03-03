def color_table(colors):

    table = []

    table.append("Id     Name     Hexcode")
    table.append("-----------------------")

    if len(colors) < 1:
        table.append("There are no colors")
    else:
        for color in colors:
            table.append(f"{str(color['id']).rjust(2)} {color['name'].ljust(12)} {color['hexcode']}")

    return "\n".join(table)