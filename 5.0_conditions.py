"""Exercise 5.0: Making the program decide

WHAT THE PROGRAM MUST DO
    Ask the user for a number, then display a different message depending on which
    range that number falls into. At least four ranges.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your four ranges, what are their exact boundaries, and what does each
       message say? Write the boundaries down before you code them.

WHAT THE AI CANNOT KNOW
    Your ranges and your boundaries. It can be an age, a budget, a satisfaction score,
    a delivery time. Choose something with a real meaning and defend the cut-off points.

    Boundaries are where programs go wrong. Decide explicitly whether a value exactly
    on the boundary belongs to the range above or the one below.

CHECK IT YOURSELF
    Test each of your boundary values exactly: if one range ends at 25, run it with 25.
    Then with 24 and 26. Write in a comment whether each landed where you intended.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: une note de satisfaction client, nombre entier entre 0 et 10, tapée par l'utilisateur
# 2. Process: le programme regarde dans quelle tranche se trouve la note
# 3. Out: un message qui indique le profil du client et l'action à mener
# 4. My ranges, my boundaries, my messages:
#    Inspiré du NPS (Net Promoter Score), avec les détracteurs découpés en deux,
#    car un client à 2/10 et un client à 6/10 ne demandent pas la même réaction.
#    - 0 à 3  -> "Very dissatisfied: contact this customer as a priority."
#    - 4 à 6  -> "Dissatisfied: detractor, find out what went wrong."
#    - 7 à 8  -> "Passive: satisfied but not loyal yet."
#    - 9 à 10 -> "Promoter: loyal customer, ask for a review."
#    Frontières : chaque valeur limite appartient à la tranche indiquée
#    (3 = very dissatisfied, 4 = dissatisfied, 6 = dissatisfied, 7 = passive,
#    8 = passive, 9 = promoter).
#    En dehors de 0 à 10 -> "Error: please enter a score between 0 and 10."

# Your code below
score = int(input("Enter a satisfaction score (0-10): "))

if score < 0 or score > 10:
    print("Error: please enter a score between 0 and 10.")
elif score <= 3:
    print("Very dissatisfied: contact this customer as a priority.")
elif score <= 6:
    print("Dissatisfied: detractor, find out what went wrong.")
elif score <= 8:
    print("Passive: satisfied but not loyal yet.")
else:
    print("Promoter: loyal customer, ask for a review.")