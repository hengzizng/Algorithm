import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Problem1204 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("1204input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		final int SCORE_COUNT = 101; // 점수가 0점 ~ 100점 까지이므로 101
		int T = Integer.parseInt(br.readLine()); // 테스트 케이스의 수
		int[] modes = new int[T]; // 최빈값들을 담는 배열
		
		for (int i = 0; i < T; i++) {
			int t = Integer.parseInt(br.readLine()); // 테스트케이스 번호
			
			st = new StringTokenizer(br.readLine(), " ");
			// scoresCount => index: 점수, value: index에 해당하는 점수를 받은 학생들의 수
			int[] scoresCount = new int[SCORE_COUNT];
			
			for (int j = 0; j < 1000; j++) { // 학생 수는 1000명
				int score = Integer.parseInt(st.nextToken()); // 현재 학생의 점수
				scoresCount[score]++;
			}
						
			int modeScore = 0; // 최빈값에 해당하는 점수
			int mode = 0; // 최빈값
			for (int j = 0; j < SCORE_COUNT; j++) {
				if (mode <= scoresCount[j]) {
					modeScore = j;
					mode = scoresCount[j];
				}
			}
			
			modes[t - 1] = modeScore;
		}
		
		for (int t = 0; t < T; t++) {
			System.out.println("#" + (t + 1) + " " + modes[t]);
		}

	}

}
