import time
import requests
import threading

def monitor(url, interval, bot_name):
    while True:
        try:
            response = requests.get(url, timeout=10)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{bot_name}] {url} → {response.status_code}")
        except Exception as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{bot_name}] Error: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    # Start thread for clientbot21.php (every 4 sec)
    threading.Thread(target=monitor, args=("https://zihadbd.shop/clientbot21.php", 4, "jimkar bot"), daemon=True).start()

    # Start thread for talhanc.php (every 3 sec)
    threading.Thread(target=monitor, args=("https://zihadbd.shop/talhannc.php", 1, "talhan bot"), daemon=True).start()

    # Keep main thread alive (0.5 sec sleep)
    while True:
        time.sleep(0.5)
