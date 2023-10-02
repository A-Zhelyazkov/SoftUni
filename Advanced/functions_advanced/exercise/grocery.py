def grocery_store(**kwargs):
    result = ''
    sorted_els = sorted(kwargs.items(), key=lambda items: (-items[1], -len(items[0]), items[0]))
    for key,value in sorted_els:
        result += f"{key}: {value}\n"
    return result


print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))
