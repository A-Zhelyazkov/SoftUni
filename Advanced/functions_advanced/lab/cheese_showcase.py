def sorting_cheeses(**kwargs):
    result = ''
    cheeses = sorted(kwargs.items(), key=lambda items: (-len(items[1]), items[0]))
    for cheese, quantity in cheeses:
        result += f"{cheese}\n"
        for i in sorted(quantity, reverse=True):
            result += f"{i}\n"
    return result


print(
 sorting_cheeses(
 Parmesan=[102, 120, 135],
 Camembert=[100, 100, 105, 500, 430],
 Mozzarella=[50, 125],
 )
)

