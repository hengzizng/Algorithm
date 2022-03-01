import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BJ14890 {
    public static int N, L;

    public static void main(String[] args) throws Exception {
        // [ 경사로 조건 ]
        // 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
        // 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
        // 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
        // 가로, 세로의 경사로는 서로 영향을 끼치지 않는다

        // [ 경사로 불가 조건 ]
        // 경사로를 놓은 곳에 또 경사로를 놓는 경우
        // 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
        // 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
        // 경사로를 놓다가 범위를 벗어나는 경우

        // --- 각 행, 열 반복 시작 ---
        // *** N만큼 반복 시작 ***
        // height에 시작 위치의 높이를, length에 연속된 높이의 개수를 저장
        // [if] 높이가 같으면 length++
        // [else if] 현재 높이 - height == 1 이면 (현재 높이가 더 높음)
        //   length가 L보다 길거나 같은지 확인
        //     조건 만족하면 height 현재 높이로, length 1로 설정
        //     조건 만족하지 않으면 *** break (false)
        // [else if] 현재 높이 - height == -1 이면 (이전 높이가 더 높음)
        //   현재 위치 + (L - 1) 까지 높이가 같은지 확인
        //     조건 만족하면 현재 위치 += (L - 1), height 현재 높이로, length 0로 설정
        //     조건 만족하지 않으면 *** break (false)
        // [else] 높이 차이가 1 초과이면
        //   *** break (false)
        // *** N만큼 반복 종료 ***
        // --- 각 행, 열 반복 종료 ---

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        String[] input = in.readLine().split(" ");
        N = Integer.parseInt(input[0]); // 지도 크기
        L = Integer.parseInt(input[1]); // 경사로 길이

        // 지도 상태
        int[][] rows = new int[N][N];
        int[][] cols = new int[N][N];
        for (int i = 0; i < N; i++) {
            input = in.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                rows[i][j] = Integer.parseInt(input[j]);
                cols[j][i] = rows[i][j];
            }
        }

        int roadCount = 0; // 지나갈 수 있는 길의 개수
        for (int i = 0; i < N; i++) {
            if (canPass(rows[i])) { // i열 확인
                roadCount++;
            }
            if (canPass(cols[i])) { // i행 확인
                roadCount++;
            }
        }

        System.out.println(roadCount);
    }

    // 지나갈 수 있는 길이면 true를, 못지나가는 길이면 false를 반환
    public static boolean canPass(int[] map) {
        int index = 0; // 확인할 위치
        int height = map[index], length = 1; // height: 기준 높이, length: height 높이의 연속 개수

        while (++index < N) {
            if (map[index] == height) { // 현재 높이와 이전 높이가 같으면
                length++;
            } else if (map[index] - height == 1) { // 현재 높이가 더 높으면
                if (length >= L) { // 같은 높이 연속 개수가 경사로를 놓을 수 있을 만큼이면
                    height = map[index];
                    length = 1;
                } else { // 경사로를 놓을 수 없으면
                    return false;
                }
            } else if (map[index] - height == -1) { // 현재 높이가 더 낮으면
                // 현재 높이가 연속된 수가 경사로를 놓을 수 있을 만큼인지 확인
                height = map[index];
                for (int j = 1; j < L; j++) {
                    if (index + j == N || map[index + j] != height) {
                        return false;
                    }
                }

                index += (L - 1);
                length = 0;
            } else {
                return false;
            }
        }

        return true;
    }
}
