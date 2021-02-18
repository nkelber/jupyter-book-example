# Python Basics II
<img align="left" src="https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/CC_BY.png"><br />

Created by [Nathan Kelber](http://nkelber.com) and Ted Lawless for [JSTOR Labs](https://labs.jstor.org/) under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/)<br />
For questions/comments/improvements, email nathan.kelber@ithaka.org.<br />
___

[![Python Basics 2 image](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/video/python-basics-2.png)](https://www.youtube.com/watch?v=yzApQqZkJ2c)

**Python Basics II**

**Description:** This lesson describes the basics of [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) including:
* [Boolean values](https://docs.tdm-pilot.org/key-terms/#boolean-value)
* [Boolean operators](https://docs.tdm-pilot.org/key-terms/#boolean-operator)
* [Comparison operators](https://docs.tdm-pilot.org/key-terms/#comparison-operator)
* `if` statements
* `else` statements
* `elif` statements
* `while` and `for` loop statements
* Handling errors with `try` and `except`

and the basics of writing functions:

* `def` statements
* [Local scope](https://docs.tdm-pilot.org/key-terms/#local-scope)
* [Global scope](https://docs.tdm-pilot.org/key-terms/#global-scope)

This is part 2 of 3 in the series *Python Basics* that will prepare you to do text analysis using the [Python](https://docs.tdm-pilot.org/key-terms/#python) programming language.

**Use Case:** For Learners (Detailed explanation, not ideal for researchers)

**Difficulty:** Beginner

**Completion Time:** 90 minutes

**Knowledge Required:** 
* [Getting Started with Jupyter Notebooks](./getting-started-with-jupyter.ipynb)
* [Python Basics I](./python-basics-1.ipynb)

**Knowledge Recommended:** None

**Data Format:** None

**Libraries Used:** `random` to generate random numbers

**Research Pipeline:** None
___

## Flow Control Statements

In *Python Basics* I, you learned about [expressions](https://docs.tdm-pilot.org/key-terms/#expression), [operators](https://docs.tdm-pilot.org/key-terms/#operator), [variables](https://docs.tdm-pilot.org/key-terms/#variable), and a few native [Python](https://docs.tdm-pilot.org/key-terms/#python) [functions](https://docs.tdm-pilot.org/key-terms/#). We wrote programs that executed line-by-line, starting at the top and running to the bottom. This approach works great for simple programs that may execute a few tasks, but as you begin writing programs that can do multiple tasks you'll need a way for your programs to decide which action comes next. We can control when (or if) code gets executed with [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement). If a program is a set of steps for accomplishing a task, then [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) help the program decide the next action. 

[Flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) work like a flowchart. For example, let's say your goal is to hang out and relax with friends. There are a number of steps you might take, depending on whether your friends are available or you feel like making some new friends.

![Flowchart to hangout with friends](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/friends_flowchart.png)

Each diamond in our flowchart represents a decision that has to be made about the best step to take next. This is the essence of [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement). They help a program decide what the next step should be given the current circumstances. 

## Boolean Values

One way we to create [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) is with [boolean values](https://docs.tdm-pilot.org/key-terms/#boolean-value) that have two possible values: **True** or **False**. In our example above, we could consider a "Yes" to be "True" and a "No" to be "False." When we have the data we need to answer each question, we could store that answer in a variable, like:

* ```are_friends_available = False```
* ```make_new_friends = True```
* ```new_friend_available = True```

This would allow us to determine which action to take next. When we assign [boolean values](https://docs.tdm-pilot.org/key-terms/#boolean-value) to a [variable](https://docs.tdm-pilot.org/key-terms/#variable), the first letter must be capitalized: 

# Note, the first letter of a boolean value must always be capitalized in Python
are_friends_available = false
print(are_friends_available)

# The boolean values **True** and **False** cannot be used for variable names. 
# Treating the boolean value True as a variable will create an error
True = 7

## Comparison Operators
Now that we have a way to store [integers](https://docs.tdm-pilot.org/key-terms/#integer), [floats](https://docs.tdm-pilot.org/key-terms/#float), [strings](https://docs.tdm-pilot.org/key-terms/#string), and [boolean values](https://docs.tdm-pilot.org/key-terms/#boolean-value) in [variables](https://docs.tdm-pilot.org/key-terms/#variable), we can use a [comparison operator](https://docs.tdm-pilot.org/key-terms/#comparison-operator) to help make decisions based on those values. We used the [comparison operator](https://docs.tdm-pilot.org/key-terms/#comparison-operator) `==` in *Python Basics* I. This operator asks whether two [expressions](https://docs.tdm-pilot.org/key-terms/#expression) are equal to each other. 

# Comparing two values with the comparison operator ==
67 == 67

# Note, a comparison operator uses ==
# Do not confuse with variable assignment statement which uses =
67 = 67

There are additional [comparison operators](https://docs.tdm-pilot.org/key-terms/#comparison-operator) that can help us with [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement).

|Operator|Meaning|
|---|---|
|==|Equal to|
|!=|Not equal to|
|<|Less than|
|>|Greater than|
|<=|Less than or equal to|
|>=|Greater than or equal to|

# Using the "Not equal to" operator
67 != 32

# Using the "Not equal to" operator
67 != 67

# Using the "equal to" operator with strings
'hello world' == 'hello world'

# Using the "equal to" operator to compare a string with an integer
'55' == 55 # A string cannot be equal to a float or an integer

# Using the "equal to" operator to compare an integer with a float
55 == 55.0 # An integer can be equal to a float

# Using a comparison operator on a variable
number_of_dogs = 0 # Creating a variable number_of_dogs
number_of_dogs >= 1 # Checking whether number_of_dogs is greater than or equal to 1

## Boolean Operators (and/or/not)
We can also use [Boolean operators](https://docs.tdm-pilot.org/key-terms/#boolean-operator) (**and**/**or**/**not**) to create [expressions](https://docs.tdm-pilot.org/key-terms/#expression) that evaluate to a single [Boolean value](https://docs.tdm-pilot.org/key-terms/#boolean-value) (**True**/**False**). 

### Using the Boolean Operator `and`
The `and` operator determines whether *both* conditions are **True**.

# If condition one is True AND condition two is True
# What will the evaluation be?
True and True

# If condition one is True AND condition two is False
# What will the evaluation be?
True and False

In order for an ```and``` [expression](https://docs.tdm-pilot.org/key-terms/#expression) to evaluate to **True**, every condition must be **True**. Here is the "Truth Table" for every pair:

|Expression|Evaluation|
|---|---|
|True and True|True|
|True and False|False|
|False and True|False|
|False and False|False|

Since `and` [expressions](https://docs.tdm-pilot.org/key-terms/#expression) require all conditions to be **True**, they can easily result in **False** evaluations.

### Using the Boolean Operator ```or```
The ```or``` operator determines whether *any* condition is **True**.

# Is expression one True OR is expression two True?
True or False

# Is condition one True OR is condition two True?
False or False

An ```or``` [expression](https://docs.tdm-pilot.org/key-terms/#expression) evaluates to **True** if *any* condition is **True**. Here is the "Truth Table" for every pair:

|Expression|Evaluation|
|---|---|
|True or True|True|
|True or False|True|
|False or True|True|
|False or False|False|

Since ```or``` [expressions](https://docs.tdm-pilot.org/key-terms/#expression) only require a single condition to be **True**, they can easily result in **True** evaluations.

### Using the Boolean Operator ```not```
The```not``` operator only operates on a single expression, essentially flipping **True** to **False** or **False** to **True**. 

# The not operator flips a True to False
not False

### Combining Boolean and Comparison Operators

We can combine [Boolean operators](https://docs.tdm-pilot.org/key-terms/#boolean-operator) and [comparison operators](https://docs.tdm-pilot.org/key-terms/#comparison-operator) to create even more nuanced **Truth** tests.

# Evaluating two conditions with integers at once
(3 < 22) and (60 == 34) # What does each condition evaluate to?

# Evaluating two conditions with integers at once
(3 == 45) or (3 != 7) # What does each condition evaluate to?

So far, we have evaluated one or two conditions at once, but we could compare even more at once. (In practice, this is  rare since it creates code that can be difficult to read.)

# Evaluating four conditions at once
(3 < 7) and ('Hello' != 'Goodbye') and (17 == 17.000) and (2 + 2 != 4) # What does each condition evaluate to?

[Boolean operators](https://docs.tdm-pilot.org/key-terms/#boolean-operator) also have an order of operations like mathematical [operators](https://docs.tdm-pilot.org/key-terms/#operator). They resolve in the order of `not`, `and`, then `or`. 

## Writing a Flow Control Statement

The general form of a [flow control statement](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) in [Python](https://docs.tdm-pilot.org/key-terms/#python) is a condition followed by an action clause:

`In this condition:`<br />
&nbsp; &nbsp; &nbsp; &nbsp;`perform this action`

Let's return to part of our flowchart for hanging out with friends.

![Flowchart showing if homework is yes then do assignment](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/do_homework_chart.png)

We can imagine a [flow control statement](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) that would look something like:

`if have_homework == True:`<br />
&nbsp; &nbsp; &nbsp; &nbsp; `complete assignment`
    
The condition is given followed by a colon (:). The action clause then follows on the next line, indented into a [code block](https://docs.tdm-pilot.org/key-terms/#code-block).  

* If the condition is fulfilled (evaluates to **True**), the action clause in the block of code is executed. 
* If the condition is not fulfilled (evaluates to **False**), the action clause in the block of code is skipped over.

## Code Blocks
A [code block](https://docs.tdm-pilot.org/key-terms/#code-block) is a snippet of code that begins with an indentation. A [code block](https://docs.tdm-pilot.org/key-terms/#code-block) can be a single line or many lines long. Blocks can contain other blocks forming a hierarchal structure. In such a case, the second block is indented an additional degree. Any given block ends when the number of indentations in the current line is less than the number that started the block. 

![Visualization of code block indentations](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/code_block_indentation.png)

## Types of Flow Control Statements

The code example above uses an `if` statement, but there are other kinds of [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) available in [Python](https://docs.tdm-pilot.org/key-terms/#python). 

|Statement|Means|Condition for execution|
|---|---|---|
|`if`|if|if the condition is fulfilled|
|`elif`|else if|if no previous conditions were met *and* this condition is met|
|`else`|else|if no condition is met (no condition is supplied for an `else` statement)|
|`while`|while|while condition is true|
|`for`|for|execute in a loop for this many times|
|`try`|try|try this and run the `except` code if an error occurs|

Let's take a look at each of these [flow control statement](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) types.

## `if` Statements

An `if` statement begins with an [expression](https://docs.tdm-pilot.org/key-terms/#expression) that evaluates to **True** or **False**.

* if **True**, then perform this action
* if **False**, skip over this action

In practice, the form looks like this:

`if this is True:` <br />
&nbsp; &nbsp; &nbsp; &nbsp; `perform this action`

Let's put an `if` statement into practice with a very simple program that asks the user how their day is going and then responds. We can visualize the flow of the program in a flowchart.

![Flowchart of a good day program](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/good_day_flowchart.png)

Our program will use a single `if` statement. If the user types "Yes" or "yes", then our program will send a response.

# A program that responds to a user having a good day
print('Are you having a good day? (Yes or No)') # Ask user if they are having a good day
having_good_day = input() # Define a variable having_good_day to hold the user's input in a string

if having_good_day == 'Yes' or having_good_day == 'yes':  # If the user has input the string 'Yes' or 'yes'
    print('Glad to hear your day is going well!') # Print: Glad to hear your day is going well!

Our program works fairly well so long as the user inputs 'Yes' or 'yes'. If they type 'no' or something else, it simply ends. If we want to have our program still respond, we can use an `else` statement.

## `else` Statements

An `else` statement *does not require a condition* to evaluate to **True** or **False**. It simply executes when none of the previous conditions are met. The form looks like this:

`else:` <br />
&nbsp; &nbsp; &nbsp; &nbsp; `perform this action`

Our updated flowchart now contains a second branch for our program.

![The program flowchart with two branches](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/good_day_flowchart2.png)
    


# A program that responds to whether the user is having a good or bad day
print('Are you having a good day? (Yes or No)') # Ask user if they are having a good day
having_good_day = input() # Define a variable having_good_day to hold the user's input

if having_good_day == 'Yes' or having_good_day == 'yes': # If the user has input the string 'Yes' or 'yes'
    print('Glad to hear your day is going well!') # Print: Glad to hear your day is going well!
    
else: # Execute this if none of the other branches executes
    print('I wish your day was going better.') # Note that we can use double quotations in our string because it begins and ends with single quotes

Our new program is more robust. The new `else` statement still gives the user a response if they do not respond "Yes" or "yes". But what if we wanted to add an option for when a user says "No"? Or when a user inputs something besides "Yes" or "No"? We could use a series of `elif` statements.

## `elif` Statements

An `elif` statement, short for "else if," allows us to create a list of possible conditions where one (and only one) action will be executed. `elif` statements come after an initial `if` statement and before an `else` statement:

`if condition A is True:` <br />
&nbsp; &nbsp; &nbsp; &nbsp; `perform action A` <br />
`elif condition B is True:` <br />
&nbsp; &nbsp; &nbsp; &nbsp; `perform action B` <br />
`elif condition C is True:` <br />
&nbsp; &nbsp; &nbsp; &nbsp; `perform action C` <br />
`elif condition D is True:` <br />
&nbsp; &nbsp; &nbsp; &nbsp; `perform action D` <br />
`else:` <br />
&nbsp; &nbsp; &nbsp; &nbsp;`perform action E`

For example, we could add an `elif` statement to our program so it responds to both "Yes" and "No" with unique answers. We could then add an `else` statement that responds to any user input that is not "Yes" or "No".

![Flowchart showing three branches](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/good_day_flowchart3.png)

# A program that responds to whether the user is having a good or bad day
print('Are you having a good day? (Yes or No)') # Ask user if they are having a good day
having_good_day = input() # Define a variable having_good_day to hold the user's input

if having_good_day == 'Yes' or having_good_day == 'yes': # If the user has input the string 'Yes' or 'yes'
    print('Glad to hear your day is going well!') # Print: Glad to hear your day is going well!
    
elif having_good_day == 'No' or having_good_day == 'no': # else if the user has input the string 'No'
    print('Sorry to hear that. I hope it gets better.') # Print: Sorry to hear that. I hope it gets better.
    
else: # Execute this if none of the other branches executes
    print('Sorry, I only understand "Yes" or "No"') # Note that we can use double quotations in our string because it begins and ends with single quotes

### The difference between`elif` and `if`?

When an `elif` condition is met, all other `elif` statements are skipped over. This means that one (and only one) [flow control statement](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) is executed when using `elif` statements. The fact that only one `elif` statement is executed is important because it may be possible for multiple [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) to evaluate to **True**. A series of `elif` statements evaluates from top-to-bottom, only executing the first `elif` statement whose condition evaluates to **True**. The rest of the `elif` statements are skipped over (whether they are **True** or **False**). 

In practice, a set of mutually exclusive `if` statements will result in the same actions as an `if` statement followed by `elif` statements. There are a few good reasons, however, to use `elif` statements:

1. A series of `elif` statements helps someone reading your code understand that a single flow control choice is being made.
2. Using `elif` statements will make your program run faster since other conditional statements are skipped after the first evaluates to **True**. Otherwise, every `if` statement will be evaluated.
3. Writing a mutually exclusive set of `if` statements can be very complex.

Expanding on the concept of our "How is your day going?" program, let's take a look at an example that asks the user "How is your week going?" It will take two inputs: the day of the week (`day_of_week`) and how the user feels the week is going (`having_good_week`).

![How is your week going flowchart](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/good_week_elif.png)

# A program that responds to the user's input for the day of the week and how their week is going.
print('What day of the week is it?')
day_of_week = input() 
print('Are you having a good week?')
having_good_week = input()

if day_of_week == 'Friday' or day_of_week == 'friday':
    print('Enjoy the weekend!')
    
if having_good_week == 'Yes' or having_good_week == 'yes':
    print('I hope the rest of the week is good too!')
    
if having_good_week == 'No' or having_good_week == 'no':
    print('Sorry to hear that. I hope the rest of the week is better.')
    
else:
    print('Sorry, I only understand "Yes" or "No"')

In the program above, try changing the `elif` statements to `if` statements. What happens if the user inputs 'Friday' and 'Yes'?

## `while` Loop Statements

So far, we have used [flow control statements](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) like decision-making branches to decide what action should be taken next. Sometimes, however, we want a particular action to loop (or repeat) until some condition is met. We can accomplish this with a `while` loop statement that takes the form:

`while condition:` <br />
&nbsp; &nbsp; &nbsp; &nbsp;`take this action`

After the [code block](https://docs.tdm-pilot.org/key-terms/#code-block) is executed, the program loops back to check and see if the `while` loop condition has changed from **True** to **False**. The code block stops looping when the condition becomes **False**.

In the following program, the user will guess a number until they get it correct. 

![flowchart for number-guessing program](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/guess_number_flowchart.png)

# A program that asks the user to guess a number
secret_number = 4 # The secret number is set here by the programmer.
print('I am thinking of a number between 1-10. Can you guess it?') # Ask the user to make a guess
guess = input() # Take the user's first guess
while guess != str(secret_number): # While the users guess does not equal secret_number
    print('Nope. Guess again!') # Print "Nope. Guess Again!"
    guess = input() # Allow the user to change the value of guess
print('You guessed the secret number, ' + str(secret_number)) # Print a congratulations message with the secret number

### Stopping Accidental Infinite Loops
When using a `while` loop, it is possible to accidentally create an infinite loop that never ends. This happens because the `while` condition *never* becomes **False**. 

If you accidentally write code that infinitely repeats, you can stop the execution by selecting **Interrupt** from the **Kernel** menu. (Alternatively, you can press the letter **i** twice on your keyboard.) You may also want to remove the output of the rogue cell. You can do this from the **Cell** menu.
* Clearing output from a single cell: **Cell** ▶ **Current Outputs** ▶ **Clear**
* Clearing output from all cells: **Cell** ▶ **All Output** ▶ **Clear**

![Clearing current outputs](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/clear_output.gif)

# An infinite loop
while True:
    print('Oh noes!')

### A Repeating `while` Loop

In the program above, the `while` loop checked to see if the user guessed a particular number. We could also use a `while` loop to repeat a [code block](https://docs.tdm-pilot.org/key-terms/#code-block) a particular number of times. 

# A simple program that prints out 1, 2, 3
number = 0
while number < 3:
    number = number + 1 # We can also write an equivalent shortcut: number += 1
    print(number)
     

## `for` Loop Statements with a `range()` Function

An abbreviated way to write a `while` loop that repeats a specified number of times is using a `for` loop with a `range()` function. This loop takes the form:

`for i in range(j):` <br />
&nbsp; &nbsp; &nbsp; &nbsp;`take this action`
    
where `i` is a generic [variable](https://docs.tdm-pilot.org/key-terms/#variable) for counting the number of iterations and `j` is the number of times you want the [code block](https://docs.tdm-pilot.org/key-terms/#code-block) to repeat. 

The starting value of `i` is 0. After each loop, `i` increases by one until it reaches `j`. The loop then stops. The [variable](https://docs.tdm-pilot.org/key-terms/#variable) names `i` and `j` are merely conventions. Using a different name may make the purpose of your code clearer to readers.

# A `for` loop that repeats 'What?' five times. Changing the `range()` number will change the number of repetitions.
for i in range(3):
    print('What?')

What happens when you change the name of [variable](https://docs.tdm-pilot.org/key-terms/#variable) `i`?

# A `for` loop that prints the value of the current iteration, here called `i`. 
for i in range(5):
    print(i)

In the examples above, the `range()` [function](https://docs.tdm-pilot.org/key-terms/#function) takes a single argument that specifies the number of loops. The assumption is our `range()` [function](https://docs.tdm-pilot.org/key-terms/#function) will start at 0, but we can specify any starting [integer](https://docs.tdm-pilot.org/key-terms/#integer) by adding an additional [argument](https://docs.tdm-pilot.org/key-terms/#argument).

# A `for` loop that starts looping at 27 and stops looping at 32
for i in range(27,32):
    print(i)

# A `for` loop that starts looping at -13 and stops looping at 7
for i in range(-3, 7):
    print(i)

We can also specify the size of each step for the `range()` [function](https://docs.tdm-pilot.org/key-terms/#function). In the above examples, the [function](https://docs.tdm-pilot.org/key-terms/#function) adds one for each increment step, but we can add larger numbers or even specify negative numbers to have the `range()` [function](https://docs.tdm-pilot.org/key-terms/#function) count down. The general form is:

`for i in range(start, stop, increment):` <br />
 &nbsp; &nbsp; &nbsp; &nbsp;`loop this action`

# A `for` loop that counts down from ten to one, followed by printing `Go!`
for i in range(10, 0, -1):
    print(i)
print('Go!')

## `Continue` and `Break` Statements
`while` loops and `for` loops can also use `continue` and `break` statements to affect flow control. 
* A `continue` statement immediately restarts the loop.
* A `break` statement immediately exits the loop.

Let's return to our secret number guessing program. We will write the same program workflow using `continue` and `break` statements.

![Flowchart for secret number guessing program](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/guess_number_flowchart.png)

# A program that asks the user to guess a number
guess = 0
secret_number = str(4) # The secret number is set here by the programmer. Notice it is turned into a string so it can be easily compared with user inputs.
print('I am thinking of a number between 1-10.') # Ask the user to make a guess
while True:
    print('What is your guess?')
    guess = input()
    if guess == secret_number:
        break
    else:
        continue
print('You guessed the secret number, ' + secret_number) # Print a congratulations message with the secret number

## Exception Handling with `try` and `except`

When running code that may create an error, we can use `try` and `except` statements to stop a program from crashing.

# Try running the first code block, if there's an error then run the `except` code
# Divide 100 by a number the user chooses

print('100 divided by...')
user_number = input()
try:
    print(100 / int(user_number))
except:
    print("You can't divide by zero.")


# Dividing by zero causes an error
100 / 0

## Functions

We have used several [Python](https://docs.tdm-pilot.org/key-terms/#python) [functions](https://docs.tdm-pilot.org/key-terms/#function) already, including `print()`, `input()`, and `range()`. You can identify a function by the fact that it ends with a set of parentheses `()` where [arguments](https://docs.tdm-pilot.org/key-terms/#argument) can be **passed** into the function. Depending on the [function](https://docs.tdm-pilot.org/key-terms/#function) (and your goals for using it), a [function](https://docs.tdm-pilot.org/key-terms/#function) may accept no [arguments](https://docs.tdm-pilot.org/key-terms/#argument), a single [argument](https://docs.tdm-pilot.org/key-terms/#argument), or many [arguments](https://docs.tdm-pilot.org/key-terms/#argument). For example, when we use the `print()` [function](https://docs.tdm-pilot.org/key-terms/#function), a [string](https://docs.tdm-pilot.org/key-terms/#string) (or a variable containing a [string](https://docs.tdm-pilot.org/key-terms/#string)) is passed as an [argument](https://docs.tdm-pilot.org/key-terms/#argument).

[Functions](https://docs.tdm-pilot.org/key-terms/#function) are a convenient shorthand, like a mini-program, that makes our code more **modular**. We don't need to know all the details of how the `print()` [function](https://docs.tdm-pilot.org/key-terms/#function) works in order to use it. [Functions](https://docs.tdm-pilot.org/key-terms/#function) are sometimes called "black boxes", in that we can put an [argument](https://docs.tdm-pilot.org/key-terms/#argument) into the box and a **return value** comes out. We don't need to know the inner details of the "black box" to use it. (Of course, as you advance your programming skills, you may become curious about how certain [functions](https://docs.tdm-pilot.org/key-terms/#function) work. And if you work with sensitive data, you may *need* to peer in the black box to ensure the security and accuracy of the output.) 

## Libraries and Modules

While [Python](https://docs.tdm-pilot.org/key-terms/#python) comes with many [functions](https://docs.tdm-pilot.org/key-terms/#function), there are thousands more that others have written. Adding them all to [Python](https://docs.tdm-pilot.org/key-terms/#python) would create mass confusion, since many people could use the same name for [functions](https://docs.tdm-pilot.org/key-terms/#function) that do different things. The solution then is that [functions](https://docs.tdm-pilot.org/key-terms/#function) are stored in [modules](https://docs.tdm-pilot.org/key-terms/#module) that can be **imported** for use. A [module](https://docs.tdm-pilot.org/key-terms/#module) is a [Python](https://docs.tdm-pilot.org/key-terms/#python) file (extension ".py") that contains the definitions for the [functions](https://docs.tdm-pilot.org/key-terms/#function) written in [Python](https://docs.tdm-pilot.org/key-terms/#python). These [modules](https://docs.tdm-pilot.org/key-terms/#module) (individual [Python](https://docs.tdm-pilot.org/key-terms/#python) files) can then be collected into even larger groups called [packages](https://docs.tdm-pilot.org/key-terms/#package) and [libraries](https://docs.tdm-pilot.org/key-terms/#library). Depending on how many [functions](https://docs.tdm-pilot.org/key-terms/#function) you need for the program you are writing, you may import a single [module](https://docs.tdm-pilot.org/key-terms/#module), a [package](https://docs.tdm-pilot.org/key-terms/#package) of [modules](https://docs.tdm-pilot.org/key-terms/#module), or a whole [library](https://docs.tdm-pilot.org/key-terms/#library). 

The general form of importing a [module](https://docs.tdm-pilot.org/key-terms/#module) is:
`import module_name`

You may recall from the "Getting Started with Jupyter Notebooks" lesson, we imported the `time` [module](https://docs.tdm-pilot.org/key-terms/#module) and used the `sleep()` [function](https://docs.tdm-pilot.org/key-terms/#function) to wait 5 seconds.

print('Waiting 5 seconds...')
import time # We import the `time` module
time.sleep(5) # We run the sleep() function from the time module using `time.sleep()`
print('Done')

We can also just import the `sleep()` [function](https://docs.tdm-pilot.org/key-terms/#function) without importing the whole `time` [module](https://docs.tdm-pilot.org/key-terms/#module). 

print('Waiting 5 seconds...')
from time import sleep # We import just the sleep() function from the time module
sleep(5) # Notice that we just call the sleep() function, not time.sleep
print('Done')

## Writing a Function

In the above examples, we **called** a [function](https://docs.tdm-pilot.org/key-terms/#function) that was already written. To call our own [functions](https://docs.tdm-pilot.org/key-terms/#function), we need to define our [function](https://docs.tdm-pilot.org/key-terms/#function) first with a **function definition statement** followed by a [code block](https://docs.tdm-pilot.org/key-terms/#code-block):

`def my_function():` <br />
&nbsp; &nbsp; &nbsp; &nbsp;`do this task`
    

After the [function](https://docs.tdm-pilot.org/key-terms/#function) is defined, we can **call** on it to do us a favor whenever we need by simply executing the [function](https://docs.tdm-pilot.org/key-terms/#function) like so:

`my_function()`

After the function is defined, we can call it as many times as we want without having to rewrite its code. In the example below, we call `my_function` twice. 

# Creating a simple function to double a number
print('I will double any number. Give me a number.')
inputnumber = input()

def my_function():
    outputnumber = int(inputnumber) * 2
    print(outputnumber)

my_function()

print('Give me a new number.')
inputnumber = input()

my_function()

print('Give me one last number.')
inputnumber = input()

my_function()

Using [functions](https://docs.tdm-pilot.org/key-terms/#function) also makes it easier for us to update our code. Let's say we wanted to change our program to square our `inputnumber` instead of doubling it. We can simply change the [function](https://docs.tdm-pilot.org/key-terms/#function) definition one time to make the change everywhere. See if you can make the change. (Remember to also change your program description in the first line!)

# Creating a simple function to raise a number to the second power.
print('I will raise any number to the second power. Give me a number.')
inputnumber = input()

def my_function():
    outputnumber = int(inputnumber) ** 2
    print(outputnumber)

my_function()

print('Give me a new number.')
inputnumber = input()

my_function()

print('Give me one last number.')
inputnumber = input()

my_function()

By changing our [function](https://docs.tdm-pilot.org/key-terms/#function) one time, we were able to make our program behave differently in three different places. Generally, it is good practice to avoid duplicating program code to avoid having to change it in multiple places. When programmers edit their code, they may spend time **deduplicating** to make the code easier to read and maintain.

## Parameters vs. Arguments

When we write a [function](https://docs.tdm-pilot.org/key-terms/#function) definition, we can define a [parameter](https://docs.tdm-pilot.org/key-terms/#parameter) to work with the [function](https://docs.tdm-pilot.org/key-terms/#function). We use the word [parameter](https://docs.tdm-pilot.org/key-terms/#parameter) to describe the [variable](https://docs.tdm-pilot.org/key-terms/#variable) in parentheses within a [function](https://docs.tdm-pilot.org/key-terms/#function) definition:

`def my_function(input_variable):` <br />
&nbsp; &nbsp; &nbsp; &nbsp;`do this task`

In the pseudo-code above, `input_variable` is a [parameter](https://docs.tdm-pilot.org/key-terms/#parameter) because it is being used within the context of a [function](https://docs.tdm-pilot.org/key-terms/#function) *definition*. When we actually call and run our [function](https://docs.tdm-pilot.org/key-terms/#function), the actual [variable](https://docs.tdm-pilot.org/key-terms/#variable) or value we pass to the [function](https://docs.tdm-pilot.org/key-terms/#function) is called an [argument](https://docs.tdm-pilot.org/key-terms/#argument). 

# A program to greet the user by name

def greeting_function(user_name): #`user_name` here is a parameter since it is in the definition of the `greeting_function`
    print('Hello ' + user_name)

greeting_function('Sam') # 'Sam' is an argument that is being passed into the `greeting_function`

In the above example, we passed a [string](https://docs.tdm-pilot.org/key-terms/#string) into our [function](https://docs.tdm-pilot.org/key-terms/#function), but we could also pass a [variable](https://docs.tdm-pilot.org/key-terms/#variable).

# A program to greet the user by name

def greeting_function(user_name): #`user_name` here is a parameter since it is in the definition of the `greeting_function`
    print('Hello ' + user_name)

print('What is your name?')
answer = input()
greeting_function(answer) # `answer` is an argument that is being passed into the `greeting_function`

## Function Return Values

Whether or not a [function](https://docs.tdm-pilot.org/key-terms/#function) takes an [argument](https://docs.tdm-pilot.org/key-terms/#argument), it will return a value. If we do not specify that return value in our [function](https://docs.tdm-pilot.org/key-terms/#function) definition, it is automatically set to `None`, a special value like the Boolean `True` and `False` that simply means null or nothing. (`None` is not the same thing as, say, the integer `0`.) We can also specify return values for our [function](https://docs.tdm-pilot.org/key-terms/#function) using a [flow control statement](https://docs.tdm-pilot.org/key-terms/#flow-control-statement) followed by `return` in the [code block](https://docs.tdm-pilot.org/key-terms/#code-block). 

Let's write a function for telling fortunes. We can call it `fortune_picker` and it will accept a number (1-6) then return a string for the fortune.

# A fortune-teller program that contains a function `fortune_picker`
# `fortune_picker` accepts an integer (1-6) and returns a fortune string

def fortune_picker(fortune_number): # A function definition statement that has a parameter `fortune_number`
    if fortune_number == 1:
        return 'You will have six children'
    elif fortune_number == 2:
        return 'You will become very wise'
    elif  fortune_number == 3:
        return 'A new friend will help you find yourself'
    elif fortune_number == 4:
        return 'Do not eat the sushi'
    elif fortune_number == 5:
        return 'That promising venture... it is a trap.'
    elif fortune_number == 6: 
        return 'Sort yourself out then find love.'

print(fortune_picker(5))

In our example, we passed the [argument](https://docs.tdm-pilot.org/key-terms/#argument) `3` that returned the [string](https://docs.tdm-pilot.org/key-terms/#string) `'A new friend will help you find yourself'`. To change the fortune, we would have to pass a different [integer](https://docs.tdm-pilot.org/key-terms/#integer) into the [function](https://docs.tdm-pilot.org/key-terms/#function). To make our fortune-teller random, we could import the [function](https://docs.tdm-pilot.org/key-terms/#function) `randint()` that chooses a random number between two [integers](https://docs.tdm-pilot.org/key-terms/#integer). We pass the two [integers](https://docs.tdm-pilot.org/key-terms/#integer) as [arguments](https://docs.tdm-pilot.org/key-terms/#argument) separated by a comma.

# A fortune-teller program that uses a random integer

from random import randint # import the randint() function from the random module

def fortune_picker(fortune_number): # A function definition statement that has a parameter `fortune_number`
    if fortune_number == 1:
        return 'You will have six children'
    elif fortune_number == 2:
        return 'You will become very wise'
    elif  fortune_number == 3:
        return 'A new friend will help you find yourself'
    elif fortune_number == 4:
        return 'Do not eat the sushi'
    elif fortune_number == 5:
        return 'That promising venture... it is a trap.'
    elif fortune_number == 6: 
        return 'Sort yourself out then find love.'

random_number = randint(1, 6) # Choose a random number between 1 and 6 and assign it to a new variable `random_number`
print(fortune_picker(random_number))

## Local and Global Scope

We have seen that [functions](https://docs.tdm-pilot.org/key-terms/#function) make maintaining code easier by avoiding duplication. One of the most dangerous areas for duplication is [variable](https://docs.tdm-pilot.org/key-terms/#variable) names. As programming projects become larger, the possibility that a [variable](https://docs.tdm-pilot.org/key-terms/#variable) will be re-used goes up. This can cause weird errors in our programs that are hard to track down. We can alleviate the problem of duplicate [variable](https://docs.tdm-pilot.org/key-terms/#variable) names through the concepts of [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope) and [global scope](https://docs.tdm-pilot.org/key-terms/#global-scope).

We use the phrase [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope) to describe what happens within a [function](https://docs.tdm-pilot.org/key-terms/#function). The [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope) of a [function](https://docs.tdm-pilot.org/key-terms/#function) may contain [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable), but once that [function](https://docs.tdm-pilot.org/key-terms/#function) has completed the [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable) and their contents are erased. 

On the other hand, we can also create [global variables](https://docs.tdm-pilot.org/key-terms/#global-variable) that persist at the top-level of the program *and* within the [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope) of a [function](https://docs.tdm-pilot.org/key-terms/#function).

* In the [global scope](https://docs.tdm-pilot.org/key-terms/#global-scope), [Python](https://docs.tdm-pilot.org/key-terms/#python) does not recognize any [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable) from within [functions](https://docs.tdm-pilot.org/key-terms/#function)
* In the [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope) of a [function](https://docs.tdm-pilot.org/key-terms/#function), [Python](https://docs.tdm-pilot.org/key-terms/#python) can recognize and modify any [global variables](https://docs.tdm-pilot.org/key-terms/#global-variable)
* It is possible for there to be a [global variable](https://docs.tdm-pilot.org/key-terms/#global-variable) and a [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable) with the same name

Ideally, [Python](https://docs.tdm-pilot.org/key-terms/#python) programs should limit the number of [global variables](https://docs.tdm-pilot.org/key-terms/#global-variable) and create most [variables](https://docs.tdm-pilot.org/key-terms/#variable) in a [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope).

# Demonstration of global variable being use in a local scope
# The program crashes when a local variable is used in a global scope
global_secret_number = 7

def share_number():
    local_secret_number = 13
    print('The global secret number is ' + str(global_secret_number))
    print('The local secret number is ' + str(local_secret_number))
    

share_number()
print('The global secret number is ' + str(global_secret_number))
print('The local secret number is ' + str(local_secret_number))

The code above defines a [global variable](https://docs.tdm-pilot.org/key-terms/#global-variable) `global_secret_number` with the value of 7. A [function](https://docs.tdm-pilot.org/key-terms/#function), called `share_number`, then defines a [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable) `local_secret_number` with a value of 13. When we call the `share_number` [function](https://docs.tdm-pilot.org/key-terms/#function), it prints the [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable) and the [global variable](https://docs.tdm-pilot.org/key-terms/#global-variable). After the `share_number()` [function](https://docs.tdm-pilot.org/key-terms/#function) completes we try to print both variables in a [global scope](https://docs.tdm-pilot.org/key-terms/#global-scope). The program prints `global_secret_number` but crashes when trying to print `local_secret_number` in a [global scope](https://docs.tdm-pilot.org/key-terms/#global-scope). 

It's a good practice not to name a [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable) the same thing as a [global variable](https://docs.tdm-pilot.org/key-terms/#global-variable). If we define a [variable](https://docs.tdm-pilot.org/key-terms/#variable) with the same name in a [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope), it becomes a [local variable](https://docs.tdm-pilot.org/key-terms/#local-variable) within that scope. Once the [function](https://docs.tdm-pilot.org/key-terms/#function) is closed, the [global variable](https://docs.tdm-pilot.org/key-terms/#global-variable) retains its original value.

# A demonstration of global and local scope using the same variable name
secret_number = 7

def share_number():
    secret_number = 10
    print(secret_number)

share_number()
print(secret_number)


## The Global Statement

A [global statement](https://docs.tdm-pilot.org/key-terms/#global-statement) allows us to modify a [global variable](https://docs.tdm-pilot.org/key-terms/#global-variable) in a [local scope](https://docs.tdm-pilot.org/key-terms/#local-scope). 

# Using a global statement in a local scope to change a global variable locally

secret_number = 7

def share_number():
    global secret_number # The global statement indicates this the global variable, not a local variable
    secret_number = 10
    print(secret_number)

share_number()
print(secret_number)

___
## Lesson Complete
Congratulations! You have completed *Python Basics* II. There is only one more lesson in *Python Basics*:

* *Python Basics* III

## Start Next Lesson: [Python Basics III](./python-basics-3.ipynb)

