
import random
from turtle import Turtle, Screen
from tkinter import messagebox
# creating a window
screen=Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Colors available: red,"
                                                          " orange, yellow, green, blue, violet, pink.").lower()
colors=["red", "orange", "yellow", "green", "blue", "violet", "pink"]
y=90

all_turtles=[] # turtles are gonna be in the list
# creating turtles
for i in range(0, 7):
    a_turtle=Turtle("turtle")
    a_turtle.color(colors[i])
    a_turtle.penup()
    # placing turtles
    a_turtle.goto(x=-230, y=y)
    all_turtles.append(a_turtle)
    y-=30

is_race_on=False
if user_bet:
    is_race_on = True

while is_race_on:
    for a_turtle in all_turtles:
        # if tutrle crosses x=230, race is off
        if a_turtle.xcor() > 230:
            is_race_on=False
            winner_color = a_turtle.pencolor()
            if winner_color == user_bet:
                messagebox.showinfo(title="Congratulations!", message=f"You won! The winner is the {a_turtle.pencolor()} turtle!")
            else:
                messagebox.showinfo(title="Ooops :(", message=f"You lost. The winner is the {a_turtle.pencolor()} turtle")
        # if line x=230 isn't crossed, race continues
        rand_distance = random.randint(0, 10)
        a_turtle.forward(rand_distance)

screen.exitonclick()