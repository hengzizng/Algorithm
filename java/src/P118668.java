class P118668 {
    public static void main(String[] args) {
        
    }

    public int solution(int alp, int cop, int[][] problems) {
        // 모든 문제를 풀기 위해 요구되는 최대 알고력, 최대 코딩력
        int maxAlp = 0, maxCop = 0;
        for (int[] problem : problems) {
            maxAlp = Math.max(maxAlp, problem[0]);
            maxCop = Math.max(maxCop, problem[1]);
        }

        // times[i][j]: 알고력 i, 코딩력 j를 만들기 위한 최소 시간
        int SIZE = 152;
        int[][] times = new int[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (i > alp || j > cop) {
                    times[i][j] = 300;
                }
            }
        }

        for (int a = 0; a <= maxAlp; a++) {
            for (int c = 0; c <= maxCop; c++) {
                // 알고력 1 증가
                times[a + 1][c] = Math.min(times[a + 1][c], times[a][c] + 1);
                // 코딩력 1 증가
                times[a][c + 1] = Math.min(times[a][c + 1], times[a][c] + 1);
                // 문제 풀이
                for (int[] problem : problems) {
                    // 이번 문제 풀이가 가능할 경우
                    if (a >= problem[0] && c >= problem[1]) {
                        int nextAlp = Math.min(maxAlp, a + problem[2]);
                        int nextCop = Math.min(maxCop, c + problem[3]);
                        times[nextAlp][nextCop] = Math.min(times[nextAlp][nextCop], times[a][c] + problem[4]);
                    }
                }
            }
        }

        return times[maxAlp][maxCop];
    }
}