import number_game

def main():
    game = number_game.Game()
    print("Welcome to guess number game!!!\n")
    game.getHelp()
    while True:
        command = input("*) Type the game mode you want to play \n")
        if command == "1": #Guess number mode
            game.guessNumber()
            pass
        elif command == "2": #Pick number mode
            game.pickNumber()
            pass
        elif command == "help" or command == "4":
            game.getHelp()
            pass
        elif command == 'quit' or command == 'exit' or command == '3':
            break
        else:
            print("In order to get help type 'help'")

main()