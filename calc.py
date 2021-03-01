result = 0
history = []
next_history_id = 0

command = input("Please enter a command: ")

while command:

    if command == "clear":
        result = 0
        history = []
        print(f"Result: {result}")
        command = input("Please enter a command: ")
        continue
    
    elif command == "remove":

        history_id = int(
            input("Please enter the history entry id to remove: "))

        for entry in history:
            if entry[0] == history_id:
                history.remove(entry)
                break

        command = input("Please enter a command: ")
        continue

    elif command == "history":

        print("Id     Name     Value")
        print("-----------------------")

        if len(history) < 1:
            print("There is no history")
        else:
            for id, name, value in history:
                print(f"{str(id).rjust(2)} {name.ljust(12)} {value}")
        command = input("Please enter a command: ")
        continue

    num = float(input("Please enter an operand: "))

    next_history_id = next_history_id + 1
    history.append((next_history_id, command, num))

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
