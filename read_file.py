
# with open("colors.txt", "r") as colors_file:

#     colors_file.seek(30)

#     colors_data = colors_file.read(30)

# print(colors_data)


# start_line = 3
# stop_line = 6

# with open("colors.txt", "r") as colors_file:

#     lines = []

#     for line_count, color in enumerate(colors_file):
#         if line_count >= start_line and line_count < stop_line:
#             lines.append(color.strip())
#         if line_count >= stop_line:
#             break

# print(lines)

with open("colors.txt", "r") as colors_file:
    lines = colors_file.readlines()

print(lines)
