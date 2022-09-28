import kotlinx.coroutines.*

fun main() = runBlocking {    // Creates a blocking coroutine that executes in current thread (main)

    println("Main program starts: ${Thread.currentThread().name}")  // main thread

    val job: Job = launch {   // Thread: main(it’s a child coroutine of runBlocking!)
        println("Fake work starts: ${Thread.currentThread().name}")     // Thread: main
        delay(1000)   // Coroutine is suspended but Thread: main is free (not blocked)
        println("Fake work finished: ${Thread.currentThread().name}") // Thread: main
    }

    // job.cancel()
    job.join()      // main thread: wait for coroutine to finish

    println("Main program ends: ${Thread.currentThread().name}")    // main thread
}



