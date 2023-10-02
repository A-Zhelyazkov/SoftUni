year = int(input()) + 1
string_year = str(year)

while len(string_year) != len(set(string_year)):
    year += 1
    string_year = str(year)

print(year)