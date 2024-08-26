# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie La Joie
#               Shweta Kumaran
#               Eugenio Casaubon
# Section:      521
# Assignment:   Team Lab: Topic 13
# Date:         7 December 2022

from random import randint
import turtle
turt = turtle.Turtle()



def randBoard():
  ''' This function creates a random bingo board and writes to a file.
        There are no parameters taken in but returns the bingo board. '''
  # set the 5 x 5 board by putting in random numbers
  # if in the 3x3 location, it is a free space, so the number will be zero
  board = [[
    randint(1, 99),
    randint(1, 99),
    randint(1, 99),
    randint(1, 99),
    randint(1, 99)
  ],
           [
             randint(1, 99),
             randint(1, 99),
             randint(1, 99),
             randint(1, 99),
             randint(1, 99)
           ],
           [randint(1, 99),
            randint(1, 99), 0,
            randint(1, 99),
            randint(1, 99)],
           [
             randint(1, 99),
             randint(1, 99),
             randint(1, 99),
             randint(1, 99),
             randint(1, 99)
           ],
           [
             randint(1, 99),
             randint(1, 99),
             randint(1, 99),
             randint(1, 99),
             randint(1, 99)
           ]]

  # output board by writing it into a file
  # open file
  file = open('hiddenBingoBoard.txt', 'w')
  # write header
  file.write('B I N G O\n')
  # loop through board and output each row followed by a newline
  for j in range(5):
    for i in range(5):
      file.write(str(board[j][i]) + ' ')
    file.write('\n')
  # close file
  file.close()
  return board


def printBoard(board):
  ''' This function prints out the bingo board spaced out and nicely. It takes
      in the board that wants to be printed as a parameter'''
  print('B   I   N   G   O ')
  # goes thru board and prints each element spaced out
  for i in range(5):
    for j in range(5):
      if (j == 4):
        print(f'{board[i][j]:<3}')
      else:
        print(f'{board[i][j]:<3}', end=" ")

def left():
    turt.left(90)
    turt.fd(5)
    turt.left(90)

def right():
    turt.right(90)
    turt.fd(5)
    turt.right(90)

def display_pic():
    '''This function utilizes turtle and creates a graphic for bingo as the intro
         to the game. No parameters and no returns. '''
    turt.color("black")
    turt.penup()
    turt.setx(-250)
    turt.right(90)
    turt.pendown()
    turt.pensize(5)
    turt.left(90)
    turt.fd(100)
    turt.left(90)
    turt.fd(5)
    turt.left(90)
    turt.fd(100)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    left()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    left()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    left()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(100)
    turt.left(90)
    turt.fd(5)
    turt.left(90)
    turt.fd(100)
    turt.penup()
    turt.left(90)
    turt.fd(10)
    turt.left(90)
    turt.fd(120)
    turt.pendown()
    turt.fd(60)
    right()
    turt.fd(60)
    turt.bk(20)
    left()
    turt.fd(20)
    right()
    turt.fd(20)
    left()
    turt.fd(20)
    right()
    turt.fd(20)
    left()
    turt.fd(20)
    right()
    turt.fd(20)
    left()
    turt.fd(20)
    right()
    turt.fd(20)
    left()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(20)
    left()
    turt.pendown()
    turt.fd(60)
    right()
    turt.fd(60)
    turt.penup()
    turt.left(90)
    turt.fd(10)
    turt.left(90)
    turt.fd(80)
    turt.pendown()
    turt.fd(100)
    left()
    turt.fd(100)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(30)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(30)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(20)
    turt.penup()
    turt.fd(40)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(40)
    turt.pendown()
    turt.fd(20)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(40)
    turt.pendown()
    turt.fd(20)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(20)
    turt.penup()
    turt.fd(40)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(30)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.fd(30)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(100)
    left()
    turt.fd(100)
    turt.penup()
    turt.left(90)
    turt.fd(10)
    turt.left(90)
    turt.fd(130)
    turt.pendown()
    turt.fd(60)
    right()
    turt.fd(60)
    turt.penup()
    turt.fd(10)
    left()
    turt.pendown()
    turt.fd(10)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(10)
    left()
    turt.pendown()
    turt.fd(10)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(10)
    turt.penup()
    right()
    turt.fd(70)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    right()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(50)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(50)
    turt.pendown()
    turt.fd(10)
    left()
    turt.pendown()
    turt.fd(10)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(10)
    turt.penup()
    left()
    turt.fd(10)
    turt.pendown()
    turt.fd(60)
    right()
    turt.fd(60)
    turt.penup()
    turt.left(90)
    turt.fd(10)
    turt.left(90)
    turt.fd(100)
    turt.pendown()
    turt.fd(100)
    left()
    turt.fd(100)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    left()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    left()
    turt.fd(10)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(40)
    turt.penup()
    turt.fd(20)
    turt.pendown()
    turt.fd(10)
    right()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    left()
    turt.fd(20)
    turt.penup()
    turt.fd(60)
    turt.pendown()
    turt.fd(20)
    right()
    turt.fd(100)
    left()
    turt.fd(100)
    turtle.done()


def display_inst():
  ''' This function displays the rules of bingo andf calls the graphic function as well.
  There are no inputs and returns.'''
  # visual intro to the game
  display_pic()  # I am working on the turtle graphics for the picture :)
  # print out the instructions
  print("Howdy! Welcome to Bingo!")
  print("There aren't too many rules or instructions to play our game :)")
  print(
    "All you have to do is input a two digit number when instructed and you are all good!"
  )
  print(
    "The game will tell you if your number is on the randomly generated board :) "
  )
  print(
    "Almost like you're the game master! The program will let you know if you get a Bingo!"
  )
  print("We hope you enjoy!")


def user_input(trials):
  ''' This function gets the user input and does error checking if an invalid entry.
    The parameters is the list of entries people have already tried and returns the usernum'''
  try:
    # get number from user
    user_num = int(input('Please enter a number between 1-99: '))
  except:
    # say invalid and ask to retry
    print()
    print('The number you entered is invalid')
    user_input(trials)
  if user_num < 1 or user_num > 99:
    # if number is out of range, say invalid and try again
    print()
    print('The number you entered is invalid')
    user_input(trials)
  # check if number has already been tried
  find = False
  for i in range(len(trials)):
    if (trials[i] == user_num):
      print('The number you entered is invalid')
      user_input(trials)
  # return user num
  return user_num


def bingo_check(board):
  ''' This function performs a check of the parameter board is a bingo. It does a vertical, horizontal, and diagonal check
    and returns true or false for if a bingo or not.'''
  # var returning at the end
  val = False
  # checks if there is a bingo horizontally
  for i in range(5):
    if board[i][0] == "o" and board[i][1] == "o" and board[i][
        2] == "o" and board[i][3] == "o" and board[i][4] == "o":
      val = True
  # checks if there is a bingo vertically
  for j in range(5):
    if board[0][j] == 'o' and board[1][j] == 'o' and board[2][
        j] == 'o' and board[3][j] == 'o' and board[4][j] == 'o':
      val = True
  # checks for the 2 diagonals
  if board[0][0] == "o" and board[1][1] == "o" and board[2][
      2] == "o" and board[3][3] == "o" and board[4][4] == "o":
    val = True
  elif board[4][0] == "o" and board[3][1] == "o" and board[2][
      2] == "o" and board[1][3] == "o" and board[0][4] == "o":
    val = True
  # return if or not a bingo
  return val


def findNum(answerBoard, hiddenBoard, num):
  ''' This function checks if the user number is in the board. If so, it will adjust hidden with a different
    character. This function taken in the answer board being compared to, the hidden board being changed, and the number
    being found. No returns.'''
  # loop through the list of lists
  for i in range(5):
    for j in range(5):
      # check if the number exists
      if answerBoard[i][j] == num:
        # change the hidden board
        hiddenBoard[i][j] = 'o'


########### PROGRAM MAIN #############
# display instructions
display_inst()
# create a random board and save it as answers
answers = randBoard()
# create the hidden board which is what the user can see
hidden = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'o', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X']]
#print out the answer board: used for testing
#printBoard(answers)
# a list used to keep track of numbers that have already been tried
trials = []
# variable to condition loop to see if bingo has been achieved
bingo = False
# a count variable to see how many tries it takes
count = 0
# loops until bingo found
while bingo == False:
  # update count var
  count += 1
  # get the user input by calling function
  num = user_input(trials)
  # add the number tried to list
  trials.append(num)
  # check for the number in the board
  findNum(answers, hidden, num)
  # print the hidden board to the user
  printBoard(hidden)
  # check if the board has achieved a bingo
  if bingo_check(hidden) == True:
    bingo = True

# closing statement for the game
print(
  f'Game Over! Congratulations you completed the game in {count} number of tries'
)
