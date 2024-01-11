# This file was created by: Shaunik Musukula

# all imported libraries/modules
import random as rand
import turtle as t
from math import floor
import os

# globalizing scope of vars so they can be accessed everywhere
global player_image, cpu_image, paper_choice, scissors_choice, rock_choice
global text
global scissors_image, rock_image, paper_image
global window
global rock_h, rock_w
global scissors_h, scissors_w
global paper_h, paper_w


# child class that inherits properties of t.Turtle obj
class text_and_image(t.Turtle):

    # move object without drawing a random line
    def teleport(self, x: int, y: int) -> None:
        self.penup()
        self.goto(x, y)
        self.pendown()
    
    # write to window with custom font
    def text(self, text: str) -> None:
        self.write(text, font=("Verdana", 15, "normal"))
    
    # select correct image based on choice
    def image_select(self, choice: str) -> None:
        # dictionary with keys corresponding to choice
        image_dict = {
        "rock" : rock_image,
        "paper" : paper_image,
        "scissors" : scissors_image
        }

        # set image shape to value corresponding with key
        self.shape(image_dict[choice])

    # check whether player clicks the instance
    def check_click(self, x: int, y: int, length: int, height: int) -> bool:
        # first element is the left side of the instance
        # second element is the right side of the instance
        innerbound = (self.pos()[0] + height/2, self.pos()[0] - height/2)

        # first element is the top of the instance
        # second element is the bottom of the instance
        outerbound = (self.pos()[1] + length/2, self.pos()[1] - length/2)

        return x >= innerbound[1] and x <= innerbound[0] and y >= outerbound[1] and y <= outerbound[0]

# take random CPU input
def CPU() -> str:
    choices = ["rock", "paper", "scissors"]
    return rand.choice(choices)

# eval round
def evaluate(player1: str, player2: str) -> int:
    win_dict = {
        "paper" : "rock",
        "scissors" : "paper",
        "rock" : "scissors"
    }

    if win_dict[player1] == player2:
        return 1
    elif win_dict[player2] == player1:
        return 2
    else:
        return 0
    
# calculate win rate and return a visual
def win_loss_stats(win: int, round: int) -> str:
    """
    The win rate bar is made of 10 "blocks." Each block is either
    a "-" or a " ". The "-" represents win rate to the nearest
    10th percentile. The " " represents loss rate to the nearest
    10th percentile. The accurate percentage is displayed next to
    the bar.

    When ran it could return this:
    [----      ] 43%
    """

    if round != 0:
        # calculate the win rate to the nearest 10
        percentage_to_ten = 10*(floor(10*(win/round)))
    
    # avoids ZeroDivision Error
    else:
        percentage_to_ten = 0

    # calculates loss rate to the nearest 10
    space = 10 - percentage_to_ten//10

    if round != 0:
        return ("[" + "-"*(10-space) + " "*space + "] " + str(floor((win/round) * 100)) + "%")
    
    # avoids Zero Division Error
    else:
        return ("[          ] 0%")

# clear the screen after round is over
def reset_screen() -> None:
    player_image.hideturtle()
    cpu_image.hideturtle()
    text.hideturtle()
    text.clear()
    paper_choice.hideturtle()
    rock_choice.hideturtle()
    scissors_choice.hideturtle()

# set base values for the analytics
win_count, round_count, analytic_round = 0, 1, 0

# set window & image dimensions
width, height = 1000, 800
rock_w, rock_h = 256, 280
paper_w, paper_h = 256, 208
scissors_w, scissors_h = 260, 173


# initialize directory for images
games_dir = os.path.dirname(__file__)
images_dir = os.path.join(games_dir, "images")

# set up window
window = t.Screen()
window.setup(width+10, height+8)
window.setworldcoordinates(0, 0, width, height)
window.screensize(canvwidth=width, canvheight=height, bg="lightblue")

# set up different images for rock, paper, and scissors
rock_image = os.path.join(images_dir, 'rock.gif')
paper_image = os.path.join(images_dir, 'paper.gif')
scissors_image = os.path.join(images_dir, 'scissors.gif')

# add the images as a shape
window.addshape(rock_image)
window.addshape(paper_image)
window.addshape(scissors_image)

# create instances to display actions
player_image = text_and_image()
cpu_image = text_and_image()
text = text_and_image()

# set up images for possible choices
paper_choice = text_and_image()
rock_choice = text_and_image()
scissors_choice = text_and_image()

def show_choice() -> None:
    # show paper choice
    paper_choice.teleport(0, 0)
    paper_choice.image_select("paper")
    paper_choice.showturtle()

    # show scissors choice
    scissors_choice.teleport(350, 0)
    scissors_choice.image_select("scissors")
    scissors_choice.showturtle()

    # show rock choice
    rock_choice.teleport(-350, 0)
    rock_choice.image_select("rock")
    rock_choice.showturtle()

    # tell player to choose
    text.teleport(-100, 200)
    text.text("Click your choice")

def main(player_choice: str) -> None:
    # globalize scope of certain vars that are needed
    global cont
    global win_count
    global round_count
    global analytic_round
    global in_game

    in_game = True

    # hide previous objects
    reset_screen()

    # display round count
    text.teleport(-300, 360)
    text.text("Round " + str(round_count))
    """
    # take player choice
    player_choice = player_in()

    # accounts for different input possibilities
    if player_choice == "exit":
        quit()
    elif player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice!")
        quit()
    """
        
    # take random CPU choice
    CPU_choice = CPU()
    result = evaluate(player_choice, CPU_choice) # evaluate result of round
    
    # show player choice textually
    text.teleport(-300, 330)
    text.text("Player Choice: " + player_choice)
        
    # show CPU choice textually
    text.teleport(-300, 300)
    text.text("CPU Choice: " + CPU_choice)
        
    # move player image
    player_image.teleport(-200, 0)
    text.teleport(-220, 200)

    # display player choice visually
    text.text("Player:")
    player_image.image_select(player_choice)

    # show image of player choice
    player_image.showturtle()

    # V.S. sign
    text.teleport(-30, 0)
    text.text("V.S.")

    # move CPU image
    cpu_image.teleport(200, 0)
    text.teleport(200, 200)

    # display CPU choice visually
    text.text("CPU:")
    cpu_image.image_select(CPU_choice)

    # show image of CPU choice
    cpu_image.showturtle()

    # runs if player wins
    if result == 1:
        text.teleport(-300, -190)
        text.text("Player won!")
        win_count += 1 # increment total win count
        round_count += 1 # increment total round count
        analytic_round += 1 # increment effective round count

    # runs if CPU wins
    elif result == 2:
        text.teleport(-300, -190)
        text.text("CPU won!")
        round_count += 1 # increment total round count
        analytic_round += 1 # increment effective round count

        # runs if draw occurs
    else:
        text.teleport(-300, -190)
        text.text("Draw!")
        round_count += 1 # increment total round count

    # display win rate after round
    text.teleport(100, 360)
    text.text("Win rate: " + win_loss_stats(win_count, analytic_round))

    # tell player how to continue
    text.teleport(-300, -210)
    text.text("Click anywhere to continue")

    # toggle whether a click makes game continue or selects a choice
    in_game = False
    cont = True

# check what the player clicks or whether they are continuing
def check(x: int, y: int) -> None:
    global cont
    global in_game

    if not in_game:
        # checks where player clicks
        if not cont:
            if rock_choice.check_click(x, y, rock_w, rock_h):
                main("rock")
            elif scissors_choice.check_click(x, y, scissors_w, scissors_h):
                main("scissors")
            elif paper_choice.check_click(x, y, paper_w, paper_h):
                main("paper")

        # shows choices if game needs to continue
        else:
            reset_screen()
            show_choice()
            cont = False

in_game = False
cont = False

# run first function to show choice
reset_screen()
show_choice()

# run main program
window.onclick(check)

# exit after closing window
t.done()
