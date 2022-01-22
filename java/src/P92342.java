import java.util.Arrays;

public class P92342 {
    public static int maxDifference, winCount;
    public static int[] answer;

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(9, new int[]{0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1})));
    }

    public static int[] solution(int n, int[] info) {
        // n: 화살 개수, info: 어피치의 점수 개수 {10점개수, 9점개수, ..., 0점개수}

        // 라이언이 가장 큰 점수 차이로 이기기 위한 점수 개수 배열 리턴 {10점개수, 9점개수, ..., 0점개수}
        // 라이언이 이길 수 없다면 [-1] 리턴
        // 여러 방법일 경우, 낮은 점수를 더 많이 맞힌 경우로 선정

        // k점에 라이언 개수 > 어피치 개수 -> 라이언 k점
        // 라이언 최종 점수 > 어피치 최종 점수 일때 라이언 우승

        answer = new int[11];
        setScore(n, 0, 0, 0, new int[11], info);

        // 이긴 횟수가 한번도 없다면 이길 방법이 없다
        return winCount == 0 ? new int[]{-1} : answer;
    }

    // restCount: 남은 화살 개수, index: 개수를 비교할 점수(인덱스), result: 라이언이 쏜 화살 수
    // ryanTotalScore: 지금까지의 라이언 점수, apeachTotalScore: 지금까지의 어피치 점수
    public static void setScore(int restCount, int index, int ryanTotalScore, int apeachTotalScore, int[] result, int[] info) {
        if (index >= 10) {
            // 라이언이 이기지 못했거나 이전에 구한 점수차보다 작다면
            int difference = ryanTotalScore - apeachTotalScore;
            if (ryanTotalScore <= apeachTotalScore || difference < maxDifference) {
                return;
            }

            winCount++;
            result[10] += restCount; // 쓰고 남은 화살을 0점 개수에 더해준다

            if (difference == maxDifference) { // 이전의 점수차와 같다면
                // 낮은 점수의 개수부터 확인하기 때문에 개수가 다른 점수를 찾는다면 바로 종료 가능
                for (int i = 10; i >= 0; i--) {
                    if (answer[i] < result[i]) {
                        answer = result;
                        break;
                    } else if (answer[i] > result[i]) {
                        break;
                    }
                }
            } else { // 이번의 점수차가 더 크다면
                maxDifference = difference;
                answer = result;
            }

            return;
        }

        int[] copied = new int[11];
        for (int i = 0; i < 11; i++) {
            copied[i] = result[i];
        }

        // 이번 점수 라이언 승
        int addScore = 10 - index;
        if (restCount >= info[index] + 1) {
            copied[index] = info[index] + 1;
            setScore(restCount - copied[index], index + 1, ryanTotalScore + addScore, apeachTotalScore, copied, info);
        }

        // 이번 점수 라이언 패
        addScore = info[index] == 0 ? 0 : addScore;
        copied[index] = 0;
        setScore(restCount, index + 1, ryanTotalScore, apeachTotalScore + addScore, copied, info);
    }
}
