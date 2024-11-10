function playAudio() {
    const audio = document.getElementById('audio');
    audio.play();
    setTimeout(() => {
        audio.pause();
        audio.currentTime = 0;  // 재생 위치를 처음으로 리셋
    }, 3000);  // 3초 재생 후 중지
}
