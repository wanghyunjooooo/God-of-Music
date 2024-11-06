from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 퀴즈 데이터 (이미지와 정답을 추가하여 확장 가능)
quiz_data = [
    {"image": "static/images/scene1.png", "answer": "song1"},
    {"image": "static/images/scene2.png", "answer": "song2"},
    # 여기에 추가적인 이미지와 정답을 넣을 수 있습니다.
]

@app.route('/')
def quiz():
    scene = random.choice(quiz_data)  # 랜덤으로 퀴즈 장면 선택
    return render_template('quiz.html', scene=scene)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('answer').strip().lower()
    correct_answer = request.form.get('correct_answer').strip().lower()
    
    if user_answer == correct_answer:
        return redirect(url_for('correct'))
    else:
        return redirect(url_for('wrong'))

@app.route('/correct')
def correct():
    return render_template('correct.html')  # 정답 페이지

@app.route('/wrong')
def wrong():
    return render_template('wrong.html')  # 오답 페이지

if __name__ == '__main__':
    app.run(debug=True)
