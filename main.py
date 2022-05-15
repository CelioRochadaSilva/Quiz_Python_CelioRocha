# inicio codificação
import csv

class Usuario:
    def __init__(self, name):

    def criacaoConta(self):

    def savarInformacao(self):
    
    def iniciarjogo(self):



class quizJogo:
    userRespostas = []

    def __init__(self, difficulty, subject, username):
        self.difficulty = difficulty
        self.subject = subject
        self.fileName = "quiz{}".format(self.difficulty)
        self.username = username

    def start(self):
        respostas = []

    def checkAnswers(self):
        score = 0

    def checkAnswers(self):
        score = 0
        respostas = []

    def calcGrade(self, score):
        self.percentage = score*100/5
        gradeTable = [50, 60, 70, 80, 90,100]
        print("Nome de usuário:", self.username)
        print("Você acertou {}/5".format(score))
        print("Você obteve {}% ".format(self.percentage))

    def submitScore(self, grade):
        with open("scores.txt", "r") as f:
            scoresReader = csv.reader(f)
            scores = [line for line in scoresReader if line != []]

def fileClear(file):
    with open("{}.txt".format(file), "w") as f:
        clear = csv.writer(f)
        clear.writerow([])

def main():
    print('       Sejam bem Vindo(a)!')
    print('Jogo Quiz ')
    print('=*' * 15)
    user = Usuario (input("\nDigite seu nome: "))
    print()
    user.criacaoConta(), user.savarInformacao()
    #file = random.choice(list(file.fileInfo())) # randomizando perguntas
    user.iniciarjogo()