from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
food = Food()
screen.listen()
score = Scoreboard()
snake = Snake()
snake.start()
food.relocate()
screen.setup(1000, 1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def game():
    game_is_on = True
    while game_is_on:
        score.update_score()
        time.sleep(0.1)
        screen.update()
        snake.move()

        if snake.segment[0].distance(food) < 15:
            print("nom nom nom")
            food.relocate()
            score.increase_score()
            snake.new_segment()

        if snake.segment[0].xcor() > 480 or snake.segment[0].ycor() > 480:
            score.reset_game()
            snake.clear_seg()
        elif snake.segment[0].xcor() < -480 or snake.segment[0].ycor() < -480:
            score.reset_game()
            snake.clear_seg()
        for segment in snake.segment[1:]:
            if snake.segment[0].distance(segment) < 10:
                score.reset_game()
                snake.clear_seg()

        with open("snake_hs.txt") as hs:
            if int(hs.read()) < score.high_score:
                with open("snake_hs.txt", "w") as tracker:
                    tracker.write(str(score.high_score))

        if not score.game_on:
            game_is_on = False

game()




screen.exitonclick()
