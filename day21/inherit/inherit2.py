class Child:
    def __init__(self):
        self.lives_in_house = True
        self.earnMoney = False
    
    def playVideogames(self):
        print('Likes playing videogames')

class Father(Child):

    def __init__(self):
        super().__init__()

    def activites(self):
        print('I have to work')
        super().playVideogames()

    def do_exercise(self):
        print('Make excercise')

dad = Father()
dad.activites()