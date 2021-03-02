calc_history = []
next_calc_history_id = 0

def append_calc_history(calc_history_list, op_name, op_value):

    global next_calc_history_id

    next_calc_history_id += 1
    calc_history_list.append((next_calc_history_id, op_name, op_value))

def remove_calc_history_entry(calc_history_list, calc_history_entry_id):

    for calc_history_entry in calc_history_list:
        if calc_history_entry[0] == calc_history_entry_id:
            calc_history.remove(calc_history_entry)
            break
        
def calculate_result(calc_history_list):

    result = 0
    
    for _, command, num in calc_history_list:

        if command == "add":
            result = result + num
        elif command == "subtract":
            result = result - num
        elif command == "multiply":
            result = result * num
        elif command == "divide":
            result = result / num

    return result

def calc_history_table(calc_history_list):

    table = []
    table.append("Id | Operation | Operand")
    table.append("------------------------")

    if len(calc_history) < 1:
        table.append("This is no history.")
    else:
        for id, op_name, op_value in calc_history:
            table.append(
                f"{str(id).rjust(2)} | {op_name.ljust(9)} | {str(op_value).rjust(7)}")

    return "\n".join(table)

def calc_ops_count_table(calc_history_list):

    add_count = 0
    subtract_count = 0
    multiply_count = 0
    divide_count = 0

    for _1, op_name, _2 in calc_history_list:
        if op_name == "add":
            add_count += 1
        elif op_name == "subtract":
            subtract_count += 1
        elif op_name == "multiply":
            multiply_count += 1
        elif op_name == "divide":
            divide_count += 1

    count_table = []
    count_table.append("Op Counts")
    count_table.append("----------------")
    count_table.append(f"Add: {add_count}")
    count_table.append(f"Subtract: {subtract_count}")
    count_table.append(f"Multiply: {multiply_count}")
    count_table.append(f"Divide: {divide_count}")

    return "\n".join(count_table)

def int_input(prompt):
    return int(input(prompt))

def float_input(prompt):
    return float(input(prompt))

def get_command():
    return input("Please enter a command: ")

def get_remove_history_entry_id():
    return int_input("Please enter the id of the history entry to remove: ")

def get_operand():
    return float_input("Please enter an operand: ")

command = "clear"

while command:

    if command == "clear":
        calc_history = []
        print(f"Result: {calculate_result(calc_history)}")
    elif command == "history":
        print(calc_history_table(calc_history) + "\n")
        print(calc_ops_count_table(calc_history))
    elif command == "remove":
        calc_history_entry_id = get_remove_history_entry_id()
        remove_calc_history_entry(calc_history, calc_history_entry_id)
    else:
        num = get_operand()
        append_calc_history(calc_history, command, num)
        print(f"Result: {calculate_result(calc_history)}")

    command = get_command()
