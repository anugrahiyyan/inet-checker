import subprocess
import re
import time
from plyer import notification


# This program was made by Galbatorix
# This tools is free to use. 

downtime_count = 0


def get_ping_time():
    try:
        output = subprocess.check_output(["ping", "-n", "1", "google.com"], universal_newlines=True)
        match = re.search(r"Average = (\d+)ms", output)
        if match:
            avg_ping = match.group(1)
            return float(avg_ping)
    except subprocess.CalledProcessError:
        return None

def send_notification(message):
    notification.notify(
        title="Internet Status",
        message=message,
        app_name="Internet Checker",
    )

if __name__ == "__main__":
    while True:
        ping_time = get_ping_time()
        if ping_time is not None:
            print(f"Internet aman jaya boss. Ping: {ping_time} ms. GAJI MASIH AMAN WKWK >.<, <<---OK--->>>")
            if ping_time > 200:
                send_notification(f"MAMPUS PANIKK HIYAHIYAHIYA, PING TELKOM INDIHOMO : {ping_time} ms")
                downtime_count += 1
                print(f"Downtime count: {downtime_count}")
            else:
                downtime_count += 1  # Reset downtime count
        else:
            print("INTERNET MODARRRR. MAMMPUSSSSS GA GAJIAN AKWOAKWOAKOAK, ========> Sending to system alert...")
            send_notification("INTERNET E MODAR BOSSS, MAMMPUSSSSS GA GAJIAN AKWOAKWOAKOAK.")
            downtime_count += 1
            print(f"Downtime count: {downtime_count}")
        
        # Wait for 1 second before checking again
        time.sleep(1)
