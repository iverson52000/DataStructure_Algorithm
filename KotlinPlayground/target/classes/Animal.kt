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
    }
}