import pyautogui
import time
from datetime import datetime, timedelta
from pynput import keyboard
import random
import threading

# I want to only click at last mouse position.
# interval 30seconds
# time_interval = 30 : 'event'가 발생하는 주기 설정
time_interval_input = input('input auto mouse click event interval time(min:10 seconds):').strip()
time_interval = int(time_interval_input) if time_interval_input else 10

while (True):
    if (time_interval < 10):
        time_interval = int(input('input auto mouse click event interval time(min:10 seconds):'))
    else:
        break

pressed_keyboard_event = False

format_time_reg = "%Y-%m-%d %H:%M:%S"

# mouse click event
def click_event():
    pyautogui.click(button="left")
    time.sleep(1)

def double_click_event():
    pyautogui.doubleClick(button="left")
    time.sleep(1)

# keyboard pressed event
def pressed_event(key):
    global pressed_keyboard_event

    try:
        if key == keyboard.Key.enter or key == keyboard.Key.space:
            print()
            print(f'{key.name} event. have good day!')
            pressed_keyboard_event = True
    except ArithmeticError:
        pass


if __name__ == "__main__":
    start_time = datetime.now()
    start_time_str = start_time.strftime(format_time_reg)

    click_event_time = start_time + timedelta(seconds=time_interval)
    click_event_time_str = click_event_time.strftime(format_time_reg)
    # print(f"click event time:${click_event_time_str}")
    print(f"start time:{start_time_str} >>> next click event time:{click_event_time_str}")

    # observe keyboard event
    keyboard_listener = keyboard.Listener(on_press=pressed_event)
    keyboard_thread = threading.Thread(target=keyboard_listener.start)
    keyboard_thread.start()

    # infinity click event
    while (True):
        if pressed_keyboard_event == True:
            keyboard_listener.stop()
            keyboard_thread.join()
            break

        # current_time에 현재시간 기입
        current_time = datetime.now()

        # 현재시간과 클릭한 시간 비교
        if (current_time >= click_event_time):
            # 클릭한 시간이 현재 시간 이전이면 '마우스 좌클릭' 이벤트 발생
            click_event()
            
            # 클릭한 이벤트 시간을 문자화 - 콘솔에 표시해주기 위함
            click_event_time = current_time + timedelta(seconds=time_interval)
            click_event_time_str = click_event_time.strftime(format_time_reg)

            print(f' - click event! >>> next click event time:{click_event_time_str}')
        else:
            current_time_str = current_time.strftime(format_time_reg)
            print(f'\r{current_time_str}', end='', flush=True)

        time.sleep(1)