from data.colors_list import ColorsList
from view.colors_table import color_table as color_grid

if __name__ == '__main__':

    colors_list = ColorsList()

    colors_list.add_color("red", "#ff0000")
    
    colors_list.add_color("green", "#00ff00")
    colors_list.add_color("blue", "#0000ff")

    print(color_grid(colors_list) + "\n")
    
    colors_list.remove_color_by_id(2)
    
    colors_list.add_color("purple", "#ff00ff")
    
    print(color_grid(colors_list))
