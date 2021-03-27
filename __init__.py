from hooks.test_driver_change import test_driver_change
from hooks.test_penalty_change import test_penalty_change
from hooks.test_on_session_change import test_on_session_change
from hooks.test_status_change import test_status_change
from hooks.test_pit_status_change import test_pit_status_change
from hooks.test_low_speed import test_low_speed
from hooks.test_on_flag_change import test_on_flag_change

HOOKS = {}


def register(event, hooks, func):
    if event not in hooks:
        hooks[event] = []
    hooks[event].append(func)
    print("Registered hook {} for event {}".format(func.__name__, event))


register("onCarCountChange", HOOKS, test_driver_change)
register("onDriverPenaltyChange", HOOKS, test_penalty_change)
register("onSessionChange", HOOKS, test_on_session_change)
register("onFinishStatusChange", HOOKS, test_status_change)
register("onPitStateChange", HOOKS, test_pit_status_change)
register("onLowSpeed", HOOKS, test_low_speed)
register("onShownFlagChange", HOOKS, test_on_flag_change)