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
        for calc_history_entry in calc_history_list:

            table_row = [
                str(calc_history_entry.id).rjust(2),
                calc_history_entry.op_name.ljust(9),
                str(calc_history_entry.op_value).rjust(7),
            ]

            table.append(" | ".join(table_row))

    return "\n".join(table)

def calc_ops_count_table(calc_history_list):

    op_names = [ c.op_name for c in calc_history_list ]

    count_table = []
    count_table.append("Op Counts")
    count_table.append("----------------")

    for calc_operation in calc_operations:
        count_table.append(f"{calc_operation.label}: {op_names.count(calc_operation.name)}")

    return "\n".join(count_table)