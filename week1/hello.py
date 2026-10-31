"""
Week 1 · Lab 1.1 — My First Python Script
=========================================
Follow the lab on the course dashboard, and write your code here.
Notebooks named below are in week1/notebooks/.
Stuck after trying? See solutions/week1/hello.py.

Run it with:   python week1/hello.py
"""

# TODO 1: Print a greeting.
#   How: put your text in quotes inside print().
#   Check: your greeting appears in the terminal when you run the file.
print("Good evening, everyone!")

# TODO 2: Create a variable that holds your name.
#   How: name = "Your Name"  (read = as "gets").
#   Help: week1-deepdive-1-python-speaks.ipynb, section 1 (Variables).
name = "Shadrack"

# TODO 3: Create a message, then print it together with your name.
#   How: join the two strings with +, as below.
#   Try next: print the same sentence with an f-string: f"I am {name}".
#   Help: week1-deepdive-1-python-speaks.ipynb, section 3 (f-strings).
#   Practice: week1-assignment.ipynb, Challenges 1 and 2.
message = "Good evening, I am "


print(message + name )