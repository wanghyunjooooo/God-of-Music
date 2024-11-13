from flask import Flask, render_template, request, redirect, url_for
import random

# 두 번째 Flask 앱 객체 생성
songquiz_app = Flask(__name__)

# 퀴즈 데이터 - 각 문제에 대한 오디오 파일 경로와 정답을 설정
songquiz_data = [
    {"audio": "/static/audio/부모님관람불가.mp3", "answer": "부모님관람불가", "music_video_url": "https://www.youtube.com/embed/YkCXVgcsGTU"},
    {"audio": "/static/audio/Happy.mp3", "answer": "Happy,해피", "music_video_url": "https://www.youtube.com/embed/sWXGbkM0tBI"},
    {"audio": "/static/audio/Songbird.mp3", "answer": "Songbird,송버드", "music_video_url": "https://www.youtube.com/embed/2XqVNFBtVo4"},
    {"audio": "/static/audio/Whiplash.mp3", "answer": "Whiplash,위플래쉬,위플래시", "music_video_url": "https://www.youtube.com/embed/jWQx2f-CErU"},
    {"audio": "/static/audio/WISH.mp3", "answer": "Wish,위시", "music_video_url": "https://www.youtube.com/embed/hvQZs3k6Ytk"},
    {"audio": "/static/audio/질주.mp3", "answer": "질주", "music_video_url": "https://www.youtube.com/embed/FRilMXZqNhA"},
    {"audio": "/static/audio/How sweet.mp3", "answer": "how sweet,하우스윗", "music_video_url": "https://www.youtube.com/embed/Q3K0TOvTOno"},
    {"audio": "/static/audio/Supersonic.mp3", "answer": "supersonic,수퍼소닉,슈퍼소닉", "music_video_url": "https://www.youtube.com/embed/0LiQp7y8Wwc"},
    {"audio": "/static/audio/Thrill ride.mp3", "answer": "thrill ride,스릴라이드", "music_video_url": "https://www.youtube.com/embed/XMs2CIiqRDI"},
    {"audio": "/static/audio/To x.mp3", "answer": "to.x,to x,투엑스", "music_video_url": "https://www.youtube.com/embed/5_n6t9G2TUQ"},
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
    user_answer = request.form.get('answer').strip().lower().replace(" ", "")
    correct_answers = request.form.get('correct_answer').strip().lower().split(',')
    correct_answers = [ans.strip().replace(" ", "") for ans in correct_answers]  # 정답 리스트에서 띄어쓰기 제거

    music_video_url = request.form.get('music_video_url')
    audio = request.form.get('audio')
    video_id = music_video_url.split('/embed/')[-1]

    # 여러 정답 중 하나와 일치하는지 확인
    if user_answer in correct_answers:
        songquiz_score['correct'] += 1
    else:
        songquiz_score['wrong'] += 1

    songquiz_index += 1  # 문제 인덱스 증가

    if user_answer in correct_answers:
        return render_template('songquiz-correct.html', correct_answer=correct_answers[0], music_video_url=music_video_url, video_id=video_id, audio=audio)
    else:
        return render_template('songquiz-wrong.html', correct_answer=correct_answers[0], music_video_url=music_video_url, video_id=video_id, audio=audio)

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
