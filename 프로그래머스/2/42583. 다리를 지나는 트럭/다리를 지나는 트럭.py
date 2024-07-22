from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    complete = []

    trucks = deque(truck_weights)
    loading = deque()
    loading_time = deque()

    while True:
        time += 1

        if loading and time-loading_time[0] == bridge_length:
            complete.append(loading.popleft())
            loading_time.popleft()

            if complete == truck_weights:
                return time

        if len(trucks) >= 1 and sum(loading) + trucks[0] <= weight :
            loading.append(trucks.popleft())
            loading_time.append(time)