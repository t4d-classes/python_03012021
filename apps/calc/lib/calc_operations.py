
class CalcOperation:

    def __init__(self, label, name, func):
        self.label = label
        self.name = name
        self.func = func

calc_operations = [
    CalcOperation('Add', 'add', lambda r, n: r + n),
    CalcOperation('Subtract', 'subtract', lambda r, n: r - n),
    CalcOperation('Multiply', 'multiply', lambda r, n: r * n),
    CalcOperation('Divide', 'divide',  lambda r, n: r / n),
    CalcOperation('Exponent', 'exponent', lambda r, n: r ** n),
    CalcOperation('Floor Division', 'floordiv', lambda r, n: r // n),
]

def find_calc_operation_by_name(calc_operations, op_name):

    for calc_operation in calc_operations:
        if calc_operation.name == op_name:
            return calc_operation

    return None

def calc(result, calc_history_entry):

    global calc_operations

    calc_operation = find_calc_operation_by_name(calc_operations, calc_history_entry["op_name"])
    if calc_operation:
        calc_operation_func = calc_operation.func
        return calc_operation_func(result, calc_history_entry["op_value"])
    else:
        return result