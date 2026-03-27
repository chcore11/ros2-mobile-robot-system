import time
import serial

PORT = "COM3"
BAUDRATE = 115200

def main():
    ser = None
    try:
        ser = serial.Serial(PORT, BAUDRATE, timeout=1)
        time.sleep(2)  # 等 Arduino 串口稳定
        print(f"[INFO] Serial connected: {PORT} @ {BAUDRATE}")

        commands = ["forward", "left", "right", "stop", "test"]

        for cmd in commands:
            message = cmd + "\n"
            ser.write(message.encode("utf-8"))
            print(f"[SEND] {cmd}")
            time.sleep(0.5)

            reply = ser.readline().decode("utf-8", errors="ignore").strip()
            if reply:
                print(f"[RECV] {reply}")
            else:
                print("[RECV] <no response>")

            time.sleep(1.0)

    except serial.SerialException as e:
        print(f"[ERROR] Serial failed: {e}")

    finally:
        if ser is not None and ser.is_open:
            ser.close()
            print("[INFO] Serial closed")

if __name__ == "__main__":
    main()