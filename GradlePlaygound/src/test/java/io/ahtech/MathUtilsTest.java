package io.ahtech;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MathUtilsTest {
    MathUtils mathUtils;

    @BeforeEach
    void setup() {
        mathUtils = new MathUtils();
    }

    @Test
    void testAdd() {
        assertEquals(5, mathUtils.add(2, 3));

    }
}