import time
import serial

PORT = "COM3"
BAUDRATE = 115200
INTERVAL = 1.0

def main():
    ser = None
    try:
        ser = serial.Serial(PORT, BAUDRATE, timeout=1)
        print(f"[INFO] Serial connected: {PORT} @ {BAUDRATE}")

        while True:
            message = "hello robot\n"
            ser.write(message.encode("utf-8"))
            print(f"[SEND] {message.strip()}")
            time.sleep(INTERVAL)

    except serial.SerialException as e:
        print(f"[ERROR] Serial exception: {e}")

    except KeyboardInterrupt:
        print("\n[INFO] Stopped by user.")

    finally:
        if ser is not None and ser.is_open:
            ser.close()
        print("[INFO] Serial port closed.")

if __name__ == "__main__":
    main()