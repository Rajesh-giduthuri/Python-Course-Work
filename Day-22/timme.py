#seconds
import time
print("Hi.....")
time.sleep(5)
print("Hello.....")


#hours minutes seconds
import IPython
from IPython.display import clear_output
seconds=0
minutes=0
hours=0
while True:
    print(f"{hours}:{minutes}:{seconds}")
    time.sleep(1)
    seconds+=1
    if seconds==60:
        minutes+=1
        seconds=0
        if minutes==60:
            print("taki tike....1 minute alarm completed")
            break
            hours+=1
            minutes=0
    clear_output(wait=True)

print(f"{hours}:{minutes}:{seconds}")         


#hours minutes seconds
import time

seconds = 0
minutes = 0
hours = 0

while True:
    print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)

    time.sleep(1)

    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1

        if minutes == 1:
            print("\nTaki tike auu....... 1 minute alarm completed")
            break