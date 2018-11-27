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
