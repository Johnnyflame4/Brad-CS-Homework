/**
* Starter Code Function Practice Code Along
*
*
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int64_t add(int64_t a, int64_t b) {
    return a + b;

}

int64_t subtract(int64_t a, int64_t b) {
    return a - b;
}

int64_t multiply(int64_t a, int64_t b) {
    return a * b;
}

int64_t divide(int64_t a, int64_t b) {
    return a / b;
}

int64_t modulus(int64_t a, int64_t b) {
    return a % b; // remainder
}

int main() {
    int64_t a = 10000000;
    int64_t b = 5000;

    printf("Addition: %ld\n", add(a, b));
    printf("Subtraction: %ld\n", subtract(a, b));
    printf("Multiplication: %ld\n", multiply(a, b));
    printf("Division: %ld\n", divide(a, b));
    printf("Modulus: %ld\n", modulus(a, b));
    return 0;
}