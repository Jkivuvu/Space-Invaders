import time
import turtle
import random
from player import Player
from game_area import area

spaces = ['space1.gif', 'space2.gif', 'space3.gif', 'space4.gif']
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(760, 1000)
screen.bgpic(f'images/{random.choice(spaces)}')
screen.listen()
Aliens_list = []
Player_1 = []


area()


def player():
    the_player = Player()
    Player_1.append(the_player)


def alien_army():
    global Aliens_list
    Colors = ['Green', 'Orange', 'Blue', 'Red', 'Yellow', 'Brown', 'Purple', 'Pink']
    x = -270
    y = 430
    Aliens_list = []
    for t in range(5):
        for i in range(7):
            aliens_attack = turtle.Turtle()
            aliens_attack.penup()
            aliens_attack.shape('turtle')
            aliens_attack.shapesize(1, 1)
            aliens_attack.sety(y)
            aliens_attack.setx(x)
            aliens_attack.seth(-90)
            aliens_attack.color(random.choice(Colors))
            x += 90
            Aliens_list.append(aliens_attack)
        x = -270
        y -= 50


alien_army()
player()
screen.tracer(0)
Player_1[0].move_left()
Player_1[0].move_right()
bullets = []
alien_bullets = []


def alien_shots():
    shooter = random.choice(Aliens_list)
    shot = turtle.Turtle()
    shot.penup()
    shot.shape('square')
    shot.shapesize(0.25, 0.75)
    shot.seth(-90)
    shot.setx(shooter.xcor())
    shot.sety(shooter.ycor())
    shot.color('red')
    alien_bullets.append(shot)


def shoot():
    bullet = turtle.Turtle()
    bullet.penup()
    bullet.shape('square')
    bullet.seth(90)
    bullet.shapesize(0.25, 0.75)
    bullet.setx(Player_1[0].xcor())
    bullet.sety(Player_1[0].ycor())
    bullet.color('green')
    bullets.append(bullet)
def play_functions():
    screen.tracer(0)
    Player_1[0].move_left()
    Player_1[0].move_right()
    screen.onkeypress(shoot, 'space')
    screen.onkeypress(Player_1[0].move_left, 'Left')
    screen.onkeypress(Player_1[0].move_right, 'Right')

play_functions()

direction = random.randint(0, 1)
move_y = 0
alien_shoot = 0
lives = 3
life = turtle.Turtle()
life.hideturtle()
game_over = turtle.Turtle()
game_over.hideturtle()
winner = turtle.Turtle()
winner.hideturtle()

play = True

while play:
    winner.clear()
    game_over.clear()
    life.clear()
    life.color('white')
    life.penup()
    life.sety(460)
    life.write(f'Lives: {lives}', move=False, align='center', font=('Arial', 10, 'normal'))
    life.hideturtle()

    time.sleep(0.1)
    move_y += 0.1
    alien_shoot += 1
    screen.update()
    if len(Player_1) < 1:
        if lives != 0:
            time.sleep(3)
            for x in bullets:
                x.hideturtle()
                bullets.remove(x)

            for x in alien_bullets:
                x.hideturtle()
                alien_bullets.remove(x)
            time.sleep(3)

            player()
            play_functions()
        else:
            game_over.clear()
            game_over.color('white')
            game_over.write('Game Over', move=False, align='center', font=('Arial', 20, 'normal'))
            game_over.penup()
            game_over.goto(0, -50)
            game_over.penup()
            game_over.write('Click To Exit Game', move=False, align='center', font=('Arial', 10, 'normal'))
            game_over.hideturtle()
            screen.update()
            time.sleep(1)
            play = False



    for enemie in Aliens_list:
        if enemie.xcor() >= 320:
            direction = 0
        elif enemie.xcor() <= -320:
            direction = 1
        try:
            if enemie.distance(Player_1[0]) < 150:
                lives = 0
        except IndexError:
            pass


    if direction == 1:
        for i in Aliens_list:
            i.setx(i.xcor() + 20)
    elif direction == 0:
        for i in Aliens_list:
            i.setx(i.xcor() - 20)
            # print(i.xcor())
    if move_y >= 10:
        for i in Aliens_list:
            i.sety(i.ycor() - 20)
        move_y = 0
    if alien_shoot >= 3:
        try:
            alien_shots()
        except IndexError:
            winner.color('white')
            winner.write('You are the Winner', move=False, align='center', font=('Arial', 20, 'normal'))
            winner.penup()
            winner.goto(0, -50)
            winner.penup()
            winner.write('Click To Exit Game', move=False, align='center', font=('Arial', 10, 'normal'))
            winner.hideturtle()
            screen.update()
            play = False

        alien_shoot = 0
    for shot in alien_bullets:
        try:
            shot.sety(shot.ycor() - 40)
            if shot.ycor() <= -490:
                shot.hideturtle()
                alien_bullets.remove(shot)
            elif shot.distance(Player_1[0]) < 30:
                shot.hideturtle()
                alien_bullets.remove(shot)
                Player_1[0].hideturtle()
                Player_1.remove(Player_1[0])
                lives -= 1
        except IndexError:
            pass

    try:
        for bullet in bullets:
            bullet.sety(bullet.ycor() + 40)
            if bullet.ycor() >= 490:
                bullet.hideturtle()
                bullets.remove(bullet)
            for alien in Aliens_list:
                if alien.distance(bullet) < 30:
                    bullet.hideturtle()
                    try:
                        bullets.remove(bullet)
                    except ValueError:
                        pass
                    alien.hideturtle()
                    Aliens_list.remove(alien)

    except IndexError:
        pass

screen.exitonclick()
