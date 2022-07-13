import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*
import org.apache.commons.math3.distribution.LaplaceDistribution
import kotlin.math.min
import kotlin.random.Random

class CustomTriple<A : Any, B : Any, C : Any>(
    val first: A,
    val second: B,
    val third: C
) {
    fun printType() {
        println("The type of first ${first::class}")
        println("The type of second ${second::class}")
        println("The type of third ${third::class}")
    }
}

const val testVal = "*/"
fun displayBorder(character: String = testVal, length: Int = 15) {
    for (i in 1..length) {
        print(character)
    }
}

fun main() {
    val customTriple = CustomTriple(1, 2, 3)
    customTriple.printType()
    displayBorder()
    val arr = listOf(1, 2, 3)
    val arrSize = min(arr.size, 10)
    println(arr.subList(0, arrSize))

}


