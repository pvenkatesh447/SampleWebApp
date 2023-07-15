print("welcome to guessing challenge")
print("Thinking a number between 1 to 100")
print("If your guess is below 1 and above 100,i'll tell you out of the bounds")
print("if your guess is more than 10 away from my number,i'll tell you you're cold")
print("if your guess is within 10 away from my number,i'll tell you you're warm")
print("if your guess is farther than the previous number,i'll tell you you're coldest")
print("if your guess is closer than the previous number,i'll tell you you're warmer")
print("ALL THE BEST")
print("LET'S START THE GAME")


from random import randint
num=randint(1,100)
guesess=[0]
while True:
    guess=int(input("guess the number between 1 to 100:"))
    if guess<1 or guess>100:
              print("out of bounds")
              continue
    if guess==num:
              print("congrats!you have guess the correct number in {}attempts".format(len(guess)))
              break
    guesess.append(guess)

    if guesess[-2]:
        if abs(num-guess)<abs(num-guesess[-2]):
            print("WARMER")
        else:
            print("COLDER")
    else:
        if abs(num-guess)<10:
            print("WARM")
        else:
            print("COLD")