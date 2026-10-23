"""Exercise 5.2: Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: un code de carte de fidélité tapé par le client
# 2. Process: le programme redemande le code tant qu'il est faux, 3 fois maximum
# 3. Out: un message après chaque essai, puis un résumé
# 4. My stop condition, my attempt limit, my summary:
#    - Arrêt : le client tape le bon code (fid2026)
#    - Limite : 3 essais, comme une carte bancaire. Après 3 erreurs, la carte est bloquée.
#    - Majuscules et espaces : acceptés ("FID2026" et " fid2026 " marchent aussi)
#    - Résumé : le nombre d'essais utilisés, et si l'accès est accepté ou bloqué


# Your code below
code = "fid2026"
attempts = 0

while attempts < 3:
    answer = input("Enter your loyalty card code: ")
    attempts += 1
    if answer.strip().lower() == code:
        print("Correct code.")
        break
    else:
        print("Wrong code.")

print("Summary: you used", attempts, "attempt(s) out of 3.")
if answer.strip().lower() == code:
    print("Access granted.")
else:
    print("Card blocked.")
