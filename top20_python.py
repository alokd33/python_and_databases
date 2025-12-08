def valid_parentheses(s1):
    """
    :param s1: string  brackets
    :return: True, False
    """
    mapping  = {"}":"{", "]":"[", ")":"(" }
    stack = []
    for char in s1 :
        if char in mapping :
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

a = valid_parentheses("{[()]}")
print(a)


