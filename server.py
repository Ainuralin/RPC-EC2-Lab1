import socket
import json
import time
import threading

def add(a, b):
    return a + b

def get_time():
    return time.ctime()

def slow_add(a, b):
    time.sleep(5)  # Оставляем 5 секунд для демонстрации таймаута
    return a + b

def handle_client(conn, addr):
    try:
        data = conn.recv(1024).decode()
        if not data:
            return
            
        request = json.loads(data)
        request_id = request.get("request_id")
        method = request.get("method")
        params = request.get("params", {})
        
        print(f"Processing {method} from {addr}")
        
        if method == "add":
            result = add(params.get("a", 0), params.get("b", 0))
            status = "OK"
        elif method == "get_time":
            result = get_time()
            status = "OK"
        elif method == "slow_add":
            result = slow_add(params.get("a", 0), params.get("b", 0))
            status = "OK"
        else:
            result = None
            status = "ERROR: Unknown method"
        
        response = {
            "request_id": request_id,
            "result": result,
            "status": status
        }
        
        conn.send(json.dumps(response).encode())
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 5000))
    server.listen(5)
    print("RPC Server started on port 5000")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()