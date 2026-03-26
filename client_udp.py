import socket
import pygame
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "127.0.0.1"   # change later
server_port = 9999

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Client")

clock = pygame.time.Clock()

player_pos = [300, 300]
players = {}
latencies = []

colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]

def send_move(direction):
    global player_pos

    timestamp = time.time()

    # ✅ CLIENT PREDICTION
    if direction == "UP":
        player_pos[1] -= 5
    elif direction == "DOWN":
        player_pos[1] += 5
    elif direction == "LEFT":
        player_pos[0] -= 5
    elif direction == "RIGHT":
        player_pos[0] += 5

    msg = f"MOVE {direction} {timestamp}"
    client.sendto(msg.encode(), (server_ip, server_port))

    return timestamp

running = True

while running:
    clock.tick(30)

    sent_time = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        sent_time = send_move("UP")
    if keys[pygame.K_s]:
        sent_time = send_move("DOWN")
    if keys[pygame.K_a]:
        sent_time = send_move("LEFT")
    if keys[pygame.K_d]:
        sent_time = send_move("RIGHT")

    # receive state
    try:
        client.settimeout(0.01)
        data, _ = client.recvfrom(1024)
        now = time.time()

        state = data.decode().replace("STATE ", "").split()

        players.clear()
        for p in state:
            pid, pos = p.split(":")
            x, y = pos.split(",")
            players[pid] = (int(x), int(y))

        # latency
        if sent_time:
            latency = (now - sent_time) * 1000
            latencies.append(latency)

    except:
        pass

    # draw
    screen.fill((0, 0, 0))

    for i, (pid, pos) in enumerate(players.items()):
        color = colors[i % len(colors)]
        pygame.draw.circle(screen, color, pos, 10)

        font = pygame.font.Font(None, 24)
        text = font.render(f"P{pid}", True, (255,255,255))
        screen.blit(text, (pos[0]+10, pos[1]-10))

    # show latency + jitter
    font = pygame.font.Font(None, 24)

    if latencies:
        latency_text = font.render(f"Latency: {latencies[-1]:.2f} ms", True, (255,255,255))
        screen.blit(latency_text, (10, 10))

    if len(latencies) > 1:
        jitter = abs(latencies[-1] - latencies[-2])
        jitter_text = font.render(f"Jitter: {jitter:.2f} ms", True, (255,255,255))
        screen.blit(jitter_text, (10, 30))

    pygame.display.update()

pygame.quit()