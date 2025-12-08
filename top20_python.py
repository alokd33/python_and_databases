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


def sum_two_target(target, arr):
    map_number = {}
    for index, val in enumerate(arr) :
        complement = target - val
        if complement in map_number :
            return [map_number[complement], index]

        map_number[val] = index


arr = [2, 7, 11, 15]
target = 9

arr = [2, 7, 11, 15]
target = 13

a = sum_two_target(target, arr)
print(a)
#[0, 2]

def str_are_anagram(str1, str2):
    """
    Input: s1 = “geeks”  s2 = “kseeg”
    Output: true
    Explanation: Both the string have same characters with same frequency. So, they are anagrams.

    Input: s1 = "allergy", s2 = "allergyy"
    Output: false
    Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character.
     Since the frequency of characters differs, the strings are not anagram
    """
    if len(str1) != len(str2) :
        return False
    d1 = {}
    d2 = {}
    for i in str1:
        if i in d1 :
            d1[i] = d1[i] + 1
        else:
            d1[i] = 1
    for j in str2:
        if j in d2 :
            d2[j] = d2[j] + 1
        else:
            d2[j] = 1
    print("D1 is:", d1 ,"and D2 is:", d2)
    # dict sort by key
    sorted_d1_by_key = dict(sorted(d1.items()))
    sorted_d1_string = "".join( str(k) + str(v) for k,v in sorted(d1.items()))
    sorted_d2_string = "".join(str(k) + str(v) for k, v in sorted(d2.items()))
    print("sorted_d1_by_key, sorted_d1_string, sorted_d2_string", sorted_d1_by_key, sorted_d1_string, sorted_d2_string)
    sorted_d1_by_value = dict(sorted(d1.items(), key= lambda x:x[1]))
    print("sorted_d1_by_vale:", sorted_d1_by_value)
    if d1 == d2 :
        return True
    else :
        return False
a = str_are_anagram("allergy", "allergyy")
print(a)
#False
b = str_are_anagram("geeks", "kseeg")
print(b)
# True
