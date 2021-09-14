import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.Arrays;

public class BJ2309 {
	
	public static String input = "20\r\n" + 
			"7\r\n" + 
			"23\r\n" + 
			"19\r\n" + 
			"10\r\n" + 
			"15\r\n" + 
			"25\r\n" + 
			"8\r\n" + 
			"13";

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		in = new BufferedReader(new StringReader(input));
		
		int overHeight = -100;
		int[] heights = new int[9];
//		boolean[] isReal = new boolean[9];
		for (int i = 0; i < 9; i++) {
			heights[i] = Integer.parseInt(in.readLine());
			overHeight += heights[i];
//			isReal[i] = true;
		}
		Arrays.sort(heights);
		
		// 투포인터
		int left = 0, right = 8;
		while (left < right) {
			int nowSum = heights[left] + heights[right];
			if (nowSum == overHeight) {
				break;
			} else if (nowSum > overHeight) {
				right--;
			} else {
				left++;
			}
		}
		
		for (int i = 0; i < 9; i++) {
			if (i != left && i != right) {
				System.out.println(heights[i]);
			}
		}
		
//		// 배열 추가 사용
//		outer: for (int i = 0; i < 8; i++) {
//			int fakeHeight = heights[i];
//			for (int j = i; j < 9; j++) {
//				if (heights[j] == overHeight - fakeHeight) {
//					isReal[i] = false;
//					isReal[j] = false;
//					break outer;
//				}
//			}
//		}
//
//		for (int i = 0; i < 9; i++) {
//			if (isReal[i]) {
//				System.out.println(heights[i]);
//			}
//		}

	}

}
