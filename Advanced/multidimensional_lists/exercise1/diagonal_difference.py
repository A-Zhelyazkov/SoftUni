matrix = [[int(i) for i in input().split(" ")] for _ in range(int(input()))]
rotated_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]
primary_list = []
secondary_list = []
for i in range(len(matrix)):
    primary_list.append(matrix[i][i])
    secondary_list.append(rotated_matrix[i][i])

print(abs(sum(primary_list) - sum(secondary_list)))