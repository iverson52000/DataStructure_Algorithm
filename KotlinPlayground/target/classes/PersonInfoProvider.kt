class Person {
    fun printInfo() {
        println("person's info")
    }
}

interface PersonInfoProvider {
    val providerInfo: String

    fun printInto(person: Person) {
        println(providerInfo)
        person.printInfo()
    }
}

interface SessionInfoProvider {
    fun getSessionId(): String
}

open class BasicInfoProvider : PersonInfoProvider, SessionInfoProvider {
    override val providerInfo: String
        get() = "BasicInfoProvider"

    override fun printInto(person: Person) {
        super.printInto(person)
        println("Additional print statement")
    }

    override fun getSessionId(): String {
        return "Session"
    }
}

fun main() {
    val provider = BasicInfoProvider()
    provider.printInto(Person())

    val provider2 = object : PersonInfoProvider {
        override val providerInfo: String
            get() = TODO("Not yet implemented")

        fun getSessionId() = "id"
    }

}