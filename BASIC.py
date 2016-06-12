                                         
"""
http://docs.python.org/2/tutorial/introduction.html
"""
#------RUN PYTHON FROM THE COMMAND LINE---------------------------

type "python" , it's now a python console.

If you want to go back to command line,
hit CTRL+Z and type Enter.

# -------CODE INTROSPECTION-------
# Code introspection is the ability to examine classes, functions and keywords to know what they are, 
# what they do and what they know.
# Python provides several functions and utilities for code introspection.
help() 
dir()
hasattr()
id()
type()
repr()
callable()
issubclass()
isinstance()
__doc__
__name__

#------TRY EXCEPT---------------------------
sometimes your code could run into an error TRACEBACK, then it blocks.
You can use Try Except to keep on going by giving him an alternative way out.

x='Hello'
try:
	out=int(x) this will give you an error because it's a string
except:
	out= -1

#------USE PYTHON IDLE---------------------------

open the IDLE
File\New
Type some python code in the new window and save it somewhere
as a .py (the extension is important for the color of the python code)
then press F5 tu run the code

#------PRINT---------------------------
#triple quotes print exaclt what s inside, as it is """...newlines and stufff"""
\n # newline
\ # newline in your script but won t affect your print, just for clarity

#To Print a string + string,    use +
print 'Value of ' + n # where n is a string variable, can t add number with plus, use "," insteand or %d

# To Print String  + integer variable
print 'Value of %d'  % i # where i is a integer variable
# %d means “replace with something that is outside the string”  
# the second % replace the + sign
"hello" * 10  #print ten hello

#-----STRINGS--------
word='Help'+'A'    #create

# concatenation only works with strings.
count = 4
str(count) # return 4 as a string

print len(word) # return 5, "HelpA" is 5 characters long
print astring.index("A") # return 4. The letter 'A' is 5 characters away from the beginning
print astring.count("l") # return the number of time the letter 'l' appears
print astring[3:7] # print the slice of the string
print astring.upper()
print astring.lower()
print astring.startswith("Help") # return True, check if the string start as defined
print astring.endswith("asdfasdfasdf") # the same for the end 
astring.split(" ") # split the string where you can find " ", as differents strings inside a list
astring.strip() # get rid of the space characters
astring.pop() # remove last item
word[:2]    # The first two characters
word[2:]    # Everything except the first two characters
word[-2:]    # The last two characters
word[:-2]    # Everything except the last two characters
# put "," at the end in order to avoid tu jump to the next line
s = "A bird in the hand..."

for i in s:
    if i == 'A' or i == 'a':
        print 'X',
		
# JOIN STRING
d = ["caca","dadad","dasdasd"]
print "\\".join(d)
	# the "" before the joint enable you to set the separator.

#-----OPEN READ FILES ------
open(filename,mode) # mode can be 'r' to READ, 'w' for WRITING (erasing what is inside) or 'a' APPEND, add to the file

with open('tmp.txt') as f: # when we open the file, it's now available to us
    data = f.read()
    
fileName = "randomText.txt"
file = open(fileName,'r')
print file.readline() # read line by line
# return an empty string at the end of the file ""
# so you can use a WHILE to read a file

line = file.readline()
while line != '':
    print(line)
    line = file.readline()

# readline read and return the next line from the file
# including the newline character if it exist
# that's why there is a newline when you print that.

# in order to correct that you can add a limit
# to your print command in your WHILE LOOP

printline, end = ''

# you can PRINT all lines more easily with the FOR LOOP
for line in file:
    printline, end = ''

# or PRINT the whole file
print file.read()

--- OPEN WEBBROWSER----
import webrowser
webbrowser.open('http://...')

# OPEN READ FILE via TKINTER-----------------------------
import Tkinter, tkFileDialog

selectedFile = tkFileDialog.askopenfilename() #ask a file to open

saveFile = tkFileDialog.asksaveasfilename() # create an empty file

# read the contents of the file
from_file = open( selectedFile , 'r')
contents = from_file.read()
from_file.close()

# write the contents of the file in the new one
to_file = open( saveFile , 'w')
to_file.write('Copy\n')
to_file.write(contents)
to_file.close() 
    
# -------USER INPUT-------
name=raw_input("Type your name")
	
#-----FORMAT STRINGS------
#Multiple integer variable
print 'Value of %d +5 equal %d' % (i,n) # put them in brackets
#Mix integer and strings:
print 'Value of %d +5 equal %d, je mange du %s' % (i,n,m) #where %s refer to a string

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello"
print  format_string,'%s %s. Your current balance is %.2f $.' % data


#-----LIST---------
a= [] #create empty list
a*10  # repeat the sequence ten times
a[0:2] = [1, 12]    # Replace some items
a[0:2] = []   # Remove some
a[1:1] = ['bletch', 'xyzzy']   # Insert some
a[:0] = a   # Insert (a copy of) itself at the beginning
a[:] = []   # Clear the list: replace all items with an empty list
a[0] [0:3]  #get the first 3 elements of the first element
a.append(10)  #add to the list

#-----NESTED LIST---------
# it correspond to a list in a list
listA = [['Bob',25],['Mark',34]

listA[0] == ['Bob',25]  # the first element of the list is a list in itself
listA[0][1] == 25 # but you can still access the elements within the list


# -----LIST COMPREHENSION------
# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
  
# ------ TUPLES -----------  
tupple = ('a',3,-0.2)
print tupple[2]
# you can still access the elements of a tupple, but you can't modify them as a lits
# to see what tools you can use with tuples, use dir(tuple)
        
# ------SETS-------
# Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
print set("my name is Eric and Eric is my name".split())
# Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between other sets. 
# For example, say you have a list of participants in events A and B:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
# To find out which members attended both events, you may use the "intersection" method:
>>> a.intersection(b)
set(['John'])
>>> b.intersection(a)
set(['John'])
# To find out which members attended only one of the events, use the "symmetric_difference" method:
>>> a.symmetric_difference(b)
set(['Jill', 'Jake', 'Eric'])
>>> b.symmetric_difference(a)
set(['Jill', 'Jake', 'Eric'])
# To find out which members attended only one event and not the other, use the "difference" method:
>>> a.difference(b)
set(['Jake', 'Eric'])
>>> b.difference(a)
set(['Jill'])
# To receive a list of all participants, use the "union" method:
>>> a.union(b)
set(['Jill', 'Jake', 'John', 'Eric'])

#-----CONDITIONS----------
# BOLLEANS OPERATOR
if name == "John" and age == 23: # AND both need to be TRUE
if name == "John" or name == "Rick": # OR only one would give TRUE
# IN OPERATOR:
name = "John"
if name in ["John", "Rick"]: # 
# IF ELSE:
if name in a:
  print a
elif name in b:
  print b
else:
  print c
# THE IS OPERATOR:
#the "is" operator does not match the values of the variables, but the instances themselves
x = [1,2,3]
y = [1,2,3]
print x == y # Prints out True
print x is y # Prints out False


# THE NOT OPERATOR:
#Using "not" before a boolean expression inverts it:
print not False # Prints out True
print (not False) == (False) # Prints out False

# -------LOOP----------
# THE "FOR" LOOP:
#For loops iterate over a given sequence.
primes = [2,3,5,7]
for a in primes:
    print a
    
for x in range(0,10):


list = [['first',10],['second',20],['third',30]]

for x,y in caca:
    print y
    
#USING XRANGE
if you use a for in range (1million), it s going to take a lot of memory
not if you use xrange 

colors= ["red","blue"]
for color in colors:
	print color
	
#USING REVERSE LOOP
for color in reversed(colors):
	print color
	
# LOOPING OVER A COLLECTION AND INCICES
for i,color in enumerate(colors):
	print i, "-->", colors[i]
	
# LOOPING 2 COLLECTIONS
for name, color in zip(names,colors):
	print name,"-->",color
	# is massive on memory, izip is better
	
# LOOPING IN SORTED ORDER alphabetically
for i in sorted(seasons):
    print i	

for i in sorted(seasons, reverse= True): # reverse backward
    print i		
	
# CUSTOM SORT ORDER
print sorted(seasons, key = len)

# MULTIPLE EXIT POINTS IN LOOP   (GO TO)
def fond(seq.target):
    for i, value in enumerate(seq):
        if value == tgt:
            break
    else:        # output if the end of the list has been reached without the break
        return -1
    return i     

	#in every for loop , there is an if
	
# UNPACKING SEQUENCIES
d= "ours", 0x30, "ya@gmail.com"
dAnimal,dCode,dEmail = d
print dEmail
print dAnimal
	
# you can go for each element in a string thanks to the for loop:
thing = "spam!"
for c in thing:
    print c
# "WHILE" LOOP:
count = 0
while count < 5:
    print count
    count += 1
# WHILE ELSE and the "BREAK" and "CONTINUE" STATEMENT
# the ELSE in a WHILE STATEMENT, runs when the evaluation is False
# the Break quit a loop, and CONTINUE skip the rest and continue.
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    count += 1
    if num == 5:
        print "Sorry, you lose!"
        break
else:
    print "You win!"
#------FUNCTIONS---------------
def my_function(): # function without argument
	'''
	(number,number)-> number   help when you call the function
	whatever you type between tripled quoted string will be
	the result of the help on that function eg "help(my_function)"
	'''
    print "Hello From My Function!"
    
def my_function_with_args(username, greeting): # function with arguments
    print "Hello, %s , From My Function!, I wish you %s"%(username, greeting)
    
def sum_two_numbers(a, b):
  return a + b #return a value to the caller, using the keyword- 'return'
# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

#-------CLASSES AND OBJECTS--------
#Objects are an encapsulation of variables and functions into a single entity.
class MyClass(object):
      variable = "blah"

      def function(self):
           print "This is a message inside the class." # this is the creation of your class
in the function, use (self) so that you can call it later (eg print self.name)
myobjectx = MyClass()   # Then, create an object with this class
print myobjectx.variable  # this is how you get access to the variable withon the object, you can modify it
myobjectx.function()    # this is how you call the function

class Fruit(object):
	"""A class that makes various tasty fruits."""
	def __init__(self, name, color, flavor, poisonous):
		self.name = name
		self.color = color
		self.flavor = flavor
		self.poisonous = poisonous
	
	def description(self):
		print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)
		
	def is_edible(self):
		if not self.poisonous:
			print "Yep! I'm edible."
		else:
			print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

#--------CLASSES INHERITANCE--------~
# class DerivedClass(BaseClass), a class can inherit from anotehr class
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1= side1
        self.side2= side2
        self.side3= side3
# the class Triangle inherit from the class shape, then share Shape attributes and methods

# You can overwrite elements from a class when needed:
class PartTimeEmployee(Employee): # the Class "PartTimeEmployee" inherit from the class "Employee"
     def calculate_wage(self, hours): # the class "Employee" already has the function "calculate_wage", here we overwrite this function just for the class "PartTimeEmployee"
            self.hours = hours
            return hours * 12.00  # thanks to the overwrite, the math inside this function can now be different
            
# you can re access to an overwritten element of your class,
# You can directly access the attributes or methods of a superclass with Python's built-in super call.
class DerivedClass(Base):
   def some_method(self):
       super(DerivedClass, self).meth()   # Where meth() is a method from the base class. 
#  example
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
    
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
 
 def __init__(self, employee_name):
  self.employee_name = employee_name
 
 def calculate_wage(self, hours):
  self.hours = hours
  return hours * 12.00
  
 def full_time_wage(self, hours):
  return super(PartTimeEmployee, self).calculate_wage(hours) # get the function from the parent Class
        
milton = PartTimeEmployee("Milton")
print milton.calculate_wage(10)

#--------DICTIONNARIES---------
# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
# OR this way

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

>>>print phonebook["John"]
938477566

>>>'Jack' in phonebook
True

# add to a dictionnary
>>>phonebook["yann"] = 575454646

for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)
    
del phonebook["John"] # remove a value
phonebook.pop("John")  # remove a value

#-----MODULES AND PACKAGES----------
#Modules in Python are simply Python files with the .py extension, which implement a set of functions. 
# Modules are imported from other modules using the import command.
http://docs.python.org/2/library/ # Python standard library

import urllib   # import the library
urllib.urlopen(...)   # use it

dir(urllib)   #We can look for which functions are implemented in each module by using the dir function:
#When we find the function in the module we want to use, 
# we can read about it more using the help function, inside the Python interpreter
help(urllib.urlopen)  

# Writing Python modules is very simple. To create a module of your own, simply create a new .py file with the module name,
# and then import it using the Python file name (without the .py extension) using the import command.

# WRITING PACKAGES
# Packages are namespaces which contain multiple packages and modules themselves. 
# They are simply directories, but with a twist.

# Each package in Python is a directory which MUST contain a special file called __init__.py. 
# This file can be empty, and it indicates that the directory it contains is a Python package, 
# so it can be imported the same way a module can be imported.

# If we create a directory called foo, which marks the package name, 
# we can then create a module inside that package called bar. 
# We also must not forget to add the __init__.py file inside the foo directory.

# To use the module bar, we can import it in two ways:
import foo.bar
from foo import bar
# In the first method, we must use the foo prefix whenever we access the module bar. 
# In the second method, we don't, because we import the module to our module's namespace.

# The __init__.py file can also decide which modules the package exports as the API, 
# while keeping other modules internal, by overriding the __all__ variable, like so:
__init__.py:
__all__ = ["bar"]

# ------GENETARORS--------
http://www.learnpython.org/page/Generators

# -----MULTIPLE FUNCTION ARGUMENT------
# Every function in Python receives a predefined number of arguments, if declared normally, like this:
def foo(first, second, third, *therest):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(therest)
# The "therest" variable is a list of variables, which receives all arguments which were given to 
# the "foo" function after the first 3 arguments. So calling foo(1,2,3,4,5) will print out:
First: 1
Second: 2
Third: 3
And all the rest... [4, 5]
# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, 
# using the following syntax:
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("return") == "first":
        return first

...

result = bar(1, 2, 3, action = "sum", return = "first")
print "Result: %d" % result

# ------REGULAR EXPRESSION------
http://www.learnpython.org/page/Regular%20Expressions
http://docs.python.org/2/tutorial/errors.html#handling-exceptions
# But sometimes you don't want exceptions to completely stop the program. 
# You might want to do something special when an exception is raised. This is done in a try/except block.






  



