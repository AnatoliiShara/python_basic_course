#input method (2-3 variables, which have different types)
a=10
print(a)
my_string = 'Hello, World!'
print(my_string)
my_flt = 45.06
print(my_flt)
my_bool = 5 > 9 #логический оператор
print(my_bool)
my_list = ['item_1', 'item_2', 'item_3', 'item_4']
print(my_list)
my_tuple = ('one', 'two', 'three')
my_tuple
my_dict = {'letter': 'g', 'number': 'seven', 'symbol': '&'}
print(my_dict)

If...else
#a)
x = int(input())
y = int(input())
if x > 0:
    if y > 0: # x>0, y>0
        print("The first quarter")
    else: # x>0, y<0
        print("The fourth quarter")
else:
    if y > 0: # x<0, y>0
        print("The second quarter")
    else: # x<0, y<0
        print("The third quarter")
#b)

if grade >= 65:  # condition
            print("Passing grade")  # expression
else:
            print("Failing grade")

#usage of operators NOT, AND, ==, <>, !=

print((9 > 7) and (2 < 4))  # both are True
print((8 == 8) or (6 != 6))  # one of them is True
print(not (3 <= 1))  # expression is False
        True
        True
        True

