import random
import time
import os
from termcolor import colored

game_log = []

class Player(object):
    def __init__(self,initial,position):
        self.initial = initial.upper()
        self.position = position
        self.last_number = 0
    
    def play(self):
        print "Player",self.initial.upper(), 'press enter to roll the dice'
        raw_input()
        number = dice_roll()
        self.last_number = number
        position_log = self.initial + " Current position: " + str(self.position) + ", Dice roll: " + str(self.last_number)
        game_log.append(position_log)
        if number + self.position > 100:
            print 'Invalid Dice roll!'
        else:
            self.position = number + self.position
        self.follow_snake_and_ladder()
        moved = self.initial + " Moved to "+ str(self.position)+ " position"
        game_log.append(moved)
        
        
    def is_winner(self):
        if self.position == 100:
            return True
        else:
            return False

    def follow_snake_and_ladder(self):
        while self.position in snake or self.position in ladder:
            if self.position in snake:
                position_log = 'Oops, snake at '+ str(self.position) +'. ' + self.initial + ' falls down to ' + str(snake[self.position]) + ' position'
                self.position = snake[self.position]
                game_log.append(position_log)
            else:
                position_log = 'Hurrey, ladder at '+ str(self.position) +'. ' + self.initial +' climbs up to ' + str(ladder[self.position])+' position'
                self.position = ladder[self.position]
                game_log.append(position_log)

            


matrix = range(1,101) # Defining list of 100 elements starting from 1-100
snake = {
    98: 80,
    91: 71,
    95: 75,
    64: 42,
    62:19,
    56:53,
    44:26,
    31:9,
    14:4

}
ladder = {
    1:38,
    6:16,
    11:49,
    21:60,
    24:87,
    26:47,
    51:67,
    73:93,
    78:100
}

while True:
    p1 = raw_input('Player 1: Please enter your name(less than 10 characters): ')
    if len(p1) <= 10: break
    else:
        print 'Name must be less than 10 characters'
        continue
# Assigning Intial to player2
while True:
    p2 = raw_input('Player 2: Please enter your name(less than 10 characters): ')
    if len(p2) <= 10: 
        if p2 != p1: 
            break
        else:
            print 'Name already chosen by Player1. Please enter adifferent name: '
            continue
    else:
        print 'Name must be less than 10 characters: '
        continue


player1 = Player(p1,0)
player2 = Player(p2,0)
current_player = [player1]

def print_board_row(row):
    print '|', #prints first vertical bar and stays on same line because of ','
    # if row  number is odd, j takes values 9 to 0
    if row%2==1:
        for col in range(9,-1,-1):
            colored_number = colored(str(matrix[10*row+col]),'white')
            colored_number = ' '* (12 - len(str(matrix[10*row+col]))) + colored_number
            print colored_number,'|', #
    # if row number is even then j takes values from 0 to 9
    else:
        for col in range(10):
            colored_number = colored(str(matrix[10*row+col]),'white')
            colored_number = ' '* (12 - len(str(matrix[10*row+col]))) + colored_number
            print colored_number,'|',
    print ''

def get_player_cell(row, col):
    index = matrix[10*row+col]
    a = '|'
    spaces = 14
    player_cell_output = ''
    if player1.position == index:
        player_cell_output = player_cell_output + colored(player1.initial,'yellow',attrs=['bold','underline','blink'])
        spaces = spaces - len(player1.initial)
    if player2.position == index:
        player_cell_output = player_cell_output + colored(player2.initial,'cyan',attrs=['bold','underline','blink'])
        spaces = spaces - len(player2.initial)
    #spaces to fill
    left_spaces = spaces/2
    right_spaces = spaces - left_spaces
    return a + ' '*left_spaces + player_cell_output + ' '*right_spaces

def print_player_row(row):
    output =''
    if row%2==1:
        for col in range(9,-1,-1):
           output = output + get_player_cell(row,col)
    else:
        for col in range(10):
            output = output + get_player_cell(row,col)
    print output + '|'

def get_snake_ladder_cell(row, col):
    index = matrix[10*row+col]
    a = '|'
    cell_output = ''
    if index in snake:
        cell_output = cell_output + colored('Sn'+ str(snake[index]), 'red') + ' '*(14 -len('Sn'+ str(snake[index])))
    elif index in ladder:
        cell_output = cell_output + colored('Ld' + str(ladder[index]),'blue')  + ' '*(14 -len('Ld'+ str(ladder[index])))
    return a + cell_output.ljust(14, ' ')


def print_snake_ladder_row(row):
    output =''
    if row%2==1:
        for col in range(9,-1,-1):
           output = output + get_snake_ladder_cell(row,col)
    else:
        for col in range(10):
            output = output + get_snake_ladder_cell(row,col)
    print output + '|'

def print_bottom_line():
    a = '|'
    b = '______________|'*10
    #this prints border line |,______________| * 10
    print '{0}{1}'.format(a, b)
    
def log_last_5_moves():
    print 'Last 5 moves'
    for move in game_log[-5:]:
        print move


#Printing snake & Ladder Board
def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print '_'*150 # To print first horizontal line of the code
    # Grid Position
    # i represents row number
    for row in range(9,-1,-1): # i takes the value 9 to 0
        print_board_row(row)
        print_player_row(row)
        print_snake_ladder_row(row)
        print_bottom_line()
    
def dice_roll():
    dice = random.randint(1,6)
    return dice

def flip():
    global current_player
    if current_player[0].initial == player1.initial:
        current_player[0] = player2
    else:
        current_player[0] = player1

def game():
    print_board()
    while True:
        current_player[0].play()
        print_board()
        #log_last_5_moves()

        if current_player[0].is_winner():
            print 'Player',current_player[0].initial,'has won the game'
            break
        if current_player[0].last_number != 6:
            game_log.append('-------------------------------------------------------')
            flip()
        else:
            game_log.append('Player ' + current_player[0].initial+ ', since you got 6, it is your turn again')
        log_last_5_moves()

       


game()

        
        
        

