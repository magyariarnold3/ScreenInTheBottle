import subprocess
import time

def run_wtype(key_name: str):
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
  

def main():
    time.sleep(3)
    run_wtype("shift+space")

    time.sleep(3)
    run_wtype("space")


if __name__ == "__main__":
    main()