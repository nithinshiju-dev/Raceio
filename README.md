# Raceio — SDN-Based Multiplayer Racing Network

Raceio is a simplified multiplayer racing game designed to demonstrate
real-time network communication using UDP sockets and Software-Defined
Networking (SDN).

The project simulates multiple players communicating with a central game
server through a programmable network. SDN is used to identify and prioritize
game traffic, while network performance is evaluated using latency, jitter,
packet loss, and throughput measurements.

---

## Project Overview

In a multiplayer racing game, player state information such as position,
speed, and movement needs to be exchanged frequently and with low delay.

Raceio focuses on the networking aspect of multiplayer gaming rather than
complex game graphics.

Each player periodically sends their current game state to the server using
UDP. The server processes the received states and distributes the relevant
information to the connected players.

An SDN controller manages the network and applies traffic-handling rules
for game traffic.

### Main Objectives

- Implement real-time UDP game-state communication
- Support multiple players communicating with a game server
- Use sequence numbers to identify missing or outdated packets
- Handle packet loss in real-time communication
- Use SDN to prioritize game traffic
- Deploy the communication system using Mininet
- Measure network latency and jitter
- Measure packet loss and throughput
- Compare network performance under different traffic conditions
