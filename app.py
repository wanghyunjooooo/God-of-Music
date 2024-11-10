from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 퀴즈 데이터 (이미지와 정답을 추가하여 확장 가능)
quiz_data = [
    {"image": "/static/images/apt.png", "answer": "apt,아파트"},
    {"image": "/static/images/별별별.png", "answer": "별별별"},
    {"image": "/static/images/네모네모.png", "answer": "네모네모"},
    {"image": "/static/images/녹아내려요.png", "answer": "녹아내려요"},
    {"image": "/static/images/반딧불.png", "answer": "반딧불"},
    {"image": "/static/images/삐그덕.png", "answer": "삐그덕"},
    {"image": "/static/images/사랑돈명예.png", "answer": "사랑 돈 명예 ,love money fame"},
    {"image": "/static/images/해야.png", "answer": "해야"},
    {"image": "/static/images/boomboombase.png", "answer": "boomboombase ,붐붐베이스"},
    {"image": "/static/images/chkchkboom.png", "answer": "chkchkboom , 칙칙붐"},
    {"image": "/static/images/girlsneverdie.png", "answer": "girlsneverdie , 걸스네버다이"},
    {"image": "/static/images/nectar.png", "answer": "nectar"},
    {"image": "/static/images/sos.png", "answer": "sos"},
    {"image": "/static/images/steady.png", "answer": "steady , 스테디"},
    {"image": "/static/images/sticky.png", "answer": "sticky"},
    {"image": "/static/images/supernova.png", "answer": "supernova , 수퍼노바"},
    {"image": "/static/images/supersonic.png", "answer": "supersonic, 수퍼소닉"},
    {"image": "/static/images/xo.png", "answer": "xo"},
    {"image": "/static/images/drip.png", "answer": "drip"},
    {"image": "/static/images/mantra.png", "answer": "mantra , 만트라"},
    {"image": "/static/images/power.png", "answer": "power , 파워"},
    {"image": "/static/images/whiplash.png", "answer": "whiplash ,위플래시 , 위플래쉬"},
    {"image": "/static/images/magnetic.png", "answer": "magnetic , 마그네틱"},
    {"image": "/static/images/trigger.png", "answer": "trigger , 트리거"},
    {"image": "/static/images/뭣같아.png", "answer": "뭣같아"},
    {"image": "/static/images/부모님관람불가.png", "answer": "부모님관람불가"},
    {"image": "/static/images/baggyjeans.png", "answer": "baggyjeans , 배기진스"},
    {"image": "/static/images/love119.png", "answer": "love119 , 러브119 , 러브원원나인"},
    {"image": "/static/images/serenade.png", "answer": "serenade, 세레나데"},
    {"image": "/static/images/watchit.png", "answer": "watchit , 와치잇"},
    {"image": "/static/images/wish.png", "answer": "wish ,위시"},
    {"image": "/static/images/클락션.png", "answer": "클락션"},
    {"image": "/static/images/abcd.png", "answer": "abcd , 에이비씨디 , 에이비시디"},
    {"image": "/static/images/cherish.png", "answer": "cherish , 체리쉬"},
    {"image": "/static/images/cosmic.png", "answer": "cosmic, 코스믹"},
    {"image": "/static/images/dunkshot.png", "answer": "dunkshot , 덩크슛"},
    {"image": "/static/images/forever.png", "answer": "forever , 포에버"},
    {"image": "/static/images/howsweet.png", "answer": "howsweet , 하우스윗"},
    {"image": "/static/images/impossible.png", "answer": "impossible, 임파서블"},
    {"image": "/static/images/meow.png", "answer": "meow , 미아오"},
    {"image": "/static/images/spot.png", "answer": "spot , 스팟"},
    {"image": "/static/images/smallgirl.png", "answer": "smallgirl , 스몰걸"},
    {"image": "/static/images/to.x.png", "answer": "to.x , tox,투엑스"},
    {"image": "/static/images/내가s면넌나의n이되어줘.png", "answer": "내가s면넌나의n이되어줘"},
    {"image": "/static/images/첫만남은계획대로되지않아.png", "answer": "첫만남은계획대로되지않아"},

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
    user_answer = request.form.get('answer').strip().lower().replace(" ", "")  # 사용자 입력에서 띄어쓰기 제거
    correct_answers = request.form.get('correct_answer').strip().lower().split(',')
    correct_answers = [ans.strip().replace(" ", "") for ans in correct_answers]  # 정답 리스트에서도 띄어쓰기 제거
    correct_image = request.form.get('correct_image')  # 정답 이미지 경로 추가

    if user_answer in correct_answers:
        global score
        score['correct'] += 1  # 정답 수 증가
        return render_template('correct.html', correct_answer=correct_answers[0], correct_image=correct_image)
    else:
        score['wrong'] += 1  # 오답 수 증가
        return render_template('wrong.html', correct_answer=correct_answers[0], correct_image=correct_image)  # 오답 페이지에 정답과 이미지를 전달

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
    return render_template('correct.html')  # 정답 페이지

@app.route('/wrong')
def wrong():
    return render_template('wrong.html')  # 오답 페이지

if __name__ == '__main__':
    app.run(debug=True)