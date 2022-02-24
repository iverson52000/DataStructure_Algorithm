fun main() {
    val square: (Int) -> Int = { num ->
        num * num
    }

//    println(square(5))

    val printName: (String) -> Unit = {
        println(it)
    }

    println(
        listOf(
            1 to 1,
            2 to 4,
            3 to 9
        )
    )
}