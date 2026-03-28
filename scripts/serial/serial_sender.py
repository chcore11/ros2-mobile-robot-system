import serial
import time

PORT = "COM3"
BAUDRATE = 115200

def main():
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    time.sleep(2)

    print("Control with WASD keys, q to quit")

    while True:
        cmd = input(">>> ").strip().lower()

        if cmd == "q":
            break

        if cmd == "w":
            msg = "forward\n"
        elif cmd == "s":
            msg = "back\n"
        elif cmd == "a":
            msg = "left\n"
        elif cmd == "d":
            msg = "right\n"
        else:
            print("Invalid key")
            continue

        ser.write(msg.encode("utf-8"))
        print(f"[SEND] {msg.strip()}")

        reply = ser.readline().decode().strip()
        if reply:
            print(f"[RECV] {reply}")

    ser.close()

if __name__ == "__main__":
    main()