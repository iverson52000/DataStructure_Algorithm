import java.util.Arrays;
import java.util.PriorityQueue;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello java 17!");

        int[][] input = { { 1, 3 }, { -2, 2 } };
        int[][] res = kClosest(input, 2);

        System.out.println(Arrays.deepToString(res));

    }

    public static int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (p1, p2) -> p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1]);

        for (int[] point : points) {
            pq.offer(point);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        int[][] res = new int[k][2];

        for (int i = 0; i < k; i++) {
            res[i] = pq.poll();
        }
        while (k > 0) {
            res[--k] = pq.poll();
        }

        System.out.println();
        return res;

    }
}
