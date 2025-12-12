"""
Программа для нахождения минимального и максимального расстояний между точками
Реализация методом нисходящего проектирования - Итерация 2
"""

import random


def main():
    """Главная функция программы"""
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ ВЫЧИСЛЕНИЯ РАССТОЯНИЙ МЕЖДУ ТОЧКАМИ")
    print("=" * 50)
    
    points = []  # Список для хранения точек
    results = None  # Результаты вычислений
    
    while True:
        show_menu()
        choice = input("\nВаш выбор (0-6): ").strip()
        
        if choice == '0':
            print("\nДо свидания!")
            break
        
        # Обработка выбора пользователя
        if choice == '1':
            points = add_points_manually(points)
            results = None  # Сбрасываем результаты при добавлении новых точек
        elif choice == '2':
            points = generate_random_points(points)
            results = None
        elif choice == '3':
            show_all_points(points)
        elif choice == '4':
            results = calculate_distances(points)
        elif choice == '5':
            show_calculation_results(results, points)
        elif choice == '6':
            points = clear_all_points(points)
            results = None
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
    print("\n" + "=" * 50)
    print("РУЧНОЙ ВВОД ТОЧЕК")
    print("=" * 50)
    print("Введите координаты в формате: x y")
    print("Например: 3.5 -2.1")
    print("Для завершения введите 'stop'")
    print("-" * 50)
    
    count = 0
    while True:
        user_input = input(f"Точка {len(points) + 1} > ").strip()
        
        if user_input.lower() == 'stop':
            if len(points) + count < 2:
                print("Нужно минимум 2 точки! Продолжайте ввод.")
                continue
            break
        
        try:
            # Парсим ввод пользователя
            parts = user_input.split()
            if len(parts) != 2:
                print("Ошибка: нужно ввести ДВА числа через пробел!")
                continue
            
            x = float(parts[0])
            y = float(parts[1])
            
            # Добавляем точку
            points.append((x, y))
            count += 1
            print(f"Добавлена точка ({x:.2f}, {y:.2f})")
            
        except ValueError:
            print("Ошибка: введите корректные числа!")
    
    print(f"\nДобавлено {count} точек")
    print(f"Всего точек в памяти: {len(points)}")
    return points


def generate_random_points(points):
    """Сгенерировать случайные точки"""
    print("\n" + "=" * 50)
    print("ГЕНЕРАЦИЯ СЛУЧАЙНЫХ ТОЧЕК")
    print("=" * 50)
    
    try:
        count = int(input("Сколько точек сгенерировать? "))
        
        if count <= 0:
            print("Число должно быть положительным! Установлено: 5")
            count = 5
        
        print(f"\nГенерация {count} случайных точек...")
        
        for i in range(count):
            x = random.uniform(-100, 100)
            y = random.uniform(-100, 100)
            points.append((x, y))
            print(f"  {i+1:3}. ({x:7.2f}, {y:7.2f})")
        
        print(f"\nСгенерировано {count} точек")
        print(f"Всего точек в памяти: {len(points)}")
        
    except ValueError:
        print("Ошибка: введите целое число!")
    
    return points


def show_all_points(points):
    """Показать все сохраненные точки"""
    print("\n" + "=" * 50)
    print("ВСЕ ТОЧКИ В ПАМЯТИ")
    print("=" * 50)
    
    if not points:
        print("Память пуста. Точек нет.")
        return
    
    print(f"Всего точек: {len(points)}\n")
    
    for i, (x, y) in enumerate(points, 1):
        print(f"{i:4}. ({x:8.2f}, {y:8.2f})")


def calculate_distances(points):
    """Вычислить минимальное и максимальное расстояния"""
    print("\n" + "=" * 50)
    print("ВЫЧИСЛЕНИЕ РАССТОЯНИЙ")
    print("=" * 50)
    
    if len(points) < 2:
        print("Ошибка: нужно минимум 2 точки!")
        print("Используйте пункты 1 или 2 для добавления точек")
        return None
    
    print(f"Начинаю вычисления для {len(points)} точек...")
    
    # ВЫЗОВ ОСНОВНОГО АЛГОРИТМА (ЗАГЛУШКА)
    results = calculate_min_max_distance(points)
    
    if results:
        print("\nВычисления завершены!")
        print(f"Минимальное расстояние: {results['min_distance']:.4f}")
        print(f"Максимальное расстояние: {results['max_distance']:.4f}")
    else:
        print("\nОшибка при вычислениях")
    
    return results


def calculate_min_max_distance(points):
    """
    ОСНОВНОЙ АЛГОРИТМ: найти минимальное и максимальное расстояния
    МЕЖДУ ВСЕМИ ПАРАМИ ТОЧЕК
    
    Вход: список кортежей [(x1, y1), (x2, y2), ...]
    Выход: словарь с результатами или None при ошибке
    
    ЭТА ФУНКЦИЯ ОСТАВЛЕНА В ВИДЕ ЗАГЛУШКИ
    согласно заданию нисходящего проектирования
    """
    print("[АЛГОРИТМ ЗАГЛУШКА] Вычисление минимального и максимального расстояний")
    
    # Проверка количества точек
    if len(points) < 2:
        return None
    
    # ВРЕМЕННАЯ РЕАЛИЗАЦИЯ ДЛЯ ТЕСТИРОВАНИЯ
    # Здесь будет полный алгоритм перебора всех пар точек
    
    # Примерные вычисления для демонстрации
    import math
    
    # Берем первую и последнюю точку для демонстрации
    x1, y1 = points[0]
    x2, y2 = points[-1]
    
    # Вычисляем расстояние между ними
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Создаем заглушку результатов
    results = {
        'min_distance': distance * 0.5,  # Примерное минимальное
        'max_distance': distance * 1.5,  # Примерное максимальное
        'min_points': (points[0], points[1] if len(points) > 1 else points[0]),
        'max_points': (points[0], points[-1]),
        'total_points': len(points),
        'total_pairs': len(points) * (len(points) - 1) // 2
    }
    
    print(f"   Анализируется {results['total_pairs']} пар точек...")
    print("   [РЕАЛЬНЫЙ АЛГОРИТМ БУДЕТ РЕАЛИЗОВАН В СЛЕДУЮЩЕЙ ИТЕРАЦИИ]")
    
    return results


def show_calculation_results(results, points):
    """Показать результаты вычислений"""
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЙ")
    print("=" * 50)
    
    if not results:
        print("Результатов нет. Сначала выполните вычисления (пункт 4)")
        return
    
    print(f"Всего проанализировано точек: {results['total_points']}")
    print(f"Количество проверенных пар: {results['total_pairs']}")
    print("\n" + "-" * 30)
    print("МИНИМАЛЬНОЕ РАССТОЯНИЕ:")
    print(f"  Расстояние: {results['min_distance']:.6f}")
    p1, p2 = results['min_points']
    print(f"  Точка 1: ({p1[0]:.2f}, {p1[1]:.2f})")
    print(f"  Точка 2: ({p2[0]:.2f}, {p2[1]:.2f})")
    
    print("\n" + "-" * 30)
    print("МАКСИМАЛЬНОЕ РАССТОЯНИЕ:")
    print(f"  Расстояние: {results['max_distance']:.6f}")
    p1, p2 = results['max_points']
    print(f"  Точка 1: ({p1[0]:.2f}, {p1[1]:.2f})")
    print(f"  Точка 2: ({p2[0]:.2f}, {p2[1]:.2f})")
    
    print("\nВнимание: это демонстрационные данные!")
    print("Реальный алгоритм будет в следующей итерации")


def clear_all_points(points):
    """Очистить все точки из памяти"""
    print("\n" + "=" * 50)
    print("ОЧИСТКА ПАМЯТИ")
    print("=" * 50)
    
    if not points:
        print("Память и так пуста")
        return []
    
    confirm = input(f"Вы уверены? Удалить {len(points)} точек? (y/N): ").strip().lower()
    
    if confirm == 'y' or confirm == 'yes' or confirm == 'да':
        print("Все точки удалены!")
        return []
    else:
        print("Отмена. Точки сохранены.")
        return points


# Точка входа в программу
if __name__ == "__main__":
    main()