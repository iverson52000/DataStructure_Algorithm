import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class CalculatorTest {
    private val calculator = Calculator()

    @Test
    fun `Adding 1 and 3 should be equal to 4`() {
        assertEquals(4, calculator.add(1, 3))
    }
}