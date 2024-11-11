from flask import Flask, render_template, request, redirect, url_for
import random

# 두 번째 Flask 앱 객체 생성
songquiz_app = Flask(__name__)

# 퀴즈 데이터 - 각 문제에 대한 오디오 파일 경로와 정답을 설정
songquiz_data = [
    {"audio": "/static/audio/Steady.mp3", "answer": "steady", "music_video_url": "https://www.youtube.com/embed/IKlkZZv76Ho"},
    {"audio": "/static/audio/Dunk Shot.mp3", "answer": "dunk shot", "music_video_url": "https://www.youtube.com/embed/4vgac97VlCE"},
    # 추가적인 문제를 여기에 추가
]

songquiz_score = {'correct': 0, 'wrong': 0} 
songquiz_index = 0  

@songquiz_app.route('/')
def quiz():
    global songquiz_score, songquiz_index
    if songquiz_index >= 10:
        return redirect(url_for('results'))
    
    question = songquiz_data[songquiz_index % len(songquiz_data)]
    return render_template('songquiz.html', question=question)

@songquiz_app.route('/check_answer', methods=['POST'])
def check_answer():
    global songquiz_index
    user_answer = request.form.get('answer').strip().lower()
    correct_answer = request.form.get('correct_answer').strip().lower()
    music_video_url = request.form.get('music_video_url')
    audio = request.form.get('audio')

    video_id = music_video_url.split('/embed/')[-1]

    if user_answer == correct_answer:
        songquiz_score['correct'] += 1
    else:
        songquiz_score['wrong'] += 1

    songquiz_index += 1
    if user_answer == correct_answer:
        return render_template('songquiz-correct.html', correct_answer=correct_answer, music_video_url=music_video_url, video_id=video_id, audio=audio)
    else:
        return render_template('songquiz-wrong.html', correct_answer=correct_answer, music_video_url=music_video_url, video_id=video_id, audio=audio)

@songquiz_app.route('/results')
def results():
    global songquiz_score, songquiz_index
    correct_count = songquiz_score['correct']
    wrong_count = songquiz_score['wrong']
    songquiz_score = {'correct': 0, 'wrong': 0}
    songquiz_index = 0
    return render_template('songquiz-results.html', correct=correct_count, wrong=wrong_count)

if __name__ == '__main__':
    songquiz_app.run(debug=True)