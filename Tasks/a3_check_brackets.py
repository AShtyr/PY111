def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    check_list = []
    count = 0
    for i in range(len(brackets_row.replace(' ', ''))):
        if brackets_row[i] == '(':
            count += 1
        else:
            count -= 1
        check_list.append(count)

    if all(k >= 0 for k in check_list) and count == 0:
        return True
