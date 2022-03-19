fun printFilteredStrings(list: List<String>, predicate: ((String) -> Boolean)?) {
    list.forEach {
        if (predicate?.invoke(it) == true) {
            println(it)
        }
    }
}

var predicate: (String) -> Boolean = {
    it.startsWith("J")
}

fun getPrintPredicate(prefix: String): (String) -> Boolean {
    return { it.startsWith(prefix) }
}

fun main() {
    val list = listOf("Kotlin", "Java", "C++", "Javascript")
    printFilteredStrings(list, getPrintPredicate("J"))

    printFilteredStrings(list, null)
}
