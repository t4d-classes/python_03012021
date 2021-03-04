from random import randint

# letters = [ chr(code) for code in range(65,75) ]

# print(letters)
# print(letters[2])

# print(letters[2:])
# print(letters[2:5])

# print(letters[1:5:3])

# html_element = "<b>Hi!</b>"

# print(html_element[3: -4])

class NameElement:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.id}:{self.name}"

def get_rand_name():
    return "".join([ chr(randint(65, 86)) for _ in range(4) ])

names = [ NameElement(randint(1, 100), get_rand_name()) for _ in range(1000) ]

print(names)

# names.sort(key=lambda n: n.name)

sorted_names = sorted(names, key=lambda n: n.name)

print(names[:10])
print(sorted_names[:10])
