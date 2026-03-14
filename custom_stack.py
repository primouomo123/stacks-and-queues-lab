def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    stack = []
    valid_parenthesis = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in valid_parenthesis.values():
            stack.append(char)
        elif char in valid_parenthesis.keys():
            if not stack or stack[-1] != valid_parenthesis[char]:
                return False
            stack.pop()
    return len(stack) == 0