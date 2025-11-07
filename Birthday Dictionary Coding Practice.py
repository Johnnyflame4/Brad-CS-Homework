"""
Coding Practice Exercise 33 - Birthday Dictionary
NAME: Brad Wing
SEMESTER: Fall 2025
"""

def main():
    
    # Create a dictionary of names and birthdays
    birthday_dictionary = {
        "Albert Einstein": "03/14/1879",
        "Benjamin Franklin": "01/17/1706", 
        "Ada Lovelace": "12/10/1815",
        "Marie Curie": "11/07/1867",
        "Leonardo da Vinci": "04/15/1452",
        "Isaac Newton": "01/04/1643",
        "Nikola Tesla": "07/10/1856"
    }
    
    # Welcome message and display available names
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthday_dictionary.keys():
        print(name)
    
    # Ask user for input
    print(">>> Who's birthday do you want to look up?")
    user_input = input().strip()
    
    # Look up the birthday using .get() method to avoid KeyError
    birthday = birthday_dictionary.get(user_input, None)
    
    if birthday:
        print(">>> {}'s birthday is {}.".format(user_input, birthday))
    else:
        print(">>> Sorry, we don't know {}'s birthday.".format(user_input))
        print(">>> Available names are: {}".format(", ".join(birthday_dictionary.keys())))

if __name__ == "__main__":
    main()
