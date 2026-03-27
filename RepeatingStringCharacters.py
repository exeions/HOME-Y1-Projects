#~ Write a new function that passing in a new string. The function should return a string whereby each character of the original string has been repeated once.

# def repeat(str):
    
#     result = ""

#     for char in str:
#         result += char + char

#     return result

# print(repeat("Malachi"))

## Quicker method

def repeat(str):
    for x in str:
        yield x * 2

print("".join(repeat("hello")))