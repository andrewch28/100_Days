# ***100 Days of Python - Insights.***
## ***Keyboard Shortcuts***
ctrl + /    (make everything a comment # or turn it to code from #)<br />
ctrl + z    (undo)<br />
ctrl + y    (undo ctrl + z )<br />
alt + shift (ability to change a number of nearest lines at the same time)
## ***Day 1 - Day 11:***

1. Escape character:
```ruby
\
```
2. Starting a new line:
```ruby
\n
```
3. Addidng two decimal digits:
```ruby
"{:.2f}".format(bill)
```
4. Counting a character:
```ruby
name = turtle
counter = name.count('t')
```
5. Random library:
```ruby
import random
random.random()  #returns a float between 0 and 1
random.randint(1,10) #random integer between 1 and 10, including 10
```
6. List:
```ruby
fruits = ['apple', 'peach']
fruits.append('strawberry')
fruits.extend(['banana', 'orange'])

fruits.index('banana')
```
7. Rounding:
```ruby
int(163,7) = 163
round(163,7) = 164
```
8. Trick for getting indexes:
```ruby
word = 'camel'
guess_letter = 'c'
for position in range(len(word)):
    if word[position] == guess_letter:
        print('Correct!')
```
9. Join
```ruby
display = ['a', 'b', 'c']
connect = " ".join(display)
```

10. Functions
```ruby
def my_function(something)
...
    my_function(123)
```
In this case **something** is a parameter and **123** is an argument.<br />

There are two types of arguments: keyword arguments and positional arguments. The last ones' are not specified in any way and are assigned depending on their order (like 123). Keyword arguments are clearly specified like **my_function(something = 123)**.

11. Math library:
```ruby
import math
math.ceil(3,1) = 4  #rounds float to the next integer (not the closest)
```
12. Don't forget
```ruby
shift_amount *= -1
```
13. Don't forget 2

By convention we should use this syntax:
```ruby
for _ in range(3):
    print('Hey!')
    #remember that range DOESN'T include the last number
    #here it will print out 0, 1, 2
```

14. Remove:
```ruby
list.remove('apple')
```
## ***Day 12. Scope.***
**Local** scope is created only by functions - when you create a variable or a function inside another function. That way they are only accessible inside the function where they are defined.<br />
<br />
If a variable is defined outside the function it is then called a **global** variable or function, which means that it can be accessed from anywhere.<br />
To change global variable inside a local function:
```ruby
enemies = 1
def function():
    global enemies
    enemies += 1
```
Now the global value of enemies is 2<br />

Convention regarding **Constant:**<br />
If you want to show that the variable is a constant and shoud not be changed, you should use uppercase:
```ruby
PI = 3.1459
```

## ***Day 13. Debugging.***
1) Describe the problem
2) Reproduce the Bug - find out when the mistake occures and when it doesn't
3) Play computer - go through the code line by line
4) Print is your friend
5) Debugger
6) Take a break and come back later
7) Run the code often
8) StackOverflow!

## ***Day 14.***
Nothing new, just a project.
## ***Day 15. Coffee Machine.***
There are mutable and **immutable** objects in python:<br />
String and int are immutable and therefore we **can not** modify them, but only assign a new value. As a result we have to use **function global** to be able to change the value of a global value inside of a certain fucntion.<br />
However, if we talk about **lists or dictionaries** - they are **mutable** and that is why we **don't have** to use **global** function, because when we call them inside of a fuction we do not reassign them, but we modify (mutate) them, which will be done automatically.
## ***Day 16. Object-Oriented Programming.***
Before that day we focused only on a procedural programming - when one procedure is executed after another one.<br />
<br />
In OOP we have a so-called **Class**, which is basically a blueprint for a certain **object**. When we define a Class we give it certain **attributes** (variables) and **methods** (functions).<br />
<br />
Let's assume that we have a class called CarBlueprint (notice that the name of a class must always be capitalized - this is a PascalCase).<br />
<br />
We can create an object from this blueprint with a following syntax:
```ruby
car = CarBlueprint()  #car is an object, that has certain attributes and methods

car.speed #this is how we access an attribute (variable) speed, which is available for this class

car.stop() #and this is how we can access a method of this object
```

To search for various packages visit **pypi.org** or rewatch Lecture 149.
## ***Day 17. The Quiz Project & the benefits of OOP.***
To create a **class** we use:
```ruby
class User:
    pass

user_1 = User()             #we create an object called user_1 from a class User
user_1.id = '001'           #we set id attribute to a value 001
user_1.username = 'angela'  #we set username attribute to the value angela
```
Remember that an attribute is basically a variable that is associated with an object.<br />
<br />
How can I specify all these attributes, when I create my object from the **class**?<br />
**Attributes:**

```ruby
class Car:
    def __init__(self):
    #to initialise attributes

    #__init__ function is going to be automatically called any time you create a new object from this class
```
```ruby
class Car:               #we pass seats value as a parameter
    def __init__(self, seats):
        self.seats = seats #--- seats is a value to which attribute is equal to
#       |       |
#       |       |
#       |     #seats is the name of an attribute
#self is a name of an object
```
To set certain attribute's values by default we use this syntax:
```ruby
class Car():
    def __init__(self):
        self.speed = 0
```

**Methods:**<br />
We create a class called Car and then initialize object my_car with 5 seats in it by passing an argument 5 inside a Class function.<br />
Then we use a function called enter_race_mode() on an object my_car which is supposed to change the number of seats to two, which is exactly what is going to happen after we execute this code.

```ruby
class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode():
        self.seats = 2

my_car = Car(5)
print(my_car.seats) #answer is 5

my_car.enter_race_mode()
print(my_car.seats) #answer is 2
```
If we want to change the way our code is distributed over the page we should go to the **code** at the top of the page and then click on **class**.

## ***Day 18. Turtle and the GUI.***
**Ways to import a module:**<br >

First option:
```ruby
import turtle
timmy = turtle.Turtle()
```
Second option (best one):
```ruby
from turtle import Turtle
timmy = Turtle()
```
Third option (not recommended):
```ruby
from turtle import *  #imports everything from the module at once
timmy = Turtle()
```
Fourth option (aliases):
```ruby
import turtle as t
timmy = t.Turtle()
```

**Tuples:**
```ruby
my_tuple = (1, 3, 8) #the key difference comparing with lists is that tuples are immutable

#If you nevertheless want to modify it, you shall convert it into a list:
list(my_tuple)
```
## ***Day 19. Instances, State and Higher Order Functions.***
When we use a function as an argument (pass it into another function) we **don't** add the **parentheses!** Because parentheses trigger the function to happen then and there, while we want to use it later.

After passing the function to another function, we can use the passed fucntion inside higher order function.

**Higher Order Function** - basically a function that takes another function as an input and then works with it inside the body.
# THINK ABOUT ADDING AN EXAMPLE OF A HIGHER OREDER FUNCTION
**instances and state:**<br >
All objects are instances of classes, and conversely, all instances of classes are objects. To create an object from a class means to instantiate it. We are creating an instance of the class Turtle. However each instance may have different features, while the object is simply their common characteristic.
```ruby
timmy = Turtle()
timme.color = green #the state of timmy's color attribute is green
```
## ***Day 20. Snake Game Part 1.***
!REMEMBER:
Everything we write under ```def __init__(self):``` will be automatically executed when we create an object! If we put a method there, it will be called automatically as well! (lecture 187, 3:19). If we create a method inside a class and we want it to be executed automatically we should use ```self.move()``` under ```def __init__(self):```  (considering we have already defined method move outside of ```__init__```)
## ***Day 21. Snake Game Part 2. Inheritance and List slicing.***
The idea is that one class is able to inherit all the attributes and methods of the over one:

We have a class called Fish
```ruby
class Fish:
    def __init__(self):
```
In order to get this fish class to inherit from Animal class:
```ruby
class Fish (Animal): #in ( ) we specify the class from which we want to inherit
    def __init__(self):
        super().__init__() # allows us to get all the attributes and methods of an Animal Class
```

In this case Fish is called ***subclass*** and Animal is ***superclass***.

More complicated example:
```ruby
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe() #the function is executed as in the class from which we inhereted it, and afterwards the line below will be additionally executed
        print("doing this underwater")

    def swim(self):
        print("moving in water.")
```
## ***Day 22. The Pong Game***
This was a cool game) but it was generally a revision, so nothing new here.
## ***Day 23. Capstone Project Turtle.***
The code is not that important, it is all about thinking and creating an approach for every problem.

Rewatch Lecture 218 from time to time.
## ***Day 24. File, Directories and Paths.***
Some syntax for FILE I/O

```ruby
file = open("my_file.txt")
contents = file.read()
file.close()
```

```ruby
with open("my_file.txt") as file:
    contents = file.read()
```
```ruby
with open("my_file.txt", "w") as file:
    file.write("Hello, there!")
```
Absolute File Path:<br >
**/work/project/talk.ppt**

Relative File Path: <br >
Working directory is a folder that we are currently working from. And relative path shows us the path from this current folder to the needed file. Imagine that we are in a **folder project** and this is the folder where **file talk.ppt** is located, then our relative path will be **./talk.ppt(  ./ basically mean to seek in the current folder).**

**../ means to go the previous outer folder**. If project folder is in a work folder this syntax will get us into work folder.

For more information check out DAY24 Lectures or your notebook.

Methods:

1. readlines() method:

returns all lines in the file as a list, where each line is an item in the list object

2. strip() method:

removes spaces at the beginning and at the end of the string

## ***Day 25. Working with CSV Data and the Pandas library.***

### CSV, reader
```ruby
import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
#we get a csv object, if we want to print it, we have to iterate over it
```

### Pandas
```ruby
import pandas as pd
df = pd.read_csv(" ")
print(df['temp'])
```
There are two types of data in pandas: **DataFrame and Series**

A **DataFrame** is a data structure such as our weather_date, which contains multiple columns. However if we select one column from the DataFrame: ```df['temp']``` it's type is going to be **Series**.

```ruby
print(type(df)) #this is a DataFrame
print(type(df['temp'])) #this is a Series
```

Some methods for pandas Series:
```ruby
s.to_csv("filename.csv") #to convert df into a csv
```
```ruby
s.to_dict() #to convert df into a dictionary
```
```ruby
s.to_list() #to convert df into a list
```
```ruby
s.mean()
```

Comment on the difference between functions and methods:

Functions are independent blocks of code that can be called from anywhere, while methods are tied to objects or classes and need an object or class instance to be invoked

Getting data in columns:
- ```df['condition']```
- ```df.condition```
- These approaches have the same result

Getting data in rows:
- ```df[df['day'] == 'Monday']```


Creating df from scratch:
```ruby
data_dict = {
    'students' : [ ],
    'scores' : [ ],
}

df = pd.DataFrame(data_dict)    # DataFrame is basically a class
```
If you have a 1x1 Series and you want to extract its value:

To fully understand better check out the documentation

```df['temp'].item()```

## ***Day 26. List comprehension and the NATO Alphabet.***

### List comprehension:

```new_list = [new_item for item in list]```

if we have a list ```numbers = [1, 2, 3]``` and we want to add 1 to each element of the list, instead of a loop we can use list comprehension:
```new_list = [n+1 for n in numbers]```

### Conditional list comprehension:
```new_list = [new_item for item in list if test]```

Imagine we have a list of names: ```names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']``` and we want to print out those which are shorter than 5 characters long:

```short_names = [name for name in names if len(name) < 5]```

Random thoughts:

1. Python sequences - list, range, string, tuple. The thing is that they all have specific order.

2. !Remember that range excludes the last number

3. Methods:
- ```string.upper()```
- ```string.lower()```

### Dictionary Comprehension

new_dict = {new_key:new_value for item in list}

new_dict = {newe_key:new_value for key, value in dict.items()}

```.items()``` returns an iterable object through which we can itterate and get key,value pairs one by one.

Example:
1. We have a list of student and we want to assign to each one of them a random score ```students_scores = {student : random.randint(1,100) for student in names}```

2. We want to get students and their score printed out for those who got more than 60. ```passed_students = {student:score for (student, score) in students_scores.items() if score > 60}```

### How to iterate over Pandas DataFrame
```ruby
for (index, row) in student_data_frame.iterrows():
    print(row)  #each row is a pandas Series object, which means we can tap into the row by printing
    print(row.student)
```
# REVISE ITTEROWS()
## ***Day 27.GUI with Tkinter and Function argumnets.***

Until now we knew only positional and keyword arguments

### Advance arguments
**1. Arguments with default values**
```ruby
def my_function(a=1, b=2, c=3)
    ...
my_function() #we can call function with no arg, cause they become optional once we have set a default value for them
```

If we have a default atguments it makes it optional and we don't have to specify it when calling the function and thosee which do not have any default values are required to be specified.

**2. Unlimited Positional Arguments - ```*args```**
```ruby
def add(*args) #the funstion accepts any number of arguments
    for n in args:
        print(n)

add(2, 5, 6, 7)
```
```(*args)``` collect all the argumnets into a tuple:
```ruby
def add(*args)
    print(args) #this will return a tuple of arguments

    print(type(args)) #tuple
    print(args[0]) #to get the first argument / first element of the tuple
```
**3. Many Keyworded Arguments - ```**kwargs```**

The difference with *args is that in this casee arguments are keyworded and the fact that ```*args``` returns a tuple and ```**kwargs``` return a dictionary

```ruby
def calculate(**kwargs):
    print(kwargs) #print dictionary where key is the name of the argument and the value is it's value

calculate(add=3, multiply=5)

#result is:
    {'add':3, 'multiply':5}
```

Classes
```ruby
class Car:

    def __init__(self, **kw):
        self.make = kw["kw"]
        self.model = kw["model"]

my_car = Car(make='Nissan', model='Skyline')
```

However if dont's specify any of the arguments we wll get an error, to avoid this we should use another approach:

It works the same, however if there are no arguments ```get()``` is goint to return 0
```ruby
class Car:

    def __init__(self, **kwargs):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='Nissan', model='Skyline')
```

### Tkinter
```ruby
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
```

### Tkinter Layout Managers
1. **Pack**. Places each of the widgets next to each other going from top to bottom. We can modify it a bit with ```side = 'left'``` or ```side = 'right'```. It's hard to specify a precise location.

2. **Place**. All about precise positioning. ```my_label.place(x=0, y=0)``` - top left corner. Remember that for the object to be seen we must always use one of the three layouts.

3. **Grid**. You can divide the window into manu columns and rows. ```my_label.grid(column=0, row=0)```. !Notice you can't mix pack and grid in the same program.


### Add info about config if needed!

## ***Day 28. Tkinter, Dynamic typing and the Pomodoro GUI app.***

### Canvas widget

```ruby
canvas = Canvas(width = 200, height = 224)
tomato_img = PhotoImage(file = "tomato.png") # to convert png into img
canvas.create_image(100, 112, image = tomato_img)
canvas.pack() #or other layout manager
```

### math module

```ruby
import math

math.floor(5,7) = 5 #The math.floor() method rounds a number DOWN to the nearest integer and returns the result.

#To round a number UP to the nearest integer, look at the math.ceil() method.
math.ceil(5,1) = 6
```
## ***Day 29. Building a password Manager GUI App with Tkinter.***
```ruby
b = Label(...)
b.grid(row=2, column=0, columnspam=2) #columnspan represents how many columns will the label take - in this case it will take 2 columns = column number 0 and column number 1
```
To keep the coursor inside the entry widget by default:
```ruby
website_entry.focus()
```
To set a default value at the entry widget:
```ruby
email_entry.insert(0, "email") # at the beginning
email_entry.insert(END, "email") # at the end
```
To get value from the entry widget:
```ruby
email = email_entry.get()
#email stores the value which was inserted in the entry widget
```

```ruby
letters = ["c", "s", "k", "a"]
club = "".join(letters) #returns a string object
```
## ***Day 30. Errors, Exceptions and JSON Data.***
There are a number of errors:
- FileNotFoundError
- KeyError
-IndexError
### Catching Exceptions
1) try: - something that might cause an exception
2) except: - Do this if there was an exception
3) else: - Do this if there was NO exception (success)
4) finally: - Do this no matter what happens
It is a convention to specify an exception we want to catch:
```ruby
except FileNotFoundError:
```
Getting error message:
```ruby
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
```
Raising exceptions:
```ruby
raise KeyError("This is an error i made up"):
```
### JSON
```ruby
import json

json.dump() #write
json.load() #read
json.update() #update
```
Writing:
```ruby
new_data = {
    website:{
        "email":email,
        "password":password,
    }
}
with open ("data.json", "w") as file:
    json.dump(new_data, file, indent=4)
````
Reading:
```ruby
with open ("data.json", "r") as file:
    data = json.load(file)
````
Updating:
```ruby
with open ("data.json", "r") as file:
    #Reading old data
    data = json.load(file)
    #Updating old data with new data
    data.update(new_data)
with open ("data.json", "w") as file:
    #Saving updated data
    json.dump(new_data, file, indent=4)
```
## ***Day 31. Capstone Project. Flashy cards***
### iterrows( )
```ruby
to_learn = df.to_dict(orient="records")

#Creates a list of dictionary where each row is a dictinoary which consists out of column name : value pairs)
#[{'French':'partie', 'English':'part'}, {...}, {...}]
#[{'name': 'Art', 'email': 'andrewch2817@gmail.com', 'year': 1961, 'month': 6, 'day': 3},
# {'name': 'Kate', 'email': 'andrewch2817@gmail.com', 'year': 1961, 'month': 7, 'day': 3}]
```
The whole day was about creating the project, so to properly revise it, the best option is to head over to the code of the project itself
## ***Day 32. Send Email(smtplib) and Manage Dates (datetime).***
### smtplib
```ruby
import smptlib #module for sending emails
```
Example:
```ruby
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #ensuring secure connection 
    connection.login(user=USERNAME, password=PASSWORD)
    connection.sendmail(from_addr=USERNAME,
                        to_addrs=USERNAME,
                        msg=f"Subject: Happy birthday!\n\nHave a nice day!")
                        #we first specify a subject, then the text of the message
```
### datetime
```ruby
import datetime
```
```ruby
now = datetime.datetime.now()

#datetime is a module where there is a class also called datetime, which has method now, which returns current date
```
```ruby
now = datetime.datetime.now()
year = now.year #year attribute to return the year from the date
```
There are other attributes like ```.month```, ```.day```

There is also a method to return the day of the week (in numeric value from 0 to 6)
```ruby
day_of_week = now.weekday()
```
Creating a datetime object:
```ruby
date_of_birth = datetime.datetime(year=2003, month=10, day=28)
```

!Notice replace doesn't change the original variable, therefore if you want to save the replacement you have to save the result in another variable
```ruby
text = text.replace("[NAME]", birthdays[current_day]["name"])
```
### iterrows( ) and dictionary comprehension
```ruby
to_learn = df.to_dict(orient="records")

#Creates a list of dictionary where each row is a dictinoary which consists out of column name : value pairs)
#[{'French':'partie', 'English':'part'}, {...}, {...}]
#[{'name': 'Art', 'email': 'andrewch2817@gmail.com', 'year': 1961, 'month': 6, 'day': 3},
#{'name': 'Kate', 'email': 'andrewch2817@gmail.com', 'year': 1961, 'month': 7, 'day': 3}]
```
### Reading a file
Notice that ```readlines()``` returns every line as an element of the list,<br >
while ```read()``` reads the file as it is and you then can print it out the same way as it is stored in the file
