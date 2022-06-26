import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

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

fun main() {
    val customTriple = CustomTriple(1, "test", 5.0)
    customTriple.printType()
}


