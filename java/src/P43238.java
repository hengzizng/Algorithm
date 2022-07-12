import java.util.Arrays;

public class P43238 {
    public static void main(String[] args) {
        System.out.println(solution(6, new int[]{7, 10}));
        System.out.println(28);
    }

    public static long solution(int n, int[] times) {
        // 최댓값을 구하기 위해 times 배열 정렬
        Arrays.sort(times);
        // 이진 탐색을 위한 시간의 최소, 최댓값
        long minTime = 1, maxTime = (long) times[times.length - 1] * n;
        // 모든 사람이 심사를 받는 데 걸리는 시간의 최솟값
        long time = 0;

        while (minTime <= maxTime) {
            // 이진 탐색을 위한 시간의 중간값
            long midTime = (minTime + maxTime) / 2;

            // 이번 time동안 심사를 받을 수 있는 사람의 최대 수를 구한다.
            long peopleCount = 0;
            for (int t : times) {
                peopleCount += midTime / t;
                // 심사를 받을 수 있는 사람의 수가 n을 넘으면 더 더할 필요 X
                if (peopleCount >= n) {
                    break;
                }
            }

            // 심사를 받을 수 있는 사람 수가 n보다 작다면 시간을 늘린다.
            if (peopleCount < n) {
                minTime = midTime + 1;
            }
            // 심사를 받을 수 있는 사람 수가 n보다 크거나 같다면 시간을 줄인다.
            else {
                time = midTime;
                maxTime = midTime - 1;
            }
        }

        return time;
    }
}
