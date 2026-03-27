#~ Write a new function that take in a credit card number and returns a masked number. Only show the last 4 digits of the credit card number. 

# def credit_card_masker(card_num):
    
#     mask = len(card_num) - 4
#     y = ""
#     y += ("*" * mask) + card_num[-4] + card_num[-3] + card_num[-2] + card_num[-1]
    
#     return y

# print(credit_card_masker("5514 6897 8435 4914"))

def masking(number, mask):
    str = ''
    n = mask
    for x in number[:-n]:
        str += '*'
    str += number[-n:]
    return str


print(masking("5514689784354914", 4))