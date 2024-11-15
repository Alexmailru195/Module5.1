import random

cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

unique_genres = set(cinema_genres)

print(unique_genres)

unique_genres.add("драма")
unique_genres.add("фантастика")

print(unique_genres)

unique_genres.remove("экшн")
print(unique_genres)

unique_genres.discard(random.choice(list(unique_genres)))
print(unique_genres)

final_genres_list = list(unique_genres)

print("Итоговый список жанров:", final_genres_list)