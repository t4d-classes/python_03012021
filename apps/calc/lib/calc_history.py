import csv

class CalcHistoryEntry:

    def __init__(self, entry_id, op_name, op_value):
        self.id = entry_id
        self.op_name = op_name
        self.op_value = op_value

class CalcHistoryList:

    def __init__(self):
        self._calc_history = []

    # @property
    # def calc_history(self):
    #     return self._calc_history.copy()

    def __add__(self, op_info):
        op_name, op_value = op_info
        next_calc_history_id = max( [ t.id for t in self._calc_history ] or [0] ) + 1
        new_calc_history_entry = CalcHistoryEntry(next_calc_history_id, op_name, op_value)
        self._calc_history.append(new_calc_history_entry)
        return self


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

    def save_history(self, file_name):
        # custom CSV file writer
        # with open(file_name, "w") as history_file:
        #     for calc_history_entry in self._calc_history:
        #         history_file.write(",".join([
        #             str(calc_history_entry.id),
        #             calc_history_entry.op_name,
        #             str(calc_history_entry.op_value),
        #         ]) + "\n")

        calc_history_dict_list = [
            dict(op_id=e.id, op_name=e.op_name, op_value=e.op_value)
            for e in  self._calc_history ]

        with open(file_name, "w") as history_csv_file:
            writer = csv.DictWriter(
                history_csv_file,
                fieldnames=list(calc_history_dict_list[0].keys()))
            writer.writeheader()
            for entry in calc_history_dict_list:
                writer.writerow(entry)


    def load_history(self, file_name):
        self._calc_history.clear()
        # with open(file_name, "r") as history_file:
        #     for raw_calc_history_entry in history_file:
        #         calc_history_entry = raw_calc_history_entry.strip().split(",")
        #         self._calc_history.append(CalcHistoryEntry(
        #             int(calc_history_entry[0]),
        #             calc_history_entry[1],
        #             float(calc_history_entry[2])
        #         ))

        with open(file_name, "r") as history_csv_file:
            reader = csv.DictReader(history_csv_file)
            for calc_history_entry in reader:
                self._calc_history.append(CalcHistoryEntry(
                    int(calc_history_entry["op_id"]),
                    calc_history_entry["op_name"],
                    float(calc_history_entry["op_value"])
                ))


    def __iter__(self):
        return self._calc_history.__iter__()

    def __next__(self):
         return self._calc_history.__next__()

    def __len__(self):
        return len(self._calc_history)