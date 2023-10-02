string = input()

lowered_string = string.lower()

counter = lowered_string.count("water") + lowered_string.count("sand") + lowered_string.count("sun")\
          + lowered_string.count("fish")

print(counter)

