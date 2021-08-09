import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Problem1228 {
	public static String str = "11\n" + "449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205\n"
			+ "7\n"
			+ "I 1 5 400905 139831 966064 336948 119288 I 8 6 436704 702451 762737 557561 810021 771706 I 3 8 389953 706628 552108 238749 661021 498160 493414 377808 I 13 4 237017 301569 243869 252994 I 3 4 408347 618608 822798 370982 I 8 2 424216 356268 I 4 10 512816 992679 693002 835918 768525 949227 628969 521945 839380 479976";

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("1228input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//		in = new BufferedReader(new StringReader(str));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#").append(tc).append(" ");

			in.readLine(); // 원본 암호문 길이
			List<String> cryptogram = new LinkedList<String>(); // 원본 암호문
			st = new StringTokenizer(in.readLine(), " ");
			for (int i = 0; i < 10; i++) {
				cryptogram.add(st.nextToken());
			} // 입력 완료

			int commandCnt = Integer.parseInt(in.readLine()); // 명령어 개수
			st = new StringTokenizer(in.readLine(), " ");
			for (int i = 0; i < commandCnt; i++) {
				st.nextToken();
				int insertIdx = Integer.parseInt(st.nextToken()); // 삽입 위치
				int insertCnt = Integer.parseInt(st.nextToken()); // 삽입 개수
				List<String> newList = new LinkedList<String>(); // 삽입할 암호문
				for (int j = 0; j < insertCnt; j++) {
					newList.add(st.nextToken());
				}
				if (insertIdx > 9) { // 삽입할 인덱스가 10 이상이면 처리하지 않음
					continue;
				}
				cryptogram.addAll(insertIdx, newList);
			}

			ListIterator<String> it = cryptogram.listIterator();
			int cnt = 0;
			while (it.hasNext() && cnt++ < 10) {
				sb.append(it.next()).append(" ");
			}
			sb.append("\n");
		}

		System.out.println(sb.toString());
	}

}
