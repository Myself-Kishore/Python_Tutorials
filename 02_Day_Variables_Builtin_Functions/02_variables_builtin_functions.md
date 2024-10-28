<div align="center">
  <h1>🐍 Python Learning 🐍</h1> 
</div>
  
<div align="center">
  🧡🧡🧡 HAPPY CODING 🧡🧡🧡
</div>


<div align="center">
  <h1> Python Learning : Day 2 - Variables, Builtin Functions</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/msnkishore1702/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>


  <sub>Author :
  <a href="https://www.linkedin.com/in/msnkishore1702/" target="_blank">Sohatej Naga Kishore</a><br>
  <small> First Edition : October, 2024</small>
  </sub>
</div>


[<< Day 1](../readme.md) | [Day 3 >>](../03)

![Python_Tutorials](../Images/MaintopPython.jpeg)

- [📘 Day 2](#-day-2)
  - [Built in functions](#built-in-functions)
  - [Variables](#variables)
    - [Creating Variables](#creating-variables)
    - [Assigning Multiple Variables in a Line](#assigning-multiple-variables-in-a-line)
  - [Data Types](#data-types)
  - [Checking Data types and Casting](#checking-data-types-and-casting)


# 📘 Day 2

## Built in functions

In Python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, and _dir()_. In the following table you will see an exhaustive list of Python built-in functions taken from [python documentation](https://docs.python.org/3.9/library/functions.html).

![Built-in Functions](../Images/02Builtin_Functions.png)

Let us open the Python shell and start using some of the most common built-in functions. 
### From this point onward, I will be working with you in Jupyter Notebook for any Python development. Should you need instructions to install Jupyter Notebook on your PC, you can refer to this installation guide.
- For [Windows](https://youtu.be/bkOEYmyMtEU?si=zypl7ihyDSXmWwEG)
- For [Mac](https://youtu.be/drbaFALFKDg?si=_E1B9VPnAdUzQ7i_)

### Should you prefer to proceed with the Python Shell, you are welcome to do so.

Let us open the Jupyter Notebook and start using some of the most common built-in functions.

![Built-in functions](../Images/02sample_Builtin.png)

Let us practice more by using different built-in functions

![Dir Built in Functions](../Images/02reserved_keywords.png)

As you can see from the terminal above, Python has got reserved words. We do not use reserved words to declare variables or functions.
We will cover variables in the next section.

I believe, by now you are familiar with built-in functions. Let us do one more practice of built-in functions and we will move on to the next section.

![Min Max Sum](../Images/02min_max.png)

## Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored.
Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

Here are some example of valid variable names:

```shell
firstname
lastname
age
country
city
first_name
last_name
```

Invalid variables names

```shell
first-name
first@name
first$name
num-1
1num
```

## Creating Variables

Python has no command for declaring a variabel.
A variable is created the moment you first assign a value to it.

_Example:_

```py
x = 5
y = "John"
print(x)   # 5
print(y)   # John
```
Variable do not need to be declared with any particular type, and can even change type after they have been set.

```py
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

It gives the output : Sally
```

### Multiple Words Variable Names

Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:

### Camel Case
Each word, except the first, starts with a capital letter:
```py
myVariableName = "Kishore"
```
### Pascal Case
Each word starts with a capital letter:
```py
myVariableName = "Kishore"
```
### Snake Case
Each word is separated by an underscore character:
```py
my_variable_name = "John"
```
## Assigning Multiple Variables in a Line
Python allows you to assign values to multiple variables in one line:
_*Examples:*_
```py
x, y, z = "Ronaldo CR7", "Messi", "Neymar"
print(x)
print(y)
print(z)
```
Output
```
Ronaldo CR7
Messi
Neymar
```

```py
first_name, last_name, country, age, is_married = 'Kishore', 'Mada', 'India', 100, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```
Output:
```
Kishore Mada India 100 False
First name: Kishore
Last name:  Mada
Country:  India
Age:  100
Married:  False
```
### One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
```py
x = y = z = "Sunil Chhetri"
print(x)
print(y)
print(z)
```
Output:
```
Sunil Chhetri
```
Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables.

_Example:_
```py
first_name = input('What is your name: ')
age = int(input('How old are you? '))  # Convert age to an integer

print("Name:", first_name)
print("Age:", age)
```
Output:
```
What is your name: Kishore
How old are you? 22
Name: Kishore
Age: 22
```
## Data Types

Every value has a datatype, and variables can hold values. Python is a powerfully composed language; consequently, we don't have to characterize the sort of variable while announcing it. The interpreter binds the value implicitly to its type.
_Example :_
```py
x = "Hello World"         #	str	
x = 20	                  # int	
x = 20.5	                # float	
x = 1j                    #	complex
x = range(6)	            # range	
x = True	                # bool	
x = b"Hello"	            # bytes
x = True	                # bool	
x = b"Hello"	            # bytes
x = bytearray(5)	        # bytearray
x = memoryview(bytes(5))	# memoryview	
x = ["apple", "banana", "cherry"]      # list	
x = ("apple", "banana", "cherry")      # tuple	
x = {"name" : "John", "age" : 36}	     # dict	
x = {"apple", "banana", "cherry"}      # set	
x = frozenset({"apple", "banana", "cherry"})  # frozenset	
```
## Checking Data types and Casting
