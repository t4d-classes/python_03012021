


html_color_names = {
    "AliceBlue": "#F0F8FF", # key-value pairs
    "AntiqueWhite": "#FAEBD7",
}
print(html_color_names)

html_color_names2 = dict(AliceBlue="#F0F8FF", AntiqueWhite="#FAEBD7")

print(html_color_names2)

html_color_names3 = dict([ ("AliceBlue", "#F0F8FF"), ("AntiqueWhite", "#FAEBD7")])

print(html_color_names3)

html_color_names4 = dict(zip(["AliceBlue", "AntiqueWhite"], ["#F0F8FF", "#FAEBD7"]))

print(html_color_names4)

html_color_names5 = dict.fromkeys(["AliceBlue", "AntiqueWhite"], "unknown color")

print(html_color_names5)

