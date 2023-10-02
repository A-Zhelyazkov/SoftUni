def  even_odd_filter(**kwargs):
    if "even" in kwargs:
        kwargs['even'] = [int(i) for i in kwargs["even"] if i % 2 == 0]
    if "odd" in kwargs:
        kwargs['odd'] = [int(i) for i in kwargs["odd"] if i % 2 == 1]

    sorted_nums = dict(sorted(kwargs.items(), key=lambda items: -len(items[1])))

    return sorted_nums

print(even_odd_filter(
 odd=[1, 2, 3, 4, 10, 5],
 even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
 odd=[2, 2, 30, 44, 10, 5],
))



