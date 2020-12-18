let counter = 0; // 몇 번만에 목표에 도달하는지 세는 변수

function collatz(n) {
  let m = n; // n은 입력받는 숫자, m은 계산 과정을 위한 변수
  while (m != 1) {
    if (m % 2 == 0) {
      // 짝수인 경우
      m /= 2;
    } else {
      m = m * 3 + 1;
    }
    counter += 1;
  }
  console.log(n + "에서 시작하면 " + counter + "번 만에 1에 도달");
  counter = 0;
}

for (var i = 1; i <= 100; i++) {
  collatz(i);
}

// 1이 될 때까지 반복
