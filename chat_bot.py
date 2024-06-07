def greet():
    bot_name = input("Name please: ")
    create_year = input("Year please: ")
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {create_year}.")


def remind_name():
    print('Please, remind me your name.')
    your_name = input("Type your name: ")
    print(f"What a great name you have, {your_name}!")


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5, and 7.")
    remainder3 = int(input("Remainder of 3 please: "))
    remainder5 = int(input("Remainder of 5 please: "))
    remainder7 = int(input("Remainder of 7 please: "))
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Welcome wise old man, aren't you? {your_age} years old.")


def count():
    print("Now I will prove to you that I can count to any number you want.")
    any_no = int(input("Give me a number: "))
    total = 0
    counter = 0
    while counter <= any_no:
        total = total + counter
        counter = counter + 1
    print(f"Have a good day, sum value of given number is {total}.")


def test():
    print("Let's test your coding knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    ans = input("Please enter the number of the correct answer: ").strip()
    if ans != '2':
        print("Try again.")
    else:
        print("Completed.")


def end():
    print("Congratulations, have a nice day!")


greet()
remind_name()
guess_age()
count()
test()
end()
