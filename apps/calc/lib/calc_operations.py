calc_operations = [
    ('Add', 'add', lambda r, n: r + n),   
    ('Subtract', 'subtract', lambda r, n: r - n),   
    ('Multiply', 'multiply', lambda r, n: r * n),   
    ('Divide', 'divide', lambda r, n: r / n),   
    ('Exponent', 'exponent', lambda r, n: r ** n),   
    ('Floor Division', 'floordiv', lambda r, n: r // n),   
]

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