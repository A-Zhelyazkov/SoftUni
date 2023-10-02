n, m = [int(i) for i in input().split()]
m_set = set()
n_set = set()
for _ in range(n):
    number = int(input())
    n_set.add(number)

for _ in range(m):
    number = int(input())
    m_set.add(number)

intersection_set = n_set.intersection(m_set)
for i in intersection_set:
    print(i)
