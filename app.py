from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 퀴즈 데이터 (이미지와 정답을 추가하여 확장 가능)
quiz_data = [
    {"image": "/static/images/apt.png", "answer": "apt"},
    {"image": "/static/images/별별별.png", "answer": "별별별"},
    {"image": "/static/images/네모네모.png", "answer": "네모네모"},
    {"image": "/static/images/녹아내려요.png", "answer": "녹아내려요"},
    {"image": "/static/images/반딧불.png", "answer": "반딧불"},
    {"image": "/static/images/삐그덕.png", "answer": "삐그덕"},
    {"image": "/static/images/사랑돈명예.png", "answer": "사랑돈명예"},
    {"image": "/static/images/해야.png", "answer": "해야"},
    {"image": "/static/images/boomboombase.png", "answer": "boomboombase"},
    {"image": "/static/images/chkchkboom.png", "answer": "chkchkboom"},
    {"image": "/static/images/girlsneverdie.png", "answer": "girlsneverdie"},
    {"image": "/static/images/nectar.png", "answer": "nectar"},
    {"image": "/static/images/sos.png", "answer": "sos"},
    {"image": "/static/images/steady.png", "answer": "steady"},
    {"image": "/static/images/sticky.png", "answer": "sticky"},
    {"image": "/static/images/supernova.png", "answer": "supernova"},
    {"image": "/static/images/supersonic.png", "answer": "supersonic"},
    {"image": "/static/images/xo.png", "answer": "xo"},
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
    correct_image = request.form.get('correct_image')  # 정답 이미지 경로 추가

    if user_answer == correct_answer:
        # 정답일 경우
        return render_template('corrent.html', correct_answer=correct_answer, correct_image=correct_image)
    else:
        # 오답일 경우
        return redirect(url_for('wrong'))  # 오답 페이지로 리디렉션

@app.route('/correct')
def correct():
    return render_template('corrent.html')  # 정답 페이지

@app.route('/wrong')
def wrong():
    return render_template('wrong.html')  # 오답 페이지

if __name__ == '__main__':
    app.run(debug=True)
