#Snakes and Ladders
import random

class board():
    #Declaring, the number of snakes and ladders in total, the empty dictionary with all the snakes and ladders and an array to avoid duplicates
    num_of_SnL = random.randint(10,25)
    SnL = {}
    array_for_gen = list(range(1,100))
    #loop uses the generated array and pops values out and puts them into a dictionary with the key being the square the player is on and the value being the square they will end up on
    while num_of_SnL >= 0:
        x = array_for_gen.pop(random.randint(0, len(array_for_gen) - 1))
        y = array_for_gen.pop(random.randint(0, len(array_for_gen) - 1))
        SnL[x] = y
        num_of_SnL -= 1
    #Empty lists for corresponding snakes and ladders to be built
    snakes = {}
    ladders = {}
    #Linearly searches through lists and sorts them into snakes and ladders
    for item in SnL:
        if item > SnL[item]:
            snakes[item] = SnL[item]
        else:
            ladders[item] = SnL[item]
#Makes a player class which inherits the board and a dice method
class player(board):
    position = 0
    name = "placeholder_name"

    def dice(self):
        u = random.randint(1,6)
        self.position += u
#function that explains instructions to players on front menu
def instructions():
    print("Hi, Welcome to Snakes and Ladders! This game is made for 2 to 4 players. You will be asked to select the number of players you would like to play with.")
    print("Each player will then choose a nickname. A random player will be chose to begin the game. Each player will then take turns rolling the dice trying to ")
    print("reach the end of the game, the 100th tile. Along the way, players will encounter either snakes or ladders. Snakes take you from tiles and bring you ")
    print("back closer to the start while ladders take you closer to the end. Good luck and Have fun!")
#creating instances/objects of the player class for the maximum amount of players
player0 = player()
player1 = player()
player2 = player()
player3 = player()
#Placing all the players into a list to make it easier to index each player
list_of_players = [player0, player1, player2, player3]
#Naming all the characters and then calls the main game function
def player_naming(num_of_players):
    num = num_of_players
    while num_of_players >= 1:
        list_of_players[num_of_players - 1].name = input("Please enter a name: ")
        num_of_players -= 1
    turn(random.randint(0, num - 1), num)
#turn function starts all the games
def turn(player_id, num_of_players):
    while ((player0.position < 100) and (player1.position < 100) and (player2.position < 100) and (player3.position < 100)):
        print("Hi, there {0}! What would you like to do on your turn?".format(list_of_players[player_id].name))
        print("- type \"ladders\" to check for the position of ladders")
        print("- type \"position\" to check for your location on the board")
        print("- type \"roll\" to advance and end your turn")
        m = input("- type \"snakes\" to check for the position of snakes\n")
        # Currently both ladders and snakes return all snakes and ladders
        if m == "ladders":
            print(board().ladders)
        elif m == "snakes":
            print(board().snakes)
        elif m == "roll":
            new_square = list_of_players[player_id].dice()
            for tile in list_of_players[player_id].SnL:
                if tile == list_of_players[player_id].position:
                    print("going on a snake")
                    list_of_players[player_id].position = list_of_players[player_id].SnL[tile]
                else:
                    pass
            print("You are now on tile {0}.".format(list_of_players[player_id].position))
            player_id = ((player_id + 1) % num_of_players)
        elif m == "position":
            print("You are on tile number {0}".format(list_of_players[player_id].position))

    if player0.position > 100:
        print("Congratulations {0}! You are the winner!".format(player0.name))
    elif player1.position > 100:
        print("Congratulations {0}! You are the winner!".format(player1.name))
    elif player2.position > 100:
        print("Congratulations {0}! You are the winner!".format(player2.name))
    elif player3.position > 100:
        print("Congratulations {0}! You are the winner!".format(player3.name))
#this is where the main game acutally beings

while True:
    k = input('Welcome To Snakes and Ladders \nHow would you like to begin?\n- Instructions\n- Start\n- Exit\n')
    if k == "Instructions":
        instructions()
    elif k == "Start":
        n = input("Please Select The Number of Players you would like to play with:\n- Two Player\n- Three Players\n- Four Players\n")
        if n == "Two Player":
            player_naming(2)
        elif n == "Three Players":
            player_naming(3)
        elif n == "Four Players":
            player_naming(4)
    elif k == "Exit":
        exit()
