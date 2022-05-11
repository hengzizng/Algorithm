import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class BJ2493 {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(in.readLine()); // 탑의 개수
        int[] heights = new int[N + 1]; // 탑들의 높이

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        for (int topNo = 1; topNo <= N; topNo++) {
            heights[topNo] = Integer.parseInt(st.nextToken());
        }

        // stack에 N번 -> 1번 순서로 넣는다. (for문)
        // --- stack의 peek의 높이 <= 이번에 넣을 탑의 높이 --- 반복
        // stack pop 의 receivers 값에 이번에 넣을 탑 번호를 넣는다.
        // --- 반복 종료
        int[] receivers = new int[N + 1]; // 수신하는 탑 번호
        Stack<Integer> tops = new Stack<>();
        for (int topNo = N; topNo >= 1; topNo--) {
            while (!tops.isEmpty() && heights[tops.peek()] <= heights[topNo]) {
                receivers[tops.pop()] = topNo;
            }
            tops.add(topNo);
        }

        // 출력
        StringBuilder sb = new StringBuilder();
        for (int topNo = 1; topNo <= N; topNo++) {
            sb.append(receivers[topNo]).append(" ");
        }
        sb.setLength(sb.length() - 1);
        System.out.println(sb.toString());
    }
}
