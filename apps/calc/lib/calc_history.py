class CalcHistoryEntry:

    def __init__(self, entry_id, op_name, op_value):
        self.id = entry_id
        self.op_name = op_name
        self.op_value = op_value

def append_calc_history(calc_history_list, op_name, op_value):
    next_calc_history_id = max( [ t.id for t in calc_history_list ] or [0] ) + 1
    new_calc_history_entry = CalcHistoryEntry(next_calc_history_id, op_name, op_value)
    calc_history_list.append(new_calc_history_entry)


def remove_calc_history_entry(calc_history_list, calc_history_entry_id):
    for calc_history_entry in calc_history_list:
        if calc_history_entry.id == calc_history_entry_id:
            calc_history_list.remove(calc_history_entry)
            break