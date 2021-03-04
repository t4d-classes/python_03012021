from utils import int_input, float_input

def get_command():
    return input("Please enter a command: ")

def get_remove_history_entry_id():
    return int_input("Please enter the id of the history entry to remove: ")

def get_operand():
    return float_input("Please enter an operand: ")

def get_file_name():
    return input("Please enter a file name: ")