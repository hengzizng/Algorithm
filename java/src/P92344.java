class P92344 {
    public static void main(String[] args) {

    }

    // N: 행 수, M: 열 수
    public int N, M;

    // skill: [[type, r1, c1, r2, c2, degree], ...]
    // type: 1(공격받음), 2(회복)
    public int solution(int[][] board, int[][] skill) {
        N = board.length;
        M = board[0].length;

        int[][] change = new int[N + 1][M + 1];
        for (int i = 0; i < skill.length; i++) {
            if (skill[i][0] == 1) { // 공격받을 경우
                skill[i][5] *= -1;
            }

            change[skill[i][1]][skill[i][2]] += skill[i][5];
            change[skill[i][1]][skill[i][4] + 1] -= skill[i][5];
            change[skill[i][3] + 1][skill[i][2]] -= skill[i][5];
            change[skill[i][3] + 1][skill[i][4] + 1] += skill[i][5];
        }

        // 행별로 오른쪽으로 누적
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                change[r][c + 1] += change[r][c];
            }
        }
        // 열별로 아래로 누적
        int answer = 0;
        for (int c = 0; c < M; c++) {
            for (int r = 0; r < N; r++) {
                change[r + 1][c] += change[r][c];
                // 파괴되지 않은 건물인지 파악
                if (board[r][c] + change[r][c] > 0) {
                    answer++;
                }
            }
        }

        return answer;
    }
}
