class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.poin = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? : ")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            print("You got it right")
            self.poin += 1
        else:
            print("Thats wrong")
        
        print(f"The correct asnwer was : {correct}") 
        print(f"Your poin now is : {self.poin}")