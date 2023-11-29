package unit-tests-3;

import static org.junit.Assert.*;
import org.junit.Test;

public class EvenOddNumberTest {

    @Test
    public void testEvenNumber() {
        assertTrue(evenOddNumber(4));
    }

    @Test
    public void testOddNumber() {
        assertFalse(evenOddNumber(7));
    }

    @Test
    public void testZero() {
        assertTrue(evenOddNumber(0));
    }

    @Test
    public void testNegativeEvenNumber() {
        assertTrue(evenOddNumber(-6));
    }

    @Test
    public void testNegativeOddNumber() {
        assertFalse(evenOddNumber(-9));
    }

    public boolean evenOddNumber(int n) {
        return n % 2 == 0;
    }
}
