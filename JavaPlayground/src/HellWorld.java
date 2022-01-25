import java.util.ArrayList;

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

public class HellWorld {

    public static void main(String[] args) {

        // int[][] input = { { 1, 3 }, { -2, 2 } };
        // int[][] res = kClosest(input, 1);
        // System.out.println(Arrays.deepToString(res));

        Machine mach1 = new Machine();
        mach1.start();

        Info info1 = new Machine();
        info1.showInfo();

        // outputInfo(mach1);

        ArrayList<Integer> arr = new ArrayList<>();

        Test1 test1 = new Test1();

        try {
            test1.run();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}
