import evdev
import time
import subprocess

TARGET_NAME = "BLE-M3 UNKNOWN"
AXIS_X = 53
AXIS_Y = 54

def find_device_by_name(target_name):
    '''
    Select the device with specified name device from the device list.
    '''
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == target_name:
            return device
    return None

def run_wtype(key_name: str):
    '''
    Simulates a keypress usint the 'wtype' Linux command.

    Args:
        key_name (str): The name of the key to press (e.g., 'Page_Down', 'space').

    Raises:
        Exception: If the wtype command fails or is not installed.S
    '''
    try:
        if "+" in key_name:
            keys = key_name.split("+")
            modifier = keys[0]
            key = keys[1]
            subprocess.run(["wtype", "-M", modifier, "-k", key], check=True)
        else:
            subprocess.run(["wtype", "-k", key_name], check=True)
    except Exception as err:
        raise Exception (f"Error executing wtype: {err}")

def is_increasing(values):
    '''
    Check if the numbers are in ascending order.
    '''
    count = 0
    for i in range(1, len(values)):
        if (values[i] > values[i-1]):
            count += 1
    if count >= len(values) / 2:
        return True
    return False


def is_declining(values):
    '''
    Check if the numbers are in descending order.
    '''
    count = 0
    for i in range(1, len(values)):
        if (values[i] < values[i-1]):
            count += 1
    if count >= len(values) / 2:
        return True
    return False


def decode_event(current_batch: list, code: int, previous_button: str):
    '''
    Args:
        current_batch: list of event
        code: which axis send
        previous_button: The previously pressed button, if there is no new action

    Returns:
        tuple: A tupple formatted as (action_name, empty_list, reset_code)
    '''
    values: list[int] = [event.value for event in current_batch]
    if len(current_batch) > 0:
        if len(values) > 2:
            if code == AXIS_Y:
                if is_increasing(values):
                    return "UP", [], 0
                elif is_declining(values):
                    return "DOWN", [], 0
            elif code == AXIS_X:
                if is_increasing(values):
                    return "LEFT", [], 0
                elif is_declining(values):
                    return "RIGHT", [], 0
        elif len(values) == 2 or len(values) == 1:
            # the shutter sends these codes when I press the middle or bottom button
            if 828 in values:
                return "BOTTOM", [], 0
            if 300 in values or 501 in values:
                return "MIDDLE", [], 0
    else:
        return previous_button, [], 0

def send_key_to_zathura(key_name):
    match key_name:
        case "UP":
            run_wtype("shift+space")
        case "DOWN":
            run_wtype("space")

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
                        pressed_button, current_batch, code = decode_event(current_batch, code, pressed_button)
                        print(pressed_button)
                        send_key_to_zathura(pressed_button)
                    
        except OSError:
            print("The device is disconnected")
            time.sleep(3)
        except Exception as error:
            print(f"An unexpected error has occured: {error}")
            time.sleep(3)


if __name__ == "__main__":
    main()