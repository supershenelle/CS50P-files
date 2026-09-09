#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int coins = 0;

    // Quarters
    while (cents >= 25)
    {
        cents -= 25;
        coins++;
    }

    // Dimes
    while (cents >= 10)
    {
        cents -= 10;
        coins++;
    }

    // Nickels
    while (cents >= 5)
    {
        cents -= 5;
        coins++;
    }

    // Pennies
    while (cents >= 1)
    {
        cents -= 1;
        coins++;
    }

    printf("%i\n", coins);
    return 0;
}
