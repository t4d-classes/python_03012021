from views import calculate_result, calc_history_table, calc_ops_count_table
from lib.calc_commands import get_remove_history_entry_id, get_operand, get_command, get_file_name
from lib.calc_history import CalcHistoryList, CalcHistoryEntry

if __name__ == '__main__':

    calc_history_list = CalcHistoryList()
    command = "clear"

    # calc_history_list.calc_history.append(CalcHistoryEntry(10, 'add', 2))

    while command:

        if command == "save":
            file_name = get_file_name()
            calc_history_list.save_history(file_name)
        elif command == "load":
            file_name = get_file_name()
            calc_history_list.load_history(file_name)
        elif command == "clear":
            # calc_history_list.clear_history()
            print(f"Result: {calculate_result(calc_history_list)}")
        elif command == "history":
            print(calc_history_table(calc_history_list) + "\n")
            print(calc_ops_count_table(calc_history_list))
        elif command == "remove":
            calc_history_entry_id = get_remove_history_entry_id()
            calc_history_list.remove_calc_history_entry(calc_history_entry_id)
        else:
            num = get_operand()
            # calc_history_list.append_calc_history(command.lower(), num)
            calc_history_list += (command.lower(), num)
            print(f"Result: {calculate_result(calc_history_list)}")

        command = get_command()
