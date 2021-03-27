def test_on_flag_change(driver, old_flag, new_flag):
    print(
        "I am a hook firing b/c a driver sees a different flag",
        driver,
        old_flag,
        new_flag,
    )
