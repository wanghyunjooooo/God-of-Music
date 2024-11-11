from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 퀴즈 데이터 - 각 문제에 대한 오디오 파일 경로와 정답을 설정
quiz_data = [
    {"audio": "/static/audio/Steady.mp3", "answer": "steady", "music_video_url": "https://www.youtube.com/embed/IKlkZZv76Ho"},
    {"audio": "/static/audio/Dunk Shot.mp3", "answer": "dunk shot", "music_video_url": "https://www.youtube.com/embed/4vgac97VlCE"},
    # 추가적인 문제를 여기에 추가
]

score = {'correct': 0, 'wrong': 0}  # 점수 초기화
index = 0  # 문제 인덱스 초기화

@app.route('/')
def quiz():
    global score, index
    # 10문제를 모두 풀면 결과 페이지로 이동
    if index >= 10:
        return redirect(url_for('results'))
    
    question = quiz_data[index % len(quiz_data)]  # 현재 인덱스의 문제 선택
    return render_template('songquiz.html', question=question)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global index
    user_answer = request.form.get('answer').strip().lower()
    correct_answer = request.form.get('correct_answer').strip().lower()
    music_video_url = request.form.get('music_video_url')  # 뮤직비디오 URL 가져오기
    audio = request.form.get('audio')  # 오디오 파일 경로 가져오기

    # video_id 추출
    video_id = music_video_url.split('/embed/')[-1]

    # 정답 확인
    if user_answer == correct_answer:
        score['correct'] += 1
    else:
        score['wrong'] += 1

    index += 1  # 다음 문제로 이동
    # 정답/오답 화면으로 이동
    if user_answer == correct_answer:
        return render_template('songquiz-correct.html', correct_answer=correct_answer, music_video_url=music_video_url, video_id=video_id, audio=audio)
    else:
        return render_template('songquiz-wrong.html', correct_answer=correct_answer, music_video_url=music_video_url, video_id=video_id, audio=audio)

@app.route('/results')
def results():
    global score, index
    correct_count = score['correct']
    wrong_count = score['wrong']
    # 점수와 인덱스 초기화
    score = {'correct': 0, 'wrong': 0}
    index = 0
    return render_template('songquiz-results.html', correct=correct_count, wrong=wrong_count)

if __name__ == '__main__':
    app.run(debug=True)
