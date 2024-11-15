literature_genres = ("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)

length_literals = len(literature_genres)
length_numbers = len(numbers)

max_number = max(numbers)
min_number = min(numbers)

max_literal = max(literature_genres)
min_literal = min(literature_genres)

sum_numbers = sum(numbers)

sorted_numbers_asc = tuple(sorted(numbers))
sorted_numbers_desc = tuple(sorted(numbers, reverse=True))

sorted_literals_asc = tuple(sorted(literature_genres))
sorted_literals_desc = tuple(sorted(literature_genres, reverse=True))


print(length_literals)
print(length_numbers)
print()
print(max_number)
print(min_number)
print()
print(max_literal)
print(min_literal)
print()
print(sum_numbers)
print()
print(sorted_numbers_asc)
print(sorted_numbers_desc)
print()
print(sorted_literals_asc)
print(sorted_literals_desc)
