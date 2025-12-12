"""
Программа для нахождения минимального и максимального расстояний между точками
Реализация методом нисходящего проектирования - Итерация 1
"""

def main():
    """Главная функция программы"""
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ ВЫЧИСЛЕНИЯ РАССТОЯНИЙ МЕЖДУ ТОЧКАМИ")
    print("=" * 50)
    
    points = []  # Список для хранения точек
    
    while True:
        show_menu()
        choice = input("\nВаш выбор (0-6): ").strip()
        
        if choice == '0':
            print("\nДо свидания!")
            break
        
        # Обработка выбора пользователя
        if choice == '1':
            points = add_points_manually(points)
        elif choice == '2':
            points = generate_random_points(points)
        elif choice == '3':
            show_all_points(points)
        elif choice == '4':
            calculate_distances(points)
        elif choice == '5':
            show_calculation_results(points)
        elif choice == '6':
            points = clear_all_points(points)
        else:
            print("Неверный выбор! Попробуйте снова.")


def show_menu():
    """Показать главное меню программы"""
    print("\n" + "-" * 40)
    print("ГЛАВНОЕ МЕНЮ:")
    print("-" * 40)
    print("1. Ввести точки вручную")
    print("2. Сгенерировать случайные точки")
    print("3. Показать все точки")
    print("4. Вычислить расстояния")
    print("5. Показать результаты вычислений")
    print("6. Очистить все точки")
    print("0. Выход из программы")
    print("-" * 40)


def add_points_manually(points):
    """Добавить точки через ручной ввод"""
    print("\n[Заглушка] Функция добавления точек вручную")
    print("Здесь будет реализован ввод координат")
    return points  # Возвращаем неизмененный список


def generate_random_points(points):
    """Сгенерировать случайные точки"""
    print("\n[Заглушка] Функция генерации случайных точек")
    print("Здесь будет создание случайных координат")
    return points


def show_all_points(points):
    """Показать все сохраненные точки"""
    print("\n[Заглушка] Функция показа всех точек")
    if points:
        print(f"Сейчас в памяти: {len(points)} точек")
    else:
        print("В памяти нет точек")


def calculate_distances(points):
    """Вычислить минимальное и максимальное расстояния"""
    print("\n[Заглушка] Функция вычисления расстояний")
    if len(points) >= 2:
        print("Есть достаточно точек для вычислений")
    else:
        print("Нужно минимум 2 точки!")


def show_calculation_results(points):
    """Показать результаты вычислений"""
    print("\n[Заглушка] Функция показа результатов")
    print("Сначала нужно выполнить вычисления (пункт 4)")


def clear_all_points(points):
    """Очистить все точки из памяти"""
    print("\n[Заглушка] Функция очистки точек")
    print("Все точки будут удалены")
    return []  # Возвращаем пустой список


# Точка входа в программу
if __name__ == "__main__":
    main()