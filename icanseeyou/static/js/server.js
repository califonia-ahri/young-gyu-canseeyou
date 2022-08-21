import express from "express";
import { Server } from "socket.io";
import { instrument } from "@socket.io/admin-ui";
import http from "http";

const app = express();

//볼 사이트 엔진을 pug로 설정
app.set("view engine", "pug");

//세팅할 파일을 views 내 파일로 설정
app.set("views", __dirname + "/views");

//유저가 홈페이지를 들어가게되면 __dirname/public 파일을 보여준다.
app.use("/public", express.static(__dirname + "/public"));

//home 디렉터리로 가면 요청 응답을 받아 내가 만든 home을 렌더링한다
app.get("/", (req, res) => res.render("home"));
//url은 하나만 쓸것이므로 어떤 url을 가든 홈디렉토리를 렌더링
app.get("/*", (req, res) => res.redirect("/"));

const handleListen = () => console.log("Listening on http://localhost:3000");

const httpServer = http.createServer(app);
const wsServer = new Server(httpServer, {
    cors: {
        origin: ["https://admin.socket.io"],
        credentials: true,
    },
});

instrument(wsServer, {
    auth: false,
});

function publicRooms() {
    const sids = wsServer.sockets.adapter.sids;
    const rooms = wsServer.sockets.adapter.rooms;
    const publicRooms = [];
    rooms.forEach((_, key) => {
        if (sids.get(key) === undefined) {
            publicRooms.push(key);
        }
    });
    return publicRooms;
}

function countRoom(roomName) {
    return wsServer.sockets.adapter.rooms.get(roomName).size;
}

wsServer.on("connection", (socket) => {
    socket["nickname"] = "Anon";
    socket.onAny((event) => {
        console.log(`Socket Event: ${event}`);
    });

    //방에 들어왔을 때
    socket.on("room", (roomName, done) => {
        socket.join(roomName);
        done();
        socket.to(roomName).emit("welcome", socket.nickname, countRoom(roomName));
        wsServer.sockets.emit("room_change", publicRooms());
    });

    //방에 연결이 끊길 때
    socket.on("disconnecting", () => {
        socket.rooms.forEach((room) =>
            socket.to(room).emit("bye", socket.nickname, countRoom(room) - 1)
        );
    });

    //방에 완전히 끊겼을 때
    socket.on("disconnect", () => {
        wsServer.sockets.emit("room_change", publicRooms());
    });

    socket.on("new_msg", (msg, room, done) => {
        socket.to(room).emit("new_msg", `${socket.nickname}: ${msg}`);
        done();
    });

    socket.on("nickname", (nick) => {
        socket["nickname"] = nick;
    });
});

httpServer.listen(3000, handleListen);

//http서버위에 ws서버를 만들어 결과적으로 하나의 서버로 동시에 돌린다.
// const wss = new WebSocket.Server({server});

//프론트로 받은 메시지 창고
//const sockets = [];

// wss.on("connection", (socket) => {
//     sockets.push(socket);
//     socket["nickname"] = "Anon";
//     console.log("Connected to Browser");
//     socket.on("close",() => console.log("Disconnected from Browser"));
//     socket.on("message", (msg) => {
//         const message = JSON.parse(msg);
//         switch(message.type){
//             case "new_message":
//                 sockets.forEach((aSocket) =>
//                 aSocket.send(`${socket.nickname}: ${message.payload}`));
//             case "nickname":
//                 socket["nickname"] = message.payload;
//         }
//     });
// });