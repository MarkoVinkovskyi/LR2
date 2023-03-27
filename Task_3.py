
def day_when_runner_will_reach_goal(n, x):
    distance = n
    day_count = 1
    while distance < x:
        distance *= 1.1
        day_count += 1
    return day_count
N,X=map(int,input().split())
print(day_when_runner_will_reach_goal(N, X))

