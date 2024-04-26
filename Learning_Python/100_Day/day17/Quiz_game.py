from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

Quiz = QuizBrain(question_bank)
Quiz.next_question()
