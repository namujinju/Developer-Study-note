n = int(input())
conference = []
count = 0

for i in range(n):
    a, b = input().split(" ")
    conference.append((int(a), int(b)))

conference = list(sorted(conference, key=lambda x: x[::-1]))

while len(conference):
    tuple_b = conference[0][1]
    count += conference.count((tuple_b, tuple_b)) + 1

    if len(conference) != 0:
        while conference[0][0] < tuple_b:
                conference.pop(0)
                if conference == []:
                    break

print(count)
    
