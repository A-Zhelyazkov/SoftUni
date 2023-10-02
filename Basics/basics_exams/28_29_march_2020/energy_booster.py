fruit = input()
package_size = input()
ordered_packages = int(input())
total_sum = 0

if fruit == "Watermelon":
    if package_size == "small":
        total_sum = (56 * 2) * ordered_packages
    if package_size == "big":
        total_sum = (28.7 * 5) * ordered_packages

elif fruit == "Mango":
    if package_size == "small":
        total_sum = (36.66 * 2) * ordered_packages
    if package_size == "big":
        total_sum = (19.6 * 5) * ordered_packages

elif fruit == "Pineapple":
    if package_size == "small":
        total_sum = (42.1 * 2) * ordered_packages
    if package_size == "big":
        total_sum = (24.8 * 5) * ordered_packages

elif fruit == "Raspberry":
    if package_size == "small":
        total_sum = (20 * 2) * ordered_packages
    if package_size == "big":
        total_sum = (15.2 * 5) * ordered_packages

if 400 <= total_sum <= 1000:
    total_sum *= 0.85
elif total_sum > 1000:
    total_sum *= 0.5

print(f"{total_sum:.2f} lv.")
