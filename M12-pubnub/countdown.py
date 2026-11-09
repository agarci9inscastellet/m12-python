import threading
import time


def countdown(seconds, stop_event):
    for i in range(seconds, 0, -1):
        if stop_event.is_set():
            return
        #print(f"\rTime left: {i:2d} seconds", end="", flush=True)
        time.sleep(1)
    print("\n⏰ Time's up!")

def get_user_input(stop_event, result):
    word = input("\nEnter a word: ")
    result.append(word)   # store the word
    stop_event.set()      # stop the countdown

def main():
    stop_event = threading.Event()
    user_input = []

    timer_thread = threading.Thread(target=countdown, args=(10, stop_event))
    input_thread = threading.Thread(target=get_user_input, args=(stop_event, user_input))

    timer_thread.start()
    input_thread.start()

    input_thread.join()
    stop_event.set()
    timer_thread.join()

    if user_input:
        print(f"\nYou entered: {user_input[0]}")
    else:
        print("\nNo input received.")

if __name__ == "__main__":
    main()