def test_pit_status_change(driver, old_status, new_status):
    print(
        "I am a hook firing b/c a driver had a pit status change",
        driver,
        old_status,
        new_status,
    )
