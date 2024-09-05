def main():
	first_course_mass = int(input("Первое значение массы (в граммах): ")) / 1000
	second_course_mass = int(input("Второе значение массы (в граммах): ")) / 1000
	third_course_mass = int(input("Третье значение массы (в граммах): ")) / 1000
	print(f"""Рецепт
политическая теория: {first_course_mass:.3f} кг
история политических учений: {second_course_mass:.3f} кг
математика: {third_course_mass:.3f} кг
Приправить политической историей. Добавить математические модели по вкусу.
""")