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