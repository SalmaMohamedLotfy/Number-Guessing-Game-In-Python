import random
def main():
    print(" Welcome to 'guess the number'! ")
    print(" Im thinking of a number between 1 and 100. ")
    # Generate a random number between 1 and 100
    number_to_guess=random.randint(1,100)
    attempts=0
    score=100
    #loop until the user guesses the number
    while True:
        # Get the users guess
        my_guess =int(input("Enter a guess: "))
        attempts+=1
        # check if the guess is correct
        if my_guess>number_to_guess:
          print (" Your guess is too high. " )
          score-=10
        elif my_guess<number_to_guess:
          print( " Your guess is too low. ")
          score-=10
        else:
            print(" Good job ! you guessed the number in " + str(attempts) + " attempts. ")
            print (" Your final score now is : " + str(score) )
            break
        if score<=0:
            print(" Game over, The number was " + str(number_to_guess))
            break
if __name__ == '__main__':
    main()        
            
         