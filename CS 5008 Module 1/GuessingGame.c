
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// random number generator function

int gerRandomNumber(int min, int max) {
    return rand() % (max - min + 1) + min;
}

// get input from player

int getinput() {
    int input;
    printf("Enter your guess (1-100): ");
    scanf("%d", &input);
    return input;
}
// need loop that gives foodback for high or low or correct
// we need a loop to start or play again

int runGame(int randomNumber) {
    int guess = 0;
    int attempts = 0;

    while (guess != randomNumber) {
        guess = getinput();
        attempts++;
        if (guess < randomNumber) {
            printf("Too low! Try again.\n");
        } else if (guess > randomNumber) {
            printf("Too high! Try again.\n");
        } else {
            printf("Congratulations! You guessed the correct number: %d\n", randomNumber);
            printf("It took you %d attempts.\n", attempts);
        }
    }
    return 0;
}






int main() {
    srand(time(NULL)); // Seed the random number generator
    printf("Welcome to the Guessing Game!\n");
    int randomNumber = gerRandomNumber(1, 100);
    runGame(randomNumber);
    int input = getinput();
    printf("The value you entered is: %d\n", input);
    return 0;


}