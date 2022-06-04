class Intent {
    var a = 10
}

fun main() {
    val intent = Intent().apply {
        this.a = 5
    }

    println(intent.a)
}