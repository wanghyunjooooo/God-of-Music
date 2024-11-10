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
    {"image": "/static/images/drip.png", "answer": "drip"},
    {"image": "/static/images/mantra.png", "answer": "mantra"},
    {"image": "/static/images/power.png", "answer": "power"},
    {"image": "/static/images/whiplash.png", "answer": "whiplash"},
    {"image": "/static/images/magnetic.png", "answer": "magnetic"},
    {"image": "/static/images/trigger.png", "answer": "trigger"},
    {"image": "/static/images/뭣같아.png", "answer": "뭣같아"},
    {"image": "/static/images/부모님관람불가.png", "answer": "부모님관람불가"},
    {"image": "/static/images/baggyjeans.png", "answer": "baggyjeans"},
    {"image": "/static/images/love119.png", "answer": "love119"},
    {"image": "/static/images/serenade.png", "answer": "serenade"},
    {"image": "/static/images/watchit.png", "answer": "watchit"},
    {"image": "/static/images/wish.png", "answer": "wish"},
    {"image": "/static/images/클락션.png", "answer": "클락션"},
    {"image": "/static/images/abcd.png", "answer": "abcd"},
    {"image": "/static/images/cherish.png", "answer": "cherish"},
    {"image": "/static/images/cosmic.png", "answer": "cosmic"},
    {"image": "/static/images/dunkshot.png", "answer": "dunkshot"},
    {"image": "/static/images/forever.png", "answer": "forever"},
    {"image": "/static/images/howsweet.png", "answer": "howsweet"},
    {"image": "/static/images/impossible.png", "answer": "impossible"},
    {"image": "/static/images/meow.png", "answer": "meow"},

    # 여기에 추가적인 이미지와 정답을 넣을 수 있습니다.
]

# 사용자의 정답 결과를 저장할 전역 변수
score = {
    'correct': 0,
    'wrong': 0
}

@app.route('/')
def quiz():
    global score
    if score['correct'] + score['wrong'] >= 10:  # 10문제를 풀면 결과 페이지로 이동
        return redirect(url_for('results'))
    
    scene = random.choice(quiz_data)  # 랜덤으로 퀴즈 장면 선택
    return render_template('mvquiz.html', scene=scene)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('answer').strip().lower()  # 사용자 입력
    correct_answer = request.form.get('correct_answer').strip().lower()  # 정답
    correct_image = request.form.get('correct_image')  # 정답 이미지 경로 추가

    if user_answer == correct_answer:
        global score
        score['correct'] += 1  # 정답 수 증가
        return render_template('corrent.html', correct_answer=correct_answer, correct_image=correct_image)
    else:
        score['wrong'] += 1  # 오답 수 증가
        return render_template('wrong.html', correct_answer=correct_answer, correct_image=correct_image)  # 오답 페이지에 정답과 이미지를 전달

@app.route('/results')
def results():
    global score
    correct_count = score['correct']
    wrong_count = score['wrong']
    score['correct'] = 0  # 점수 초기화
    score['wrong'] = 0
    return render_template('results.html', correct=correct_count, wrong=wrong_count)

@app.route('/correct')
def correct():
    return render_template('corrent.html')  # 정답 페이지

@app.route('/wrong')
def wrong():
    return render_template('wrong.html')  # 오답 페이지

if __name__ == '__main__':
    app.run(debug=True)
