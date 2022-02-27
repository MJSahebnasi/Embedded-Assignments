import enum
import threading
import time

import matplotlib.pyplot as plt


class State(enum.Enum):
    S1 = 1
    S2 = 2
    S3 = 3


heater = False
cooler = False
cooler_round_per_sec = 0

crnt_state = State.S1
next_state = None

supernode_crnt_state = None  # todo
supernode_next_state = None

T_lock = None  # for both T and T_modified
T = 25  # temperature
T_modified = False

terminate_program = False


class AirConditioner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not terminate_program:
            if crnt_state == State.S1:
                # todo
                return
            elif crnt_state == State.S2:
                return
            elif crnt_state == State.S3:
                return
        return T


class UserInput(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global terminate_program
        global T
        global T_modified

        while not terminate_program:
            time.sleep(2)
            user_input = int(input(' -> enter an int as a new value for T (-1 to terminate the program): '))
            print(user_input)
            if user_input == -1:
                terminate_program = True
            else:
                T_lock.acquire()
                T = user_input
                T_modified = True
                T_lock.release()


if __name__ == '__main__':
    print('the initial T: ' + str(T))

    T_lock = threading.Lock()

    user_input_thread = UserInput()
    air_conditioner_thread = AirConditioner()

    user_input_thread.start()
    air_conditioner_thread.start()
