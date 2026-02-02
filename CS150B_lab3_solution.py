from DungeonGame import play_game, check_hp

#step 1
#Name: Billy, Major: General Computer Science

# Debri = "Junk"
# print("Boulder")
# print("Rubble")
# print("Thats a lot of " + Debri + "!")

#step 2
#(Prints)
# 1): Something is missing in the line below!
print("Hello, Blimey, Harry, didn't you ever wonder where your mum and dad learned it all?")
# 2): Fix the line below to correct it!
print("Learn what?")
# 3): Add the print statement from the instructions below this line!
print("Yer a Wizard Harry!")

#(Variables)
# 4): Something is missing in the line below!
hero = "Wizard"
# 5): Something is wrong with the line below! Can you fix it?
enemy = "Ogre"
# 6): Create a print statemnent below using both variables created above. Follow the format in the instructions for part 6 in step 2!
print(hero, "vs", enemy + ". Who will win?")

#step 3
name = input("What is your name? => ")
num1 = int(input("Please enter a whole number => "))
num2 = float(input("Please enter a decimal number => "))

lucky_num = num1 / num2

print("Hello", name, "! Your lucky number is", lucky_num, "today!")


#step 4
name = "Algeron the Great"
play_game(name)
