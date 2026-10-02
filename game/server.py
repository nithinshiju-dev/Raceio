import socket
import json

HOST = "0.0.0.0"
PORT = 5000

players = {}
last_sequence = {}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"Raceio server running on UDP port {PORT}")
print("Waiting for players...")

while True:
    data, address = server.recvfrom(1024)

    try:
        message = json.loads(data.decode())
    except json.JSONDecodeError:
        print("Received invalid packet")
        continue

    player_id = message.get("player_id")
    sequence = message.get("sequence")

    if player_id is None or sequence is None:
        print("Packet missing player ID or sequence number")
        continue

    # Check for packet loss
    if player_id in last_sequence:
        expected_sequence = last_sequence[player_id] + 1

        if sequence > expected_sequence:
            lost = sequence - expected_sequence

            print(
                f"[PACKET LOSS] Player {player_id}: "
                f"expected {expected_sequence}, "
                f"received {sequence}, "
                f"lost approximately {lost} packet(s)"
            )

        elif sequence <= last_sequence[player_id]:
            print(
                f"[OLD PACKET] Player {player_id}: "
                f"received {sequence}, "
                f"latest is {last_sequence[player_id]}"
            )

    last_sequence[player_id] = sequence

    # Store latest player state
    players[player_id] = {
        "address": address,
        "x": message.get("x", 0),
        "y": message.get("y", 0),
        "speed": message.get("speed", 0),
        "sequence": sequence,
    }

    print(
        f"Player {player_id}: "
        f"x={message.get('x')} "
        f"y={message.get('y')} "
        f"speed={message.get('speed')} "
        f"seq={sequence}"
    )

    # Send current game state to every player
    response = {
        "type": "game_state",
        "players": players,
    }

    response_data = json.dumps(response).encode()

    for player in players.values():
        server.sendto(response_data, player["address"])