
import solver

if __name__ == '__main__':
    while True:
        expression = str(input("Введите выражение: "))

        result = solver.Solver(expression)

        print(
            f"Выражение: {result.expression} \n"
            f"Результат: {result.result} \n"
            f"Причина: {result.reason} \n"
        )
