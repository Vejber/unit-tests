package unit-tests-3;

import static org.junit.Assert.*;
import org.junit.Test;

public class NumberIntervalCheckerTest {

    @Test
    public void testNumberInInterval() {
        assertTrue(NumberIntervalChecker.numberInInterval(50));
        assertTrue(NumberIntervalChecker.numberInInterval(26));
        assertTrue(NumberIntervalChecker.numberInInterval(99));
    }

    @Test
    public void testNumberBelowInterval() {
        assertFalse(NumberIntervalChecker.numberInInterval(20));
        assertFalse(NumberIntervalChecker.numberInInterval(25));
    }

    @Test
    public void testNumberAboveInterval() {
        assertFalse(NumberIntervalChecker.numberInInterval(100));
        assertFalse(NumberIntervalChecker.numberInInterval(150));
    }

    @Test
    public void testBoundaryValues() {
        assertFalse(NumberIntervalChecker.numberInInterval(25));
        assertFalse(NumberIntervalChecker.numberInInterval(100));
    }
}
