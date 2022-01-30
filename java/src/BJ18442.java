import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;

public class BJ18442 {
    public static int V, P;
    public static long L, minDistanceSum = Long.MAX_VALUE, villages[], postOffices[];

    public static void main(String[] args) throws IOException {
        // 두 마을의 거리 = min(abs(x - y), L - abs(x - y))

        // 출력
        // 각 마을에서 가장 가까운 우체국과의 거리들의 합의 최소값
        // 우체국을 지을 마을들의 위치 오름차순으로

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        //////
        String test = "11 3 200\n0 0 0 0 0 0 0 0 0 0 199";
        in = new BufferedReader(new StringReader(test));
        //////

        String[] tokens = in.readLine().split(" ");
        V = Integer.parseInt(tokens[0]); // 마을의 수 (한 위치에 여러 마을이 있을 수 있다)
        P = Integer.parseInt(tokens[1]); // 우체국 수
        L = Long.parseLong(tokens[2]); // 길의 둘레

        tokens = in.readLine().split(" ");
        villages = new long[V];
        for (int i = 0; i < V; i++) {
            villages[i] = Long.parseLong(tokens[i]);
        }

        postOffices = new long[P];
        selectVillage(0, 0, new long[P]);

        StringBuilder sb = new StringBuilder();
        sb.append(minDistanceSum).append("\n");

        for (int i = 0; i < P; i++) {
            sb.append(postOffices[i]).append(" ");
        }

        sb.setLength(sb.length() - 1);
        System.out.print(sb.toString());
    }

    // 우체국을 지을 마을들을 선택하는 함수
    public static void selectVillage(int index, int count, long[] selected) {
        // 조합이 완성되면 거리를 구한다
        if (count == P) {
            long nowDistance = getDistanceSum(selected);

            if (nowDistance < minDistanceSum) {
                minDistanceSum = nowDistance;
                for (int i = 0; i < P; i++) {
                    postOffices[i] = selected[i];
                }
            }

            return;
        }

        for (int i = index; i < V; i++) {
            selected[count] = villages[i];
            selectVillage(i + 1, count + 1, selected);
        }
    }

    // 모든 마을 - 우체국 거리의 합의 최솟값을 구한다
    public static long getDistanceSum(long[] selected) {
        // middle : 현재 거리를 계산할 마을의 인덱스
        // left : middle 이전에 위치한 우체국의 인덱스
        // right : middle 이후에 위치한 우체국의 인덱스
        int left = P - 1, right = 0, middle = 0;
        long distanceSum = 0;

        while (middle < V) {
            if (villages[middle] == selected[right]) {
                left = (left + 1) % P;
                right = (right + 1) % P;
            } else {
                distanceSum += Math.min(
                        getDistance(selected[left], villages[middle]),
                        getDistance(villages[middle], selected[right])
                );
            }

            middle++;
        }

        return distanceSum;
    }

    // 두 개의 마을 간 거리를 구한다
    public static long getDistance(long x, long y) {
        long distanceAbs = Math.abs(x - y);
        return Math.min(distanceAbs, L - distanceAbs);
    }
}
