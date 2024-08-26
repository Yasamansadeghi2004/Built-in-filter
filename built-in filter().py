# def custom_filter(func, arg) :
#     if func is None:
#         func = bool
#     for item in arg:
#         if not func(item):
#             return item
    

def custom_filter(func, arg):
    result =[]
    for item in arg:
        if func(item):
            result.append(item)
    return result

number = [ 1,2, 3, 4, 5, 9, 15, 20, 25, 18]

# def sum (x):
#     if x < 18:
#         return False
#     else:
#         return True



def  sum(x):
    return x % 2 == 0

result = custom_filter(sum,number)
for num in result:
    print(num)