import re

text = input()
travel_points = 0
pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'

matches = re.findall(pattern, text)

destinations = [i[1] for i in matches]
destinations_str = ''.join(destinations)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {len(destinations_str)}")

