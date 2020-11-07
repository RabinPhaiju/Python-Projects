import re, json, pyperclip
listABCDE = ['question','a', 'b', 'c', 'd', 'answer']

# with open('question.txt','w') as ques:
    # ques.write(pyperclip.paste())

with open('question.txt','r') as ques:
    name = ques.read()


A = re.compile(r'A\.\s(.*)')
Alist = A.findall(name)
B = re.compile(r'B\.\s(.*)')
Blist = B.findall(name)
C = re.compile(r'C\.\s(.*)')
Clist = C.findall(name)
D = re.compile(r'D\.\s(.*)')
Dlist = D.findall(name)
Answer = re.compile(r'Answer:\sOption\s(.*)')
Answerlist = Answer.findall(name)

new_list = []
for i in range(1, 6):
    Q = re.compile(fr'{i}\.\s\s\n\n(.*)')
    new_list.append(Q.findall(name)[0])

    

for Question, A, B, C, D, Answer in zip(new_list, Alist, Blist, Clist, Dlist, Answerlist):
    new_dict = dict()
    new_dict[listABCDE[0]] = Question
    new_dict[listABCDE[1]] = A
    new_dict[listABCDE[2]] = B
    new_dict[listABCDE[3]] = C
    new_dict[listABCDE[4]] = D
    if Answer == 'A':
        new_dict[listABCDE[5]] = A
    elif Answer == 'B':
        new_dict[listABCDE[5]] = B
    elif Answer == 'C':
        new_dict[listABCDE[5]] = C
    elif Answer == 'D':
        new_dict[listABCDE[5]] = D   
    with open('answer.json','r+') as file:
        data = json.load(file)
        data.append(new_dict)
        file.seek(0)
        json.dump(data, file, indent=2)

print('done')



