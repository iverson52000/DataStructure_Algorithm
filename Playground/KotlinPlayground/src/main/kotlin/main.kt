import kotlinx.coroutines.*

fun main() = runBlocking {    // Creates a blocking coroutine that executes in current thread (main)

    println("Main program starts: ${Thread.currentThread().name}")  // main thread

    val deferredJob: Deferred<Int> = async {   // Thread: main
        println("Fake work starts: ${Thread.currentThread().name}")     // Thread: main
        delay(1000)   // Coroutine is suspended but Thread: main is free (not blocked)
        println("Fake work finished: ${Thread.currentThread().name}") // Thread: main
        15  // Will be returned
    }

    val num: Int =
        deferredJob.await()  // main thread: wait for coroutine to finish and return data. Can call deferredJob.join()

    println("Main program ends: ${Thread.currentThread().name}")    // main thread
    println(num)
}
