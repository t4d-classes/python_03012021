result = 0

command = input("Please enter a command: ")

while command:

    if command == "clear":
        result = 0
        print(f"Result: {result}")
        command = input("Please enter a command: ")
        continue

    num = float(input("Please enter an operand: "))

    if command == "add":
        result = result + num
    elif command == "subtract":
        result = result - num
    elif command == "multiply":
        result = result * num
    elif command == "divide":
        result = result / num

    print(f"Result: {result}")

    command = input("Please enter a command: ")
