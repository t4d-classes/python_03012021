
# try:

#     f = open("data.txt", "w")

#     f.write("some text")

# except:

#     print("handle exception")

# finally:

#     if f:
#         f.close()

cart = [
    ('apples', 1.34, 4),
    ('oranges', 1.19, 10),
    ('pomengranite', 0.99, 2),
]

with open("data.txt", "w") as data_file:
    for item in cart:
        item_data_str = [ str(t) for t in item ]
        item_data = ",".join(item_data_str)
        data_file.write(item_data + '\n')



def cart_item(raw_data):
    cart_item_parts = data.strip().split(",")
    return (
        cart_item_parts[0],
        float(cart_item_parts[1]),
        int(cart_item_parts[2])
    )


new_cart = []

with open("data.txt", "r") as data_file:
    for data in data_file:
        new_cart.append(cart_item(data))

print(new_cart)