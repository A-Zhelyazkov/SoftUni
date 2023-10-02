budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

total_gpu = gpu_count * 250
total_cpu = cpu_count * (total_gpu * 0.35)
total_ram = ram_count * (0.1 * total_gpu)
bill = total_gpu + total_cpu + total_ram

if gpu_count > cpu_count:
    bill = bill * 0.85

diff = abs(budget - bill)

if budget >= bill:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")