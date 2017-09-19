PYTHON VERSIONS  
"""
Before the code to select to specify which version of python to use within the script
"""
#! python2
#! python3


\----------- CODE INTROSPECTION  -----------
"""
Code introspection is the ability to examine classes, functions and keywords to know what they are,
what they do and what they know.
Python provides several functions and utilities for code introspection.
"""
help() 
type()
get the type of your element
dir()
good to inspect Objects, will display the Method or Attribute Fields of a Class.
Internal Method have double underscore.
all the method you can apply to a type. For Instance if it's a string, you can then type x.replace()

hasattr()
id()
type()
repr()
callable()
issubclass()
isinstance()
__doc__
__name__





\-----------  VARIABLES   ----------- 
unpack variable
x,y  = (3,5)
Assign value to variables

\-----------  UNPACKING SEQUENCE

d= "ours", 0x30, "ya@gmail.com"
dAnimal,dCode,dEmail = d
print dEmail
print dAnimal

\----------- GLOBAL LOCAL 

global x = 5

\-----------  PRINT  COMMENTS   -----------

# Leave comment in one line

Triples quotes prints exactly the content.

"""
bla
bla
============
great to print design
============

"""

\n 
newline

In Python 3, use brackets
print ('hello')

To Print a string + string,    use +
print 'Value of ' + n
Where n is a string variable, can t add number with plus, use "," insteand or %d

To Print String  + integer variable
print 'Value of %d'  % i # where i is a integer variable
%d means “replace with something that is outside the string”
the second % replace the + sign
"hello" * 10  #print ten hello



\-----------  STRING  -----------

"string" + "string"  You won't have any space in between.
"string" , "string"  This will give you a space

Concatenation only works between strings.
word='Help'+A
A = 4
str(A)
Return 4 as a string

folder = r'C:\doc\scenes\'
raw format, all the content is a string regardless of any character inside
Or you can use Escape character (\) which block the functionality of any character
print 'I\'m'

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
astring.replace()
word[:2]    # The first two characters
word[2:]    # Everything except the first two characters
word[-2:]    # The last two characters
word[:-2]    # Everything except the last two characters
put "," at the end in order to avoid tu jump to the next line
s = "A bird in the hand..."

for i in s:
    if i == 'A' or i == 'a':
        print 'X',
		
\----------- JOIN STRING
d = ["caca","dadad","dasdasd"]
print "\\".join(d)
the "" before the joint enable you to set the separator.

\-----------FORMAT STRINGS
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




\----------- OPEN \ READ FILES -----------
\-----------OPEN
open(filename,mode) # mode can be 'r' to READ, 'w' for WRITING (erasing what is inside) or 'a' APPEND, add to the file

READ

with open(text) as f:
    print f.read()
Print full text

file = open(fileName,'r')
print file.readline() # read one line
print file.readlines() # read each line , add to a list
file.write("and another line")
file.close()
file.read(n), where "n" determines number of characters.
file.writelines(lines_of_text)

Return an empty string at the end of the file ""
so you can use a WHILE to read a file

line = file.readline()
while line != '':
    print(line)
    line = file.readline()

readline read and return the next line from the file
including the newline character if it exist
that's why there is a newline when you print that.

in order to correct that you can add a limit
to your print command in your WHILE LOOP

printline, end = ''

you can PRINT all lines more easily with the FOR LOOP
for line in file:
    printline, end = ''

or PRINT the whole file
print file.read()

--- OPEN WEBBROWSER----
import webrowser
webbrowser.open('http://...')


    
\-----------USER INPUT 
p2
name=raw_input("Type your name")
python 3
name = input("What's your name? ")

	



\-----------LIST / TUPLE

\-----------LIST

a= []                           #create empty list
a*10                            # repeat the sequence ten times
a[0:2] = [1, 12]                # Replace some items
a[0:2] = []                     # Remove some
a[1:1] = ['bletch', 'xyzzy']    # Insert some
a[:0] = a                       # Insert (a copy of) itself at the beginning
a[:] = []                       # Clear the list: replace all items with an empty list
a[0] [0:3]                      #get the first 3 elements of the first element
a.append(10)                    #add to the list
a.insert(2,10)                  # Add 10 to the index 2
a.remove(2)
a.index(1)                      # iv o index of number
a.count(6)
a.sort()                        # modiify and sort your list

\----------- NESTED LIST
# it correspond to a list in a list
listA = [['Bob',25],['Mark',34]

listA[0] == ['Bob',25]  # the first element of the list is a list in itself
listA[0][1] == 25 # but you can still access the elements within the list


\----------- LIST COMPREHENSION

List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
  
\-----------  TUPLE
"""
You can't modify it.
to see what tools you can use with tuples, use dir(tuple)
More efficient than list in term of speed and srorage if you know youwon't need t modify it.
"""
tupple = ('a',3,-0.2)
print tupple[2]




\----------- SET

Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
print set("my name is Eric and Eric is my name".split())
Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between other sets. 
For example, say you have a list of participants in events A and B:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
To find out which members attended both events, you may use the "intersection" method:
>>> a.intersection(b)
set(['John'])
>>> b.intersection(a)
set(['John'])
To find out which members attended only one of the events, use the "symmetric_difference" method:
>>> a.symmetric_difference(b)
set(['Jill', 'Jake', 'Eric'])
>>> b.symmetric_difference(a)
set(['Jill', 'Jake', 'Eric'])
To find out which members attended only one event and not the other, use the "difference" method:
>>> a.difference(b)
set(['Jake', 'Eric'])
>>> b.difference(a)
set(['Jill'])
To receive a list of all participants, use the "union" method:
>>> a.union(b)
set(['Jill', 'Jake', 'John', 'Eric'])

\-----------  CONDITIONAL EXECUTION ------------------
\------------ IF ---------------------

\-----------TRY EXCEPT 
"""
sometimes your code could run into an error TRACEBACK, then it blocks.
You can use Try Except to keep on going by giving him an alternative way out.
"""
x='Hello'
try:
    out=int(x)          # error as x is a string
except Exception as e:
    print e

\ COMPARISON OPERATOR
<= less equal
== equal
!= not equal

if x != y
means if Not Equal

if name == "John" and age == 23:
They both need to be True

if name == "John" or name == "Rick":
Only one has to be True

\------- elif
Multi way
if x = 2:
    print("y")
elif x > 10:
    prin("n")
else :
    print("f")


\-----------  IN OPERATOR

name = "John"
if name in ["John", "Rick"]:

IF ELSE ----

if name in a:
  print a
elif name in b:
  print b
else:
  print c

\----------- IS OPERATOR

The "is" operator does not match the values of the variables, but the instances themselves
x = [1,2,3]
y = [1,2,3]
print x == y # Prints out True
print x is y # Prints out False


\----------- NOT OPERATOR ----

Using "not" before a boolean expression inverts it:
print not False
Prints out True

print (not False) == (False)
Prints out False

\-----------  FOR LOOP

For loops iterate over a given sequence.
Better counter loop, but could se WHILE LOOP as well.

primes = [2,3,5,7]
for a in primes:
    print a

for x in xrange(0,10):
    print x
range will give you from zero to, not including your value, so 0 to 9.

list = [['first',10],['second',20],['third',30]]
for x,y in list:
    print y

REVERSE LOOP
for color in reversed(colorsList):
	print color
	
#LOOPING OVER A COLLECTION AND INCICES
for i,color in enumerate(colors):
	print i, "-->", colors[i]
	
#LOOPING 2 COLLECTIONS
for name, color in zip(names,colors):
	print name,"-->",color
	# is massive on memory, izip is better
	
LOOPING IN SORTED ORDER alphabetically
for i in sorted(seasons):
    print i	

for i in sorted(seasons, reverse= True): # reverse backward
    print i		
	
\-----------  CUSTOM SORT ORDER
print sorted(seasons, key = len)

MULTIPLE EXIT POINTS IN LOOP   (GO TO)
def fond(seq.target):
    for i, value in enumerate(seq):
        if value == tgt:
            break
    else:        # output if the end of the list has been reached without the break
        return -1
    return i     

	#in every for loop , there is an if
	

	

\-----------  WHILE LOOP ------------------------
Use that as a counter

count = 0
while count < 5:
    print count
    count += 1    This increment by value 1


\-----------  WHILE ELSE ----
the ELSE in a WHILE STATEMENT, runs when the evaluation is False
the Break quit a loop, and CONTINUE skip the rest and continue, goes back to the top of your loop.

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


\-----------  WHILE TRUE
Creates an infinite loop

while True:
    print 'action'

\-----------  FUNCTION

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

You can prefill with default vales.
def simple(num1,num2=10)
simple(2) # just 1 argument is enough as num 2 is defined already

RETURN SEVERAL VARIABLES
x = [("Sc01","blabla","BGmatte")]
def detailBG():
    for sc in x:
        scene = sc[0]
        Brief = sc[1]
        BGtype = sc[2]
    return(scene,Brief,BGtype)

Gscene, Gbrief, GbgType = detailBG()




\-----------  CLASSES AND OBJECTS

"""
Objects are an encapsulation of variables and functions into a single entity.
Class : a template, dog
method : A defined capability of a class
Field or attribute : A bit of data in a class
Object or Instance: an instance of a class
def__init__ : a constructor  used to set up variables.
"""

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

    def__del__(self):
        prin("Object destructed")

lemon = Fruit("lemon", "yellow", "sour", False)
# this line create the object using the class

lemon.description()
lemon.is_edible()

lemon = 10
"""
lemon is no longer an object, by assigning 10, you made it an Int, this destroys the Object and run the destroy method.
"""

\-----------  CLASSES INHERITANCE
"""
Create a new Class from an existing class, extending it
"""
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

\-----------  DICTIONNARIES
# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.

phonebook = {}
phonebook["John"] = [938477566 , 'red']
phonebook["Jack"] = [938377264 , 'blue']


# OR this way

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

print phonebook["John"][1]

'Jack' in phonebook
True

Add to a dictionnary
phonebook["yann"] = 575454646

for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)
    
del phonebook["John"] # remove a value
phonebook.pop("John")  # remove a value

\-----------READ
with open("../tmp.txt","r") as scoreFile:  # open as Read mode, ../ means going back one folder from the current one
    scoreFileReader = csv.reader(scoreFile)
    scoreList = []  # empty list to receive data
    for row in scoreFileReader:
        if len (row) != 0:  # check the file has row
            scoreList = scoreList + [row]
scoreFile.close()  

\-----------WRITE
x= "bla"
y = "boo"
with open("tmp.txt", "w") as scoreFile:
    scoreFileWriter = csv.writer(scoreFile)
    scoreFileWriter.writerow([ x , y ])

scoreFile.close()

\-----------  GENETARORS
http://www.learnpython.org/page/Generators

MULTIPLE FUNCTION ARGUMENT
 Every function in Python receives a predefined number of arguments, if declared normally, like this:
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



result = bar(1, 2, 3, action = "sum", return = "first")
print "Result: %d" % result

\-----------  MODULES / PACKAGES
\----------- MODULE 

Modules in Python are simply Python files with the .py extension, which implement a set of functions.

Python is looking for module in Local, Lib and sys packages, or system PATH in env variable.
Python comes with Modules
C\Python27\Lib
Third party Modules
C\Python27\Site-package

To create a module of your own, simply create a new .py file with the module name,
and then import it using the Python file name (without the .py extension) using the import command.

import urllib   # import the library which is the name of the .py file, the file name is the module.
urllib.urlopen(...)   # use the function inside module

When your import a module, it'll run the full script.
To avoid that, add:
if __name__ == '__main__':
    print "blabla"    # This portion will only be read if you're calling the name of the file

The built-in function dir() is used to find out which names a module defines
Print dir(urllib)		#not sure about the print
Without arguments, dir() lists the names you have defined currently
dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module __builtin__:

\----------- IMPORT MODULE


import statistics as s # you call statistic by typing only s
x = s.variance(example_list)

from statistics import variance         # you don't have to type statistics anymore
from statistics import variance as v    # you don t have to type statistic, and you can call variance just with v
from statistic import *                 # import all

When importing a module, python will look in Local, sitepackages, lib


\-----------  WRITE PACKAGE 

Packages are namespaces which contain multiple packages and modules themselves.
They are simply directories, but with a twist.

Each package in Python is a directory which MUST contain a special file called __init__.py.
This file can be empty, and it indicates that the directory it contains is a Python package,
so it can be imported the same way a module can be imported.

If we create a directory called foo, which marks the package name,
we can then create a module inside that package called bar.
We also must not forget to add the __init__.py file inside the foo directory.

To use the module bar, we can import it in two ways:
import foo.bar
from foo import bar
In the first method, we must use the foo prefix whenever we access the module bar.
In the second method, we don't, because we import the module to our module's namespace.

The __init__.py file can also decide which modules the package exports as the API,
while keeping other modules internal, by overriding the __all__ variable, like so:
__init__.py:
__all__ = ["bar"]
PIP
Pip will allow you to install modules

To install PIP download and run
To run in a specific version of python, just add your version at the top and run.
#! Python3
Type import pip to check if you have installed it correctly.

Now you can use pip install to install module from Pypi

In CMD type 
pip list 		# to see all current module.
Pip install numPy 	# installation module (numPy is module name)

pip can install wheel file
http://www.lfd.uci.edu/~gohlke/pythonlibs/

Downlolad your wheel, and go in CMD and type
pip install numPy.whl

PPRINT
Print in a more readable way
pprint(dir(shotgun_api3))
pprint(help(sg.find))

\----------- BOKEH
Data visualisation
Weblink

GSPREAD MODULE
Python for google spreadsheet
ID
Details about credi

When you want to reach a sheet, you need to share (contact) the google spreadsheet with the value of json_key['client_email'], otherwise you won’t get access

cell_list = wks.range('A1:B7')		#Access range

val = wks.cell(1, 2).value		# acces single cell (row, Column)

wks.update_acell('B2', "updated")	#update cell

EXAMPLE
def lookFor(search,replace,range):
    """
    search and replace cell value in range
    :param search: value to search
    :param replace: new value
    :param range : 'A1:C6'
    """
    cell_list = wks.range(range)

    for cell in cell_list:
        if cell.value == search:
            cell.value = replace

    # Update in batch
    wks.update_cells(cell_list)


\----------- STATISTICS 
import statistics

\----------- OS 
import os
curDir = os.getcwd()

os.mkdir('newDir') create new directory
os.rename('newDir'. 'newDir2')
os.rmdir('newDir2')
os.startfile(prop_folder)	# open file

\----------- SYS
import sys

\-----------URLLIB URLPARSE
access the internet

import urllib

x = urllib.urlopen('https://www.google.com')
print x.read()              # print source code

You'll have to parse the HTML to extract data

\----------- CSV 
Comma Separated Variable
This module enables you to read and extract data from a .csv file (could be text file)

with open('example.csv') as csvfile:        # (“file.txt”, “mode”) W write A append R read
    readCSV = csv.reader(csvfile, delimiter=',')        #split by the delimiter provided

    dates = []
    colours = []                                        #empty list to store next extracted data

    for row in readCSV:                                 #parse csv file
        colour = row[3]
        date = [0]

        dates.append(date)                              # add to the list
        colours.append(colour)


\-----------PYPERCLIP
Copy to clipboard



\-----------SHOTGUN
Install API
API documentation

pip install git+git://github.com/shotgunsoftware/python-api.git

Setup your access
Go to your Setting / Script, create a new script
You’ll need your script name and ID key to connect

Schema_read
Returns properties for all fields for all entities.
pprint(sg.schema_read(“Asset”))

To get info about an element in Shotgun, RMB on the column you need more info, you’ll get its code name to be used in shotgun api
Code: Asset Name		

sg.find()
Returns a minimum of the 'id' and 'type' fields representing the entity type and id of the record(s) returned. 
An episode is sequence

In your User tab drop down menu, select Site Preference, here you can see a list of entities.

Filter needs to be a nested list.
The result will be a list of dictionaries
For bg in backgrouns:
	Print bg[“code”] 	it’s print name
	bg.get(“code”) 	.get will work even if bg doesn’t have a code

You can loop a list in reverse so that you can delete elements from the list without re ordering them.


TKINTER
Info

from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def say_hi(self):
        messagebox.showinfo("TAWOG" , "Your Gdoc has been updated")

    def createWidgets(self):

        #textInfo = Label(text="UPDATE?")
        #textInfo.pack({"side": "top"})

        self.question = Label(self)
        self.question["text"] = "Update your Gdoc?"
        self.question.pack({"side": "top"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "right"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "YES",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()




