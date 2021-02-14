class Question:
    score = 0
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
    
    def show_question(self):
        return self.question
    
    def check_answer(self,answer):
        is_right =  True if self.answer == answer else False
        if is_right:
            Question.score = Question.score + 1
        return is_right