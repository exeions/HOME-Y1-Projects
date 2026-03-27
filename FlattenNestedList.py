#~ Write a function that tasks a nested list ex: [[1,2,3,4],["a","b","c"],[5,6,7,8]] and flattens it into a one-dimensional list [1,2,3,4,a,b,c,5,6,7,8]. Your function should take a single parameter and return a flattened list.

# nested_list = [["mala", ["hala", 2], "gala", ["bell", "tell"]]]

# def flatlist(nl):
#     flattened = []

#     for x in nl:
#         if isinstance(x, list):
#             flattened.extend(x)
#         else:
#             flattened.append(x)

#     return flattened

# print(flatlist(nested_list))

nestedlist = [[1,2,3,4], ["a", "b", "c"], [5, 6, 7, 8]]

def flatlist(nl):
    flatlist=[]
    for sublist in nl:
        for data in sublist:
            flatlist.append(data)
    return flatlist

print(flatlist(nestedlist))