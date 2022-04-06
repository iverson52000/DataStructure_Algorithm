class Animal(var type: String, var size: String) {
    // custom setter and getter
    var nickName: String? = null
        set(value) {
            field = value
            println("the new nick name is $value")
        }
        get() {
            println("the returned value is $field")
            return field
        }

    fun printInfo() {
        println("Hi!")
        val nickNameToPrint = nickName ?: "no nickname"
        printInfo2()
    }

    private fun printInfo2() {
        println("Hi from info 2!")
        val nickNameToPrint = nickName ?: "no nickname"
    }
}

fun main() {
    val animal = Animal("a", "b")
    animal.printInfo()
}