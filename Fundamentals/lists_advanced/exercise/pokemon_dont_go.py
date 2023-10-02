seq = [int(i) for i in input().split()]
removed_els = []

while seq:
    index = int(input())
    if index < 0:
        increment = seq[0]
        removed_els.append(seq[0])
        seq[0] = seq[-1]
        for i in range(0, len(seq)):
            num = seq[i]
            if num <= increment:
                seq[i] += increment
            else:
                seq[i] -= increment
        continue
    if index >= len(seq):
        removed_els.append(seq[-1])
        increment = seq[-1]
        seq[-1] = seq[0]
        for i in range(0, len(seq)):
            num = seq[i]
            if num <= increment:
                seq[i] += increment
            else:
                seq[i] -= increment
        continue
    removed_index = seq[index]
    removed_els.append(removed_index)
    seq.pop(index)

    for i in range(0, len(seq)):
        num = seq[i]
        if num <= removed_index:
            seq[i] += removed_index
        else:
            seq[i] -= removed_index

print(sum(removed_els))
