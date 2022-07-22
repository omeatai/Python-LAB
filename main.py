print(chr(97))  # a
print(chr(100))  # d
print(chr(0))  # '\x00'
print(chr(1114111))  # '\U0010ffff'
print(ord('\x00'))  # 0
print(ord('\U0010ffff'))  # 1114111

# x = "Hey"
# y = type("Hey")
# num = 5

# def test_function():
#   return "Hey"

# class Example:
#   def __init__(self):
#     return 2 + 4

# print(callable(x)) # False
# print(callable(y)) # True
# print(callable(num)) # False
# print(callable(test_function)) # True
# print(callable(Example)) # True

# print(type(bytes())) # <class 'bytes'>
# print(type(bytearray())) # <class 'bytearray'>
# print(bytes("hey", "UTF-8")) # b'hey'
# print(bytes("hey", "UTF-16")) # b'\xff\xfeh\x00e\x00y\x00'
# print(bytes(1)) # b'\x00'
# print(bytes(4)) # b'\x00\x00\x00\x00'
# print(bytes([1,2,3])) # b'\x01\x02\x03'
# print(bytearray([1,2,3])) # bytearray(b'\x01\x02\x03')

# x = bytearray([1,2,3])
# x.append(4)
# print(x) # bytearray(b'\x01\x02\x03\x04')
# x.reverse()
# print(x) # bytearray(b'\x04\x03\x02\x01')

# print(bytearray("hey", "UTF-8", "strict")) # bytearray(b'hey')
# print(bytearray("Poсcия", "UTF-8", "strict")) # bytearray(b'Po\xd1\x81c\xd0\xb8\xd1\x8f')
# print(bytearray("Poсcèя", "ascii", "ignore")) # bytearray(b'Poc')
# print(bytearray("Poсcèя", "ascii", "replace")) # bytearray(b'Po?c??')

# print(bool(1)) # True
# print(type(bool(1))) # <class 'bool'>
# print(bool(0)) # False
# print(bool(True)) # True
# print(bool(False)) # False
# print(bool("hey")) # True
# print(bool([1, 0])) # True
# print(bool([0, 0, False])) # True
# print(bool({"": False})) # True
# print(bool(1 == 2)) # False
# print(bool(1 == 1)) # True

# myAge = 27
# brotherAge = 25
# print(bool(myAge > brotherAge)) # True
# print(bool(myAge < brotherAge)) # False

# print(bin(1)) # 0b1
# print(type(bin(1))) # <class 'str'>
# print(bin(4)) # 0b100
# print(bin(64)) # 0b1000000
# print(bin(128)) # 0b10000000
# print(bin(255)) # 0b11111111
# print(bin(0x4)) # 0b100
# print(bin(0x64)) # 0b1100100
# print(format(4, 'b')) # 100
# print(format(255, 'b')) # 11111111

# print(ascii(1)) # '1'
# print(ascii([])) # '[]'
# print(ascii('encodé')) # 'encod\xe9'
# print(ascii('Россия')) # '\u0420\u043e\u0441\u0441\u0438\u044f'
# print(ascii(['encodé', 'Россия'])) # '['encod\xe9', '\u0420\u043e\u0441\u0441\u0438\u044f']'
# print(type(ascii(['encodé', 'Россия']))) # <class 'str'>

# print(any([""])) #False
# print(any(["", False, 0])) #False
# print(any(["", False, 0, 11])) #True
# print(any(["", False, 0, True])) #True
# print(any("Hey")) #True

# listSame = [1, 1, 1]
# listDiff = [1, 2, 3]

# print(any([x == 1 for x in listSame])) #True
# print(any([x == 10 for x in listSame])) #False
# print(any([x == 1 for x in listDiff])) #True

# names = ["John", "Joe", "James"]

# print(any([x == "Joe" for x in names])) #True
# print(any([x == "Dave" for x in names])) #False

# for i in range(10):
#   print(f"i={i}")

#   if i == 7:
#     #import pdb; pdb.set_trace()
#     breakpoint()

# class Person:
#   def __init__(self):
#     print("This is from the Super class!")

# class Student(Person):
#   def __init__(self):
#     # Person.__init__(self)
#     super().__init__()
#     print("This is from the Sub class.")

# p1 = Student()

#PRINT
# name = input('What is your name?\n')
# print(f"Your name is {name}.")

#TYPE
# sum = 2 + 4
# print(sum)
# print(type(sum))

# a,b,c = 1,2,3
# print(a,b,c)

#STRING FORMATTING
# name = 'Jonny'
# Age = 56
# print(f"Hi {name}, you are {Age} years old.")
# print("Hi {}, you are {} years old.".format(name, Age))

#STRING METHODS
# quote = "to be or not"
# print(quote.capitalize())
# print(quote.title())
# print(quote.upper())
# print(quote.casefold())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))

#DATETIME
# import datetime

# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%C"))
# print(x.strftime("%D"))
# print(x.strftime("%F"))
# print(x.strftime("%G"))
# print(x.strftime("%H"))
# print(x.strftime("%I"))
# print(x.strftime("%W"))
# print(x.strftime("%Y"))
# print(x.strftime("%Z"))

# Friday
# June
# 20
# 06/01/18
# 2018-06-01
# 2018
# 00
# 12
# 22
# 2018

#DATETIME - YEAR
# import datetime

# birth_year = int(input('What year were you born?\n'))
# current_year = datetime.datetime.now()
# age = current_year.year - birth_year
# print(f"You are approximately {age} years old.")

#PASSWORD CHECKER
# username = input('What is your name?\n')
# password = input('Enter your password:\n')
# password_length = len(password)
# hashed_password = '*' * password_length
# print(f"Hey {username.title()}, your password [{hashed_password}] is {password_length} characters long.")

#LIST METHODS
# numbers = [1,2,3,4,5,6]
# numbers.append(7)
# print(numbers)
# numbers.insert(2,100)
# print(numbers)
# numbers.extend([1,2,3,100,200])
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.pop(1)
# print(numbers)
# numbers.remove(100)
# print(numbers)
# numbers.clear()
# print(numbers)

#LIST METHODS2
# letters = ['a','b','c','a','b']
# print(letters.index('b'))
# print(letters.index('b',0,3))
# print('a' in letters)
# print('d' in letters)
# print(letters.count('b'))
# print(letters)
# letters.reverse()
# print(letters)
# letters.sort()
# print(letters)
# more_letters = sorted(letters, reverse=True)
# print(more_letters)
# print(more_letters[::-1])
# #
# nums = list(range(10,21))
# print(nums)
# string_nums = [str(i) for i in nums]
# print(string_nums)
# nums_set = '-'.join(string_nums)
# print(nums_set)

#LIST UNPACKING
# a,_,c,*args,d = [10,20,30,40,50,60,70]
# print(a)
# print(c)
# print(d)

#DICTIONARY
# user = {
#   'name': 'James',
#   'age': 32,
#   'cars': ['toyota','mazda']
# }

# print(user.get('friends', ['paul','ade']))
# print(user.get('age'))

# print("############## KEYS AND VALUES ###########")
# user2 = dict(name='henry',age='24')
# print(user2)
# print('name' in user2.keys())
# print('henry' in user2.values())
# print(user2.keys())
# print(user2.values())
# print(user2.items())
# print("############## COPY AND POP #################")
# user3 = user.copy()
# print(user3)
# print(user3.pop('cars'))
# print(user3)
# print("############## UPDATE AND POPITEM ##############")
# user4 = user.copy()
# user4.update({'sex': 'Male'})
# print(user4)
# print(user4.popitem())
# print(user4)
# user4.clear()
# print(user4)

#TUPLES
# nums = (1,2,3,4,5,6,5,6)
# print(nums.count(5))
# print(nums.index(4))

#SETS
# my_set = {1,2,3,4,5,4,5,6}
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# print('##########################')
# mylist = [2,2,4,4,5,5]
# print(list(set(mylist)))
# print('##########################')
# myset2 = my_set.copy()
# print(myset2)
# myset2.clear()
# print(myset2)

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()
