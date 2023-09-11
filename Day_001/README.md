# Day One

Our first day at coding in Python.  
Apparently the flow for this course is a series of exercises followed by a challenge. The challenge being that day's project

### Exercise 1.1
Simple print() statement to print a string.

### Exercise 1.2
Debugging exercise.  
Instructor provides some python code that throws errors.  
Multiple print() statements that have misplaced/missing/or embedded quote characters.  
From the errors thrown by an interpreter the student is expected to *fix* the code so that the expected strings are printed to the screen.

### Exercise 1.3
Getting close to real coding now. Here we introduce variables. We are to make use of one or more variables in order to print a user supplied string to the print() function.  
I chose to make use of the concept of user accounts on a host and instead of a user supplied string I will pull the user's name from the shell environment and count the characters in that username. This script can be run by any user and give *personalized* output for that user. Cool eh? Only Day one and I'm already way ahead of expectations for the level of simplicity implied by the course content so far.  
I'm sure a day in the next two week (those first 15 days are supposed to be basic) will be devoted to module import.

```
from os import environ


username = environ.get("USER")           # probably not portable to other OS
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

```
a = 5
b = 10
print(a)    # console will emit '5'
print(b)    # console will emit '10'
a,b = b,a
print(a)    # console will emit '10'
print(b)    # console will emit '5'
```
It is my firm belief that good, or better still ***Best*** practices should be instilled in newly hatched Python Coders at the earliest opportunity. Like Exercise 1.4

## Project

The project for today is to write a script for generating Band Names. The script in essence takes two user supplied strings, concatenates them with a separating ' ' (space) and prints that result to screen.  
Oh boy!  
To simplify debugging I will start with doing some input validation on the user supplied strings. If there is one thing I learned in my forays into IT Security and PenTesting it is that if user's can fudge up an input ---> **They Will!!!**

#### Project Steps

	1) Announce start-up with a welcome message
	2) Provide two consecutive prompts that take user input
	3) Validate user input can be output as length limited strings
	4) Print solution message that includes the strings concatenated into one

#### The code

```
# Code goes here when I get around to transposing raw python to markdown
```
For now we'll have to settle for a [link](./gen_band_name.py)

## Takeaways

Can't believe I'm already engaging in bad habits. To my knowledge Python coders take pride in writing portable code. That is, code that will run regardless of the host it is run on. There is a rather lot of modules readily available from the [Python Package Index](https://pypi.org) that will run pretty much anywhere. Regardless if the host is a Mac, that crap from Redmond WA, or a safe and reliable out of the box Linux&trade; host  
It may even be a requirement to provide for multi-platform to get on the Index. I really don't know and at the moment am not going to take the time to find out. All I know is that every package I've come across from PyPI seems to be installable on any platform.
btw it took longer to compose this README than it did to write the code. That does not bode well for getting thru this class as quickly as I presumed I would.
Also discovered I should not push every little change moments after I make it or I'll end up with a git log that is polluted with tiny inconsequential edits. Do a Day **THEN** push it up.
