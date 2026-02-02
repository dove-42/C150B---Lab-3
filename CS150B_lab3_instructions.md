# Lab 03 - Comments, Printing, Type Casting, Oh my!
## Introduction
Welcome to lab! This lab is going to give you some more practice with varibles, printing, input, and type casting. It will also give you some practice with comments.

## Step 1 (Comments)
FIXME - fill in with Gino's instructions for step 1

## Step 2 (Printing and Variables)
FIXME - fill in with Gino's instructions for step 2

## Step 3 (Input and Casting)
In this step you will be working with input and casting. By now you have probably run into TypeErrors while coding. These happen when you try to do an action that doesn't make sense for a given variable's type--like trying to do math on strings. The types you need to know for this lab are:
- float: Decimal (or "floating point") numbers like 13.2, 0.0, or 46.8.
- int: Whole numbers like 13, 207, 5.
- string: Anything with quotes ("" or '') around it. The quotes tell the computer to treat the charcters or numbers between them as words. "Hello" is a string and so is "2048".

The input() function will always read in data as a string type. If you want to do math with input, you will need to cast it to a number type (int or float) first. Each type has a unique keyword for casting.
- int: int()
- float: float()
- string: str()

You can directly cast input as you are reading it in (remember that sentences inside the parentheses of the input function will print a prompt to the user's screen):
```python3
num = int(input("What is your favorite number? => "))
```

Or you can load it into a variable and then cast it after (you can cast any variable this way, not just ones loaded from user input):
```python3
string_num = input("What is your favorite number? => ")
int_num = int(string_num)
```

Your job in this step is to write some code that will:
1) Take in a user's name and store it in a variable.
2) Take in a whole number from the user and store it in a variable.
3) Take in a decimal number from the user and store it in a variable.
4) Calculate the users "lucky number" by dividing the whole number by the decimal number and store the result in a variable.
4) Print a message that greets the user and tells them what their lucky number is. (You will need to use the variables you created in earlier steps for this).

If your code is working and you input "student", "20", and "4.0", you should have this sentence printed to your terminal:
```
Hello, student! Your lucky number is 5.0 today!
```
Ensure you are following the format exactly (case, punctuation, spacing).

## Step 4 (Defeat the Ogre!)
Now that you've had some more practice with casting, let's play a game. You are now a wizard and have to defeat a terrible ogre who is attacking your village. To do this:
1) Create a varibale called "name" and set it's value to whatever you want your wizard name to be.
2) Uncomment the last line below "step 4" WITHOUT changing it in any way. This line is something called a "function call" and we will learn more about it later in the class. For now, all you need to know is uncommenting this line lets the computer load the game.
```python3
   #Uncomment this line to play the game
   #play_game(name)
```
3) Hit the run button in the upper left corner. This will start the game. You should see an ogre in your terminal if everything is working
correctly. (You may have to fill out the inputs for the previous step before it will load).
4) Play the game to completion for full points on this step of the lab. Good luck!

## Step 5 (Turning in)
Congratulations! You’ve completed the lab and should now have a better understanding of comments, printing, variables, types, and casting! Make sure you click through the canvas link to the assignment if you haven’t already. This triggers the linking process, so canvas can get an updated score. Go ahead and click the "submit" button to have your lab graded.
