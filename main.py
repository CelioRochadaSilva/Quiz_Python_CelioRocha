# inicio codificação
import csv

class Usuario:
    def __init__(self, name):
        self.name = name

    def criacaoConta(self):
        self.username = self.name[:3] 

    def savarInformacao(self):
        with open("jogadores.txt", "r") as file:
            fileReader = csv.reader(file)
            #file = random.choice(list(file.fileInfo())) # randomizando perguntas
            fileInfo = [info for info in fileReader if info != []]
            fileInfo.append([self.username,  self.name])
            #print(fileInfo)
    
    def iniciarjogo(self):
        try:
            userDifficulty = int(input("Escolha dificuldade:\n1.Fácil\n2.Médio\n3.Difícil\nResponda: "))
            print()
        except:
            userDifficulty = 3
            
        userSubject = input("Escolha um assunto:\n1. Conhecimento Gerais \n2. Tecnologia\nResponda: ")
        if userSubject == "1":
            userSubject = "Conhecimento Gerais"
        else:
            userSubject = "Tecnologia"

        quiz = quizJogo(userDifficulty, userSubject, self.username)
        quiz.start(), quiz.checkAnswers()   



class quizJogo:
    userRespostas = []

    def __init__(self, difficulty, subject, username):
        self.difficulty = difficulty
        self.subject = subject
        self.fileName = "quiz{}".format(self.difficulty)
        self.username = username

    def start(self):
        respostas = [] #esse answers
        with open("{}.txt".format(self.fileName), "r") as f:
            quizReader = csv.reader(f)
            for line in quizReader:
                if "{}".format(self.subject) in line:
                    for line in quizReader:
                        
                        if "fim {}_quiz".format(self.subject) in line:
                            break
                        if "[fim perguntas]" in line:
                            userRespostas = input("Digite sua resposta: ")
                            self.userRespostas.append([userRespostas.lower()])
                        
                        print(*line)

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