# Day One

Our first day at coding in Python.<br>
Apparently the flow for this course is a series of exercises followed by a challenge. The challenge being that day's project

### Exercise 1.1
Simple print() statement to print a string.

#### Code
```python
print("Hello, World!")
```

### Exercise 1.2
Debugging exercise.<br>
Instructor provides some python code that throws errors.<br>
Multiple print() statements that have misplaced/missing/or embedded quote characters.<br>
From the errors thrown by an interpreter the student is expected to *fix* the code so that the expected strings are printed to the screen.

This is something we all face nearly every day, at least on the days we write code &#x1F612;

### Exercise 1.3
Getting close to real coding now.<br>
Here we are introduced to variables.<br>
We are to make use of one or more variables in order to print a user supplied string to the print() function.<br>
I chose to make use of the concept of **user accounts** on a host. So instead of a user supplied string I pull the user's name from the shell environment and count the characters in the username found. This script can be run by any user and give *personalized* output for that user. Cool eh?<br>
 Only Day one and I'm already way ahead of expectations for the level of simplicity implied by the course content so far.<br>

#### Code
 
```
from os import environ


username = environ.get("USER")           # maybe not be portable to other OS; I'm doing this on Debian bookworm
print(f"Your username is: {username}")   # f-strings FTW
print(f"There are {len(username)} characters in your username")

```

### Exercise 1.4

Gotta say something about this. The exercise asks the student to swap the values contained by two variables `a` and `b`  
Now I don't fault the instructor for showing students how to break the task down to the simplest elements. For new learners it can be imperative to break a task down to the simplest of a series of tasks leading to solution. But oh my, this is such a good place to emphasize how Python makes coding so much easier than other languages. The pattern of 
```
x,y = y,x   # swap x for y and y for x in one line of code
```
is so common I gasped at the given solution. There is absolutely no need for a third variable for the initial two to take turns residing in.

If I were writing the exercise the code would look like this
#### Code

```
a = 5
b = 10
print(a)    # console will emit '5'
print(b)    # console will emit '10'
a,b = b,a
print(a)    # console will emit '10'
print(b)    # console will emit '5'
```
It is my firm belief that good, or better still ***Best*** practices should be instilled in newly hatched Python Coders at the earliest opportunity.<br>
Like Exercise 1.4

## Project

The project for today is to write a script for generating Band Names. The script in essence takes two user supplied strings, concatenates them with a separating ' ' (space) and prints that result to screen.  
Oh boy!  
To simplify debugging I will start with doing some input validation on the user supplied strings.<br>
If there is one thing I learned in my forays into IT Security and PenTesting it is that if users can<br>
fudge up an input ---> **They Will!!!**

#### Project Steps

	1) Announce start-up with a welcome message
	2) Provide two consecutive prompts that take user input
	3) Validate user input can be output as length limited strings
	4) Print solution message that includes the strings concatenated into one

#### The Code

```
# file gen_band_name.py as suggested by Instructor
print("""
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    Welcome to Band Name the generator
    You will prompted for two strings
    Please only use letters [A-Z] or [a-z]
    or numbers [0-9]
    If any input is over 12 characters long you will be prompted
    for a new value
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    """)

def gen_name():
	first_word = input("Please enter the name of the city or town you were born in: ")
	second_word = input("Please enter the name you called your first pet: ")
	print("Your home-town band might be named...")
	print(first_word, second_word)


# have we learned this pattern yet?
if __name__ == '__main__':
	# call our function
	gen_name()
```
File is also available [Here](./gen_band_name.py)

## Takeaways

Can't believe I'm already engaging in bad habits.<br>
To my knowledge Python coders take pride in writing portable code. That is, code that will run regardless of the host it is run on. There is a rather lot of modules readily available from the [Python Package Index](https://pypi.org) that will run pretty much anywhere. Regardless if the host is a Mac, that crap from Redmond WA, or a safe and reliable out of the box Linux&trade; host.<br> 
It may even be a requirement to provide for multi-platform to get on PyPi. I really don't know and at the moment am not going to take the time to find out. All I know is that every package I've come across from PyPI seems to be installable on any platform.
btw it took longer to compose this README than it did to write the code. That does not bode well for getting thru this class as quickly as I presumed I would.
Also discovered I should not push every little change moments after I make it or I'll end up with a git log that is polluted with tiny inconsequential edits. Do a Day **THEN** push it up.
