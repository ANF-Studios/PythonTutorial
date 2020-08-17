# Hey everyone and welcome back to another text tutorial!
# In this script we will use Maths to work with Python
# Watch the video here: https://youtu.be/RpBskLBshoc

# As you know we already have did basic math, today we will do some more complex calculations
# Not too complex, that is for another video because it's too hard 🤣
print(2+2) # As you might know that this is a very simple caclulation of 2 adding 2, which is 5.

# Well, just like that we can do more heavy (heavy as relatively harder or humans) calculations like:
print(234 * 6 + 23)

# We can even take a step further by using divsion which returns a floating point number
print(56 * 2 + 7 / 4)

# A floating point value always has a decimal point in it no matter what
# They are also slower compared to normal ones called ints (integer)

# Also, if it is not clear, you can also use negative values like so:
print(-34 / 9 + -2)

# Since division returns a floating point number and sometimes we want an int
# We simply do "//" like so:
print(7//2) # You can optionally leave or not leave a space between characters

# You can also get the remainder of a value, by simply using:
print(9 % 4)
# If it does not leave a remainder, it simple gives 0
print(4 % 2)

# With Python, it is also possible to calculate powers of a value, using **:
print(5 ** 2) # Which is 25

# You can also do fun stuff such as:
Width = 923
Height = 383

print(Width * Height) # Nice way to do homework 😏

# Another example would be:
Fortune = input('Enter a random number from 1 to 10: ')
Misfortune = input('Enter a random number from 1 to 10: ')

Fate = Fortune - Misfortune
print('Your fourtune is {} out of 10!'.format(Fate))

# And here's a calculator from the tutorial:
x = int(input('Enter a number: ')) # The int tells the console that it is a number
y = int(input('Enter a number: ')) # Because input is a string by default

Multi = x * y
Divi = x / y
Add = x + y
Sub = x - y

print("""Multiplication: {}
Division: {}
Addition: {}
Subtraction: {}""".format(Multi, Divi, Add, Sub))

# Howeverm using a selected operator requires a condition, which is a topic for another video
# Stay tuned! Remember, if there is something wrong in this, be sure to open an issue
# Join my Discord Server here: https://discord.gg/fKWpK7A
# (Man this tutorial is filled with ads 😆) Enjoy!
