import heapq


def min_cost_to_connect_cables(lengths):
    heapq.heapify(lengths)

    total_cost = 0

    while len(lengths) > 1:
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        cost = first + second
        total_cost += cost

        heapq.heappush(lengths, cost)

    return total_cost


cable_lengths = [4, 3, 2, 6]
print("Мінімальні загальні витрати:", min_cost_to_connect_cables(cable_lengths))
