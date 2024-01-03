// 게임 상태를 저장할 변수들
let answer = [];
let attempts = 9;

// 페이지 로드 시 게임 초기화
window.onload = initializeGame;

function initializeGame() {
    // 시도 가능 횟수 설정
    attempts = 9;

    // 중복되지 않는 3개의 랜덤한 숫자 생성
    answer = generateRandomNumbers();

    // 입력 필드와 결과창 초기화
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    document.querySelector('.result-display').innerHTML = '';
    document.getElementById('game-result-img').src = '';

    // 버튼 활성화
    document.querySelector('.submit-button').disabled = false;
}

// 중복되지 않는 3개의 랜덤 숫자 생성
function generateRandomNumbers() {
    let numbers = [];
    while (numbers.length < 3) {
        let num = Math.floor(Math.random() * 10);
        if (!numbers.includes(num)) {
            numbers.push(num);
        }
    }
    return numbers;
}

// 숫자 확인
function check_numbers() {
    let num1 = document.getElementById('number1').value;
    let num2 = document.getElementById('number2').value;
    let num3 = document.getElementById('number3').value;

    if (!num1 || !num2 || !num3) {
        alert('모든 숫자를 입력해주세요!');

        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        return;
    }

    // 숫자 배열로 변환
    let inputNumbers = [parseInt(num1), parseInt(num2), parseInt(num3)];

    // 결과 확인
    let result = checkResult(inputNumbers);
    displayResult(inputNumbers, result);

    // 시도 횟수 감소
    attempts -= 1;

    // 게임 종료 체크
    if (result.strikes === 3) {
        endGame(true);
    } else if (attempts <= 0) {
        endGame(false);
    }

    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    
}

// 결과 확인 로직
function checkResult(inputNumbers) {
    let strikes = 0;
    let balls = 0;

    inputNumbers.forEach((num, index) => {
        if (num === answer[index]) {
            strikes += 1;
        } else if (answer.includes(num)) {
            balls += 1;
        }
    });

    return { strikes, balls };
}

// 결과 표시
function displayResult(inputNumbers, result) {
    let resultDiv = document.createElement('div');
    resultDiv.classList.add('check-result');

    let leftDiv = document.createElement('div');
    leftDiv.classList.add('left');
    leftDiv.textContent = inputNumbers.join(' ');

    let resultTextDiv = document.createElement('div');
    resultTextDiv.classList.add('result-text');
    resultTextDiv.textContent = ':';

    let rightDiv = document.createElement('div');
    rightDiv.classList.add('right');
    if (result.strikes === 0 && result.balls === 0) {
        let outDiv = document.createElement('div');
        outDiv.classList.add('out', 'num-result');
        outDiv.textContent = 'O';
        rightDiv.appendChild(outDiv);
    } else {
        if (result.strikes > 0) {
            let strikeDiv = document.createElement('div');
            strikeDiv.classList.add('strike', 'num-result');
            
            
            strikeDiv.textContent = `${result.strikes} S`;
            //strikeDiv.textContent = `S`;
            rightDiv.appendChild(strikeDiv);
        }
        if (result.balls > 0) {
            let ballDiv = document.createElement('div');
            ballDiv.classList.add('ball', 'num-result');
            ballDiv.textContent = `${result.balls} B`; 
            //ballDiv.textContent = `B`;  
            rightDiv.appendChild(ballDiv);
        }
    }

    resultDiv.appendChild(leftDiv);
    resultDiv.appendChild(resultTextDiv);
    resultDiv.appendChild(rightDiv);
    document.querySelector('.result-display').appendChild(resultDiv);
}

// 게임 종료 처리
function endGame(win) {
    let img = document.getElementById('game-result-img');
    img.src = win ? 'success.png' : 'fail.png';
    document.querySelector('.submit-button').disabled = true;
}
