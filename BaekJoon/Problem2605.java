import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Problem2605 {
	
	public static String str = "5\n"
			+ "0 1 1 3 2";

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		in = new BufferedReader(new StringReader(str));
		
		int studentCount = Integer.parseInt(in.readLine()); // 학생 수
		StringTokenizer st = new StringTokenizer(in.readLine());
		List<Integer> students = new LinkedList<Integer>(); // 학생들 리스트
		for (int i = 0; i < studentCount; i++) {
			int index = i - Integer.parseInt(st.nextToken());
			students.add(index, i + 1);
		}
		
		StringBuilder sb = new StringBuilder();
		ListIterator<Integer> it = students.listIterator();
		while (it.hasNext()) {
			sb.append(it.next()).append(" ");
		}
		
		System.out.println(sb.toString());
		
 
	}

}
