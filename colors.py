
colors = []

colors.append((1, "red", "#ff0000"))
colors.append((2, "green", "#00ff00"))
colors.append((3, "blue", "#0000ff"))

print("Id     Name     Hexcode")
print("-----------------------")

if len(colors) < 1:
    print("There are no colors")
else:
    for id, name, hexcode in colors:
        print(f"{str(id).rjust(2)} {name.ljust(12)} {hexcode}")

color_id = 2

# color_index = 0
# not_found = True

# while not_found and color_index < len(colors):
    
#     if colors[color_index][0] == color_id:
#         colors.remove(colors[color_index])
#         not_found = False

#     color_index = color_index + 1

for color in colors:
    if color[0] == color_id:
        colors.remove(color)
        break


print(colors)


# print(color)
# print(color[0]) # id
# print(color[1]) # name

# color_id, color_name, color_hexcode = color

# print(color_id)
# print(color_data)
# print(color_hexcode)