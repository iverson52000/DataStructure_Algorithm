fun main() {
    val square: (Int) -> Int = { num ->
        num * num
    }

    println(square(5))

    val printName: (String) -> Unit = {
        println(it)
    }

    printName("Albert")
}