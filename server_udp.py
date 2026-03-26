import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 9999))

print("Server started...")

clients = {}
players = {}
next_id = 1

UPDATE_RATE = 0.05
server.setblocking(False)

while True:
    try:
        data, addr = server.recvfrom(1024)
        message = data.decode()

        if addr not in clients:
            clients[addr] = next_id
            players[next_id] = [300, 300]
            print(f"Player {next_id} joined")
            next_id += 1

        player_id = clients[addr]

        parts = message.split()
        if parts[0] == "MOVE":
            direction = parts[1]

            if direction == "UP":
                players[player_id][1] -= 5
            elif direction == "DOWN":
                players[player_id][1] += 5
            elif direction == "LEFT":
                players[player_id][0] -= 5
            elif direction == "RIGHT":
                players[player_id][0] += 5

    except:
        pass

    # broadcast state
    state = "STATE "
    for pid, pos in players.items():
        state += f"{pid}:{pos[0]},{pos[1]} "

    for c in clients:
        server.sendto(state.encode(), c)

    time.sleep(UPDATE_RATE)