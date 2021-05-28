
def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    for i in range(len(brackets_row.split(' '))):
        if brackets_row.split(' ')[i] != '()':
            brackets_row.split(' ')[0] == brackets_row.split(' ')[len(brackets_row.split(' ')) - 1]





