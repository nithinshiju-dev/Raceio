import socket
import json
import time
import sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

if len(sys.argv) < 2:
    print("Usage: python client.py <player_id>")
    sys.exit(1)

player_id = int(sys.argv[1])

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(1)

sequence = 0
x = 0
y = 0
speed = 50

print(f"Player {player_id} started")
print("Sending game-state updates...")

while True:
    sequence += 1
    x += 5

    message = {
        "player_id": player_id,
        "sequence": sequence,
        "x": x,
        "y": y,
        "speed": speed,
        "timestamp": time.time(),
    }

    data = json.dumps(message).encode()

    client.sendto(
        data,
        (SERVER_IP, SERVER_PORT)
    )

    print(f"Sent: {message}")

    try:
        response, _ = client.recvfrom(4096)
        game_state = json.loads(response.decode())

        print(f"Received game state: {game_state}")

    except socket.timeout:
        print("No response from server")

    time.sleep(0.1)