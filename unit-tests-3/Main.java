package unit-tests-3;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class Main {

    public static void main(String[] args) {
        // Запуск тестов для evenOddNumber
        Result evenOddResult = JUnitCore.runClasses(EvenOddNumberTest.class);

        for (Failure failure : evenOddResult.getFailures()) {
            System.out.println(failure.toString());
        }

        if (evenOddResult.wasSuccessful()) {
            System.out.println("Тесты для evenOddNumber прошли успешно!");
        } else {
            System.out.println("Тесты для evenOddNumber не прошли успешно.");
        }

        System.out.println(); // Добавим пустую строку для разделения результатов

        // Запуск тестов для numberInInterval
        Result intervalResult = JUnitCore.runClasses(NumberIntervalCheckerTest.class);

        for (Failure failure : intervalResult.getFailures()) {
            System.out.println(failure.toString());
        }

        if (intervalResult.wasSuccessful()) {
            System.out.println("Тесты для numberInInterval прошли успешно!");
        } else {
            System.out.println("Тесты для numberInInterval не прошли успешно.");
        }
    }
}
