#~ Write a function that strips and returns a username for any given email address. For example user@org.com, the output should return user.

## My Solution

# def email_strip(email):
#     if "@" in email:
#         char_index = 0

#         for char in email:
#             if char == "@":
#                 char_index = email.index(char)
#                 break
#             else:
#                 pass
#         print(email[:char_index])
#     else:
#         print("Invalid Email")

# email_strip("malachi@gmail.com")

## Cleaner Solution

# def email_strip(email):
#     if "@" in email:
#         char_index = email.index("@")
#         print(email[:char_index])
#     else:
#         print("Invalid Email")

# email_strip("malachi@gmail.com")

## Model Solution

# email = "user@org.com"

# print(email.split("@")[0])

## Extension ~ Can you now extract from a list of emails the usernames

emails = ["malachi@gmail.com", "liam@gmail.com", "mia@gmail.com", "harry@gmail.com", "isaac@outlook.com", "aiden@outlook.com", "user@org.com"]

def email_stripper(emails):
    users = []
    
    if isinstance(emails, list):
        for email in emails:
            users.append(email.split("@")[0])
        return users
    else:
        return "Invalid, please input a list."

print(email_stripper(emails))