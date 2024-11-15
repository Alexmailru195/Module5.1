my_items = {"вода", "еда", "нож", "палатка", "фонарик", "одежда", "аптечка", "книга", "телефон", "спички"}

friend_items = {"еда", "фотоаппарат", "палатка", "книга", "одежда", "вода", "аптечка", "черепаха"}

both_items = my_items & friend_items
only_my_items = my_items - friend_items
only_friend_items = friend_items - my_items
common_items = my_items & friend_items

print("Вещи, которые бы взяли мы двое:", both_items)
print("Вещи, которые взял только я:", only_my_items)
print("Вещи, которые возьмет мой близкий человек:", only_friend_items)
print("Вещи, которые есть у нас обоих:", common_items)