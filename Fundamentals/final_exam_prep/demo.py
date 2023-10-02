songs = {"Beethoven": {"sonata": "g major"}}

i = songs.items()
if "g major" in songs["Beethoven"]["sonata"]:
    print("yes")
# for key, value in songs.items():
#     print(key)
#     print(value.items())