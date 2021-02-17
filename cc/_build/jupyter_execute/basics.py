# Test File

<img align="left" src="https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/CC_BY.png"><br />

Created by [Nathan Kelber](http://nkelber.com) and Ted Lawless for [JSTOR Labs](https://labs.jstor.org/) under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/)<br />
For questions/comments/improvements, email nathan.kelber@ithaka.org.<br />
___

**Python Basics I**

**Description:** This lesson describes [operators](https://docs.tdm-pilot.org/key-terms/#operator), [expressions](https://docs.tdm-pilot.org/key-terms/#expression), data types, [variables](https://docs.tdm-pilot.org/key-terms/#variable), and basic [functions](https://docs.tdm-pilot.org/key-terms/#function). Complete this lesson if you are familiar with [Jupyter notebooks](https://docs.tdm-pilot.org/key-terms/#jupyter-notebook) or have completed *Getting Started with Jupyter Notebooks*, but do not have any experience with [Python](https://docs.tdm-pilot.org/key-terms/#python) programming. This is part 1 of 3 in the series *Python Basics* that will prepare you to do text analysis using the [Python](https://docs.tdm-pilot.org/key-terms/#python) programming language.

**Use Case:** For Learners (Detailed explanation, not ideal for researchers)

**Difficulty:** Beginner

**Completion Time:** 75 minutes

**Knowledge Required:** 
* [Getting Started with Jupyter Notebooks](./getting-started-with-jupyter.ipynb)

**Knowledge Recommended:** None

**Data Format:** None

**Libraries Used:** None

**Research Pipeline:** None
___

[![Getting Started with Jupyter Notebooks](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/video/python-basics.png)](https://www.youtube.com/watch?v=90wFLSjlFL8)

## Introduction

[Python](https://docs.tdm-pilot.org/key-terms/#python) is the fastest-growing language in computer programming. Learning [Python](https://docs.tdm-pilot.org/key-terms/#python) is a great choice because [Python](https://docs.tdm-pilot.org/key-terms/#python) is:

* Widely-adopted in the digital humanities and data science
* Regarded as an easy-to-learn language
* Flexible, having wide support for working with numerical and textual data 
* A skill desired by employers in academic, non-profit, and private sectors

The second most-popular language for digital humanities and data science work is [R](https://docs.tdm-pilot.org/key-terms/#r). We plan to create additional support for learning [R](https://docs.tdm-pilot.org/key-terms/#r) soon. If you are interested in helping develop open educational resources for [R](https://docs.tdm-pilot.org/key-terms/#r), please reach out to Nathan Kelber (nathan.kelber@ithaka.org).

The skills you'll learn in *Python Basics* I-III are general-purpose [Python](https://docs.tdm-pilot.org/key-terms/#python) skills, applicable for any of the text analysis notebooks that you may explore later. They are also widely applicable to many other kinds of tasks in [Python](https://docs.tdm-pilot.org/key-terms/#python) beyond text analysis.

**Making Mistakes is Important**

Every programmer at every skill level gets errors in their code. Making mistakes is how we all learn to program. Programming is a little like solving a puzzle where the goal is to get the desired outcome through a series of attempts. You won't solve the puzzle if you're afraid to test if the pieces match. An error message will not break your computer. Remember, you can always reload a notebook if it stops working properly or you misplace an important piece of code. Under the edit menu, there is an option to undo changes. (Alternatively, you can use **command z** on Mac and **control z** on Windows.) To learn any skill, you need to be willing to play and experiment. Programming is no different.

# Expressions and Operators

The simplest form of Python programming is an [expression](https://docs.tdm-pilot.org/key-terms/#expression) using an [operator](https://docs.tdm-pilot.org/key-terms/#operator). An [expression](https://docs.tdm-pilot.org/key-terms/#expression) is a simple mathematical statement like:

> 1 + 1

The [operator](https://docs.tdm-pilot.org/key-terms/#operator) in this case is `+`, sometimes called "plus" or "addition". Try this operation in the code box below. Remember to click the "Run" button or press Ctrl + Enter (Windows) or shift + return (OS X) on your keyboard to run the code.

# Type the expression in this code block. Then run it.


Python can handle a large variety of [expressions](https://docs.tdm-pilot.org/key-terms/#expression). Let's try subtraction in the next [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell).

# Type an expression that uses subtraction in this cell. Then run it.


We can also do multiplication (\*) and division (/). While you may have used an "×" to represent multiplication in grade school, [Python](https://docs.tdm-pilot.org/key-terms/#python) uses an asterisk (\*). In [Python](https://docs.tdm-pilot.org/key-terms/#python),

> 2 × 2

is written as

> 2 * 2

Try a multiplication and a division in the next [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell).

# Try a multiplication in this cell. Then try a division.
# What happens if you combine them? What if you combine them with addition and/or subtraction?


When you run, or **evaluate**, an [expression](https://docs.tdm-pilot.org/key-terms/#expression) in [Python](https://docs.tdm-pilot.org/key-terms/#python), the order of operations is followed. (In grade school, you may remember learning the shorthand "PEMDAS".) This means that [expressions](https://docs.tdm-pilot.org/key-terms/#expression) are evaluated in this order:

1. Parentheses
2. Exponents
3. Multiplication and Division (from left to right)
4. Addition and Subtraction (from left to right)

[Python](https://docs.tdm-pilot.org/key-terms/#python) can evaluate parentheses and exponents, as well as a number of additional [operators](https://docs.tdm-pilot.org/key-terms/#operator) you may not have learned in grade school. Here are the main [operators](https://docs.tdm-pilot.org/key-terms/#operator) that you might use presented in the order they are evaluated:

|Operator| Operation| Example | Evaluation |
|---|----|---|---|
|\*\*| Exponent/Power| 3 ** 3 | 27 |
|%| Modulus/Remainder| 34 % 6 | 4 |
|/| Division | 30 / 6 | 5|
|\*| Multiplication | 7 * 8 | 56 |
|-| Subtraction | 18 - 4| 14|
|+| Addition | 4 + 3 | 7 |

# Try operations in this code cell.
# What happens when you add in parentheses?


# Data Types (Integers, Floats, and Strings)

All [expressions](https://docs.tdm-pilot.org/key-terms/#expression) evaluate to a single value. In the above examples, our [expressions](https://docs.tdm-pilot.org/key-terms/#expression) evaluated to single numerical value. Numerical values come in two basic forms:

* [integer](https://docs.tdm-pilot.org/key-terms/#integer)
* [float](https://docs.tdm-pilot.org/key-terms/#float) (or floating-point number)

An [integer](https://docs.tdm-pilot.org/key-terms/#integer), what we sometimes call a "whole number", is a number without a decimal point that can be positive or negative. When a value uses a decimal, it is called a [float](https://docs.tdm-pilot.org/key-terms/#float) or floating-point number. Two numbers that are mathematically equivalent could be in two different data types. For example, mathematically 5 is equal to 5.0, yet the former is an [integer](https://docs.tdm-pilot.org/key-terms/#integer) while the latter is a [float](https://docs.tdm-pilot.org/key-terms/#float). 

Of course, [Python](https://docs.tdm-pilot.org/key-terms/#python) can also help us manipulate text. A snippet of text in Python is called a [string](https://docs.tdm-pilot.org/key-terms/#string). A [string](https://docs.tdm-pilot.org/key-terms/#string) can be written with single or double quotes. A [string](https://docs.tdm-pilot.org/key-terms/#string) can use letters, spaces, line breaks, and numbers. So 5 is an [integer](https://docs.tdm-pilot.org/key-terms/#integer), 5.0 is a [float](https://docs.tdm-pilot.org/key-terms/#float), but '5' and '5.0' are [strings](https://docs.tdm-pilot.org/key-terms/#string). A [string](https://docs.tdm-pilot.org/key-terms/#string) can also be blank, such as ''. 

|Familiar Name | Programming name | Examples |
|---|---|---|
|Whole number|integer| -3, 0, 2, 534|
|Decimal|float | 6.3, -19.23, 5.0, 0.01|
|Text|string| 'Hello world', '1700 butterflies', '', '1823'|

The distinction between each of these data types may seem unimportant, but [Python](https://docs.tdm-pilot.org/key-terms/#python) treats each one differently. For example, we can ask [Python](https://docs.tdm-pilot.org/key-terms/#python) whether an [integer](https://docs.tdm-pilot.org/key-terms/#integer) is equal to a [float](https://docs.tdm-pilot.org/key-terms/#float), but we cannot ask whether a [string](https://docs.tdm-pilot.org/key-terms/#string) is equal to an [integer](https://docs.tdm-pilot.org/key-terms/#integer) or a [float](https://docs.tdm-pilot.org/key-terms/#float).

To evaluate whether two values are equal, we can use two equals signs between them. The expression will evaluate to either `True` or `False`.

# Run this code cell to determine whether the values are equal
42 == 42.0

# Run this code cell to compare an integer with a string
15 == 'fifteen'

# Run this code cell to compare an integer with a string
15 == '15'

When we use the addition [operator](https://docs.tdm-pilot.org/key-terms/#operator) on [integers](https://docs.tdm-pilot.org/key-terms/#integer) or [floats](https://docs.tdm-pilot.org/key-terms/#float), they are added to create a sum. When we use the addition [operator](https://docs.tdm-pilot.org/key-terms/#operator) on [strings](https://docs.tdm-pilot.org/key-terms/#string), they are combined into a single, longer [string](https://docs.tdm-pilot.org/key-terms/#string). This is called [concatenation](https://docs.tdm-pilot.org/key-terms/#concatenation). 

# Combine the strings 'Hello' and 'World'
'Hello' + 'World'

Notice that the [strings](https://docs.tdm-pilot.org/key-terms/#string) are combined exactly as they are written. There is no space between the [strings](https://docs.tdm-pilot.org/key-terms/#string). If we want to include a space, we need to add the space to the end of 'Hello' or the beginning of 'World'. We can also concatenate multiple [strings](https://docs.tdm-pilot.org/key-terms/#string).

# Combine three strings
'Hello ' + 'World' + '!'

When we use addition [operator](https://docs.tdm-pilot.org/key-terms/#operator), the values must be all numbers or all [strings](https://docs.tdm-pilot.org/key-terms/#string). Combining them will create an error.

# Try adding a string to an integer
'55' + 23

Here, we receive the error `can only concatenate str (not "int") to str`. [Python](https://docs.tdm-pilot.org/key-terms/#python) assumes we would like to join two [strings](https://docs.tdm-pilot.org/key-terms/#string) together, but it does not know how to join a [string](https://docs.tdm-pilot.org/key-terms/#string) to an [integer](https://docs.tdm-pilot.org/key-terms/#integer). Put another way, [Python](https://docs.tdm-pilot.org/key-terms/#python) is unsure if we want:

>'55' + 23 

to become
>'5523'

or 
>78

We *can* multiply a [string](https://docs.tdm-pilot.org/key-terms/#string) by an [integer](https://docs.tdm-pilot.org/key-terms/#integer). The result is simply the [string](https://docs.tdm-pilot.org/key-terms/#string) repeated the appropriate number of times.

# Multiply a string by an integer
'Hello World!' * 5

# Variables



A [variable](https://docs.tdm-pilot.org/key-terms/#variable) is like a container that stores information. There are many kinds of information that can be stored in a [variable](https://docs.tdm-pilot.org/key-terms/#variable), including the data types we have already discussed ([integers](https://docs.tdm-pilot.org/key-terms/#integer), [floats](https://docs.tdm-pilot.org/key-terms/#float), and [string](https://docs.tdm-pilot.org/key-terms/#string)). We create (or *initialize*) a [variable](https://docs.tdm-pilot.org/key-terms/#variable) with an [assignment statement](https://docs.tdm-pilot.org/key-terms/#assignment-statement). The [assignment statement](https://docs.tdm-pilot.org/key-terms/#assignment-statement) gives the variable an initial value.

# Initialize an integer variable and add 22 
new_integer_variable = 5
new_integer_variable + 22

The value of a [variable](https://docs.tdm-pilot.org/key-terms/#variable) can be overwritten with a new value. 

# Overwrite the value of my_favorite_number when the commented out line of code is executed. 
# Remove the # in the line "#my_favorite_number = 9" to turn the line into executable code.

my_favorite_number = 7
my_favorite_number = 9
my_favorite_number

# Overwriting the value of a variable using its original value
cats_in_house = 1
cats_in_house = cats_in_house + 2
cats_in_house

# Initialize a string variable and concatenate another string
new_string_variable = 'Hello '
new_string_variable + 'World!'

You can create a [variable](https://docs.tdm-pilot.org/key-terms/#variable) with almost any name, but there are a few guidelines that are recommended.

## Variable Names Should be Descriptive

If we create a [variable](https://docs.tdm-pilot.org/key-terms/#variable) that stores the day of the month, it is helpful to give it a name that makes the value stored inside it clear like `day_of_month`. From a logical perspective, we could call the [variable](https://docs.tdm-pilot.org/key-terms/#variable) almost anything (`hotdog`, `rabbit`, `flat_tire`). As long as we are consistent, the code will execute the same. When it comes time to read, modify, and understand the code, however, it will be confusing to you and others. Consider this simple program that lets us change the `days` [variable](https://docs.tdm-pilot.org/key-terms/#variable) to compute the number of seconds in that many days. 

# Compute the number of seconds in 3 days
days = 3
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

days * hours_in_day * minutes_in_hour * seconds_in_minute

We could write a program that is logically the same, but uses confusing [variable](https://docs.tdm-pilot.org/key-terms/#variable) names.

hotdogs = 60
sasquatch = 24
example = 3
answer = 60

answer * sasquatch * example * hotdogs

This code gives us the same answer as the first example, but it is confusing. Not only does this code use [variable](https://docs.tdm-pilot.org/key-terms/#variable) names that are confusing, it also does not include any comments to explain what the code does. It is not clear that we would change `example` to set a different number of days. It is not even clear what the purpose of the code is. As code gets longer and more complex, having clear [variable](https://docs.tdm-pilot.org/key-terms/#variable) names and explanatory comments is very important. 

## Variable Naming Rules

In addition to being descriptive, [variable](https://docs.tdm-pilot.org/key-terms/#variable) names must follow 3 basic rules:

1. Must be one word (no spaces allowed)
2. Only letters, numbers and the underscore character (\_)
3. Cannot begin with a number




# Which of these variable names are acceptable? 
# Comment out the variables that are not allowed in Python and run this cell to check if the variable assignment works. 
# If you get an error, the variable name is not allowed in Python.

$variable = 1
a variable = 2
a_variable = 3
4variable = 4
variable5 = 5
variable-6 = 6
variAble = 7
Avariable = 8


## Variable Naming Style Guidelines

The three rules above describe absolute rules of [Python](https://docs.tdm-pilot.org/key-terms/#python) [variable](https://docs.tdm-pilot.org/key-terms/#variable) naming. If you break those rules, your code will create an error and fail to execute properly. There are also style *guidelines* that, while they won't break your code, are generally advised for making your code readable and understandable. These style guidelines are written in the [Python Enhancement Proposals (PEP) Style Guide](https://www.python.org/dev/peps/pep-0008/).

The current version of the style guide advises that [variable](https://docs.tdm-pilot.org/key-terms/#variable) names should be written:
>lowercase, with words separated by underscores as necessary to improve readability.

If you have written code before, you may be familiar with other styles, but these notebooks will attempt to follow the PEP guidelines for style. Ultimately, the most important thing is that your [variable](https://docs.tdm-pilot.org/key-terms/#variable) names are consistent so that someone who reads your code can follow what it is doing. As your code becomes more complicated, writing detailed comments with `#` will also become more important.

snake_case_variable
kebab-case-variable
CamelCaseVariable

# Functions

Many different kinds of programs often need to do very similar operations. Instead of writing the same code over again, you can use a [function](https://docs.tdm-pilot.org/key-terms/#function). Essentially, a [function](https://docs.tdm-pilot.org/key-terms/#function) is a small snippet of code that can be quickly referenced. There are three kinds of [functions](https://docs.tdm-pilot.org/key-terms/#function):

* Native [functions](https://docs.tdm-pilot.org/key-terms/#function) built into [Python](https://docs.tdm-pilot.org/key-terms/#python)
* [Functions](https://docs.tdm-pilot.org/key-terms/#function) others have written that you can import
* [Functions](https://docs.tdm-pilot.org/key-terms/#function) you write yourself

We'll address [functions](https://docs.tdm-pilot.org/key-terms/#function) you write yourself in *Python Basics* II. For now, let's look at a few of the native [functions](https://docs.tdm-pilot.org/key-terms/#function). One of the most common [functions](https://docs.tdm-pilot.org/key-terms/#function) used in [Python](https://docs.tdm-pilot.org/key-terms/#python) is the `print()` [function](https://docs.tdm-pilot.org/key-terms/#function) which simply prints a [string](https://docs.tdm-pilot.org/key-terms/#string).

# A print function that prints: Hello World!
print('Hello World!')

We could also define a [variable](https://docs.tdm-pilot.org/key-terms/#variable) with our [string](https://docs.tdm-pilot.org/key-terms/#string) ```'Hello World!'``` and then pass that [variable](https://docs.tdm-pilot.org/key-terms/#variable) into the `print()` function. It is common for functions to take an input, called an [argument](https://docs.tdm-pilot.org/key-terms/#argument), that is placed inside the parentheses (). 

# Define a string and then print it
our_string = 'Hello World!'
print(our_string)

There is also an `input()` [function](https://docs.tdm-pilot.org/key-terms/#function) for taking user input.

# A program to greet the user by name
print('Hi. What is your name?') # Ask the user for their name
user_name = input() # Take the user's input and put it into the variable user_name
print('Pleased to meet you, ' + user_name) # Print a greeting with the user's name

We defined a [string](https://docs.tdm-pilot.org/key-terms/#string) [variable](https://docs.tdm-pilot.org/key-terms/#variable) ```user_name``` to hold the user's input. We then called the `print()` [function](https://docs.tdm-pilot.org/key-terms/#function) to print the [concatenation](https://docs.tdm-pilot.org/key-terms/#concatenate) of 'Pleased to meet you, ' and the user's input that was captured in the [variable](https://docs.tdm-pilot.org/key-terms/#variable) ```user_name```. Remember that we can use a ```+``` to [concatenate](https://docs.tdm-pilot.org/key-terms/#concatenate), meaning join these [strings](https://docs.tdm-pilot.org/key-terms/#string) together. 

We could also use an `f string` to print a variable name within a larger string.

# Placing an f before a string, allows us to reference variables in brackets {}
print(f'Hello {user_name}, pleased to meet you!')

We can [concatenate](https://docs.tdm-pilot.org/key-terms/#concatenate) many [strings](https://docs.tdm-pilot.org/key-terms/#string) together, but we cannot [concatenate](https://docs.tdm-pilot.org/key-terms/#concatenate) [strings](https://docs.tdm-pilot.org/key-terms/#string) with [integers](https://docs.tdm-pilot.org/key-terms/#integer) or [floats](https://docs.tdm-pilot.org/key-terms/#float).

# Concatenating many strings within a print function
print('Hello, ' + 'all ' + 'these ' + 'strings ' + 'are ' + 'being ' + 'connected ' + 'together.')

# Trying to concatenate a string with an integer causes an error
print('There are ' + 7 + 'continents.')

We can transform one [variable](https://docs.tdm-pilot.org/key-terms/#variable) type into another [variable](https://docs.tdm-pilot.org/key-terms/#variable) type with the `str()`, `int()`, and `float()` [functions](https://docs.tdm-pilot.org/key-terms/#function). Let's convert the [integer](https://docs.tdm-pilot.org/key-terms/#integer) above into a [string](https://docs.tdm-pilot.org/key-terms/#string) so we can [concatenate](https://docs.tdm-pilot.org/key-terms/#concatenate) it.

print('There are ' + str(7) + ' continents.')

Mixing [strings](https://docs.tdm-pilot.org/key-terms/#string) with [floats](https://docs.tdm-pilot.org/key-terms/#float) and [integers](https://docs.tdm-pilot.org/key-terms/#integer) can have unexpected results. See if you can spot the problem with the program below.

# A program to tell a user how many months old they are
print('How old are you?') # Ask the user their age
user_age = input() # Take the user input and put it into the variable user_age
number_of_months = int(user_age) * 12 # Define a new variable number_of_months that multiplies the user's age by 12
print('That is more than ' + str(number_of_months) + ' months old!' ) # Print a response that tells the user they are at least number_of_months old

In order to compute the [variable](https://docs.tdm-pilot.org/key-terms/#variable) ```number_of_months```, we multiply ```user_age``` by 12. The problem is that ```user_age``` is a [string](https://docs.tdm-pilot.org/key-terms/#string). Multiplying a [string](https://docs.tdm-pilot.org/key-terms/#string) by 12 simply makes the string repeat 12 times. After the user gives us their age, we need that input to be converted to an [integer](https://docs.tdm-pilot.org/key-terms/#integer). At the same time, we have to convert the [integer](https://docs.tdm-pilot.org/key-terms/#integer) ```number_of_months``` back to a [string](https://docs.tdm-pilot.org/key-terms/#string) for our final `print()` function. 

# A program to tell a user how many months old they are
print('How old are you?') # Ask the user their age
user_age = input() # Take the user input and put it into the variable user_age
number_of_months = int(user_age) * 12 # Define a new variable number_of_months that multiplies the user's age by 12
print('That is more than ' + str(number_of_months) + ' months old!' ) # Print a response that tells the user they are at least number_of_months old

___
# Lesson Complete

Congratulations! You have completed *Python Basics* I. There are two more lessons in *Python Basics*:

* *Python Basics* II
* *Python Basics* III

## Python Basics I Quiz

If you would like to check your understading of this lesson, you can [take this quick quiz](https://docs.google.com/forms/d/e/1FAIpQLSdTPq_BotRY_eqJIfIXT2OoWkv9MwgOKngWcTYJfilwbQ6eAQ/viewform?usp=sf_link).

## Start Next Lesson: [Python Basics II](./python-basics-2.ipynb)

