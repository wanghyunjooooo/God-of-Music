from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 퀴즈 데이터 (이미지와 정답을 추가하여 확장 가능)
quiz_data = [
    {"image": "/static/images/apt.png", "answer": "song1"},
    {"image": "/static/images/별별별.png", "answer": "song2"},
    # 여기에 추가적인 이미지와 정답을 넣을 수 있습니다.
]

@app.route('/')
def quiz():
    scene = random.choice(quiz_data)  # 랜덤으로 퀴즈 장면 선택
    return render_template('mvquiz.html', scene=scene)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('answer').strip().lower()  # 사용자 입력
    correct_answer = request.form.get('correct_answer').strip().lower()  # 정답

    if user_answer == correct_answer:
        return redirect(url_for('correct'))  # 정답일 경우
    else:
        return redirect(url_for('wrong'))  # 오답일 경우

@app.route('/correct')
def correct():
    return render_template('corrent.html')  # 정답 페이지


@app.route('/wrong')
def wrong():
    return render_template('wrong.html')  # 오답 페이지

if __name__ == '__main__':
    app.run(debug=True)
