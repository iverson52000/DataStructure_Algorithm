import java.util.ArrayList;
import java.util.Arrays;

public class App {

    public static void main(String[] args) {
        App app = new App();

        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1, 2, 3));

        System.out.println("1. arr is: " + arr);

        app.show(arr);

        System.out.println("4. arr is: " + arr);
    }

    public void show(ArrayList<Integer> arr) {
        System.out.println("2. arr is: " + arr);

        arr.add(4);

        System.out.println("3. arr is: " + arr);

    }

}