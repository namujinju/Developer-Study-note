sched = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
         (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]
sched_start = [(i[0], i[2]) for i in sched]
sched_end = [(i[1], i[2]) for i in sched]
memo = {}


for i in sched_start:
    if i[0] in memo:
        memo[i[0]] += i[1]
    else:
        memo[i[0]] = i[1]
for i in sched_end:
    if i[0] in memo:
        memo[i[0]] -= i[1]
    else:
        memo[i[0]] = -i[1]

memo_list = list(memo.values())
print(memo_list)

for i in range(len(memo_list)-1, 0-1, -1):
    if memo_list[i] > 0:
        max_time = list(memo.keys())[i]
        break

max_value = sum(memo_list[:i+1])
print(max_time, max_value)
