import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class BJ1158 {
	public static String str = "7 3";

	public static void main(String[] args) throws IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		in = new BufferedReader(new StringReader(str));

		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		int N = Integer.parseInt(st.nextToken()); // 사람 수
		int K = Integer.parseInt(st.nextToken()); // K번째 사람 제거

		List<Integer> people = new LinkedList<Integer>();
		for (int n = 1; n <= N; n++) {
			people.add(n);
		} // 입력 완료

		ListIterator<Integer> it = people.listIterator();
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		int person = -1; // 지워질 사람
		while (!people.isEmpty()) { // 사람이 없을때까지 반복
			for (int k = 0; k < K; k++) { // k번 반복
				if (!it.hasNext()) {
					it = people.listIterator(0);
				}
				person = it.next();
			}
			it.remove();
			sb.append(person).append(", ");
		}
		
		sb.setLength(sb.length() - 2);
		sb.append(">");
		System.out.println(sb.toString());
	}

}
