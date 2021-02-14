from question_model import Question
from data import question_data


question_bank = []
for ques in question_data:
    question_bank.append(Question(ques['text'],ques['answer']))


for ques in question_bank:
    ans = input(ques.show_question())
    if(ques.check_answer(ans.title())):
        print('You got it right!')
    else:
        print("Wrong!")
        print('The correct answer is : ',ques.answer)
    print('Your current score is : ', Question.score," / ",len(question_bank))