# Lab 03 - Comments, Printing, Type Casting, Oh my!
## Introduction
Welcome to lab! This lab is going to give you some more practice with varibles, printing, input, and type casting. It will also give you some practice with comments.

## Step 1 (Comments)
Before getting into printing and type casting, one useful feature most programming languages have are **comments**! 
Comments are a great way to give information within the code without interfering with the code itself-- like a description to a picture! 
Not only that, but you can comment out any code you don't want to test or to set aside code.
```python3
# Hello! I am a comment!

Hello, I am not a comment!
```
To make comments, place a hashtag (#) on the left side before your code or your description. 
You can tell you have done it right as comments have a decreased opacity as shown above!

- For Step 1, your goal is to set your name and major underneath **#Step1** and have it commented out:
```python3
# Name: Boby the Bob, Major: Musical Intstruments
```

Next for Step 1, there is some code in **#Step1** we currently dont want. However, rather then deleting it, we might have a use for it later, so commenting it out would be the best idea.

- Comment out all the code in **#Step1**:
```python3
print("I'm code that wants to be commented!")

# print("Im good")
```
**TIP:** When it comes to comments, you can add and remove multiple comments if you highlight the code and click: **CTRL + /**


## Step 2 (Printing and Variables)
**Printing** and **Variables** are some of the most important things to learn when it comes to coding. Understanding these concepts can help you write, test, and read code!

Thats cool and all, but what are they?

**PRINTING**: You have seen print statements throughout the labs and lecture, but what do they actually do?
```python3
print("Hello!")
```
Lets break it down!
- The word **print** is a built-in function for Python, meaning it will have specific rules. In this case, **print** means it will display output to the console for a user to see!
- The parenthesis **()** are used to surround what we want to be **printed** out! In the example, **Hello!** is in the parenthesis, so it will be printed out!
- The quotes **" "** mean whatever is in them, which this case is **Hello!**, will be **printed** out exactly how it looks! This makes it possible to write!

**BENEFITS TO PRINTING**: Showing program results, debugging, writing, formatting, user interaction, etc.

**VARIABLES**: The process of storing information by a name you create:
```python3
boxes = "bunch of data and stuff"
storage = "4"
print("please put the " + boxes + " in storage " + storage + ".")
```
Lets break it down!
- The word **boxes** and **storage** are the variables in the code. Variables can be named whatever you like, however naming it related to what your doing can help keep track of what your code does!
- The equal sign **=** is what connects are variable. Without this, a variable wont be created and have anything in it!
- The **"bunch of data and stuff"** and **"4"** is what is being stored in the variables! This means whenever we type **boxes** or **storage**, it will instead be what is stored in them!
- In the print, you can see that are variables **boxes** and **storage** dont have quotes. This makes it so it will be connected back to the variable we created! If it was surrounded by quotes, it will only produce the word "boxes" and not actually what is inside **boxes**, which in this example is **"bunch of data and stuff"**.

**BENEFITS TO VARIABLES**: Be able to store, duplicate, label, manage and manipulate data, etc.


### **Step 2 will get you practice in understanding what and how to make prints and variables!**

1) Fill in the error to make the print work!
2) Fix the error to make the print work!
3) Create a print statement by copying and pasting the line below:
```python3
Your a Wizard Harry!
```
4) Fill in the error to make the variable work!
5) Fix the error to make the variable work!
6) Create a print statement using both variables above and format it like the line below! If done correctly, it should look like this:
```
Wizard vs Orge. Who will win?
```
Remember, you can use the plus **+** (no space) or the comma **,** (adds space) to connect strings and variables together! 
**NOTE:** Hard coding is the process of typing the answer without actually using any variables. If you type this line in without variables, you won't get points!

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
1) Create a variable called "name" and set it's value to whatever you want your wizard name to be.
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
