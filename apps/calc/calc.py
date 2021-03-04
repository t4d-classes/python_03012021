from views import calculate_result, calc_history_table, calc_ops_count_table
from lib.calc_commands import get_remove_history_entry_id, get_operand, get_command
from lib.calc_history import CalcHistoryList

if __name__ == '__main__':

    calc_history_list = CalcHistoryList()
    command = "clear"

    while command:

        if command == "clear":
            calc_history_list.clear_history()
            print(f"Result: {calculate_result(calc_history_list.calc_history)}")
        elif command == "history":
            print(calc_history_table(calc_history_list.calc_history) + "\n")
            print(calc_ops_count_table(calc_history_list.calc_history))
        elif command == "remove":
            calc_history_entry_id = get_remove_history_entry_id()
            calc_history_list.remove_calc_history_entry(calc_history_entry_id)
        else:
            num = get_operand()
            calc_history_list.append_calc_history(command.lower(), num)
            print(f"Result: {calculate_result(calc_history_list.calc_history)}")

        command = get_command()
