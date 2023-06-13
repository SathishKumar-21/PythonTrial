lists = ["computer", "monitor", "mouse", "keyboard", "printer", "speaker"]
shopping = lists
print(id(lists))
print(shopping)

lists += ['joystick']
print(id(lists))
print(id(shopping))
