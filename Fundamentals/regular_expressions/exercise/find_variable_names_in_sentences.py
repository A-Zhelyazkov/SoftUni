import re

text = input()

pattern = r"\b_{1}[a-zA-Z0-9]+\b"

result = re.findall(pattern, text)
results = [i[1:] for i in result]
print(','.join(results), sep=",")