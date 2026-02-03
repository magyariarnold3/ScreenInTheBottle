import evdev
from evdev import InputDevice, categorize, ecodes

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

print("Available input devices:")
print("------------------------")
for i, device in enumerate(devices):
    print(f"{i}: {device.path} - {device.name} - {device.phys}")

try:
    device_index = int(input("Select a device by entering its index: "))
    selected_device = devices[device_index]
except:
    print("Invalid selection.")
    exit(1)

print(f"\nPush the buttons on the selected device ({selected_device.name}). Press Ctrl+C to exit.\n")

try:
    for event in selected_device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == key_event.key_down:
                print(f"Key pressed: {key_event.keycode}")
            elif key_event.keystate == key_event.key_up:
                print(f"Key released: {key_event.keycode}")
except KeyboardInterrupt:
    print("\nExiting...")
except OSError:
    print("Device disconnected. Exiting...")