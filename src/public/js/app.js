const socket = io(); //socketIO를 프론트와 연결

//카메라
const myFace = document.getElementById("myFace");
const muteBtn = document.getElementById("mute");
const cameraBtn = document.getElementById("camera");

//채팅창
const welcome = document.getElementById("welcome");
const form = welcome.querySelector("form");
const room = document.getElementById("room");

room.hidden = true;

let myStream;
let muted = false;
let cameraOff = false;

let roomName;

//캠, 오디오를 화면에 출력
async function getMedia() {
  try {
    myStream = await navigator.mediaDevices.getUserMedia({
      audio: true,
      video: true,
    });
    myFace.srcObject = myStream;
  } catch (e) {
    console.log(e);
  }
}

// 음소거 버튼
function handleCameraClick() {
  if (!cameraOff) {
    cameraBtn.innerText("Camera Turn on");
    cameraOff = true;
  } else {
    cameraBtn.innerText("Camera Turn Off");
    cameraOff = false;
  }
}

// 카메라 버튼
function handleMuteClick() {
  if (!muted) {
    muteBtn.innerText("Unmute");
    muted = true;
  } else {
    muteBtn.innerText("Mute");
    muted = false;
  }
}

// 메시지를 입력받았을 때 페이지에 올려주는 함수
function addMessage(msg) {
  const ul = room.querySelector("ul");
  const li = document.createElement("li");
  li.innerText = msg;
  ul.appendChild(li);
}

// 방에 들어와있을때
// 메시지를 받았을 때 서버로 옮기기
function handleMessageSubmit(event) {
  event.preventDefault();
  const input = room.querySelector("#msg input");
  const value = input.value;
  socket.emit("new_msg", input.value, roomName, () => {
    addMessage(`You : ${value}`);
    input.value = "";
  });
}

function handleNicknameSubmit(event) {
  event.preventDefault();
  const input = room.querySelector("#name input");
  const value = input.value;
  socket.emit("nickname", value);
  input.value = "";
}

// 해당 방에 들어왔을 때 페이지에서 할 처리
function showRoom() {
  const h3 = room.querySelector("h3");
  welcome.hidden = true;
  room.hidden = false;
  h3.innerText = `Room ${roomName}`;
  const msgForm = room.querySelector("#msg");
  const nameForm = room.querySelector("#name");
  msgForm.addEventListener("submit", handleMessageSubmit);
  nameForm.addEventListener("submit", handleNicknameSubmit);
}

//해당 방에 들어왔을 때 처리함수
function handleRoomSubmit(event) {
  event.preventDefault();
  const input = form.querySelector("input");
  //서버로 원하는 것을 모두 소켓에 담아 보낼 수 있음
  socket.emit(
    //백엔드에 펑션 실행스위치를 주는 듯?
    "room",
    input.value,
    showRoom //서버에서 호출되는 펑션
  );
  roomName = input.value;

  input.value = "";
}
/*--------------------------실행 파트------------------------ */
getMedia();

muteBtn.addEventListener("click", handleMuteClick);
cameraBtn.addEventListener("click", handleCameraClick);

form.addEventListener("submit", handleRoomSubmit);

socket.on("welcome", (user, newCount) => {
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName} (${newCount})`;
  addMessage(`${user} joined!`);
});

socket.on("bye", (left, newCount) => {
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName} (${newCount})`;
  addMessage(`${left} left ㅜㅜ`);
});

socket.on("new_msg", addMessage);

socket.on("room_change", (rooms) => {
  const roomList = welcome.querySelector("ul");
  roomList.innerHTML = "";
  if (rooms.length === 0) {
    return;
  }
  rooms.forEach((room) => {
    const li = document.createElement("li");
    li.innerText = room;
    roomList.appendChild(li);
  });
});
