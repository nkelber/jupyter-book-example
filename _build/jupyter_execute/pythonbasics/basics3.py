# Python Basics III
<img align="left" src="https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/CC_BY.png"><br />

Created by [Nathan Kelber](http://nkelber.com) and Ted Lawless for [JSTOR Labs](https://labs.jstor.org/) under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/)<br />
For questions/comments/improvements, email nathan.kelber@ithaka.org.<br />
___

**Description:** This lesson describes the basics of [lists](https://docs.tdm-pilot.org/key-terms/#list) and [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary) including:

* The `in` and `not in` [operators](https://docs.tdm-pilot.org/key-terms/#operator)
* [Lists](https://docs.tdm-pilot.org/key-terms/#list)
* [List](https://docs.tdm-pilot.org/key-terms/#list) methods (`index()`, `append()`, `insert()`, `sort()`)
* [Dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary)
* [Dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) methods (`update()`, `keys()`, `values()`, `items()`, `get()`)

This is part 3 of 3 in the series *Python Basics* that will prepare you to do text analysis using the [Python](https://docs.tdm-pilot.org/key-terms/#python) programming language.

**Use Case:** For Learners (Detailed explanation, not ideal for researchers)

**Difficulty:** Beginner

**Completion Time:** 90 minutes

**Knowledge Required:** 
* [Getting Started with Jupyter Notebooks](./getting-started-with-jupyter.ipynb)
* [Python Basics I](./python-basics-1.ipynb)
* [Python Basics II](./python-basics-2.ipynb)

**Knowledge Recommended:** None

**Data Format:** None

**Libraries Used:** None

**Research Pipeline:** None
___

In *Python Basics* I, we learned about three data types: [integers](https://docs.tdm-pilot.org/key-terms/#integer), [floats](https://docs.tdm-pilot.org/key-terms/#float), and [strings](https://docs.tdm-pilot.org/key-terms/#string). In this lesson, we will learn about two additional data types: [lists](https://docs.tdm-pilot.org/key-terms/#list) and [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary). [Lists](https://docs.tdm-pilot.org/key-terms/#list) and [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary) help us store many values inside a single [variable](https://docs.tdm-pilot.org/key-terms/#variable). This is helpful for a few reasons.

* We can store many items in a single [list](https://docs.tdm-pilot.org/key-terms/#list) or [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary), making it easier to keep the data together 
* [Lists](https://docs.tdm-pilot.org/key-terms/#list) and [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary) only require a single [assignment state](https://docs.tdm-pilot.org/key-terms/#assignment-statement)
* [Lists](https://docs.tdm-pilot.org/key-terms/#list) and [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary) have additional capabilities that will make organizing our data easier

The fundamental difference between a [list](https://docs.tdm-pilot.org/key-terms/#list) and a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) is that a [list](https://docs.tdm-pilot.org/key-terms/#list) stores items in sequential order (starting from 0) while a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) stores items in [key/value pairs](https://docs.tdm-pilot.org/key-terms/#key-value-pair). When we want to retrieve an item in a list, we use an [index number](https://docs.tdm-pilot.org/key-terms/#index-number) or a set of [index numbers](https://docs.tdm-pilot.org/key-terms/#index-number) called a [slice](https://docs.tdm-pilot.org/key-terms/#slice) as a reference. When we want to retrieve an item from a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary), we supply a [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) that returns the [value](https://docs.tdm-pilot.org/key-terms/#key-value-pair) (or set of values) associated with that [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair). Each of these approaches can be beneficial depending on what kind of data we are working with (and what we intend to do with the data). 

## Lists

A [list](https://docs.tdm-pilot.org/key-terms/#list) can store anywhere from zero to millions of items. The items that can be stored in a [list](https://docs.tdm-pilot.org/key-terms/#list) include the data types we have already learned: [integers](https://docs.tdm-pilot.org/key-terms/#integer), [floats](https://docs.tdm-pilot.org/key-terms/#float), and [strings](https://docs.tdm-pilot.org/key-terms/#string). A [list](https://docs.tdm-pilot.org/key-terms/#list) [assignment state](https://docs.tdm-pilot.org/key-terms/#assignment-statement) takes the form.
`my_list = [item1, item2, item3, item4...]`

# A list containing integers
my_favorite_numbers = [7, 21, 100]
print(my_favorite_numbers)

# A list containing strings
my_inspirations = ['Harriet Tubman', 'Rosa Parks', 'Pauli Murray']
print(my_inspirations)

Both `my_favorite_numbers` and `my_inspirations` have three items, but we could have also initialized them with no items `my_favorite_numbers = []` or many more items. Each item has an [index number](https://docs.tdm-pilot.org/key-terms/#index-number) that depends on their order. The first item is 0, the second item is 1, the third item is 2, etc. In the `my_inspirations` list, `'Pauli Murray'` is item 2.

# Retrieving an item in a list
my_inspirations[2]

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**What happens if you change the index number to 1? What about 3? 2.0?**

___


[Lists](https://docs.tdm-pilot.org/key-terms/#list) can also contain other [lists](https://docs.tdm-pilot.org/key-terms/#list). To retrieve a value from a [list](https://docs.tdm-pilot.org/key-terms/#list) within a [list](https://docs.tdm-pilot.org/key-terms/#list), we use two [indexes](https://docs.tdm-pilot.org/key-terms/#index-number) (or indices). 

# Retrieving an item from a list within a list
my_inspirations = [['Harriet Tubman', 'Rosa Parks', 'Pauli Murray'], ['Martin Luther King Jr.', 'Frederick Douglass', 'Malcolm X']]
my_inspirations[0][2]

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**Can you change the index for `my_inspirations` to retrieve `'Malcolm X'`?**
___

We can also select items from a [list](https://docs.tdm-pilot.org/key-terms/#list) beginning from the end/right side of a [list](https://docs.tdm-pilot.org/key-terms/#list) by using negative [index numbers](https://docs.tdm-pilot.org/key-terms/#index-number).

# Retrieving an item from the end of a list by using negative indices
my_inspirations = ['Harriet Tubman', 'Rosa Parks', 'Pauli Murray']
my_inspirations[-1]

We can also retrieve a group of consecutive items from a [list](https://docs.tdm-pilot.org/key-terms/#list) using [slices](https://docs.tdm-pilot.org/key-terms/#slice) instead of a single [index number](https://docs.tdm-pilot.org/key-terms/#index-number). We create a [slice](https://docs.tdm-pilot.org/key-terms/#slice) by indicating a starting and ending [index number](https://docs.tdm-pilot.org/key-terms/#index-number). The [slice](https://docs.tdm-pilot.org/key-terms/#slice) is a smaller [list](https://docs.tdm-pilot.org/key-terms/#list) containing all the items between our starting and stopping [index number](https://docs.tdm-pilot.org/key-terms/#index-number).

# Taking a slice of a list
historical_periods = ['Classical Antiquity', 'Early Middle Ages', 'High Middle Ages', 'Late Middle Ages', 'Early Modern Period', 'Late Modern Period', 'Contemporary History']
historical_periods[3:5]

Notice in our [slice](https://docs.tdm-pilot.org/key-terms/#slice) that the second [index](https://docs.tdm-pilot.org/key-terms/#index-number) in a [slice](https://docs.tdm-pilot.org/key-terms/#slice) is the stopping point. That is our return [list](https://docs.tdm-pilot.org/key-terms/#list) contains `historical_periods[3]` (`'Late Middle Ages'`) and `historical_periods[4]` (`'Early Modern Period'`), but it does not include `historical_periods[5]` (`'Late Modern Period'`). This can be confusing if you were expecting three items instead of two. One way to remember this is by subtracting the [indexes](https://docs.tdm-pilot.org/key-terms/#index-number) in your head (5 - 3 = 2 items).

It is not uncommon for [lists](https://docs.tdm-pilot.org/key-terms/#list) to be hundreds or thousands of items long. It would be a chore to count all those items to create a [slice](https://docs.tdm-pilot.org/key-terms/#slice). If you want to know the length of a [list](https://docs.tdm-pilot.org/key-terms/#list), you can use the `len()` function.

# Using the len() function to discover the number of items in the list
historical_periods = ['Classical Antiquity', 'Early Middle Ages', 'High Middle Ages', 'Late Middle Ages', 'Early Modern Period', 'Late Modern Period', 'Contemporary History']
len(historical_periods)

The `historical_periods` [list](https://docs.tdm-pilot.org/key-terms/#list) is 7 items long, meaning the whole [list](https://docs.tdm-pilot.org/key-terms/#list) is within the [slice](https://docs.tdm-pilot.org/key-terms/#slice) `historical_periods[0:6]`. When we take a [slice](https://docs.tdm-pilot.org/key-terms/#slice) of a [list](https://docs.tdm-pilot.org/key-terms/#list) we can also leave out the first [index number](https://docs.tdm-pilot.org/key-terms/#index-number) (0 is assumed) or the stopping [index number](https://docs.tdm-pilot.org/key-terms/#index-number) (the last item is assumed).

# Taking a slice of a list without a beginning index
historical_periods = ['Classical Antiquity', 'Early Middle Ages', 'High Middle Ages', 'Late Middle Ages', 'Early Modern Period', 'Late Modern Period', 'Contemporary History']
historical_periods[:2]

# Taking a slice of a list without a stopping index
historical_periods = ['Classical Antiquity', 'Early Middle Ages', 'High Middle Ages', 'Late Middle Ages', 'Early Modern Period', 'Late Modern Period', 'Contemporary History']
historical_periods[4:]

## The `in` and `not in` Operators

If we have a long [list](https://docs.tdm-pilot.org/key-terms/#list), it may be helpful to check whether a value is in the [list](https://docs.tdm-pilot.org/key-terms/#list). We can do this with the `in` and `not in` operators, which return a [boolean value](https://docs.tdm-pilot.org/key-terms/#boolean-value): **True** or **False**.

# Checking whether an item is in a list using the `in` operator

staff = ['Tara Richards',
 'Tammy French',
 'Justin Douglas',
 'Lauren Marquez',
 'Aaron Wilson',
 'Dennis Howell',
 'Brandon Reed',
 'Kelly Baker',
 'Justin Howard',
 'Sarah Myers',
 'Vanessa Burgess',
 'Timothy Davidson',
 'Jessica Lee',
 'Christopher Miller',
 'Lisa Grant',
 'Ryan Chan',
 'Gary Carson',
 'Anthony Mitchell',
 'Jacob Turner',
 'Jennifer Bonilla',
 'Rachel Gonzalez',
 'Andrew Clark',
 'Richard Pearson',
 'Glenn Allen',
 'Jacqueline Gallagher',
 'Carlos Mcdowell',
 'Jeffrey Harris',
 'Danielle Griffith',
 'Sarah Craig',
 'Vernon Vasquez',
 'Anthony Burton',
 'Erica Bryant',
 'Patricia Walker',
 'Karen Brown',
 'Terri Walker',
 'Michelle Knight',
 'Kathleen Douglas',
 'Debbie Estrada',
 'Jennifer Brewer',
 'Taylor Rodriguez',
 'Lisa Turner',
 'Julie Hudson',
 'Christina Cox',
 'Nancy Patrick',
 'Rita Mosley',
 'Nicholas Gordon',
 'Wanda Vasquez',
 'Jason Lopez',
 'Anna Powers',
 'Tyler Perez']

'Patricia Walker' in staff

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**Is Rita McDowell in `staff`? What about Erica Bryant?**
___

We can change the value of any item in a [list](https://docs.tdm-pilot.org/key-terms/#list) using an [assignment statement](https://docs.tdm-pilot.org/key-terms/#assignment-statement) that contains the item's [index number](https://docs.tdm-pilot.org/key-terms/#index-number).

# Changing the value of an item in a list
historical_periods = ['Classical Antiquity', 'Dark Ages', 'Modern Period']
print(historical_periods)
historical_periods[1] = 'Middle Ages'
print(historical_periods)


Now we know how to change an item in a [list](https://docs.tdm-pilot.org/key-terms/#list). And can use the `in` and `not in` operator to determine if an item is in the [list](https://docs.tdm-pilot.org/key-terms/#list). But if we don't know the [index number](https://docs.tdm-pilot.org/key-terms/#index-number) of the item, we won't know which [index number](https://docs.tdm-pilot.org/key-terms/#index-number) to change. We need a way to pass both the name of the [list](https://docs.tdm-pilot.org/key-terms/#list) and the name of the item simultaneously to a [function](https://docs.tdm-pilot.org/key-terms/#function). To do that, we'll use a special kind of [function](https://docs.tdm-pilot.org/key-terms/#function) called a [method](https://docs.tdm-pilot.org/key-terms/#method). 

## List Methods

A [method](https://docs.tdm-pilot.org/key-terms/#method) is a kind of [function](https://docs.tdm-pilot.org/key-terms/#function). (Remember, [functions](https://docs.tdm-pilot.org/key-terms/#function) end in parentheses.) [Methods](https://docs.tdm-pilot.org/key-terms/#method), however, act on objects (like [lists](https://docs.tdm-pilot.org/key-terms/#list)) so they have a slightly different written form. We will take a look at five useful [methods](https://docs.tdm-pilot.org/key-terms/#method) for working with [lists](https://docs.tdm-pilot.org/key-terms/#list).

|Method Name | Purpose | Form |
|---|---|---|
|index()| search for an item in a list and return the index number | list_name.index(item_name)|
|append()| add an item to the end of a list | list_name.append(item_name)|
|insert()| insert an item in the middle of a list | list_name.insert(index_number, item_name)|
|remove()| remove an item from a list based on value | list_name.remove('item_value')|
|sort()| sort the order of a list | list_name.sort()|

## The `index()` Method

The `index()` [method](https://docs.tdm-pilot.org/key-terms/#method) checks to see if a value is in a [list](https://docs.tdm-pilot.org/key-terms/#list). If the value is found, it returns the [index number](https://docs.tdm-pilot.org/key-terms/#index-number) for the first item with that value. (Keep in mind, there could be multiple items with a single value in a [list](https://docs.tdm-pilot.org/key-terms/#list)). If the value is not found, the `index()` [method](https://docs.tdm-pilot.org/key-terms/#method) returns a `ValueError`.

# Using the index() method to return the index number of an item by passing a value
staff = ['Tara Richards',
 'Tammy French',
 'Justin Douglas',
 'Lauren Marquez',
 'Aaron Wilson',
 'Dennis Howell',
 'Brandon Reed',
 'Kelly Baker',
 'Justin Howard',
 'Sarah Myers',
 'Vanessa Burgess',
 'Timothy Davidson',
 'Jessica Lee',
 'Christopher Miller',
 'Lisa Grant',
 'Ryan Chan',
 'Gary Carson',
 'Anthony Mitchell',
 'Jacob Turner',
 'Jennifer Bonilla',
 'Rachel Gonzalez',
 'Andrew Clark',
 'Richard Pearson',
 'Glenn Allen']

staff

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**What is the index number of Lisa Grant in `staff`?**
___

## The `append()` Method

The `append()` [method](https://docs.tdm-pilot.org/key-terms/#method) adds a value to the end of a [list](https://docs.tdm-pilot.org/key-terms/#list).

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**Can you add your name to `staff`?**
___

# Using the append() method to add an item to the end of a list
staff = ['Tara Richards',
 'Tammy French',
 'Justin Douglas',
 'Lauren Marquez',
 'Aaron Wilson',
 'Dennis Howell',
 'Brandon Reed',
 'Kelly Baker',
 'Justin Howard',
 'Sarah Myers',
 'Vanessa Burgess',
 'Timothy Davidson',
 'Jessica Lee',
 'Christopher Miller',
 'Lisa Grant',
 'Ryan Chan',
 'Gary Carson',
 'Anthony Mitchell',
 'Jacob Turner',
 'Jennifer Bonilla',
 'Rachel Gonzalez',
 'Andrew Clark',
 'Richard Pearson',
 'Glenn Allen']
# Write your append statement under this comment

list(staff) # Prints `staff` in a vertical list format to check that the name was added. The list() function will print our list in an easier to read format than the print() function.

We can also add an item to the end of a [list](https://docs.tdm-pilot.org/key-terms/#list) by using an [assignment statement](https://docs.tdm-pilot.org/key-terms/#assignment-statement).

# Adding an item to a list using an assignment statement
staff = staff + ['Einhorn Finkle'] # Concatenate name_list with the list ['Einhorn Finkle']
list(staff)

## The `insert()` Method

The `insert()` [method](https://docs.tdm-pilot.org/key-terms/#method) is similar to `append()` but it takes an [argument](https://docs.tdm-pilot.org/key-terms/#argument) that lets us choose an [index number](https://docs.tdm-pilot.org/key-terms/#index-number) to insert the new item.

# Using the insert() method to add an item at a specific index number
staff = ['Tara Richards',
 'Tammy French',
 'Justin Douglas',
 'Lauren Marquez',
 'Aaron Wilson',
 'Dennis Howell',
 'Brandon Reed',
 'Kelly Baker',
 'Justin Howard',
 'Sarah Myers',
 'Vanessa Burgess',
 'Timothy Davidson',
 'Jessica Lee',
 'Christopher Miller',
 'Lisa Grant',
 'Ryan Chan',
 'Gary Carson',
 'Anthony Mitchell',
 'Jacob Turner',
 'Jennifer Bonilla',
 'Rachel Gonzalez',
 'Andrew Clark',
 'Richard Pearson',
 'Glenn Allen']

staff.insert(5, 'Arya Stark') # Insert the name 'Arya Stark' at index 5 (The sixth name on the list)
list(staff) # Prints `staff` to check that the name was added at the right spot

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**Can you make your name the third item on `staff`?**
___

## The `remove()` Method

The `remove()` [method](https://docs.tdm-pilot.org/key-terms/#method) removes the first item from the [list](https://docs.tdm-pilot.org/key-terms/#list) that has a matching value. 

# Using the remove() method to remove the first item with a matching value
staff = ['Tara Richards',
 'Tammy French',
 'Justin Douglas',
 'Lauren Marquez',
 'Aaron Wilson',
 'Dennis Howell',
 'Brandon Reed',
 'Kelly Baker',
 'Justin Howard',
 'Sarah Myers',
 'Vanessa Burgess',
 'Timothy Davidson',
 'Jessica Lee',
 'Christopher Miller',
 'Lisa Grant',
 'Ryan Chan',
 'Gary Carson',
 'Anthony Mitchell',
 'Jacob Turner',
 'Jennifer Bonilla',
 'Rachel Gonzalez',
 'Andrew Clark',
 'Richard Pearson',
 'Glenn Allen']
# Write your remove statement under this comment

list(staff) # Prints `staff` to check that the name was removed

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**Can you remove Glenn Allen from `staff`?**
___

If you know the value you wish to remove then the `remove()` [method](https://docs.tdm-pilot.org/key-terms/#method) is the best option. If you know the [index number](https://docs.tdm-pilot.org/key-terms/#index-number) of the item, you can use a `del` statement to delete [list](https://docs.tdm-pilot.org/key-terms/#list) items.

# Using a `del` statement to delete a list item
staff = ['Tara Richards',
 'Tammy French',
 'Justin Douglas',
 'Lauren Marquez',
 'Aaron Wilson',
 'Dennis Howell',
 'Brandon Reed',
 'Kelly Baker',
 'Justin Howard',
 'Sarah Myers',
 'Vanessa Burgess',
 'Timothy Davidson',
 'Jessica Lee',
 'Christopher Miller',
 'Lisa Grant',
 'Ryan Chan',
 'Gary Carson',
 'Anthony Mitchell',
 'Jacob Turner',
 'Jennifer Bonilla',
 'Rachel Gonzalez',
 'Andrew Clark',
 'Richard Pearson',
 'Glenn Allen']
del staff[-1] # Delete the final item in the list. In this case, 'Glenn Allen'.
list(staff)

## The `sort()` Method

The `sort()` [method](https://docs.tdm-pilot.org/key-terms/#method) sorts a [list](https://docs.tdm-pilot.org/key-terms/#list) in alphabetical order, where strings with capital letters are sorted A-Z, then strings with lowercase letters are sorted A-Z.

# Using the `sort()` method to sort a list in alpha-numeric order
staff = ['Tara Richards',
 'Tammy French',
 'Justin Douglas',
 'Lauren Marquez',
 'Aaron Wilson',
 'Dennis Howell',
 'Brandon Reed',
 'Kelly Baker',
 'Justin Howard',
 'Sarah Myers',
 'Vanessa Burgess',
 'Timothy Davidson',
 'Jessica Lee',
 'Christopher Miller',
 'Lisa Grant',
 'Ryan Chan',
 'Gary Carson',
 'Anthony Mitchell',
 'Jacob Turner',
 'Jennifer Bonilla',
 'Rachel Gonzalez',
 'Andrew Clark',
 'Richard Pearson',
 'Glenn Allen']
staff.sort()
list(staff)

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**The `sort()` method can take the argument `reverse=True`. Try applying it to the `sort()` method above. What does it do?**
___

___
<h2 style="color:red; display:inline">Coding Challenge! &lt; / &gt; </h2>

**Using your knowledge of flow control statements and lists, can you write a program that transforms a list of strings into a single string of comma-separated values?**
___

# Level 1 Challenge
# A challenge to transform a list of books into a single string of comma-separated values
# The result should be the string: 'Piers Plowman, The Canterbury Tales, Revelations of Divine Love, The Decameron, Le Morte d'Arthur'
book_list = ['Piers Plowman', 'The Canterbury Tales', 'Revelations of Divine Love' 'The Decameron', "Le Morte d'Arthur"]

# Level 2 Challenge
# For even more challenge, transform a list of lists containing books and authors into a single string of comma-separated values with an 'and' before the final value. Oxford comma please.
# The result should be the string: 'Piers Plowman by William Langland, The Canterbury Tales by Geoffrey Chaucer, Revelations of Divine Love by Julian of Norwich, The Decameron by Giovanni Boccaccio, and Le Morte d'Arthur by Sir Thomas Malory'

books_with_authors = [['Piers Plowman', 'William Langland'], ['The Canterbury Tales', 'Geoffrey Chaucer'], ['Revelations of Divine Love', 'Julian of Norwich'], ['The Decameron', 'Giovanni Boccaccio'], ["Le Morte d'Arthur", 'Sir Thomas Malory']]



## Dictionaries

Like a [list](https://docs.tdm-pilot.org/key-terms/#list), a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) can hold many values within a single [variable](https://docs.tdm-pilot.org/key-terms/#variable). We have seen that the items of a [list](https://docs.tdm-pilot.org/key-terms/#list) are stored in a strictly-ordered fashion, starting from item 0. In a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary), each [value](https://docs.tdm-pilot.org/key-terms/#key-value-pair) is stored in relation to a descriptive [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) forming a [key/value pair](https://docs.tdm-pilot.org/key-terms/#key-value-pair). Technically, as of [Python](https://docs.tdm-pilot.org/key-terms/#python) 3.7 (June 2018), [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary) are also ordered by insertion. In practice, however, the most useful aspect of a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) is the ability to supply a [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) and receive a [value](https://docs.tdm-pilot.org/key-terms/#key-value-pair) without reference to [indices](https://docs.tdm-pilot.org/key-terms/#index-number). Whereas a [list](https://docs.tdm-pilot.org/key-terms/#list) is typed with brackets `[]`, a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) is typed with braces `{}`. The [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) and/or [value](https://docs.tdm-pilot.org/key-terms/#key-value-pair) can be an [integer](https://docs.tdm-pilot.org/key-terms/#integer), [float](https://docs.tdm-pilot.org/key-terms/#float), or [string](https://docs.tdm-pilot.org/key-terms/#string).

`example_dictionary = {key1 : value1, key2 : value2, key3 : value3}`

We could imagine, for example, a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) with our professional contacts' names as [keys](https://docs.tdm-pilot.org/key-terms/#key-value-pair) and their occupations as [values](https://docs.tdm-pilot.org/key-terms/#key-value-pair).

# An example of a dictionary storing names and occupations
contacts ={
 'Amanda Bennett': 'Engineer, electrical',
 'Bryan Miller': 'Radiation protection practitioner',
 'Christopher Garrison': 'Planning and development surveyor',
 'Debra Allen': 'Intelligence analyst',
 'Donna Decker': 'Architect',
 'Heather Bullock': 'Media planner',
 'Jason Brown': 'Energy manager',
 'Jason Soto': 'Lighting technician, broadcasting/film/video',
 'Marissa Munoz': 'Further education lecturer',
 'Matthew Mccall': 'Chief Technology Officer',
 'Michael Norman': 'Translator',
 'Nicole Leblanc': 'Financial controller',
 'Noah Delgado': 'Engineer, land',
 'Rachel Charles': 'Physicist, medical',
 'Stephanie Petty': 'Architect'}
from pprint import pprint # We import the pretty print function which prints out dictionaries in a neater fashion than the built-in print() function
pprint(contacts) # Use the pretty print function to print `contacts`

We can add a new [key/value pair](https://docs.tdm-pilot.org/key-terms/#key-value-pair) to our [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) using an [assignment statement](https://docs.tdm-pilot.org/key-terms/#assignment-statement).

# Adding the key 'Nathan Kelber' with the value 'Digital Humanities Fellow' to the dictionary contact
contacts['Nathan Kelber'] = 'Digital Humanities Fellow'

pprint(contacts) # Use the pretty print function to print `contacts`

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**Can you add your name to the contacts dictionary?**
___

Similar to deleting an item from a [list](https://docs.tdm-pilot.org/key-terms/#list), we can use a `del` statement to delete a [key/value pair](https://docs.tdm-pilot.org/key-terms/#key-value-pair). 

# Deleting a key/value pair from the dictionary contacts
del contacts['Bryan Miller'] 

pprint(contacts) # Use the pretty print function to print `contacts`

## Dictionary Methods

We'll take a look at five useful [methods](https://docs.tdm-pilot.org/key-terms/#method) for working with [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary): `update()`, `keys()`, `values()`, `items()`, and `get()`.

|Method Name | Purpose | Form |
|---|---|---|
|update()| add new key/value pairs to a dictionary | dict_name.update(\[(key1, value1), (key2, value2)])|
| &nbsp; | combine two dictionaries |dict_name.update(dict_name2)|
|keys()| check if a key is in a dictionary (True/False) | key_name in dict_name.keys()|
| &nbsp; | Loop through the keys in a dictionary | for k in dict.keys():|
|values()| check if a value is in a dictionary (True/False) | value_name in dict_name.values()|
| &nbsp;| Loop through the values in a dictionary | for v in dict.values():|
|items()| Loop through the keys and values in a dictionary | for k, v in dict.items():|
|get()| retrieve the value for a specific key | dict_name.get(key_name) |

## The `update()` Method

The `update()` [method](https://docs.tdm-pilot.org/key-terms/#method) is useful for adding many [key/value pairs](https://docs.tdm-pilot.org/key-terms/#key-value-pair) to a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) at once. The `update()` [method](https://docs.tdm-pilot.org/key-terms/#method) accepts a single [key/value pair](https://docs.tdm-pilot.org/key-terms/#key-value-pair), multiple pairs, or even other [dictionaries](https://docs.tdm-pilot.org/key-terms/#dictionary).

# Adding several key/value pairs to the dictionary contacts using the update() method
#contacts.update([('Matthew Kirschenbaum', 'Professor'), ('Sarah Morris', 'Librarian')])
contacts.update([('Jason Hanover', 'Animal Trainer')])
pprint(contacts) # Use the pretty print function to print `contacts`

## The `keys()` and `values()` Methods

The `keys()`, `values()`, and `items()` [methods](https://docs.tdm-pilot.org/key-terms/#method) are useful for when checking whether a particular [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) or [value](https://docs.tdm-pilot.org/key-terms/#key-value-pair) exists in a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary). We can pair them with `in` or `not in` operators to check whether a value is in our [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary) (just like we did with [lists](https://docs.tdm-pilot.org/key-terms/#list)). 

# Checking whether a string exists within a key, value, or both.
contacts ={
 'Amanda Bennett': 'Engineer, electrical',
 'Bryan Miller': 'Radiation protection practitioner',
 'Christopher Garrison': 'Planning and development surveyor',
 'Debra Allen': 'Intelligence analyst',
 'Donna Decker': 'Architect',
 'Heather Bullock': 'Media planner',
 'Jason Brown': 'Energy manager',
 'Jason Soto': 'Lighting technician, broadcasting/film/video',
 'Marissa Munoz': 'Further education lecturer',
 'Matthew Mccall': 'Chief Technology Officer',
 'Michael Norman': 'Translator',
 'Nicole Leblanc': 'Financial controller',
 'Noah Delgado': 'Engineer, land',
 'Rachel Charles': 'Physicist, medical',
 'Stephanie Petty': 'Architect'}

contacts

# Checking if the value Architect is in the contacts dictionary
# Do I know an architect?
'Architect' in contacts.values()

## The `get()` Method

If we are sure a [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) exists, we can use

`dict_name[key_name]` 

to return a value. However, if the [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) is not found, the result will be a `KeyError`. The more robust approach is usually to use the `get()` [method](https://docs.tdm-pilot.org/key-terms/#method). If the [key](https://docs.tdm-pilot.org/key-terms/#key-value-pair) is not found, the `None` value will be returned. (Optionally, we can also specify a default message to return.)

`dict_name.get('key_name', 'key_not_found_message')`

# Using the get() method to retrieve the value for the key 'Marissa Munoz'
contacts.get('Marissa Munoz', 'No contact with that name')

___
<h3 style="color:red; display:inline">Try it! &lt; / &gt; </h3>

**Try searching for a name not in contacts with `contacts[name]` and then with `contacts.get('name', 'No contact with that name')`**
___

## Combining `keys()`, `values()`, and `items()` with Flow Control Statements

It is often usful to combine `for` loops with the keys(), values(), or items() [methods](https://docs.tdm-pilot.org/key-terms/#method) to repeat a task for each entry in a [dictionary](https://docs.tdm-pilot.org/key-terms/#dictionary).

# Print every key in our contacts dictionary
for k in contacts.keys(): # The variable `k` here is just a convenient shorthand. It could easily be named `key` or something else.
    print(k)

# Print every value in our contacts dictionary
for v in contacts.values(): # The variable `v` here is just a convenient shorthand. It could easily be named `value` or something else.
    print(v)

# Print every key and value in our contacts dictionary
for k, v in contacts.items():
    print('Key: ' + k + ' Value: ' + v)

___
## Lesson Complete

Congratulations! You've completed the *Python Basics* series. 

Considering the amount of material in *Python Basics* I, II, and III, there's a good chance you won't retain it all. That's okay. Programmers often need to look up things to accomplish a task they haven't done in a while, particularly if it is in a language they don't often use. When you're working on a project, you can always come back to these lessons as reference materials. In other words, you've learned an incredible amount, so don't be surprised if it doesn't all stick at first.

If you want to help yourself retain what you've learned, the best way is to start putting it into practice. Try your hand at creating some small Python projects and recognize that the things you've learned here will cement with time and practice. When you do forget a particular thing&mdash;as we all do&mdash;a quick web search often turns up some useful examples.


## Start Another Python Skills Lesson: 
* [Working with Dataset Files](./working-with-dataset-files.ipynb)
* [Pandas I](./pandas-1.ipynb)

## Start a Text Analysis Lesson:
* [Exploring Metadata](./exploring-metadata.ipynb)


## Coding Challenge! Solutions

There are often many ways to solve programming problems. Here are a few possible ways to solve the challenges, but there are certainly more!

### Challenge Level 1

Transform a list of books into a single string of comma-separated values. Using the list:

`book_list = ['Piers Plowman', 'The Canterbury Tales', 'Revelations of Divine Love', 'The Decameron', "Le Morte d'Arthur"]`

Print the string:
`'Piers Plowman, The Canterbury Tales, Revelations of Divine Love, The Decameron, Le Morte d'Arthur'`

# Assign list to book_list
book_list = ['Piers Plowman', 'The Canterbury Tales', 'Revelations of Divine Love', 'The Decameron', "Le Morte d'Arthur"]

# Solution 1
# For loop

for book in book_list[:-1]: 
    print(book + ', ', end='')
print(book_list[-1])

# Solution 2 
# For i in range()

for i in range(len(book_list) - 1):
    print(book_list[i] + ', ', end='')
print(book_list[-1])

# Solution 3
# While loop

# While loop
i=0
while i < (len(book_list) - 1):
    print(book_list[i] + ', ', end='')
    i += 1
print(book_list[-1])

# Solution 4
# String join method
# (We did not learn this join method, but it does exactly what we want)
print(', '.join(book_list))

### Challenge Level 2

Transform a list of lists containing books and authors into a single string of comma-separated values with an 'and' before the final value. Oxford comma please.

Using the list:

`[['Piers Plowman', 'William Langland'], ['The Canterbury Tales', 'Geoffrey Chaucer'], ['Revelations of Divine Love', 'Julian of Norwich'], ['The Decameron', 'Giovanni Boccaccio'], ["Le Morte d'Arthur", 'Sir Thomas Malory']]`

Print the string:

`'Piers Plowman by William Langland, The Canterbury Tales by Geoffrey Chaucer, Revelations of Divine Love by Julian of Norwich, The Decameron by Giovanni Boccaccio, and Le Morte d'Arthur by Sir Thomas Malory'`



# Assign list to books_with_authors
books_with_authors = [['Piers Plowman', 'William Langland'], ['The Canterbury Tales', 'Geoffrey Chaucer'], ['Revelations of Divine Love', 'Julian of Norwich'], ['The Decameron', 'Giovanni Boccaccio'], ["Le Morte d'Arthur", 'Sir Thomas Malory']]

# Solution 1
# For loop
for b in books_with_authors[:-1]:
    print(b[0] + ' by ' + b[1] + ', ', end='')
print('and ' + books_with_authors[-1][0] + ' by ' + books_with_authors[-1][1])

# Solution 2
# For i in range()

for i in range(len(books_with_authors) - 1):
    print(books_with_authors[i][0] + ' by ' + books_with_authors[i][1] + ', ', end='')
print('and ' + books_with_authors[-1][0] + ' by ' + books_with_authors[-1][1])

# Solution 3
# While loop
i=0
while i < (len(books_with_authors) - 1):
    print(books_with_authors[i][0] + ' by ' + books_with_authors[i][1] + ', ', end='')
    i += 1
print('and ' + books_with_authors[-1][0] + ' by ' + books_with_authors[-1][1])

# Solution 4
# String join method 
# (We did not learn this method, but it does exactly what we want.)

new_list = []
for b in books_with_authors[:-1]:
    new_list.append(str(b[0] + ' by ' + b[1]))

print(', '.join(new_list) + ', and ' + books_with_authors[-1][0] + ' by ' + books_with_authors[-1][1])