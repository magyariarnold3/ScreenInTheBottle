import evdev
import time

TARGET_NAME = "BLE-M3 UNKNOWN"

def find_device_by_name(target_name):
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == target_name:
            return device
    return None

def is_increasing(values):
    count = 0
    for i in range(1, len(values)):
        if (values[i] > values[i-1]):
            count += 1
    if count >= len(values) / 2:
        return True
    return False

def is_declining(values):
    count = 0
    for i in range(1, len(values)):
        if (values[i] < values[i-1]):
            count += 1
    if count >= len(values) / 2:
        return True
    return False

def decode_event(events, code):
    values: list[int] = [event.value for event in events]
    print(f"Values: {values}")
    if code == 54:
        if is_increasing(values):
            print("Up")
        elif is_declining(values):
            print("Down")
    elif code == 53:
        if is_increasing(values):
            print("Left")
        elif is_declining(values):
            print("Right")
    elif code == 57:
        print("Bottom Button Pressed")

def main():
    device = None
    while device is None:
        device = find_device_by_name(TARGET_NAME)
        if device is None:
            print(f"Device '{TARGET_NAME}' not found. Please connect the device and press Enter to retry.")
            time.sleep(1)

    current_batch: list = []
    code = 0
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_ABS:
            # print(f"Code: {event.code} - {event.value}")
            if event.code in [53, 54]:
                code = event.code
                current_batch.append(event)
            elif event.code == 57 and event.value == -1:
                if len(current_batch) > 0:
                    decode_event(current_batch, code)
                    current_batch = []
                    code = 0

if __name__ == "__main__":
    main()

