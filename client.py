import socket
import json
import uuid
import time

SERVER_IP = "98.94.90.27"
PORT = 5000

def test_rpc():
    print("=== RPC Client Tests ===")
    
    # Test 1: Normal call
    print("\n1. Testing add(5, 7):")
    call_rpc("add", {"a": 5, "b": 7})
    
    # Test 2: Get time
    print("\n2. Testing get_time():")
    call_rpc("get_time", {})
    
    # Test 3: Slow function (will show retries)
    print("\n3. Testing slow_add(3, 4) [5 second delay]:")
    print("   This will timeout and retry 3 times")
    call_rpc("slow_add", {"a": 3, "b": 4})
    
    # Test 4: Unknown method
    print("\n4. Testing unknown method:")
    call_rpc("unknown", {"x": 1})

def call_rpc(method, params, timeout=2, max_retries=3):
    request_id = str(uuid.uuid4())
    request = {
        "request_id": request_id,
        "method": method,
        "params": params
    }
    
    for attempt in range(max_retries):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((SERVER_IP, PORT))
            
            sock.send(json.dumps(request).encode())
            
            response_data = sock.recv(1024).decode()
            response = json.loads(response_data)
            
            if response["status"] == "OK":
                print(f"   Success: {response['result']}")
                return response["result"]
            else:
                print(f"   Error: {response['status']}")
                return None
                
        except socket.timeout:
            print(f"   Attempt {attempt+1}: Timeout after {timeout}s")
            if attempt < max_retries - 1:
                time.sleep(1)
        except Exception as e:
            print(f"   Attempt {attempt+1}: Error - {e}")
            if attempt < max_retries - 1:
                time.sleep(1)
        finally:
            try:
                sock.close()
            except:
                pass
    
    print(f"   Failed after {max_retries} attempts")

if __name__ == "__main__":
    test_rpc()