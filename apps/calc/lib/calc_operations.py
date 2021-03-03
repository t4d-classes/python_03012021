calc_operations = [
    { "label": 'Add', "name": 'add', "func": lambda r, n: r + n },   
    { "label": 'Subtract', "name": 'subtract', "func": lambda r, n: r - n},   
    { "label": 'Multiply', "name": 'multiply', "func": lambda r, n: r * n},   
    { "label": 'Divide', "name": 'divide', "func": lambda r, n: r / n},   
    { "label": 'Exponent', "name": 'exponent', "func": lambda r, n: r ** n},   
    { "label": 'Floor Division', "name": 'floordiv', "func": lambda r, n: r // n},   
]

def find_calc_operation_by_name(calc_operations, op_name):

    for calc_operation in calc_operations:
        if calc_operation["name"] == op_name:
            return calc_operation

    return None

def calc(result, calc_history_entry):

    global calc_operations

    calc_operation = find_calc_operation_by_name(calc_operations, calc_history_entry["op_name"])
    if calc_operation:
        calc_operation_func = calc_operation["func"]
        return calc_operation_func(result, calc_history_entry["op_value"])
    else:
        return result