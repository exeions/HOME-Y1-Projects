#~ Write a function named capitals. The function should take a single parameter. Your function should return a list of all the capital letters from a string that is passed into the function.

import unittest

def capitals(str):
    
    capLetters = []
    
    for char in str:
        if char.isupper():
            capLetters.append(char)
    return capLetters

#~ ----- Unit testing ----- ~#

# class TestCaptialMethod(unittest.TestCase):

#     param_list = [("AbCdE", "ACE"), ("aBcDe", "BD")]

#     def test_cap(self):
#         for p1, p2 in self.param_list:
#             with self.subTest():
#                 str1 = "".join(capitals(p1))
#                 self.assertEqual(str1, p2)

# if __name__ == "__main__":
#     unittest.main()