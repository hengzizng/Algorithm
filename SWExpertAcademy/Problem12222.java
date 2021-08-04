import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Problem12222 {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int TC = Integer.parseInt(in.readLine());
		for (int tc = 1; tc <= TC; tc++) {
			sb.append("#").append(tc).append(" ");
			String S = in.readLine();
			int K = 1; // S의 가장 앞 글자를 하나로 둔다.

			String now = S.substring(0, 1); // 현재 문자열
			String next = S.substring(1, 2); // 현재 문자열의 뒤에 있는 비교할 문자열
			int pointer = 1 + 1; // next의 마지막 index + 1
			while (pointer < S.length()) {
				if (now.equals(next)) {
					next += S.charAt(pointer);
				} else {
					now = next;
					next = S.substring(pointer, pointer + 1);
					K++;
				}
				pointer++;
			}
			if (!now.equals(next)) {
				K++;
			}

			sb.append(K).append("\n");
		}

		System.out.println(sb.toString());

	}

}
