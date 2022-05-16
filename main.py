import csv
import random

import os

print("\n" * os.get_terminal_size().lines) # tem função de limpar tela do console


class Usuario: # classe usuário do jogo
    def __init__(self, name): # função inicial
        self.name = name
     
    def criacaoConta(self): # criação da conta do jogador: faz id
        self.username = self.name[:40] # grava até 40 caracteres no arquivo: nome completa do jogador
        #print("Nome de usuário:", self.username)
            
    def savarInformacao(self):
        #abre o arquivo para leitura txt
        with open("jogadores.txt", "r") as file:
            fileReader = csv.reader(file)
            #file = random.choice(list(file.fileInfo())) # randomizando perguntas
            fileInfo = [info for info in fileReader if info != []]
            fileInfo.append([self.username,  self.name])
            #print(fileInfo)
    


    def iniciarjogo(self):
        
        
        userDifficulty = int(input("Escolha dificuldade:\n1.Fácil\n2.Médio\n3.Difícil\nResponda: "))
                
        userDifficulty = 3
            
        userSubject = input("Escolha um assunto:\n1. Conhecimento Gerais \n2. Tecnologia\nResponda: ")
        if userSubject == "1":
            userSubject = "General Knowledge"
            quiz = quizJogo(userDifficulty, userSubject, self.username)
            quiz.start(), quiz.checkAnswers()
            return
         
        elif userSubject == "2":
            userSubject = "Technology"
            quiz = quizJogo(userDifficulty, userSubject, self.username)
            quiz.start(), quiz.checkAnswers()
            return
        else:
            print("Opção invalida")
                        

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
        answers = [] #esse answers
        with open("{}.txt".format(self.fileName), "r", encoding='utf-8') as f: # aqui
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
                        
    def checkAnswers(self): # função verificar as respostas
        score = 0
        answers = []

        with open("{}.txt".format(self.fileName), "r", encoding='utf-8') as f: # abre arquivo para leitura conforme opção selecionada
            quizReader = csv.reader(f)
            for line in quizReader:
                if "{}_respostas".format(self.subject) in line:
                    for line in quizReader:
                        if "fim {}_respostas".format(self.subject) in line:
                            break
                        answers.append(line)
                        
        for index in range(len(answers)):
            try:
                if answers[index] == self[index]:
                    score += 1
            except:
                continue
                
        self.calcGrade(score)

    def calcGrade(self, score): # faz referencia ao scores dos jogadores , nome e percentual de acertos
        self.percentage = score*100/10
        gradeTable = [50, 60, 70, 80, 90,100]
        print("Nome de usuário:", self.username)
        print("Você acertou {}/10".format(score))
        print("Você obteve {}% ".format(self.percentage))
          

        for element in gradeTable: #funcionalidade para calcular quantidade de resposta em relação as prguntas 
            done = False
            if self.percentage < element:
                grade = int(element/10)
                print("Sua nota: {}".format(element/10))
            
        self.submitScore(grade) 
        
    
    def submitScore(self, grade): # função responsavel funcinalidade arquivo scores apenas abre  para leitura e grava na memoria temporária do computado
        with open("scores.txt", "r") as f:
            scoresReader = csv.reader(f)
            scores = [line for line in scoresReader if line != []]

        scores.append([self.username, self.subject, self.difficulty, grade])

        with open("scores.txt", "w") as f: # quando jogado informa nome o mesmo é gravado nessearquivo com seu score
            scoresWriter = csv.writer(f)
            for info in scores:
                scoresWriter.writerow(info)

# def fileClear(file):
#     with open("{}.txt".format(file), "w") as f:
#         clear = csv.writer(f)
#         clear.writerow([])

def main():
    print('       Sejam bem Vindo(a)!')
    print('Jogo Quiz ')
    print('=*' * 15)
    user = Usuario (input("\nDigite seu nome: "))
    print()
    user.criacaoConta(), user.savarInformacao()
    #file = random.choice(list(file.fileInfo())) # randomizando perguntas
    user.iniciarjogo()
  
    while True: user.iniciarjogo()# loop infinito


main() 