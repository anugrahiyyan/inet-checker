import subprocess
import re
import time
import datetime
from plyer import notification
import requests

# This program was made by Galbatorix
# This tools is free to use.

downtime_count = 0

def get_ping_time():
    try:
        output = subprocess.check_output(["ping", "-n", "1", "google.com"], universal_newlines=True)
        reply_lines = [line for line in output.splitlines() if line.startswith("Reply from")]
        if reply_lines:
            ip_address = reply_lines[0].split()[2].strip("[]")
            match = re.search(r"Average = (\d+)ms", output)
            if match:
                avg_ping = float(match.group(1))
                return avg_ping, ip_address
            else:
                print("Ping failed. Could not find 'Average =...' in output.")
                return None, None
        else:
            print("Ping failed. No replies received.")
            return None, None

    except subprocess.CalledProcessError as e:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"[{current_time}] Error detected: Please Check the Main Cable or Hub!!")
        return None, None

def send_notification(message, current_time=None):
    if current_time is None:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    full_message = f"{current_time} | {message}"
    notification.notify(
        title="GBtrX Corp | Internet Status Checker",
        message=full_message,
        app_name="Internet Checker - @GBtrX Corp.",
    )

if __name__ == "__main__":
    while True:
        ping_time, ip_address = get_ping_time()
        if ping_time is not None:
            if ping_time > 990:
                current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                send_notification(f"Damn Motherfucker! Look at this shit : {ping_time} ms WTF || <<---Critical--->> ||")
                downtime_count += 1
                print(f"[{current_time}] Count: {downtime_count} | Ping : {ping_time} ms | <<---Warning--->> | ==========> Sending to system alert...")
            elif ping_time > 550:
                current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                send_notification(f"Hey Dude! Your ping is a bit high: {ping_time} ms       <<---Warning--->>")
                downtime_count += 1
                print(f"[{current_time}] Count: {downtime_count} | Ping : {ping_time} ms | <<---Warning--->> | ==========> Sending to system alert...")
            else:
                downtime_count = 0
                current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"[{current_time}] Connected to --> {ip_address} {ping_time} ms | Should we sleep yet ? || <<---Good--->> ||")
        else:
            current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            downtime_count += 1
            print(f"[{current_time}] Downtime count: {downtime_count} | WHAT THE FUCK, Look at your INTERNET dude. It's Totally Shutdown || <<---Critical--->> || ==========> Sending to system alert...")
            send_notification("RED CODE : INTERNET HAS BEEN SHUTDOWN. CHECK REQUIRED !!")

        time.sleep(5 if ping_time is None else 1)
