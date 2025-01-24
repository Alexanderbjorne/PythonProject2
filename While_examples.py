# You have 3 lives. I roll the die, if i roll 6 you win
# If not 6, you lose 1 life.

from random import randint

lives = 3
while lives > 0:
    roll = randint(1, 6) # make sure to not put a: and b: !!
    if roll == 6:
        print(f"You rolled a {roll}!You win!")
        break # this exists the while even if lives are still > 0
    print(f"You rolled a {roll}! You lose a life!")
    lives -= 1
    print(f"You have {lives} lives left")
if lives == 0:
    print("You do not have any lives left! Game over!")


