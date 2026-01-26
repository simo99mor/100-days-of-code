from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_bank = []  # initialize an empty list, it will be a list of objects (Question)
for i in range(len(question_data)):
    current_text = question_data[i]["question"]
    current_answer = question_data[i]["correct_answer"]
    current_q = Question(current_text,current_answer)
    q_bank.append(current_q)

quiz = QuizBrain(q_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You completed the quiz!")
print(f"Your final score was {quiz.score}/{len(q_bank)}")
