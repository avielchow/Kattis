import collections

n,m = [int(x) for x in input().split()]

length_of_task = [int(x) for x in input().split()]
break_time = [int(x) for x in input().split()]

break_time.sort()
length_of_task.sort()

break_time = collections.deque(break_time)
length_of_task = collections.deque(length_of_task)

ans = 0

while break_time and length_of_task:
    if break_time.popleft() >= length_of_task[0]:
        ans += 1
        length_of_task.popleft()


print(ans)
