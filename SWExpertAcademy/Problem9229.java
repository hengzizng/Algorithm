import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Problem9229 {

	public static String str = "4\r\n" + "3 45\r\n" + "20 20 20\r\n" + "6 10\r\n" + "1 2 5 8 9 11\r\n" + "4 100\r\n"
			+ "80 80 60 60\r\n" + "4 20\r\n" + "10 5 10 16";

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//		in = new BufferedReader(new StringReader(str));
		StringBuilder sb = new StringBuilder();

		int TC = Integer.parseInt(in.readLine());
		for (int tc = 1; tc <= TC; tc++) {
			sb.append("#").append(tc).append(" ");

			StringTokenizer st = new StringTokenizer(in.readLine());
			int N = Integer.parseInt(st.nextToken()); // 총 과자 봉지 개수
			int M = Integer.parseInt(st.nextToken()); // 무게 합 제한

			st = new StringTokenizer(in.readLine());
			int[] snack = new int[N]; // 오름차순 과자봉지 무게
			for (int i = 0; i < N; i++) {
				snack[i] = Integer.parseInt(st.nextToken());
			} // 입력 완료

			Arrays.sort(snack);
			int left = 0, right = N - 1;
			int nowWeight = 0;
			int maxWeight = 0;
			while (left < right) {
				nowWeight = snack[left] + snack[right];
				if (nowWeight == M) {
					maxWeight = nowWeight;
					break;
				} else if (nowWeight > M) {
					right--;
				} else {
					left++;
					maxWeight = Math.max(nowWeight, maxWeight);
				}
			}

			if (maxWeight == 0) {
				sb.append(-1);
			} else {
				sb.append(maxWeight);
			}
			sb.append("\n");
		}

		System.out.println(sb.toString());
	}

}
