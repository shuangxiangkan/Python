import pygame

class my_trivia():

    def __init__(self, filename, screen,colors):
        self.filename = filename
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.colors=colors
        self.anwer_color=[self.colors[0],self.colors[0],self.colors[0],self.colors[0]]
        # store the content of file into data
        self.data = []
        # the current problem number
        self.current = 0
        self.right_answer=False
        self.wrong_answer=False
        self.questions_number=0
        self.score=0
        # two size of font
        self.fontSize1 = pygame.font.Font(None, 40)
        self.fontSize2 = pygame.font.Font(None, 30)

    def read_file_content(self):
        f = open(self.filename, "r")
        lines = f.readlines()
        for line in lines:
            self.data.append(line.strip())
        self.questions_number=len(self.data)/6

    # show the name of game,score,the name of question, the name of answer
    def context(self):


        # show "TRIVIA GAME"
        game_name = self.fontSize1.render("TRIVIA GAME", True, self.colors[0])
        self.screen.blit(game_name, (self.screen_rect.width / 2 - 100, 5))

        # show "QUESTION"
        game_question_title = self.fontSize1.render("QUESTION" + " " + str(int(self.current/6) + 1), True, self.colors[0])
        self.screen.blit(game_question_title,(5,80))

        # show "ANSWERS"
        game_question_title = self.fontSize1.render("ANSWERS", True, self.colors[0])
        self.screen.blit(game_question_title, (5, 175))

        # show the content of question
        question = self.fontSize2.render(self.data[self.current], True, self.colors[1])
        self.screen.blit(question, (5, 120))

        # show the "SCORE"
        score_mark=self.fontSize2.render("SCORE",True,self.colors[3])
        self.screen.blit(score_mark,(self.screen_rect.width-80,5))

        # show the score
        score=self.fontSize2.render(str(self.score),True,self.colors[3])
        self.screen.blit(score,(self.screen_rect.width-50,40))

        # show answers of question
        answer1 = self.fontSize2.render("1-"+self.data[self.current+1], True, self.anwer_color[0])
        self.screen.blit(answer1, (15, 210))
        answer2 = self.fontSize2.render("2-" + self.data[self.current + 2], True, self.anwer_color[1])
        self.screen.blit(answer2, (15, 250))
        answer3 = self.fontSize2.render("3-" + self.data[self.current + 3], True, self.anwer_color[2])
        self.screen.blit(answer3, (15, 290))
        answer4 = self.fontSize2.render("4-" + self.data[self.current + 4], True, self.anwer_color[3])
        self.screen.blit(answer4, (15, 330))


        if self.right_answer:
            correct=self.fontSize1.render("CORRECT!",True,self.colors[2])
            self.screen.blit(correct,(self.screen_rect.width/2-75,370))
            press_enter=self.fontSize2.render("Press Enter For Next Question",True,self.colors[2])
            self.screen.blit(press_enter,(self.screen_rect.width / 2 - 150, self.screen_rect.height - 85))
        # show "Press Key(1-4) To Answer" at the bottom of the screen
            press_answer = self.fontSize2.render("Press Key(1-4) To Answer", True, self.colors[3])
            self.screen.blit(press_answer, (self.screen_rect.width / 2 - 110, self.screen_rect.height - 40))

        elif self.wrong_answer:
            correct=self.fontSize1.render("INCORRECT!",True,self.colors[3])
            self.screen.blit(correct,(self.screen_rect.width/2-75,370))
            press_enter=self.fontSize2.render("Press Enter For Next Question",True,self.colors[3])
            self.screen.blit(press_enter,(self.screen_rect.width / 2 - 150, self.screen_rect.height - 85))
        # show "Press Key(1-4) To Answer" at the bottom of the screen
            press_answer = self.fontSize2.render("Press Key(1-4) To Answer", True, self.colors[3])
            self.screen.blit(press_answer, (self.screen_rect.width / 2 - 110, self.screen_rect.height - 40))



    def hand_input(self,key):
        correct_answer=int(self.data[self.current+5])
        if key==-1:
            self.right_answer=False
            self.wrong_answer=False
            self.current=int((self.current+6)%(self.questions_number*6))
            self.anwer_color[0] = self.colors[0]
            self.anwer_color[1] = self.colors[0]
            self.anwer_color[2] = self.colors[0]
            self.anwer_color[3] = self.colors[0]
            # self.score=0

        elif key==correct_answer and not self.right_answer and not self.wrong_answer:
            # change the color of right answer to green
            self.right_answer=True
            self.anwer_color[correct_answer-1]=self.colors[2]
            self.score+=1
            print(self.score)


        elif not self.wrong_answer:
            self.wrong_answer=True
            self.anwer_color[key - 1] = self.colors[3]
            self.anwer_color[correct_answer - 1] = self.colors[2]


