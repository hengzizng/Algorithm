import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class SWEA1218 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		Map<Character, Character> bracket = new HashMap<Character, Character>() {{
			put(')', '(');
			put(']', '[');
			put('}', '{');
			put('>', '<'); 
		}};

		System.setIn(new FileInputStream("TestCase/SWExpertAcademy/1218input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#").append(tc).append(" ");
			
			Stack<Character> stack = new Stack<Character>();
			
			int len = Integer.parseInt(in.readLine());
			char[] chars = in.readLine().toCharArray();
			
			stack.push(chars[0]);
			for (int i = 1; i < len; i++) {
				if (bracket.containsValue(chars[i])) {
					stack.push(chars[i]);
				} else {
					if (stack.peek() == bracket.get(chars[i])) {
						stack.pop();
					} else {
						stack.push(chars[i]);
					}
				}
			}
			
			if (stack.isEmpty()) {
				sb.append(1); // 유효
			} else {
				sb.append(0); // 유효하지 않음
			}
			sb.append("\n");
		}
		
		System.out.println(sb.toString());

	}

}
