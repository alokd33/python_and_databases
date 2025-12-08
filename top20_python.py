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
# True 


def reverse_str(str1):
    return str1[::-1]
str1= "abc"
a = reverse_str(str1)
print(a) # cba


def strcharcount(str1):
    d1 = {}
    for i in str1 :
        if i in d1 :
            d1[i] = d1[i] + 1
        else :
            d1[i] = 1
    str2 = "".join([str(k) + str(v)  for k,v in d1.items()])
    return str2

str1 = "abcabc"
a = strcharcount(str1)
print(a)
#a2b2c2
