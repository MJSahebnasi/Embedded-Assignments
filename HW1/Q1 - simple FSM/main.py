import enum


class State(enum.Enum):
    S1 = 1
    S2 = 2
    S3 = 3


round_per_sec = 0

crnt_state = State.S1
next_state = None

supernode_crnt_state = None  # todo
supernode_next_state = None

# T values will be stored here
T_history = []

change_step = 5
# each of these values will be assigned to <time> every <change_step> second
T_manual_changes = [13, 28, 40, 26, 12, 32, 14, 40, 42]

time = 0
T = 25  # tempratuer


def air_conditioner(T):
    # tODO
    return T


def draw_chart(T_history):
    # TODO
    return None


if __name__ == '__main__':
    global time
    max_time = 50

    for time in range(max_time + 1):

        if time % change_step == 0:
            # applying manual changes to test the air_conditioner:
            T = T_manual_changes[time / change_step]
        else:
            T = air_conditioner(T)
            # I've separated these parts so that the changes would be vividly visible

        T_history.append(T)

    draw_chart(T_history)
