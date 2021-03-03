from functools import reduce

from lib.calc_operations import calc_operations, calc

def calculate_result(calc_history_list):

    return reduce(calc, calc_history_list, 0)

def calc_history_table(calc_history_list):

    table = []
    table.append("Id | Operation | Operand")
    table.append("------------------------")

    if len(calc_history_list) < 1:
        table.append("This is no history.")
    else:
        for id, op_name, op_value in calc_history_list:
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