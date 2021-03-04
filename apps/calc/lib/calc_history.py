class CalcHistoryEntry:

    def __init__(self, entry_id, op_name, op_value):
        self.id = entry_id
        self.op_name = op_name
        self.op_value = op_value

class CalcHistoryList:

    def __init__(self):
        self._calc_history = []

    @property
    def calc_history(self):
        return self._calc_history

    def append_calc_history(self, op_name, op_value):
        next_calc_history_id = max( [ t.id for t in self._calc_history ] or [0] ) + 1
        new_calc_history_entry = CalcHistoryEntry(next_calc_history_id, op_name, op_value)
        self._calc_history.append(new_calc_history_entry)

    def remove_calc_history_entry(self, calc_history_entry_id):
        for calc_history_entry in self._calc_history:
            if calc_history_entry.id == calc_history_entry_id:
                self._calc_history.remove(calc_history_entry)
                break
    
    def clear_history(self):
        self._calc_history.clear()