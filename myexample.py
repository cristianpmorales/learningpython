print('hello world')
# using indexes in strings
new_string = 'abcdefghijklmnop'
print(new_string)
# returns everything after b in new_string
print(new_string[5:])
# returns strings efg
print(new_string[4:7])
# returns string dfhj by using a range on where to start and stop and a step
print(new_string[1:10:2])
# revere a string
print(new_string[::-1])
name = 'Sam'
print(name)
# concatinate by taking the index of name and adding another letter
new_name = 'P' + name[1:]
print(new_name)
letter = 'q'
# will repeat q 10 times
print(letter * 10)
# change everything to uppercase
x = "hello world"
print(x)
print(x.upper())
# split and remove l
print(x.split('l'))
# will print The fox brown quick
print('The {} {} {}'.format('fox','brown','quick'))
# will print quick fox brown
print('The {2} {0} {1}'.format('fox','brown','quick'))
# assining variables in .format
print('The {q} {b} {f}'.format( f = 'fox', b = 'brown', q = 'quick'))
# creating a list
mylist = [1,2,3,4,'Name','String',7]
print(mylist)
# length of list
print(len(mylist))
# using the start stop and step method
print(mylist[2:6:3])
# concating different lists 
secondlist = [9,10,11,'random']
print(secondlist)
newlist = mylist + secondlist
print(newlist)
# using index to change the list 
mylist[0] = 'NEWCHANGE'
print(mylist)
# adding an element to the end of a list
mylist.append(100)
print(mylist)
# removing an item of a list
print('remove name using .pop ' + mylist.pop(4))
# sorting a list 
thirdlist = [1,5,99,51,885,1656,2,3,4]
thirdlist.sort()
print(thirdlist)
# reversing a list 
thirdlist = [1,5,99,51,885,1656,2,3,4]
thirdlist.reverse()
print(thirdlist)
# Using dictionaries
prices_lookup = {'Apple':2.99, 'Oranges': 1.99, 'Milk':5.80}
# Tuples
t = ('a','a','b','c','d')
print(type(t))
print(t.count('a'))
#set
numbers = [1,1,1,1,1,1,2,2,2,22,3,3,3,3,3,3,3,4,4,4,4,4,22,22,22,22]
print(numbers)
print(set(numbers))
#to find the square root  
print(25 ** .5)
# Given the string 'hello' give an index command that returns 'e'
hello = 'hello'
print(hello[1])
# Reverse the string 'hello' using slicing:
print(hello[::-1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
print(hello[-1])
# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
print(list3)
list3[2][2] = 'goodbye'
print (list3)
# Sort the list below:
list4 = [5,3,4,6,1]
print(list4.sort())
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print( d['k1'][0]['nest_key'][1][0] )
print(1 < 2 and 2 < 3)
# python uses the actual words for logic and, or, not
name = 'Jose'

if name == 'Frankie':
	print('Hello Frankie')
elif name == 'Sammy':
	print ('Hello Sammy')
elif name == 'Jose':
	print ('Hello Jose')
else:
	print('Please enter you name')
differentlist = [1,2,3,4,5,6,7,8,9,10]
for numb in differentlist:
	print('Hello')

for number in differentlist:
	if number % 2 == 0:
		print('even')
	else:
		print(f'odd')
# Creating the variable
sumoflist = 0

for num in differentlist:
	sumoflist = num + sumoflist
	print(sumoflist)
print(sumoflist)
hellostring = ' Hello World'

for letter in hellostring:
	print(letter)
for letter in ' Hello World':
	print(letter)
for _ in 'Hello World':
	print('Using the underscore in a for loop')
# tuple unpacking 
tup = [(1,2,3),(3,4,5),(5,6,7),(7,8,9),(9,10,11)]
for a,b,c in tup:
	print(c)
dictionary = {'key1':'random','key2':'value','key3':'sets'}
for key,value in dictionary.items():
	print(value)
x = 0 
while x < 5:
	print(f'The value of x = {x}')
	x += 1
