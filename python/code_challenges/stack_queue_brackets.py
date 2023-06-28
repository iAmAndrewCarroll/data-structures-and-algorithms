from data_structures.queue import Queue


def multi_bracket_validation(string):
    stack = []
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    pair_brackets = {'(': ')', '[': ']', '{': '}'}

    for brack in string:
        if brack in open_brackets:
            stack.append(brack)
        elif brack in close_brackets:
            if len(stack) == 0:
                return False
            if pair_brackets[stack[-1]] == brack:
                stack.pop()
            else:
                return False

    return len(stack) == 0
