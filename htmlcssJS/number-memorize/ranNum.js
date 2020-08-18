const table = document.querySelector("table");
const h1 = document.querySelector("h1");

const HIDDEN_CN = "hidden";
const FAILED_MES = "Failed!";
const CLEARED_MES = "Cleared!";
const TABLE_NUM = 9;
const TIME_OUT_H1 = 1500;

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
} // https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array?page=1&tab=votes#tab-top
let check_arr = new Array();

function makeNumTable() {
  let arr_num = new Array();
  check_arr = [];

  const tbody_get = document.querySelector("tbody");
  if (tbody_get) {
    // 이미 tbody가 있는 경우. 즉 숫자가 적혀 있는 경우
    tbody_get.remove();
  }

  const tbody = document.createElement("tbody");
  table.appendChild(tbody);

  for (var i = 0; i < TABLE_NUM; i++) {
    arr_num[i] = i + 1;
  }
  shuffleArray(arr_num);

  for (var i = 0; i < TABLE_NUM; i++) {
    const tr = document.createElement("tr");
    const td = document.createElement("td");

    if (i % Math.floor(Math.sqrt(TABLE_NUM)) === 0) {
      tbody.appendChild(tr);
    }
    td.innerText = arr_num[i];
    tbody.appendChild(td);
  }
}

function pushNum(num) {
  check_arr.push(num);
}

function showClear() {
  h1.innerText = CLEARED_MES;
  h1.classList.remove(HIDDEN_CN);
  let td_all = document.querySelectorAll("td");
  td_all.forEach((element) =>
    element.removeEventListener("click", handleClickedNum)
  );
}

function showFail() {
  h1.innerText = FAILED_MES;
  h1.classList.remove(HIDDEN_CN);
  let td_all = document.querySelectorAll("td");
  td_all.forEach((element) =>
    element.removeEventListener("click", handleClickedNum)
  );
}
function hideH1() {
  h1.classList.add(HIDDEN_CN);
}

function handleClickedNum(event) {
  event.target.classList.remove(HIDDEN_CN);
  const clickedNum = parseInt(event.target.innerText);
  if (check_arr.length) {
    if (check_arr[check_arr.length - 1] === clickedNum - 1) {
      pushNum(clickedNum);
    } else {
      showFail();
      setTimeout(init, TIME_OUT_H1);
      setTimeout(hideH1, TIME_OUT_H1);
    }
  } else {
    if (clickedNum === 1) {
      pushNum(clickedNum);
    } else {
      showFail();
      setTimeout(init, TIME_OUT_H1);
      setTimeout(hideH1, TIME_OUT_H1);
    }
  }
  if (clickedNum === TABLE_NUM) {
    showClear();
    setTimeout(init, TIME_OUT_H1);
    setTimeout(hideH1, TIME_OUT_H1);
  }

  console.log(clickedNum);
}

function gameStart() {
  let td_all = document.querySelectorAll("td");
  td_all.forEach((element) => element.classList.add(HIDDEN_CN));
  td_all.forEach((element) =>
    element.addEventListener("click", handleClickedNum)
  );
}

function init() {
  hideH1();
  makeNumTable();
  setTimeout(gameStart, 2000);
}

init();
