//enum class EntityType {
//    EASY, MEDIUM, HARD;
//
//    fun getFormattedName() = name.lowercase().replaceFirstChar { it.uppercase() }
//}
//
//object EntityFactory {
//    fun create() = Entity("id", "name")
//}
//
//sealed class Entity() {
//    object Help {
//        val name = "Help"
//    }
//
//    data class Easy(val id: String, val name: String) : Entity()
//    data class Medium(val id: String, val name: String) : Entity()
//    data class Hard(val id: String, val name: String, val modifier: Float) : Entity()
//}
//
//fun Entity.Medium.printInfo() {
//    println("Medium class: $id")
//}
//
//val Entity.Medium.info: String
//    get() = "some info"
//
//fun main() {
//    val entity = EntityFactory.create()
//    println(entity)
//}