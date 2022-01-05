class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        if len(self.question_list) < self.question_number:
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number}, {current_question.text} (True or False)\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You had it correct")
            self.score += 1
        else:
            print(f"Wrong,{current_answer} is the correct answer.")

        print(f"Your current score is: {self.score}/{self.question_number}")
