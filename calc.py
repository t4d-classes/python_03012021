result = 0
history = []
next_history_id = 0

calc_history = []
next_calc_history_id = 0

command = input("Please enter a command: ")

while command:

    if command == "clear":
        
        result = 0
        calc_history = []

        print(f"Result: {result}")
        
        command = input("Please enter a command: ")
        continue
    
    elif command == "history":

        print("Id | Operation | Operand")
        print("------------------------")

        if len(calc_history) < 1:
            print("This is no history.")
        else:
            for id, op_name, op_value in calc_history:
                print(f"{str(id).rjust(2)} | {op_name.ljust(9)} | {str(op_value).rjust(7)}")

        command = input("Please enter a command: ")
        continue

    elif command == "remove":

        calc_history_entry_id = int(input("Please enter the id of the history entry to remove: "))

        for calc_history_entry in calc_history:
            if calc_history_entry[0] == calc_history_entry_id:
                calc_history.remove(calc_history_entry)
                break

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

    next_calc_history_id = next_calc_history_id + 1
    calc_history_entry = (next_calc_history_id, command, num)
    calc_history.append(calc_history_entry)

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
