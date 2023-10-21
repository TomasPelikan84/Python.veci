from OOP_Data import question_data
from kviz_1 import Question
from kviz_operace import Kviz_op

question_list = []

for one_question in question_data:
    quest_t = one_question['text']
    quest_a = one_question['answer']
    new_question_list = Question(quest_t, quest_a)
    question_list.append(new_question_list)

# print(question_list)

kviz = Kviz_op(question_list)

while kviz.exist_question() == True:
    kviz.next_question()




