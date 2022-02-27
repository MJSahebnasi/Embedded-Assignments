import enum
import matplotlib.pyplot as plt


class State(enum.Enum):
    S1 = 1
    S2 = 2
    S3 = 3

heater = False
cooler = False
round_per_sec = 0

crnt_state = State.S1
next_state = None

supernode_crnt_state = None  # todo
supernode_next_state = None

time = 0
T = 25  # temperature

# each of these values will be assigned to <T> at the corresponding time
T_manual_change_values = [13, 28, 40, 26, 12, 32, 14, 40, 42]
T_manual_change_times = [3, 8, 13, 19, 24, 30, 36, 41, 47]

# T values will be stored here
T_history = []


def air_conditioner(T):
    match crnt_state:
        case
    return T


def draw_chart(T_history):
    # TODO
    fig, ax = plt.subplots()
    ax.scatter(range(len(T_history)), T_history)
    # plt.plot(range(len(T_history)), T_history, '--o')
    # ax.annotate('txt', (1, T_history[1]))
    ax.annotate("X",
                xy=(1, T_history[1]), xycoords='data',
                xytext=(1, T_history[1] + 3), textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=0.",
                                ),
                )
    plt.show()


if __name__ == '__main__':
    global time
    max_time = 50

    

# for time in range(max_time + 1):
#
#     if time in T_manual_change_times:
#         # applying manual changes to test the air_conditioner:
#         T = T_manual_change_values[T_manual_change_times.index(time)]
#     else:
#         T = air_conditioner(T)
#         # I've separated these parts so that the changes would be vividly visible
#
#     T_history.append(T)

# draw_chart(T_history)

## draw_chart(T_manual_changes)


