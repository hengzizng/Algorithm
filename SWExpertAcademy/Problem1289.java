import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Problem1289 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		System.setIn(new FileInputStream("1289input.txt"));

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine()); // 테스트케이스의 수
		
		int[] counts = new int[T];
		int count = 0; // 원래 상태로 돌아가려면 고쳐야 하는 횟수
		char flag = '0'; // 가장 마지막으로 설정한 비트 (0 또는 1)
		
		for (int i = 0; i < T; i++) {
			flag = '0';
			count = 0;
			char numsArr[] = in.readLine().toCharArray();
			
			for (char num : numsArr) {
//				System.out.println(num + " " + flag + " " + (num != flag));
				if (num != flag) {
					count++;
					flag = num;
				}
			}
			
			counts[i] = count;
		}

		for (int i = 0; i < T; i++) {
			System.out.println("#" + (i + 1) + " " + counts[i]);
		}
	}

}
