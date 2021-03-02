from functools import reduce

def calc_add(r, n):
    return r + n

calc_operations = [
    ('Add', 'add', calc_add),   
    ('Subtract', 'subtract', lambda r, n: r - n),   
    ('Multiply', 'multiply', lambda r, n: r * n),   
    ('Divide', 'divide', lambda r, n: r / n),   
    ('Exponent', 'exponent', lambda r, n: r ** n),   
    ('Floor Division', 'floordiv', lambda r, n: r // n),   
]

calc_history = []

def append_calc_history(calc_history_list, op_name, op_value):

    next_calc_history_id = max( [ t[0] for t in calc_history_list ] or [0] ) + 1
    calc_history_list.append((next_calc_history_id, op_name, op_value))


def remove_calc_history_entry(calc_history_list, calc_history_entry_id):

    for calc_history_entry in calc_history_list:
        if calc_history_entry[0] == calc_history_entry_id:
            calc_history.remove(calc_history_entry)
            break

def find_calc_operation_by_name(calc_operations, op_name):

    for calc_operation in calc_operations:
        if calc_operation[1] == op_name:
            return calc_operation

    return None

def calc(result, calc_history_entry):

    global calc_operations

    _, op_name, op_value = calc_history_entry

    calc_operation = find_calc_operation_by_name(calc_operations, op_name)
    if calc_operation:
        calc_operation_func = calc_operation[2]
        return calc_operation_func(result, op_value)
    else:
        return result

def calculate_result(calc_history_list):

    return reduce(calc, calc_history_list, 0)

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

    op_names = [ c[1] for c in calc_history_list ]

    count_table = []
    count_table.append("Op Counts")
    count_table.append("----------------")

    for op_label, op_name, _ in calc_operations:
        count_table.append(f"{op_label}: {op_names.count(op_name)}")

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
        append_calc_history(calc_history, command.lower(), num)
        print(f"Result: {calculate_result(calc_history)}")

    command = get_command()
