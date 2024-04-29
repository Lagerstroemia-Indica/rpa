import pyautogui
import time
from datetime import datetime, timedelta
import random

# I want to only click at last mouse position.
# interval 30seconds
time_interval = 30
format_time_reg = "%Y-%m-%d %H:%M:%S"


def click_event():
    pyautogui.click(button="left")
    time.sleep(1)

def double_click_event():
    pyautogui.doubleClick(button="left")
    time.sleep(1)


if __name__ == "__main__":
    start_time = datetime.now()
    start_time_str = start_time.strftime(format_time_reg)

    click_event_time = start_time + timedelta(seconds=time_interval)
    click_event_time_str = click_event_time.strftime(format_time_reg)
    # print(f"click event time:${click_event_time_str}")
    print(f"start time:{start_time_str} >>> next click event time:{click_event_time_str}")

    # infinity click event
    while (True):
        current_time = datetime.now()

        if (current_time >= click_event_time):
            click_event()
            
            click_event_time = current_time + timedelta(seconds=time_interval)
            click_event_time_str = click_event_time.strftime(format_time_reg)

            print(f' - click event! >>> next click event time:{click_event_time_str}')
        else:
            current_time_str = current_time.strftime(format_time_reg)
            print(f'\r{current_time_str}', end='', flush=True)

        time.sleep(1)

