import random

class Game:
    def guessNumber(self):
        print("+---------------------------------------+\n"
              "|-- You entered the guess number mode --|\n"
              "+---------------------------------------+\n")
        required_number = random.randint(1, 100)
        print("Required number generated\n")
        try:
            sub_number = int(input("-> Type the win number: "))
        except ValueError:
            print("\nGame ended. You doesn't type a number.\n")
            return
        while sub_number != required_number:
            if sub_number > required_number:
                try:
                    sub_number = int(input("My number is lower, choose another number: "))
                except ValueError:
                    print("Please, enter a number.")
            else:
                try:
                    sub_number = int(input("My number is bigger, choose another number: "))
                except ValueError:
                    print("Please, enter a number.")
        print("\nCongratulations! You have entered my number! It was", required_number, "\n")
        return

    def pickNumber(self):
        print("+---------------------------------------+\n"
              "|-- You entered the pick number mode ---|\n"
              "+---------------------------------------+\n")
        sub_number = random.randint(1, 100)
        print("Is it your number", sub_number, "?")
        response = input()
        max_numb = 100
        min_numb = 1
        while response != "=":
            if response == "+":
                min_numb = sub_number
                try:
                    sub_number = random.randint((sub_number + 1), (max_numb - 1))
                except ValueError:
                    print("Are you kidding? Your number must be", sub_number, "!")
            elif response == "-":
                max_numb = sub_number
                try:
                    sub_number = random.randint((min_numb + 1), (sub_number - 1))
                except ValueError:
                    print("Are you kidding? Your number must be", sub_number, "!")
            else:
                print("You doesn't type a valid character. '+' for bigger, '-' for lower, '=' for match.")
            print("Is it your number", sub_number, "?")
            response = input()

        print("\nI find it! Your number is", sub_number, "\n")
        return

    def getHelp(self):
        print("###############################################\n"
              "############## Available commands #############\n"
              "###############################################\n"
              "\t -> Guess mode (1)\n"
              "\t -> Pick mode (2)\n"
              "\t -> Exit game (3|exit|quit)\n"
              "\t -> Help (4|help)\n")