import java.io.*;
import java.util.*;

public class BJ2310 {
    public static int n;
    public static int[] prices;
    public static List<Integer>[] doors;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("testcase/BJ2310input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            // 방 수
            n = Integer.parseInt(in.readLine());

            // 입력 종료
            if (n == 0) {
                break;
            }

            // 각 방에 해당하는 금액 (0: 빈 방, 음수: 통행료, 양수: 채워질 금액)
            prices = new int[n];
            // 각 방에서 이동할 수 있는 다른 방 목록
            doors = new List[n];

            // 방 정보 입력
            for (int roomNo = 0; roomNo < n; roomNo++) {
                st = new StringTokenizer(in.readLine(), " ");
                // 방의 내용물(E: 빈 방, L: 레프리콘, T: 트롤) 이 트롤일 경우 금액을 음수로 저장
                prices[roomNo] = ("T".equals(st.nextToken()) ? -1 : 1) * Integer.parseInt(st.nextToken());
                // 이번 방에서 다른 방으로 갈 수 있는 문
                doors[roomNo] = new ArrayList<>();
                while (st.hasMoreTokens()) {
                    int doorNo = Integer.parseInt(st.nextToken()) - 1;
                    if (doorNo == -1) {
                        break;
                    }
                    doors[roomNo].add(doorNo);
                }
            }

            System.out.println(canGo() ? "Yes" : "No");
        }
    }

    // 0번 방에서 n-1번 방까지 갈 수 있는지 여부 반환
    public static boolean canGo() {
        // 출발 시 소지금이 0이기 때문에 시작부터 통행료를 지불해야 한다면 출발 불가
        if (prices[0] < 0) {
            return false;
        }

        // minPrice[i]: i번 방에서의(금액 처리 후) 최대 소지금
        int[] minPrice = new int[n];
        Arrays.fill(minPrice, -1);
        // {방 번호, 방에 도착해서 금액 처리 후 소지금}
        Queue<int[]> queue = new LinkedList<>();

        minPrice[0] = prices[0];
        queue.add(new int[]{0, prices[0]});
        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int nextRoomNo : doors[now[0]]) {
                int newPrice = now[1];
                if (prices[nextRoomNo] > 0) { // nextRoomNo번 방이 소지금을 채워주는 방이라면
                    newPrice = Math.max(newPrice, prices[nextRoomNo]);
                } else { // nextRoomNo번 방이 비었거나 통행료를 지불하는 방이라면
                    newPrice += prices[nextRoomNo];
                }

                // 소지금이 통행료보다 적었다면 이동 불가
                if (newPrice < 0) {
                    continue;
                }

                // 목적지에 도달
                if (nextRoomNo == n - 1) {
                    return true;
                }

                // 다른 방으로 이동
                if (newPrice > minPrice[nextRoomNo]) {
                    queue.add(new int[]{nextRoomNo, newPrice});
                    minPrice[nextRoomNo] = newPrice;
                }
            }
        }

        return false;
    }
}
