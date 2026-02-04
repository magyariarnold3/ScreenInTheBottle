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


def decode_event_four_button(values, code, previous_button):
    #print(f"Values: {values}"
    if len(values) > 2:
        if code == 54:
            if is_increasing(values):
                return "Up"
            elif is_declining(values):
                return "Down"
        elif code == 53:
            if is_increasing(values):
                return "Left"
            elif is_declining(values):
                return "Right"
    elif len(values) == 2 or len(values) == 1:
        if 828 in values:
            return "Bottom Button"
        if 300 in values or 501 in values:
            return "Middle Button"
    else:
        return previous_button


def main():
    while True:
        try:
            device = None
            while device is None:
                device = find_device_by_name(TARGET_NAME)
                if device is None:
                    print(f"Device '{TARGET_NAME}' not found. Please connect the device and press Enter to retry.")
                    time.sleep(1)

            current_batch: list = []
            code = 0
            previous_button = ""
            pressed_button = ""
            for event in device.read_loop():
                # must use EV_ABS(type = 3) to filter other codes
                if event.type == evdev.ecodes.EV_ABS:
                    # print(f"Code: {event.code} - {event.value}")
                    if event.code in [53, 54]:
                        code = event.code
                        current_batch.append(event)

                    # if sending the end command, which has code = 57 and value = -1
                    if event.code == 57 and event.value == -1:
                        values: list[int] = [event.value for event in current_batch]
                        if len(current_batch) > 0:
                            pressed_button = decode_event_four_button(values, code, previous_button)
                            previous_button = pressed_button
                            print(pressed_button)
                            current_batch = []
                            code = 0
                        else:
                            print(previous_button)
        except OSError:
            print("The device is disconnected")
            time.sleep(3)
        except Exception as error:
            print(f"An unexpected error has occured: {error}")
            time.sleep(3)


if __name__ == "__main__":
    main()