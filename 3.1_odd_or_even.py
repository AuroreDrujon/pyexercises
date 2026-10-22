"""Exercise 3.1: Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even. 

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: un nombre entier N tapé par l'utilisateur - OK
# 2. Process: pour chaque nombre de 1 à N, le programme vérifie s'il est pair ou impair - OK
# 3. Out: N lignes, chacune avec le nombre et "pair" ou "impair" - Ok
# 4. What happens on 0, on a negative number, on a very large number:
#    0 ou négatif -> "Erreur ! veuillez taper un nombre >= 1" - OK
#    plus de 100 -> "Erreur ! veuillez taper un nombre <= 100", car au-delà c'est trop long à lire - OK



# Your code below
number =(int(input("Enter a number :")))

if number < 1:
    print("Error: please enter a number >= 1")
elif number > 100:
    print("Error: please enter a number <= 100")
else:
 for number in range(1, number + 1):
    if number % 2 == 0:
     print(number, "is even.")
    else:
     print(number, "is odd.")