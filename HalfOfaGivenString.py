#~ Find length of string
#~ Half the length of string
#~ Print out the start and end of the string based on the half length

# # My Solution:{

# string = input("Input string: ")

# length = len(string)
# halfLength = length // 2

# print(f"Half of the string {string} = {string[:halfLength]}")
# }

## Model Solution:{

def ex1(str):
    return str[:len(str) // 2]

print(ex1("abcdef"))

#}