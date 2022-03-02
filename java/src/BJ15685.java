import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class BJ15685 {
    public static void main(String[] args) throws IOException {
        // 0세대 드래곤 커브 : 선 1개
        // 1세대 드래곤 커브 : 선 2개
        // 2세대 드래곤 커브 : 선 4개
        // n세대 드래곤 커브 : 선 2^n개

        // 방향 - 0: 우, 1: 상, 2: 좌, 3:하
        int[][] dxdy = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}}; // 0: 우, 1: 상, 2: 좌, 3:하
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        ///// test
        String test = "4\n" + "50 50 0 10\n" + "50 50 1 10\n" + "50 50 2 10\n" + "50 50 3 10";
        in = new BufferedReader(new StringReader(test));
        ///// test

        int[][] board = new int[101][101]; // 드래곤 커브가 위치한 좌표평면

        int N = Integer.parseInt(in.readLine()); // 드래곤 커브의 수
        for (int n = 1; n <= N; n++) {
            String[] input = in.readLine().split(" ");
            int x = Integer.parseInt(input[0]); // 시작점 열
            int y = Integer.parseInt(input[1]); // 시작점 행
            int d = Integer.parseInt(input[2]); // 시작 방향
            int g = Integer.parseInt(input[3]); // 세대

            List<Integer> directions = new ArrayList<>(); // 방향을 저장
            directions.add(d); // 0세대 방향
            for (int i = 1; i <= g; i++) { // 1세대 ~ g세대
                for (int j = directions.size() - 1; j >= 0; j--) {
                    d = (directions.get(j) + 1) % 4;
                    directions.add(d);
                }
            }

            board[y][x] = 1;
            for (int i = 0; i < directions.size(); i++) {
                d = directions.get(i);
                x += dxdy[d][0];
                y += dxdy[d][1];
                board[y][x] = 1;
            }
        }

        // 네 꼭짓점이 모두 드래곤 커브인 사각형 체크
        int count = 0;
        for (int x = 0; x < 100; x++) {
            for (int y = 0; y < 100; y++) {
                if (board[y][x] == 1 && board[y][x + 1] == 1 && board[y + 1][x] == 1 && board[y + 1][x + 1] == 1) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}
