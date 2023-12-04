"""
Этот модуль содержит класс AverageComparator для сравнения средних значений списков.
"""


class AverageComparator:
    """
    Этот класс сравнивает средние значения двух списков.
    """

    def __init__(self, list1, list2):
        """
        Инициализирует экземпляр AverageComparator двумя списками.

        :param list1: Первый список чисел.
        :param list2: Второй список чисел.
        """
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, numbers):
        """
        Рассчитывает среднее значение списка чисел.

        :param numbers: Список чисел.
        :return: Рассчитанное среднее значение.
        """
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def compare_averages(self):
        """
        Сравнивает средние значения двух списков.

        :return: Строка, указывающая результат сравнения.
        """
        average1 = self.calculate_average(self.list1)
        average2 = self.calculate_average(self.list2)

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        if average2 > average1:
            return "Второй список имеет большее среднее значение"

        return "Средние значения равны"
