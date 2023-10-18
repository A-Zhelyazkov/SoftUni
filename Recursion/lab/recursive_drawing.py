def draw_fig(n):
    if n == 0:
        return

    print('*' * n)
    draw_fig(n - 1)
    print('#' * n)

num = int(input())

draw_fig(num)