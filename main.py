import turtle as t
import random

is_race = False
screen = t.Screen()
screen.title("Welcome to the Races!")
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race: ")
all_turtles = []
colors = ["red", "blue", "yellow", "purple", "green", "brown"]
for i in range(6):
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    j = i*40
    new_turtle.goto(-230, -100 + j)
    all_turtles.append(new_turtle)

winner = t.Turtle()
winner.hideturtle()
winner.penup()
winner.goto(-50,0)

if user_bet:
    is_race = True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            winner.write(f"The Winner is {winning_color}!", align="center", font=("Helvetica Neue", 30, "normal"))
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost... The {winning_color} turtle is the winner!.")
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()