#include <stdio.h>
#include <stdlib.h>

void forLoopPractice(int start, int end) {
    for (int i = start; i < end; i++) {
        printf("For loop %d\n", i);
    }

    for (int i = end - 1; i >= start; i--) {
        printf("For loop %d\n", i);
    }
    for (int i = start; i < end; i += 2) {
        printf("For loop %d\n", i);
    }
}

void whileLoopPractice(int start, int end) {
    //while loop
    int i = start;
    while (i < end) {
        printf("While loop %d\n", i);
        i++;
    }

    i = end - 1;
    while (i >= start) {
        printf("While loop %d\n", i);
        i--;
    }
    i = start;
    while (i < end) {
        printf("While loop %d\n", i);
        i += 2;
    }
}

void whileLoopMenu() {
    int choice;
    while (choice != 3) {
        printf("1. For Loop\n");
        printf("2. While loop\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                forLoopPractice(0, 5);
                break;
            case 2:
                whileLoopPractice(0, 5);
                break;
            case 3:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");

        }
    }

}

int main() {
    whileLoopMenu();
    return 0;
}