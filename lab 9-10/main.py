from typing import List, Tuple
import random
import math

class Point:
    """Класс для хранения точки с координатами (x, y)"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def distance_to(self, other) -> float:
        """Вычисляет расстояние до другой точки"""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)
    
    def __str__(self) -> str:
        return f"({self.x:.2f}, {self.y:.2f})"


class PointManager:
    """Класс для управления точками и вычисления расстояний"""
    
    def __init__(self):
        self.points: List[Point] = []
        self.min_pair: Tuple[Point, Point] = None
        self.max_pair: Tuple[Point, Point] = None
        self.has_result = False
    
    def add_point(self, x: float, y: float) -> None:
        """Добавляет точку в коллекцию"""
        point = Point(x, y)
        self.points.append(point)
        print(f"Добавлена точка: {point}")
        self._reset_results()
    
    def add_random_points(self, count: int, min_coord: float = -100, max_coord: float = 100) -> None:
        """Добавляет случайные точки"""
        if count <= 0:
            print("Количество точек должно быть положительным")
            return
        
        for i in range(count):
            x = random.uniform(min_coord, max_coord)
            y = random.uniform(min_coord, max_coord)
            self.add_point(x, y)
        
        print(f"\nДобавлено {count} случайных точек")
        print(f"Всего точек: {len(self.points)}")
    
    def clear_points(self) -> None:
        """Очищает все точки"""
        self.points.clear()
        self._reset_results()
        print("Все точки удалены")
    
    def _reset_results(self) -> None:
        """Сбрасывает результаты вычислений"""
        self.min_pair = None
        self.max_pair = None
        self.has_result = False
        print("Результаты вычислений сброшены")
    
    def calculate_distances(self) -> bool:
        """Вычисляет минимальное и максимальное расстояния между точками"""
        if len(self.points) < 2:
            print("Ошибка: нужно как минимум 2 точки!")
            return False
        
        print(f"Вычисление расстояний для {len(self.points)} точек...")
        
        min_distance = float('inf')
        max_distance = 0
        
        # Перебираем все пары точек
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                distance = self.points[i].distance_to(self.points[j])
                
                # Проверяем минимальное расстояние
                if distance < min_distance:
                    min_distance = distance
                    self.min_pair = (self.points[i], self.points[j])
                
                # Проверяем максимальное расстояние
                if distance > max_distance:
                    max_distance = distance
                    self.max_pair = (self.points[i], self.points[j])
        
        self.has_result = True
        print("Вычисления завершены!")
        print(f"Минимальное расстояние: {min_distance:.4f}")
        print(f"Максимальное расстояние: {max_distance:.4f}")
        return True
    
    def show_points(self) -> None:
        """Показывает все точки"""
        if not self.points:
            print("Точек нет")
            return
        
        print(f"\nВСЕ ТОЧКИ ({len(self.points)}):")
        for i, point in enumerate(self.points, 1):
            print(f"{i:3}. {point}")
    
    def show_results(self) -> None:
        """Показывает результаты вычислений"""
        if not self.has_result:
            print("Сначала выполните вычисления!")
            return
        
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЙ")
        print("=" * 50)
        
        # Минимальная пара
        if self.min_pair:
            p1, p2 = self.min_pair
            distance = p1.distance_to(p2)
            print(f"\nМИНИМАЛЬНОЕ РАССТОЯНИЕ: {distance:.6f}")
            print(f"Точка 1: {p1}")
            print(f"Точка 2: {p2}")
        
        # Максимальная пара
        if self.max_pair:
            p1, p2 = self.max_pair
            distance = p1.distance_to(p2)
            print(f"\nМАКСИМАЛЬНОЕ РАССТОЯНИЕ: {distance:.6f}")
            print(f"Точка 1: {p1}")
            print(f"Точка 2: {p2}")
        
        print("\n" + "=" * 50)


def show_menu() -> None:
    print("\nПРОГРАММА ДЛЯ НАХОЖДЕНИЯ МИНИМАЛЬНОГО И МАКСИМАЛЬНОГО РАССТОЯНИЯ")
    print("\nГЛАВНОЕ МЕНЮ:")
    print("1. Ввести точки вручную")
    print("2. Сгенерировать случайные точки")
    print("3. Показать все точки")
    print("4. Выполнить вычисления")
    print("5. Показать результаты")
    print("6. Очистить все точки")
    print("0. Выход из программы")
    print("-" * 50)


def main():
    """Главная функция программы"""
    manager = PointManager()
    
    while True:
        show_menu()
        
        try:
            choice = input("\nВыберите действие (0-6): ").strip()
            
            if choice == '0':
                print("\nСпасибо за использование программы! До свидания!")
                break
            
            elif choice == '1':
                # Ручной ввод точек
                while True:
                    print("\nВведите координаты точки (x y)")
                    print("Например: 3.5 -2.1")
                    print("Для завершения ввода введите 'stop'")
                    
                    input_str = input("> ").strip()
                    
                    if input_str.lower() == 'stop':
                        if len(manager.points) < 2:
                            print("Нужно как минимум 2 точки! Продолжайте ввод.")
                            continue
                        break
                    
                    try:
                        parts = input_str.split()
                        if len(parts) != 2:
                            print("Ошибка: нужно ввести два числа через пробел!")
                            continue
                        
                        x = float(parts[0])
                        y = float(parts[1])
                        manager.add_point(x, y)
                        
                    except ValueError:
                        print("Ошибка: введите корректные числа!")
            
            elif choice == '2':
                # Генерация случайных точек
                try:
                    count = int(input("Сколько точек сгенерировать? "))
                    if count < 2:
                        print("Минимум 2 точки! Установлено значение 10.")
                        count = 10
                    
                    manager.add_random_points(count)
                    
                except ValueError:
                    print("Ошибка: введите целое число!")
            
            elif choice == '3':
                # Показать все точки
                manager.show_points()
            
            elif choice == '4':
                # Выполнить вычисления
                manager.calculate_distances()
            
            elif choice == '5':
                # Показать результаты
                manager.show_results()
            
            elif choice == '6':
                # Очистить все точки
                confirm = input("Вы уверены? Все точки будут удалены! (y/n): ").strip().lower()
                if confirm == 'y':
                    manager.clear_points()
            
            else:
                print("Неверный выбор! Попробуйте снова.")
        
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()