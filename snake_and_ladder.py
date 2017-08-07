import random
import time
import os
from termcolor import colored

game_log = []

class Player(object):
    def __init__(self,initial,position):
        self.initial = initial
        self.position = position
    
    def play(self):
        print "Player",self.initial, 'press enter to roll the dice'
        raw_input()
        number = dice_roll()
        if number + self.position > 100:
            print 'Invalid Dice roll!'
        else:
            self.position = number + self.position
        self.follow_snake_and_ladder()
        position_log = self.initial + " position " + str(self.position)
        game_log.append(position_log)
        
    def is_winner(self):
        if self.position == 100:
            return True
        else:
            return False

    def follow_snake_and_ladder(self):
        while self.position in snake or self.position in ladder:
            if self.position in snake:
                position_log = 'Snake at '+ str(self.position) +' snake to ' + str(snake[self.position])
                self.position = snake[self.position]
                game_log.append(position_log)
            else:
                position_log = 'Ladder at '+ str(self.position) +' Ladder to ' + str(ladder[self.position])
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

player1 = Player('A',0)
player2 = Player('B',0)
current_player = [player1]

def print_board_row(row):
    print '|', #prints first vertical bar and stays on same line because of ','
    # if row  number is odd, j takes values 9 to 0
    if row%2==1:
        for col in range(9,-1,-1):
             print '%12s' % matrix[10*row+col],'|', #
    # if row number is even then j takes values from 0 to 9
    else:
        for col in range(10):
                 print '%12s' % matrix[10*row+col],'|',
    print ''

def get_player_cell(row, col):
    index = matrix[10*row+col]
    a = '|'
    player_cell_output = ''
    if player1.position == index:
        player_cell_output = player_cell_output + player1.initial
    if player2.position == index:
        player_cell_output = player_cell_output + player2.initial
    return a + player_cell_output.center(14, ' ')

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
    while True:
        print_board()
        log_last_5_moves()
        current_player[0].play()
        print_board()
        if current_player[0].is_winner():
            print 'Player',current_player[0].initial,'has won the game'
            break
        flip()


game()

        
        
        

