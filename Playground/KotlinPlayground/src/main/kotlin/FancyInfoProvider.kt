class FancyInfoProvider : BasicInfoProvider() {
    override val providerInfo: String
        get() = super.providerInfo

    override fun printInto(person: Person) {
        super.printInto(person)
    }
}