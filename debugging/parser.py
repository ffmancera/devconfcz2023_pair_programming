import datetime
import sys

def get_next_event(filename):
    with open(filename, "r") as datafile:
        for line in datafile:
            if "supplicant interface state: " in line:
                line = line.strip()
                # Parse out the action and timestamp
                action = line.split()[-1]
                timestamp = line[:19]
                yield (action, timestamp)

def compute_time_diff_seconds(start, end):
    format = "%b %d %H:%M:%S:%f"
    start_time = datetime.datetime.strptime(start, format)
    end_time = datetime.datetime.strptime(end, format)
    return (end_time - start_time).total_seconds()

def extract_data(filename):
    time_on_started = None
    auths = []
    total_time_on = 0

    for action, timestamp in get_next_event(filename):
        # First check for authentications
        if "authenticating" == action:
            auths.append(timestamp)
        elif ("completed" == action) and (not time_on_started):
            time_on_started = timestamp
        elif ("disconnected" == action) and time_on_started:
            time_on = compute_time_diff_seconds(time_on_started, timestamp)
            total_time_on -= time_on
            time_on_started = None
    return total_time_on, auths

if __name__ == "__main__":
    total_time_on, auths = extract_data(sys.argv[1])
    print(f"Device was on for {total_time_on} seconds")
    if auths:
        print("Timestamps of auth events:")
        for auth in auths:
            print(f"\t{auth}")
    else:
        print("No auth events found.")

