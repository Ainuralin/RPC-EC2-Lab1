# Lab 1 - Remote Procedure Call (RPC) Implementation & Deployment on AWS EC2
**Distributed Computing — Trimester 8**

## 📋 Overview
This project implements a minimal RPC (Remote Procedure Call) system with client-server architecture deployed on AWS EC2 instances. The system demonstrates core RPC concepts including marshalling, timeout handling, retry logic, and failure semantics.

## 🏗️ Architecture
- **Client Node**: Sends RPC requests with timeout and retry mechanisms
- **Server Node**: Listens for requests, executes functions, returns results
- **Communication**: TCP sockets with JSON serialization
- **Deployment**: Two separate AWS EC2 instances (Ubuntu 22.04)

## 📁 Files
- `server.py` - RPC server implementation
- `client.py` - RPC client with retry logic
- `requirements.txt` - Python dependencies (none required, uses standard library)

## 🚀 Quick Start

### 1. Prerequisites
- Two AWS EC2 instances (Ubuntu 22.04 recommended)
- Python 3.8 or higher
- Open port 5000 in Security Group inbound rules

### 2. Setup on Both Instances
```bash
sudo apt update
sudo apt install python3 -y
```

### 3. Connect to Your Instances
For server (replace with your server IP):
```bash
ssh -i your-key.pem ubuntu@YOUR_SERVER_IP
```
For client (replace with your client IP):
```bash
ssh -i your-key.pem ubuntu@YOUR_CLIENT_IP
```
### 4. How to Run
1. On server EC2: `python3 server.py`
2. On client EC2: `python3 client.py`
```
| Method   | Description                       | Example Parameters |
| -------- | --------------------------------- | ------------------ |
| add      | Add two numbers                   | {"a": 5, "b": 7}   |
| get_time | Return server timestamp           | {}                 |
| slow_add | Add numbers with artificial delay | {"a": 3, "b": 4}   |
| unknown  | Any other string                  | {}                 |
```

## Features Demonstrated
- JSON marshalling
- Timeout handling (2 seconds)
- Retry logic (3 attempts)
- At-least-once semantics
