import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.assertThrows
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource


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

    companion object {
        @JvmStatic
        fun squares() = listOf(
            Arguments.of(1, 1),
            Arguments.of(2, 4),
            Arguments.of(3, 9)
        )
    }

    @ParameterizedTest
    @MethodSource("squares")
    fun `Square of a number`(input: Int, expected: Int) {
        assertEquals(expected, input * input)
    }
}