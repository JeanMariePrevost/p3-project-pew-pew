def print_debug_info():
    # print the number all objects of type "GameObject" using gc
    import gc
    from game.game_object import GameObject

    print("GameObjects count:")
    # go through all GameObjects in gc.get_objects(), and count them by class
    game_objects = {}
    for obj in gc.get_objects():
        if isinstance(obj, GameObject):
            if obj.__class__ not in game_objects:
                game_objects[obj.__class__] = 1
            else:
                game_objects[obj.__class__] += 1
    # Print from highest to lowest
    for key, value in sorted(game_objects.items(), key=lambda item: item[1], reverse=True):
        print(f"{key.__name__}: {value}")

    # Same, but for ALL objects:
    print("All objects count:")
    all_objects = {}
    for obj in gc.get_objects():
        if obj.__class__ not in all_objects:
            all_objects[obj.__class__] = 1
        else:
            all_objects[obj.__class__] += 1

    for key, value in sorted(all_objects.items(), key=lambda item: item[1], reverse=True):
        print(f"{key.__name__}: {value}")

    # for obj in gc.get_objects():
    #     if isinstance(obj, GameObject):
    #         print(obj)
