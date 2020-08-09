# If you want the user to interact with the console, we use a method called "input()", which is pretty straight forward
# Here is an example:
input() # This enables input and allows the user to type on the keyboard

# However, when it will run, it will print nothing, to print something without using print(), we do:
input('Text') # Where text is the prompt

# And here is something fun, if we want the console to print whatever the input is, we do:
print(input()) # This will simply print the user input

# Now, what's the use of this if we cannot do anything with it. We can use it like this for example:
print('Hello, my name is ' + input())

# But, there is no use in using input() if we can do nothing but take input and not use it.
# To use it we store it in a variable like so
Example = input('Your name: ') # Now, let's use it below
print('Hello ' + Example + ', I am Jason. Nice to meet you!')

# Now let's try something else with input(), like upper or capitalize, something like we did previously
# with print, quick recall: print('{0}, {1}'.format(a, b))
input('You: ').capitalize() # Makes the first letter capital
input('You: ').upper() # Makes every letter uppercase
input('You: ').lower() # Makes every letter lowercase
input('You: ').replace('Alex', 'Jason') # Replaces a given string with an included string, in this case Alex with Jason

# But, since you are here and want to learn, here's a bonus just for you:
print(input('You: ').split(' ')) # This will seperate anything that has a space in between

# Now, let my show you a simple demonstration of of could this be used for a conversation:
input('Bot: Hello!\nYou: ')
name = input('Bot: What is your name? I am Jason.\nYou: ')
input("Bot: Cool, nice to meet you {0}. How's your day?".format(name)) # Get reference from previous tutorial

# And before we finish this tutorial off there are some cool things that I wanted to show to you which
# is really, really useful: Escape Sequences!
# \n, \t, \', \", \? etc
# These are useful when you want to make some changes on how your text is displayed to work arounds on using
# quotes inside of quotes. Here are some examples:
input('This is a sentence, and you will be able to send input below this sentence\n') # New line

input('This is a sentence, but you won\'t be able to give input.') # If we simply did:
# input('This is a sentence, but you won't be able to give input.'), it would just give out an error.
# The same goes for the double quotes!
print("Didn't you said, \"Yes, I will do my homework\"?")

# And with that said, I need to do my homework so this tutorial must stop! See you next time.
# Psst.. need help: https://discord.gg/fKWpK7A
# Watch the tutorial here: https://youtu.be/mSMXbJ3uKRc