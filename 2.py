cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")

cinema_genres = tuple("Боевик" if genre == "Экшн" else genre for genre in cinema_genres)

new_genre = ("Фэнтези",)
cinema_genres = cinema_genres[:2] + new_genre + cinema_genres[2:]

genres_string = ", ".join(cinema_genres)

print("Получившийся кортеж:", cinema_genres)
print("Преобразованный кортеж в строку:", genres_string)