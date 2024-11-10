from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 퀴즈 데이터 - 각 문제에 대한 오디오 파일 경로와 정답을 설정
quiz_data = [
    {"audio": "/static/audio/Steady.mp3", "answer": "steady"},
    {"audio": "/static/audio/Dunk Shot.mp3", "answer": "dunk shot"},
    # 추가적인 문제를 여기에 추가
]

score = {'correct': 0, 'wrong': 0}  # 점수 초기화

@app.route('/')
def quiz():
    global score
    if score['correct'] + score['wrong'] >= 10:
        return redirect(url_for('results'))
    
    question = random.choice(quiz_data)
    return render_template('songquiz.html', question=question)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('answer').strip().lower()
    correct_answer = request.form.get('correct_answer').strip().lower()

    if user_answer == correct_answer:
        score['correct'] += 1
        return render_template('songquiz-correct.html')
    else:
        score['wrong'] += 1
        return render_template('songquiz-wrong.html')

@app.route('/results')
def results():
    correct_count = score['correct']
    wrong_count = score['wrong']
    score['correct'] = 0  # 초기화
    score['wrong'] = 0
    return render_template('songquiz-results.html', correct=correct_count, wrong=wrong_count)

if __name__ == '__main__':
    app.run(debug=True)
