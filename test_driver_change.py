def test_driver_change(oldCars, newCars):
    old_drivers = list(map(lambda x: x["driverName"], oldCars))
    new_drivers = list(map(lambda x: x["driverName"], newCars))
    print("I am a hook firing on driver count changes", old_drivers, new_drivers)
