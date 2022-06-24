import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

fun main() = runBlocking<Unit> {

    val flow = flow {
        delay(250L)
        emit("Appetizer")
        delay(1000L)
        emit("Main dish")
        delay(100L)
        emit("Dessert")
    }
    
    launch {
        flow.onEach {
            println("FLOW: $it is delivered")
        }.buffer().collect {
            println("FLOW: Now eating $it")
            delay(1500L)
            println("FLOW: Finished eating $it")
        }
    }

}


