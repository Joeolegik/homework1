for n in range(1, 101):  #по заданию учитываем только значения от 1 до 100, пробегаясь по списку склонение слову "процент"
    def transf_string(number:int) -> str:
        if 11 <= number <= 19 or number % 10 == 0:
            return str(number) + " процентов"
        elif number % 10 == 1:
            return str(number) + " процент"
        elif number % 10 <= 4:
            return str(number) + " процента"
        elif number % 10 <= 9:
            return str(number) + " процентов"

    print(transf_string(n))