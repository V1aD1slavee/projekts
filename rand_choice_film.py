import random
import time
import sqlite3



class RandomFilm:
    def __init__(self):
        self.choice = None

    def choice(self):
        films = [] # Список для фильмов
        while True:   # Цикл для ввода корректного числа фильмов
            try:
                hm_films = int(input("❓ Пожалуйста введите кол-во фильмов из которых мы будем выбирать: "))
                if hm_films <= 1:   # Проверяем, чтобы количество фильмов было больше 1
                    print("❌Количевство фильмов должно быть больше 1❌")
                    continue
                break        # Если ввод корректный, выходим из цикла
            except ValueError:
                print("❌Пожалуйста введите кол-во фильмов в виде числа!❌")
                continue

        # Ввод фильмов
        for i in range(hm_films):
            options = input(f"📜 Введите фильм №{i + 1}: ")
            films.append(options)

        # Выбор фильма
        total_film = random.choice(films)
        print("\n🎯 Выбираем  случайный фильм... 🎯")
        time.sleep(3)  # Задержка программы на 3 сек
        print(f"Вашим фильмом на вечер будет\n 🥳-----{total_film}-----🥳 ")
        print("🌟 Приятного просмотра 🌟")



    def main(self):
        print("Добро пожаловать в наш рандомайзер фильмов!")
        while True:
            self.choice()  # Вызываем функцию выбора фильма
            # Запрос: продолжение или выход
            while True:
                select = input("\n Хотите выбрать фильмы заново? ДА/НЕТ: ").strip().upper()
                if select == "ДА":
                    break  # Если пользователь хочет продолжить, выходим из этого цикла
                elif select == "НЕТ":
                    print("🌈Всего доброго. Ждём вас снова!🌈") 
                    print("Автор программы: *VladiSlave*")
                    exit()  # Завершаем программу
                else:
                    print("❌Ответ введён некорректно. Ответьте ДА/НЕТ❌")

play = RandomFilm
play.main()