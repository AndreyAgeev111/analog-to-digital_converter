from converter import convert as cv

if __name__ == '__main__':
    flag = True

    while flag:
        try:
            data, mode, scale = map(str, input("Введите название файла, режим работы АЦП, масштаб графика: ").split())
            cv(data, int(mode), scale)
            command = input("Хотите продолжить: ")

            if command.lower().strip() == "+":
                continue
            elif command.lower().strip() == "-":
                flag = False
            else:
                raise KeyboardInterrupt("Знак не распознан")

        except KeyboardInterrupt and ValueError:
            print("Данные введены неверно, попробуйте снова")



