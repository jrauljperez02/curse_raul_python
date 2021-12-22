from turtle import Turtle, goto
ALIGMENT = 'center'
FONT = ('Courier',24,'normal')



class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,265)
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGMENT,font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGMENT,font=FONT)

    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        