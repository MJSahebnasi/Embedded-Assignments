import enum
import threading
import time


class State(enum.Enum):
    S1 = 1
    S2 = 2
    S3 = 3
    OUT = 4


heater = False
cooler = False
cooler_round_per_sec = 0

crnt_state = State.S1  # marked as default/initial
next_state = None

superstate_crnt_state = None
superstate_next_state = None

T_lock = None  # for both T and T_modified
T = 25  # temperature
T_modified = False

terminate_program = False


class AirConditioner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    @staticmethod
    def wait_for_event():
        global T_modified

        event_happened = False

        while not event_happened:
            time.sleep(0.1)
            T_lock.acquire()
            event_happened = T_modified
            T_modified = False
            T_lock.release()

        return event_happened

    def run(self):
        global heater, cooler, T, next_state, crnt_state, superstate_crnt_state, superstate_next_state

        while not terminate_program:
            if crnt_state == State.S1:
                heater = False
                cooler = False
                event_happened = self.wait_for_event()
                if event_happened:
                    if T < 15:
                        next_state = State.S3
                    elif T > 35:
                        next_state = State.S2
                    else:
                        continue

            elif crnt_state == State.S2:
                global cooler_round_per_sec

                heater = False
                cooler = True
                superstate_crnt_state = State.S1
                cooler_round_per_sec = 4

                while not superstate_crnt_state == State.OUT:
                    if superstate_crnt_state == State.S1:
                        cooler_round_per_sec = 4

                        print('super node (S2) state:', superstate_crnt_state, '- RPS:', cooler_round_per_sec)

                        event_happened = self.wait_for_event()
                        if event_happened:
                            if T < 25:
                                superstate_next_state = State.OUT
                            elif T > 40:
                                superstate_next_state = State.S2
                            else:
                                continue
                    elif superstate_crnt_state == State.S2:
                        cooler_round_per_sec = 6

                        print('super node (S2) state:', superstate_crnt_state, '- RPS:', cooler_round_per_sec)

                        event_happened = self.wait_for_event()
                        if event_happened:
                            if T < 35:
                                superstate_next_state = State.S1
                            elif T > 45:
                                superstate_next_state = State.S3
                            else:
                                continue
                    elif superstate_crnt_state == State.S3:
                        cooler_round_per_sec = 8

                        print('super node (S2) state:', superstate_crnt_state, '- RPS:', cooler_round_per_sec)

                        event_happened = self.wait_for_event()
                        if event_happened:
                            if T < 40:
                                superstate_next_state = State.S2
                            else:
                                continue

                    superstate_crnt_state = superstate_next_state

                # state == OUT:
                if T < 25:
                    next_state = State.S1

            elif crnt_state == State.S3:
                heater = True
                cooler = False
                event_happened = self.wait_for_event()
                if event_happened:
                    if T > 30:
                        next_state = State.S1
                    else:
                        continue

            crnt_state = next_state
            print('T:', T, '- State:', crnt_state)
        return T


class UserInput(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global terminate_program
        global T
        global T_modified

        while not terminate_program:
            user_input = int(input(' -> enter an int as a new value for T (-1 to terminate the program): '))
            if user_input == -1:
                terminate_program = True
            else:
                T_lock.acquire()
                T = user_input
                T_modified = True
                T_lock.release()
            time.sleep(2)


if __name__ == '__main__':
    print('initial T:', str(T), '- initial state:', crnt_state)

    T_lock = threading.Lock()

    user_input_thread = UserInput()
    air_conditioner_thread = AirConditioner()

    user_input_thread.start()
    air_conditioner_thread.start()
