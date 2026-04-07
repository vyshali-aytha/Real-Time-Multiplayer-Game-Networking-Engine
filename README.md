# Real-Time Multiplayer System using UDP and SSL

## Overview
This project is a simple real-time multiplayer system built using Python. It allows multiple clients to connect to a server and move within a shared space while seeing each other’s positions update in real time.
The main communication is done using UDP for speed and low latency. A separate module using SSL/TLS over TCP is included to demonstrate secure communication.

## What the Project Does
- Multiple clients can connect to a server
- Each client can move using keyboard input (W, A, S, D)
- The server keeps track of all players and updates everyone
- All clients see the same positions in real time
- Latency and jitter are displayed on the client side
- A secure connection is demonstrated using SSL/TLS

## Technologies Used
- Python
- Socket Programming
- Pygame
- SSL/TLS

## Setup

1. Install required library:
   pip install pygame

2. Make sure all files are in place:
server_udp.py
client_udp.py
server_ssl.py
client_ssl.py
cert.pem
key.pem

## How to Run
### Running on a Single System

1. Start the UDP server:
python server_udp.py

2. Open two terminals and run the client:
python client_udp.py

### Running on Two Systems

1. Connect both systems to the same network
   
2. On the server system, find the IP address using:
ipconfig

2. In `client_udp.py`, update:
server_ip = "YOUR_SERVER_IP"

4. Run the server on one system and the client on the other

### Running the Security Module

1. Start the secure server:
python server_ssl.py

2. Start the secure client:
python client_ssl.py

## Controls
- W: Move up  
- A: Move left  
- S: Move down  
- D: Move right

## Output
- Player positions update in real time
- Multiple clients remain synchronized
- Latency and jitter values are displayed
- Secure connection is established using SSL/TLS

## Security
The project uses SSL/TLS with a self-signed certificate to encrypt communication between the client and server.

## Conclusion
This project demonstrates core networking concepts such as real-time communication using UDP and secure communication using SSL/TLS. The focus is on networking performance and synchronization rather than advanced user interface design.
