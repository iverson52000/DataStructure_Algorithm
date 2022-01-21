class Frog {
    private int age;
    private String name;

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static void showInfo() {
        System.out.println("Showing info!");
    }
}

public class HelloWorld {
    public static void main(String[] args) {

        // int[][] input = { { 1, 3 }, { -2, 2 } };
        // int[][] res = kClosest(input, 1);
        // System.out.println(Arrays.deepToString(res));

        Frog frog1 = new Frog();
        Frog.showInfo();

        StringBuilder sb = new StringBuilder("");
        Machine mech1 = new Machine();
        Car car1 = new Car();
        car1.start();
    }

}
