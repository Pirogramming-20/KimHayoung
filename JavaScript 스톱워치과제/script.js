// 타이머 상태와 시간을 추적하는 변수들
let isRunning = false;
let elapsedTime = 0;
let timerInterval = null;

// DOM 요소를 선택합니다.
const timerElement = document.getElementById('timer');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');
const recordsContainer = document.getElementById('records-list');
const deleteIcon = document.getElementById('delete-icon');

// 시간을 ss:ms 형식으로 변환하는 함수 (밀리초를 두 자리로 표시)
function formatTime(time) {
    const seconds = Math.floor(time / 1000).toString().padStart(2, '0');
    // 밀리초를 10으로 나누고 정수 부분만 사용하여 두 자리로 만듭니다.
    const milliseconds = Math.floor((time % 1000) / 10).toString().padStart(2, '0');
    return `${seconds}:${milliseconds}`;
}


// 타이머를 시작하는 함수
function startTimer() {
    if (!isRunning) {
        isRunning = true;
        timerInterval = setInterval(() => {
            elapsedTime += 10; // 10밀리초 증가
            timerElement.textContent = formatTime(elapsedTime);
        }, 10); // 10밀리초마다 업데이트
    }
}

// 타이머를 중지하고 구간 기록을 추가하는 함수
function stopTimer() {
    if (isRunning) {
        isRunning = false;
        clearInterval(timerInterval);
        addRecord(elapsedTime);
    }
}

// 타이머를 리셋하는 함수
function resetTimer() {
    isRunning = false;
    clearInterval(timerInterval);
    elapsedTime = 0;
    timerElement.textContent = '00:00';
    // 모든 기록을 삭제
    while (recordsContainer.firstChild) {
        recordsContainer.removeChild(recordsContainer.firstChild);
    }
}

//===============================================


// 구간 기록을 추가하는 함수
function addRecord(time) {
    const timeString = formatTime(time);
    const recordElement = document.createElement('div');
    recordElement.classList.add('record'); // 클래스명 변경
    
    const deleteButton = document.createElement('button');
    deleteButton.classList.add('delete-one');
    const imgElement = document.createElement('img');
    imgElement.src = './ellipse-outline.svg';
    imgElement.alt = 'Delete';
    deleteButton.appendChild(imgElement);

    // 클릭 이벤트 리스너 수정
    deleteButton.addEventListener('click', function() {
        toggleImage(imgElement, recordElement);
    });

    const timeText = document.createElement('span');
    timeText.textContent = timeString;

    recordElement.appendChild(deleteButton);
    recordElement.appendChild(timeText);
    recordsContainer.appendChild(recordElement);
}

// 이미지 토글 및 선택 상태 토글 함수
function toggleImage(imgElement, recordElement) {
    if (imgElement.src.includes('ellipse-outline.svg')) {
        imgElement.src = './checkmark-circle-outline.svg';
        imgElement.alt = 'Selected';
        recordElement.classList.add('selected');
    } else {
        imgElement.src = './ellipse-outline.svg';
        imgElement.alt = 'Delete';
        recordElement.classList.remove('selected');
    }
    checkAllSelected();
}

// delete-icon 클릭 이벤트 리스너
deleteIcon.addEventListener('click', function() {
    document.querySelectorAll('.record.selected').forEach(record => {
        recordsContainer.removeChild(record);
    });
    resetDeleteAllButton();
});

// delete-all 버튼 클릭 이벤트 리스너
document.getElementById('delete-all').addEventListener('click', function() {
    const records = document.querySelectorAll('.record');
    const isSelected = this.querySelector('img').src.includes('checkmark-circle-outline.svg');
    records.forEach(record => {
        const img = record.querySelector('.delete-one img');
        img.src = isSelected ? './ellipse-outline.svg' : './checkmark-circle-outline.svg';
        img.alt = isSelected ? 'Delete' : 'Selected';
        isSelected ? record.classList.remove('selected') : record.classList.add('selected');
    });
    checkAllSelected();
});

// 모든 기록이 선택되었는지 확인하는 함수
function checkAllSelected() {
    const records = document.querySelectorAll('.record');
    const allSelected = Array.from(records).every(record => record.classList.contains('selected'));
    const deleteAllImg = document.getElementById('delete-all').querySelector('img');
    if (allSelected) {
        deleteAllImg.src = './checkmark-circle-outline.svg';
        deleteAllImg.alt = 'All selected';
    } else {
        resetDeleteAllButton();
    }
}

// delete-all 버튼을 초기 상태로 되돌리는 함수
function resetDeleteAllButton() {
    const deleteAllImg = document.getElementById('delete-all').querySelector('img');
    deleteAllImg.src = './ellipse-outline.svg';
    deleteAllImg.alt = 'Select all';
}


//====================================================


// 이벤트 리스너를 버튼에 연결합니다.
startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);
