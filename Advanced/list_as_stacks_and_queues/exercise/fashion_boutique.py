clothes_received = [int(i) for i in input().split()]
rack_capacity = int(input())
count_racks = 0
while clothes_received:
    current_sum = 0

    while current_sum < rack_capacity and clothes_received:
        removed_item = clothes_received.pop()
        current_sum += removed_item
        if current_sum > rack_capacity:
            clothes_received.append(removed_item)

    count_racks += 1

print(count_racks)
