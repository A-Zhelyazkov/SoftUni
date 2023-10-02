import re

text = input()

pattern = r"\s([a-zA-Z0-9][a-zA-z0-9\-,.]*[a-zA-z0-9]@[A-Za-z-]+\.[A-Za-z]+\.?[a-zA-z]+ ?)"
results = re.findall(pattern, text)

for i in results:
    print(i.strip())