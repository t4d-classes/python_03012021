from data.colors_list import add_color, remove_color_by_id
from view.colors_table import color_table as color_grid

if __name__ == '__main__':

    colors = []

    add_color(colors, "red", "#ff0000")
    add_color(colors, "green", "#00ff00")
    add_color(colors, "blue", "#0000ff")

    print(color_grid(colors) + "\n")
    remove_color_by_id(colors, 2)
    add_color(colors, "purple", "#ff00ff")
    print(color_grid(colors))
