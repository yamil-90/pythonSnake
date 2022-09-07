from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self, color = "white") -> None:
        self.segments = []
        self.color = color
        self.create_snake()
        self.head = self.segments[0]
        
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)   
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.detect_borders()
        
    def detect_borders(self):
        if self.segments[0].xcor() > 280:
            self.segments[0].goto(-280, self.segments[0].ycor())
        elif self.segments[0].xcor() < -280:
            self.segments[0].goto( 280, self.segments[0].ycor())
        elif self.segments[0].ycor() > 280:
            self.segments[0].goto(self.segments[0].xcor(), -280)
        elif self.segments[0].ycor() < -280:
            self.segments[0].goto(self.segments[0].xcor(), 280)


    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def center(self):
            self.head.goto(0, 0)