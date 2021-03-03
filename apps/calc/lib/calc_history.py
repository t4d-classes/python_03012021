def append_calc_history(calc_history_list, op_name, op_value):

    next_calc_history_id = max( [ t["id"] for t in calc_history_list ] or [0] ) + 1
    
    calc_history_list.append({
        "id": next_calc_history_id,
        "op_name": op_name,
        "op_value": op_value,
    })


def remove_calc_history_entry(calc_history_list, calc_history_entry_id):

    for calc_history_entry in calc_history_list:
        if calc_history_entry["id"] == calc_history_entry_id:
            calc_history_list.remove(calc_history_entry)
            break