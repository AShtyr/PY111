

l_ = []

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    l_ = brackets_row.split(' ')
    l_1 = [i for i in l_ if i != '()']
    for i in range(len(l_1)):
        if l_1[i] != l_[-(i + 1)]:
            return True
        else:
            return False




