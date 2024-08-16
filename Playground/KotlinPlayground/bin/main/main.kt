import kotlinx.coroutines.*
import java.util.concurrent.Executors

fun main() {
    val execService = Executors.newFixedThreadPool(5)

    runBlocking {    // Creates a blocking coroutine that executes in the current thread (main)
        println("Main program starts: ${Thread.currentThread().name}")  // main thread

// execService.asCoroutineDispatcher()

        val job: Job = launch(execService.asCoroutineDispatcher()) {
            // Thread: main(it’s a child coroutine of runBlocking!)
            try {
                repeat(50) {
                    println("Fake work starts: ${Thread.currentThread().name}")     // Thread: main
                    delay(2000)   // Coroutine is suspended but Thread: main is free (not blocked)
                    error("Wrong!")
                    println("Fake work finished: ${Thread.currentThread().name}") // Thread: main
                }
            } finally {
                execService.shutdown()
            }
        }

        delay(5000)
//        job.cancelAndJoin()

        println("Main program ends: ${Thread.currentThread().name}")    // main thread
    }
}



