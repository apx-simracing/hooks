from rf2.interaction import chat
from reciever import get_server_config


def test_driver_change(oldCars, newCars):
    old_drivers = list(map(lambda x: x["driverName"], oldCars))
    new_drivers = list(map(lambda x: x["driverName"], newCars))

    new_drivers_diff = []

    for driver in new_drivers:
        if not driver in old_drivers:
            new_drivers_diff.append(driver)

    for driver in new_drivers_diff:
        print("Sending a welcome message to {}".format(driver))
        chat(get_server_config(), "/whisper {} Foo".format(driver))
