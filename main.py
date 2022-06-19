
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
user = {
  'name': 'James',
  'age': 32,
  'cars': ['toyota','mazda']
}

print(user.get('friends', ['paul','ade']))
print(user.get('age'))
 
user2 = dict(name='henry')
print(user2)
print('name' in user2.keys())
print('henry' in user2.values())
print(user2.keys())
print(user2.values())
print(user2.items())

user3 = user2.copy()
print(user3)
print(user3.pop('name'))
print(user3)

user2.clear()
print(user2)









