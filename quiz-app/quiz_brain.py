from question import Question
from data import question_data
import html


class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.no_of_questions = 10
        self.score = 0
        self.current_question = None

    def is_question_available(self):
        return self.question_number < self.no_of_questions

    def next_question(self):
        self.current_question = question_data[self.question_number]
        question_text = html.unescape(self.current_question['question'])
        self.question_number += 1
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer):
        question_answer = self.current_question['correct_answer']
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            return True
        else:
            return False
