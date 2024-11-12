from flask import Flask, render_template, request, redirect, url_for

# 첫 번째 Flask 앱 객체 생성
mvquiz_app = Flask(__name__)

# 퀴즈 데이터 (이미지와 정답을 추가하여 확장 가능)
mvquiz_data = [
    {"image": "/static/images/apt.png", "answer": "apt,아파트"},
    {"image": "/static/images/사랑돈명예.png", "answer": "사랑 돈 명예 ,love money fame"},
    {"image": "/static/images/boomboombase.png", "answer": "boomboombase ,붐붐베이스"},
    {"image": "/static/images/steady.png", "answer": "steady , 스테디"},
    {"image": "/static/images/supersonic.png", "answer": "supersonic, 수퍼소닉"},
    {"image": "/static/images/xo.png", "answer": "xo"},
    {"image": "/static/images/mantra.png", "answer": "mantra , 만트라"},
    {"image": "/static/images/power.png", "answer": "power , 파워"},
    {"image": "/static/images/serenade.png", "answer": "serenade,세레나데"},
    {"image": "/static/images/네모네모.png", "answer": "네모네모"},
]

# 사용자의 정답 결과를 저장할 전역 변수
mvquiz_score = {'correct': 0, 'wrong': 0}
mvquiz_index = 0  # 문제 인덱스 초기화

@mvquiz_app.route('/')
def quiz():
    global mvquiz_score, mvquiz_index
    if mvquiz_index >= 10:  # 10문제를 풀면 결과 페이지로 이동
        return redirect(url_for('results'))
    
    # 현재 문제를 순서대로 가져오기
    scene = mvquiz_data[mvquiz_index]
    return render_template('mvquiz.html', scene=scene)

@mvquiz_app.route('/check_answer', methods=['POST'])
def check_answer():
    global mvquiz_score, mvquiz_index
    user_answer = request.form.get('answer').strip().lower().replace(" ", "")
    correct_answers = request.form.get('correct_answer').strip().lower().split(',')
    correct_answers = [ans.strip().replace(" ", "") for ans in correct_answers]
    correct_image = request.form.get('correct_image')

    # 정답 확인
    if user_answer in correct_answers:
        mvquiz_score['correct'] += 1
        result_page = 'mvquiz-correct.html'
    else:
        mvquiz_score['wrong'] += 1
        result_page = 'mvquiz-wrong.html'

    # 문제 인덱스를 증가시켜 다음 문제로 이동
    mvquiz_index += 1
    return render_template(result_page, correct_answer=correct_answers[0], correct_image=correct_image)

@mvquiz_app.route('/results')
def results():
    global mvquiz_score, mvquiz_index
    correct_count = mvquiz_score['correct']
    wrong_count = mvquiz_score['wrong']
    # 점수와 인덱스 초기화
    mvquiz_score = {'correct': 0, 'wrong': 0}
    mvquiz_index = 0
    return render_template('mvquiz-results.html', correct=correct_count, wrong=wrong_count)

if __name__ == '__main__':
    mvquiz_app.run(debug=True)
