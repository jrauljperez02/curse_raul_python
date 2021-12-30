from turtle import Turtle, goto, mode
ALIGMENT = 'center'
FONT = ('Courier',24,'normal')



class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        #self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Sore {self.high_score}",align=ALIGMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt',mode='w') as data:
                data.write(f"{self.high_score}")
        
        self.score = 0
        self.update_scoreboard()

    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        