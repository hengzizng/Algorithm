import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Problem1244 {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int switchCount = Integer.parseInt(br.readLine()); // 스위치 개수
		st = new StringTokenizer(br.readLine(), " ");

		int[] switches = new int[switchCount]; // 스위치 상태
		for (int i = 0; i < switchCount; i++) {
			switches[i] = Integer.parseInt(st.nextToken());
		}

		int studentCount = Integer.parseInt(br.readLine()); // 학생 수
		for (int student = 0; student < studentCount; student++) {
			st = new StringTokenizer(br.readLine(), " "); // 성별, 받은 수

			if (Integer.parseInt(st.nextToken()) == 1) {
				multipleChange(switches, Integer.parseInt(st.nextToken()));
			} else {
				nearChange(switches, Integer.parseInt(st.nextToken()));
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < switchCount; i++) {
			if (i != 0 && i % 20 == 0) {
				sb.append("\n");
			}
			sb.append(switches[i] + " ");
		}
		sb.setLength(sb.length() - 1);
		System.out.println(sb.toString());

	}

	public static void multipleChange(int[] switches, int num) {
		for (int i = num; i <= switches.length; i += num) {
			switches[i - 1] = switches[i - 1] == 1 ? 0 : 1;
		}
	}

	public static void nearChange(int[] switches, int num) {
		int left = num - 1;
		int right = num - 1;

		while (left >= 0 && right < switches.length) {
			if (switches[left] == switches[right]) {
				switches[left] = switches[left] == 1 ? 0 : 1;
				switches[right] = switches[left];
			} else {
				break;
			}

			left--;
			right++;
		}

	}

}
