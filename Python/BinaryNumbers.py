binary = '10100'

def binary_10_checker(binary):
    x = int(binary, 2)
    
    if x % 10 == 0:
        return f"{binary} -> {x} is divisible by 10."
    else:
        return f"{binary} -> {x} is not divisible by 10."

print(binary_10_checker(binary))