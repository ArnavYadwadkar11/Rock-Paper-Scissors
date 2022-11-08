import random
import time
from colorama import Fore


def game():
    computer_choices = ['rock', 'paper', 'scissors']
    pointers = int(input(Fore.LIGHTCYAN_EX + 'How many points should the game be? '))
    player_points = 0
    computer_points = 0
    print('Rock')
    time.sleep(0.5)
    print('Paper')
    time.sleep(0.5)
    print('Scissors')
    time.sleep(0.5)
    retry = None
    while retry != 'no':
        computer = random.choice(computer_choices)
        player = input('Shoot! ')
        print(computer)
        
        # Tie
        if player.lower() == computer.lower():
            print( Fore.WHITE + "It's a tie!")
            print( Fore.YELLOW + 'Player points:' + ' ' + str(player_points) + ' ' + 'Computer points:' + ' ' + str(computer_points))
            print('You chose ' + player + ' and ' + 'computer chose ' + computer)
            if player_points == pointers:
                print('GAME OVER! You win')
                retry = input('Do you want to play again?? ')
                if retry.lower() == 'yes':
                    game()
                elif retry.lower() != 'yes':
                    print(Fore.YELLOW + 'Ok! Thanks for playing')
                    break

            elif computer_points == pointers:
                print('GAME OVER! computer wins!')
                retry = input('Do you want to play again?? ')
                if retry.lower() == 'yes':
                    game()
                elif retry.lower() != 'yes':
                    print(Fore.YELLOW + 'Ok! Thanks for playing')
                    break

        # You chose rock
        elif player.lower() == 'rock':
            if computer.lower() == 'paper':
                print(Fore.RED + 'Paper covers rock!')
                computer_points += 1
                print(Fore.YELLOW + 'Player points:' + ' ' + str(player_points) + ' ' + 'Computer points:' + ' ' + str(computer_points))
                print('You chose ' + player + ' and ' + 'computer chose ' + computer)
                if computer_points == pointers:
                    print('GAME OVER! Computer wins')
                    retry = input('Do you want to play again?? ')
                    if retry.lower() == 'yes':
                        game()
                    elif retry.lower() != 'yes':
                        print(Fore.YELLOW + 'Ok! Thanks for playing')
                        break
            else:
                print(Fore.GREEN + 'Rock smashes scissors!')
                player_points += 1
                print(Fore.YELLOW + 'Player points:' + ' ' + str(player_points) + ' ' + 'Computer points:' + ' ' + str(computer_points))
                print('You chose ' + player + ' and ' + 'computer chose ' + computer)
                if player_points == pointers:
                    print('GAME OVER! You win')
                    retry = input('Do you want to play again?? ')
                    if retry.lower() == 'yes':
                        game()
                    elif retry.lower() != 'yes':
                        print(Fore.YELLOW + 'Ok! Thanks for playing')
                        break
                    
                    
        # You chose scissors
        elif player.lower() == 'scissors':
            if computer.lower() == 'rock':
                print(Fore.RED + 'Rock smashes scissors!')
                computer_points += 1
                print(Fore.YELLOW + 'Player points:' + ' ' + str(player_points) + ' ' + 'Computer points:' + ' ' + str(computer_points))
                print('You chose ' + player + ' and ' + 'computer chose ' + computer)
                if computer_points == pointers:
                    print('GAME OVER! computer wins!')
                    retry = input('Do you want to play again?? ')
                    if retry.lower() == 'yes':
                        game()
                    elif retry.lower() != 'yes':
                        print(Fore.YELLOW + 'Ok! Thanks for playing')
                        break
            else:
                print(Fore.GREEN + 'Scissors cuts paper!')
                player_points += 1
                print(Fore.YELLOW + 'Player points:' + ' ' + str(player_points) + ' ' + 'Computer points:' + ' ' + str(computer_points))
                print('You chose ' + player + ' and ' + 'computer chose ' + computer)
                if player_points == pointers:
                    print('GAME OVER! You win')
                    retry = input('Do you want to play again?? ')
                    if retry.lower() == 'yes':
                        game()
                    elif retry.lower() != 'yes':
                        print(Fore.YELLOW + 'Ok! Thanks for playing')
                        break

        # You chose paper
        elif player.lower() == 'paper':
            if computer.lower() == 'scissors':
                print(Fore.RED + 'Scissors cuts paper')
                computer_points += 1
                print(Fore.YELLOW + 'Player points:' + ' ' + str(player_points) + ' ' + 'Computer points:' + ' ' + str(computer_points))
                print('You chose ' + player + ' and ' + 'computer chose ' + computer)
                if computer_points == pointers:
                    print('GAME OVER! Computer wins')
                    retry = input('Do you want to play again?? ')
                    if retry.lower() == 'yes':
                        game()
                    elif retry.lower() != 'yes':
                        print(Fore.YELLOW + 'Ok! Thanks for playing')
                        break
            else:
                print(Fore.GREEN + 'Paper covers rock!')
                player_points += 1
                print(Fore.YELLOW + 'Player points:' + ' ' + str(player_points) + ' ' + 'Computer points:' + ' ' + str(computer_points))
                print('You chose ' + player + ' and ' + 'computer chose ' + computer)
                if player_points == pointers:
                    print('GAME OVER! You win')
                    retry = input('Do you want to play again?? ')
                    if retry.lower() == 'yes':
                        game()
                    elif retry.lower() != 'yes':
                        print(Fore.YELLOW + 'Ok! Thanks for playing')
                        break

game()