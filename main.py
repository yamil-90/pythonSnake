from time import sleep
from turtle import Screen
from Scoreboard import Scoreboard
from Snake import Snake
from Food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)

game_continues = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.center, 'c')
screen.onkey(scoreboard.game_over, 'l')
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_continues:
    sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 20:
        food.spawn()
        scoreboard.increase_score()
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_continues = False
            scoreboard.game_over()

screen.exitonclick()

