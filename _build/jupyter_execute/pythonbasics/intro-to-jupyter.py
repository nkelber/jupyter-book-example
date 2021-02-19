# Getting Started with Jupyter Notebooks
<img align="left" src="https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/CC_BY.png"><br />

Created by [Nathan Kelber](http://nkelber.com) and Ted Lawless for [JSTOR Labs](https://labs.jstor.org/) under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/)<br />
For questions/comments/improvements, email nathan.kelber@ithaka.org.<br />
___

**Getting Started with Jupyter Notebooks**

**Description:** This lesson introduces [Jupyter notebooks](https://docs.tdm-pilot.org/key-terms/#jupyter-notebook) and [Python](https://docs.tdm-pilot.org/key-terms/#python) for absolute beginners. If you are completely new to text analysis, this is the place to start. 

**Use Case:** For Learners (Additional explanation, not ideal for researchers)

**Difficulty:** Beginner

**Completion time:** 15 minutes

**Knowledge Required:** None

**Knowledge Recommended:** None

**Data Format:** None

**Libraries Used:** `time` to demonstrate code cell execution

**Research Pipeline:** None
___

[![Getting Started with Jupyter Notebooks](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/video/getting-started.png)](https://youtu.be/3jZYC9rGrNg)

## Introduction
Welcome to your first [Jupyter notebook](https://docs.tdm-pilot.org/key-terms/#jupyter-notebook). [Jupyter notebooks](https://docs.tdm-pilot.org/key-terms/#jupyter-notebook) are documents that contain both computer code (like [Python](https://docs.tdm-pilot.org/key-terms/#python)) alongside explanatory images, figures, videos, and links. Most importantly, the code in a [Jupyter notebook](https://docs.tdm-pilot.org/key-terms/#jupyter-notebook) can be executed, modified, and deleted. As you explore this notebook, please feel free to modify the text, the code, and to generally play around with the environment. You can always [launch another instance of this notebook](https://docs.tdm-pilot.org/intro-to-jupyter-notebooks/) that will restore its original configuration. Later, you may learn how to create, modify, and save your own notebooks to share with others.

## Cells

Similar to the way an essay is composed of paragraphs, Jupyter notebooks are composed of [cells](https://docs.tdm-pilot.org/key-terms/#cell). A [cell](https://docs.tdm-pilot.org/key-terms/#cell) is like a container for a particular kind of content. There are essentially two kinds of content in Jupyter notebooks:

1. [Markdown Cells](https://docs.tdm-pilot.org/key-terms/#markdown-cell)- These can contain text, images, video, and other kinds of explanatory content you might find on a regular website. This cell is a markdown cell.
2. [Code Cells](https://docs.tdm-pilot.org/key-terms/#code-cell)- These can contain code written in a variety of languages.

A [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) can be distinguished from a [markdown cell](https://docs.tdm-pilot.org/key-terms/#markdown-cell) by the fact that it contains a pair of brackets with a colon to its left, like so ``[ ]:``

# This is a code cell 

A [markdown cell](https://docs.tdm-pilot.org/key-terms/#markdown-cell) provides information, but a [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) can be executed to perform an action. The [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) above does not contain any executable content, only a text comment. We can tell the text in the [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) is a comment because it is prefixed by a ``#``. In Python, any time a line is prefaced by a ``#`` that line is a comment and will not be executed if the code is run. In a [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell), comments are also blueish-green in color.

## Hello World: Your First Code

It is traditional in programming education to begin with a program that prints ``Hello World``. In Python, this is a simple task. We will use the ``print()`` function. This function simply prints out whatever is inside the parentheses (). We will pass the quotation "Hello World" to the print function like so:

```print("Hello World")```

Write this code into the following [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) below. To execute our code, we have a couple options:

### Option One

![Image of play button](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/play_button.png) Click the code cell you wish to run and then push the "Run" button above. 
### Option Two

Click the [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) you wish to run and press Ctrl + Enter (Windows) or shift + return (OS X) on your keyboard.

Type ```print("Hello World")``` into the box below and then run the cell.



### Try this!
* Does it matter if you use single or double quotes?
* Can you also insert a comment into the code cell?
* Can you write code and a comment on a single line? Which must come first?

After your code runs, you'll receive any output and a number will appear in the pair of brackets `[ ]:` to the left of the code cell to show the order the cell was run. If your code is complicated or takes some time to execute, an asterisk * will be displayed in the pair of brackets `[*]:` while the code executes. 

Execute the code cell below which:

1. Prints "Waiting 5 seconds..."
2. Waits 5 seconds
3. Prints "Done"

As the program is running, watch the pair of brackets and you will see the code is running `[*]:`.

print('Waiting 5 seconds...')
import time
time.sleep(5)
print('Done')


If you missed the asterisk, you can run the code cell as many times as you like. Notice that each time you run a [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) the number increases in the pair of brackets `[ ]:`. This keeps track of the order cells were run. While we will always run code in order from top to bottom, keep in mind that [code cells](https://docs.tdm-pilot.org/key-terms/#code-cell) can be run in any order. If you run a [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) at the bottom of a notebook that depends on the output of a [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) at the top, you will probably get an error. When you get an error, it's a good idea to check if you missed a [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) earlier that needed to be run first.

## Creating a Cell


![The + symbol to create a new cell](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/new_cell.png)To create a new [cell](https://docs.tdm-pilot.org/key-terms/#cell), click the + at the top of the menu. A new [cell](https://docs.tdm-pilot.org/key-terms/#cell) will be created immediately underneath the currently selected [cell](https://docs.tdm-pilot.org/key-terms/#cell).

By default, a [code cell](https://docs.tdm-pilot.org/key-terms/#code-cell) is created. To change the cell type, click on the dropdown menu.
![Change cell type menu](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/change_code_cell.gif)

## Deleting a Cell

![right clicking to delete cell](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/delete_cell.gif)


To delete a [cell](https://docs.tdm-pilot.org/key-terms/#cell), select the [cell](https://docs.tdm-pilot.org/key-terms/#cell) (or set of cells) and select "Delete Cells" from the "Edit" menu. (Alternatively, press the key "d" twice.)


## Modifying a Cell

The text in [code cells](https://docs.tdm-pilot.org/key-terms/#code-cell) can be quickly changed like a regular textbox. In order to change the content of a [markdown cell](https://docs.tdm-pilot.org/key-terms/#markdown-cell), you need to expose the markdown content underneath by double-clicking the [cell](https://docs.tdm-pilot.org/key-terms/#cell). This will reveal the plain text of the markdown that creates various elements like headings, links, images, etc. When you want the cell to render again, you can simply run it again by pushing the play button or pressing Ctrl + Enter (Windows) or shift + return (OS X) on your keyboard.

## What is Markdown?

If you are familiar with HTML, markdown is a simplified way to write HTML elements. Basically it allows you to mark out where headings, italics, bold, and other kinds of basic formatting go. In terms of styling, markdown is very minimalist. If you would like to include an element that is not included in markdown in your notebook, you can also use HTML and CSS in your [markdown cells](https://docs.tdm-pilot.org/key-terms/#markdown-cell).

## How do I write my own Markdown?
Here are some basic examples to get you started. Double-click on this cell to see how each was made. There are many markdown cheatsheets available on the web. It can be useful to [print one out](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) and keep it handy.

## Headers

## Header Size 2
### Header Size 3
#### Header Size 4

## Emphasis

*Use asterisks around texts to add emphasis, also known as italics*
_You can also use underscores_
~~A strike-thru effect is created with two tildes~~ ~~

## Lists

A list of ordered items:
1. List item 1
2. List item 2

Unordered items:
* List item
* Also a list item

+ A list item
+ Another list item

- Also an item
- The last item

## Links

This is a link to [JSTOR](http://jstor.org). 

## Images

![Description of the image for accessibility(a jstor logo)](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/logoJSTOR.png)

## Horizontal Rule

Create a horizontal rule with three hyphens, asterisks, or underscores.
____

## Lesson Complete

Congratulations! You have completed "Getting Started with Jupyter Notebooks." If you have never programmed in [Python](https://docs.tdm-pilot.org/key-terms/#python) before, we recommend you complete:
* *Python Basics* I
* *Python Basics* II
* *Python Basics* III

## Start Next Lesson: [Python Basics I](./python-basics-1.ipynb)