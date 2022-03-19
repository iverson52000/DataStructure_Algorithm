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

    @Test
    void testComputeCircleArea() {
        double radius = 2.5;
        double expected = Math.PI * radius * radius;
        assertEquals(expected, mathUtils.computeCircleArea(radius), "should return circle area");
    }

    
}