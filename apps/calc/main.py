from views import calculate_result, calc_history_table, calc_ops_count_table
from lib.calc_commands import get_remove_history_entry_id, get_operand, get_command
from lib.calc_history import remove_calc_history_entry, append_calc_history

if __name__ == '__main__':

    calc_history = []
    command = "clear"

    while command:

        if command == "clear":
            calc_history = []
            print(f"Result: {calculate_result(calc_history)}")
        elif command == "history":
            print(calc_history_table(calc_history) + "\n")
            print(calc_ops_count_table(calc_history))
        elif command == "remove":
            calc_history_entry_id = get_remove_history_entry_id()
            remove_calc_history_entry(calc_history, calc_history_entry_id)
        else:
            num = get_operand()
            append_calc_history(calc_history, command.lower(), num)
            print(f"Result: {calculate_result(calc_history)}")

        command = get_command()
