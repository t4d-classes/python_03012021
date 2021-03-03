

html_color_names = {
    "AliceBlue": "#F0F8FF", # key-value pairs
    "AntiqueWhite": "#FAEBD7",
}

print(list(html_color_names.keys()))

print("AliceBlue" in html_color_names)
print("RebeccaPurple" not in html_color_names)

print(3 in [1,2,3])
print(3 in (1,2,3))

# print(html_color_names["RebeccaPurple"])
print(html_color_names.get("RebeccaPurple", "some default"))
# print(html_color_names.get("AliceBlue"))

html_color_names["Aaqua"] = "#00FFFF"
print(html_color_names["Aaqua"])

# del html_color_names["Aqua"]

print(list(html_color_names.keys()))
