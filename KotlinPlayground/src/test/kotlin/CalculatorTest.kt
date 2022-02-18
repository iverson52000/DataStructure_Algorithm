import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.assertThrows

internal class CalculatorTest {
    private val calculator = Calculator()

    @Test
    fun `Adding 1 and 3 should be equal to 4`() {
        assertEquals(4, calculator.add(1, 3)) { "1+3 should equal 4" }
    }

    @Test
    fun `Divide by zero should throw ArithmeticException`() {
        assertThrows<ArithmeticException> { calculator.divide(1, 0) }
    }
}