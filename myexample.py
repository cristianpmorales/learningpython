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
	print('HELLO THERE')
for letter in ' Hello World':
	print(letter)
	print('HELLO THERE2')
for _ in 'Hello World':
	print('Using the underscore in a for loop')
	print('HELLO THERE3')
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
else:
	print('X is not less than 5')
# break: Breaks out of the current closet enclosing loop.
# continue: Goes to the top of the closest enclosing loop. 
# pass: Does nothing at all
# Usefull operations 
# for num in range(start,stop,range)
for num in range(3,10,2):
	print(num)
	print('for num in range(start,stop,range)')
# To get the list of numbers you type
print(list(range(3,10,2)))
# Enumarate function 
word = 'abcdefghijklmnop'
for index, letter in enumerate(word):
	print(letter)
	print(index)
# zip function
mylist = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e'] 
for item in zip(mylist,mylist2):
	print(item)
from random import shuffle
numberlist = [1,2,4,5,6,7]
shuffle(numberlist)
print(numberlist)
from random import randint
print(randint(0,100))
# input function 
result = input('What is you name:')
print(result)
# First method to append to a list
# Declare the empty list
new_list = []
for x in 'mystring':
	new_list.append(x)
print(new_list)
mystring = 'whatever'
new_list = [x for x in mystring]
print(new_list)
numberlist = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,19
evenlist = [x for x in numberlist if x%2==0]
print(evenlist)
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for x in st:
	if x == 's':
		print(st.split('s'))
# Correct solution 
for word in st.split():
	if word[0] == 's':
		print(word)
# Use range() to print all the even numbers from 0 to 10.
print(range(0,11,2))
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
listofnumbers = [x for x in range(0,51) if x%3==0]
print(listofnumbers)
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
		if x%3 == 0 and x%5 == 0 :
			print('FizzBuzz')
		elif x%5 == 0:
			print('Buzz')
		elif x%3 == 0:
			print('Fizz')
		else:
			print(x)
# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
# Correct solution
for word in st.split():
	if len(word) % 2 == 0:
		print(word)
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
newword = [word[0] for word in st.split()]
print(newword)
help(newword.insert)
def name_function():
	'''
	Docstring: Description of function
	Input: Shit is entered 
	Output: Shit happens
	'''
	print('Hello')
help(name_function)
name_function()
def pig_latin(word):
	first_letter = word[0]

	# Check if vowel
	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else: 
		pig_word = word[1:] + first_letter + 'ay'
	return pig_word
print(pig_latin('idiot'))
def myfunc(*arg):
	'''
	Docstring: Takes a number of arguments and returns a tip
	Input: None
	Output: Total
	'''
	print(sum(arg) * 1.2)
	return sum(arg) * 1.2
myfunc(100,100,100)
def mydictonaryfunc(**kwargs):
	'''
	Docstring: Find keywords in a dictonary
	input: none
	Output: hello, goodbye
	'''
	if 'greeting' in kwargs:
		print('The greeting is {}'.format(kwargs['greeting']))
	else:
		print('there is nada here')
mydictonaryfunc(greeting = 'Fuck you',salutations = 'hola')
mydictonaryfunc(what = 'Do I exist')
from fractions import Fraction
import math
# Write a function that computes the volume of a sphere given its radius.
#  If you want to calculate the volume of a sphere, you just have to find its radius and plug it into a simple formula, V = ⁴⁄₃πr³.
fourthird = Fraction(4,3)
 
def vol(rad):
	return fourthird * math.pi * rad**3 
print(vol(2))
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(thestring):
	lowercount = 0
	uppercount = 0
	for x in thestring.split():
		if x[0] == x[0].lower():
			lowercount += 1
			print('Lower')
			print(lowercount)
		else:
			uppercount += 1
			print('upper')
			print(uppercount )
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
# Write a Python function that takes a list and returns a new list with unique elements of the first list.

lst = [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(*arg):
	for x in arg:
		newthing = x
		if x == newthing:
			
