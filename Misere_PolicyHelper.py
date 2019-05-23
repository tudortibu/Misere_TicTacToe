# general policy helper functions

import numpy as np
import random
#from environment import initialize_environment, perform_action

epsilon = 0
action_list = []


def initialize_policy_helper(e, actions):
    global epsilon, action_list

    epsilon = e
    action_list = actions
    return

#not correct action update for game
# finds optimal policy with the given Q array
def find_optimal_policy(q):
    policy = ['']*len(q)
    actions = ['U', 'D', 'L', 'R']

    for state in range(0, len(q)):
        a = greedy_action(q, state)
        policy[state] = actions[a]

    policy[9] = 'E'

    return policy


def pick_e_greedy_action(q, state):

    # picks 0 - greedy, or 1 - explore with the odds determined by epsilon
    action = np.random.choice([0, 1], 1, False, [1-epsilon, epsilon])

    if action == 0:
        return greedy_action(q, state)
    else:
        return explore_action()


def greedy_action(q, state):
    max_value = max(q[state])

    for action in range(0, len(q[state])):
        if q[state][action] == max_value:
            return action


def explore_action():
    # since all states have the same actions, we can just pick from the action list
    return np.random.choice(action_list)


