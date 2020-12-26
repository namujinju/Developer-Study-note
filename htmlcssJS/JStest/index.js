// 임의의 자연수 n
// 짝수면 2로 나누고
// 홀수면 3을 곱하고 1을 더한다.
// 결국엔 1로 된다.

// n: 1 ~ 100

function Collatz(n) {
  let counter = 0;
  while (n != 1) {
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n = n * 3 + 1;
    }
    counter++;
  }
  console.log(`${i}에서 시작하면 ${counter}단계를 걸쳐 1이 됩니다`);
}

for (var i = 1; i <= 100; i++) {
  //1 ~ 100까지 확인하는 반복문
  Collatz(i);
  // n에서 시작하면 몇 단계를 걸쳐서 1이 된다.
}
