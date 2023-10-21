
class Kviz_op:

    def __init__(self, question_list):
        self.question_li = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_li[self.question_number].text
        right_answer = self.question_li[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Otazka c. {self.question_number}: {current_question} (True/False): ")
        self.checker_score(user_answer, right_answer)

    def checker_score(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            self.score += 1
            print("Uhadli jste")
        else:
            print("Neuhadli jste")
        print(f"Vase skore je: {self.score} / {self.question_number}")
        print(f"Spravna odpoved je: {right_answer}")

    def exist_question(self):
        if self.question_number < len(self.question_li):
            return True
        else:
            return False

    
        







    

