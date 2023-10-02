# country_names = tuple(input().split(", "))
# capitals = tuple(input().split(", "))
# final_res = list(zip(country_names, capitals))


# final_res = list(zip(input().split((", ")), input().split((", "))))
# for i in range(len(final_res)):
#     pair = final_res[i]
#     print(f"{pair[0]} -> {pair[1]}")


country = input().split(", ")
capital = input().split(", ")

final_res = {country[i]: capital[i] for i in range(len(country))}

for capital, country in final_res.items():
    print(f"{capital} -> {country}")