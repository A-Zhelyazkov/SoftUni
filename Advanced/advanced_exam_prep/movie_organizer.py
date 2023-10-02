def movie_organizer(*args):
    genres = {}
    result = ""
    for movie, genre in args:
        if genre not in genres:
            genres[genre] = [0]
        if movie not in genres[genre]:
            genres[genre][0] += 1
            genres[genre].append(movie)

    genres = sorted(genres.items(), key=lambda kvp: (-kvp[1][0], kvp[0], kvp))
    for key, value in genres:
        result += f"{key} - {value[0]}\n"
        value.pop(0)
        value = sorted(value)
        for word in value:
            result += f"* {word}\n"

    return result

print(movie_organizer(
    ("The Matrix", "Sci-fi")))

