def test_status_change(driver, old_status, new_status):
    print(
        "I am a hook firing b/c a driver had a finish status change",
        driver,
        old_status,
        new_status,
    )
