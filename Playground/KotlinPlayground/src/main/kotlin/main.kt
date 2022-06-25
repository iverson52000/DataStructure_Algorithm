import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

class Person {
    val height = 100
}

fun main() = runBlocking<Unit> {

    val personHeight = Person.height

}


