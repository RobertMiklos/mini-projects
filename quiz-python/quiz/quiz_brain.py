class QuizBrain():
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Otázka č. {self.question_number}: {current_question.text} (True/False): ")
        self.checkAnswer(user_answer, current_question.answer)
    
    def hasQuestion(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            self.scoreReveal()
            return False
        
    def checkAnswer(self, user_answer, right_current_answer):
        if user_answer == right_current_answer:
            print("Uhádli jste")
            self.score += 1
        else:
            print("Špatná odpověď")
            print(f"Správná odpověď je {right_current_answer}")

    def scoreReveal(self):
        print(f"Výborně uhádli jste {self.score}/{len(self.question_list)}")