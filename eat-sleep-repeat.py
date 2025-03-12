eat = 1
sleep = 2
repeat = 3

todo = [eat, sleep, repeat]
in_progress = ["",""]
done = ["",""]

print(todo)

todo.pop(sleep)
print(todo)

in_progress.insert(1, sleep)
print(in_progress)

in_progress.pop(sleep)
done.insert(0, sleep)
print(done)

