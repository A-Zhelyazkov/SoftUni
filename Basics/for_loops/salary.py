count_tabs = int(input())
salary = int(input())
facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

for i in range(count_tabs):
    websites = input()
    if websites == "Facebook":
        salary -= facebook_fine
    if websites == "Instagram":
        salary -= instagram_fine
    if websites == "Reddit":
        salary -= reddit_fine
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)

