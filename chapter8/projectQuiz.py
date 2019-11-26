#! python3
# projectQuiz.py - create quizzes with questions and answers in random order

import random


# the quiz data. keys are states and values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files:
for quizNum in range(35):
    # create quiz and answer file
    quizFile = open('capitalsquiz%s.text' % (quizNum + 1), 'w')
    answerFile = open('capitalquiz_answer%s.txt' % (quizNum + 1), 'w')
    # create quiz header
    quizFile.write('Name:\n\nDate:\n\nperiod:\n\n')
    quizFile.write((' ' * 20) + 'state capitals quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # shuffle the order of the states
    states = list(capitals.keys())
    # shuffle() 方法将序列的所有元素随机排序。
    random.shuffle(states)

    # Loop through all 50 states ,making a question for each
    for questionNum in range(50):

        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        # del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswers.remove(correctAnswer)
        # 从列表中随机选3个
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write the question and answer options to the quiz file
        quizFile.write('%s. what is the capital of %s?\n' % (questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s \n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answer key to a file
        answerFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerFile.close()