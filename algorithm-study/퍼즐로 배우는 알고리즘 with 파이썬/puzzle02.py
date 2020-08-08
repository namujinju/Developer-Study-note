sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9),
         (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]

# sched = [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8)]

sched_start = [i[0] for i in sched]
sched_end = [i[1] for i in sched]

count = 0
max_count = 0

for time in range(min(sched_start), max(sched_end)+1):
    count += sched_start.count(time)
    count -= sched_end.count(time)
    if max_count < count:
        max_count = count
        max_time = time

print(max_count, max_time)
