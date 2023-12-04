"""
тесты для проверки работы функций класса AverageComparator
"""

import pytest
from your_program import AverageComparator


def test_compare_averages_general():
    """
    Тест общего случая: сравнение средних значений двух списков.
    """
    comparator = AverageComparator([1, 2, 3], [4, 5, 6])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"


def test_compare_averages_equal():
    """
    Тест для списков с равными средними значениями.
    """
    comparator = AverageComparator([1, 2, 3], [3, 2, 1])
    assert comparator.compare_averages() == "Средние значения равны"


def test_compare_averages_different_sizes():
    """
    Тест для списков различных размеров.
    """
    comparator = AverageComparator([1, 2, 3, 4], [5, 6, 7])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"


def test_compare_averages_negative_numbers():
    """
    Тест для списков с отрицательными числами.
    """
    comparator = AverageComparator([-1, -2, -3], [4, 5, 6])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"


def test_compare_averages_decimal_numbers():
    """
    Тест для списков с десятичными числами.
    """
    comparator = AverageComparator([1.5, 2.5, 3.5], [1.0, 2.0, 3.0])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"


def test_compare_averages_empty_lists():
    """
    Тест для пустых списков.
    """
    comparator = AverageComparator([], [])
    assert comparator.compare_averages() == "Средние значения равны"


def test_compare_averages_single_element():
    """
    Тест для списков с одним элементом.
    """
    comparator = AverageComparator([5], [10])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"


def test_compare_averages_large_numbers():
    """
    Тест для списков с большими числами.
    """
    comparator = AverageComparator(
        [10**8, 2 * 10**8, 3 * 10**8], [5 * 10**7, 6 * 10**7, 7 * 10**7])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"


def test_compare_averages_repeated_numbers():
    """
    Тест для списков с повторяющимися числами.
    """
    comparator = AverageComparator([1, 2, 2, 3], [4, 4, 5, 6])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"
