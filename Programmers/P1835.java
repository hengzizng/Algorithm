public class P1835 {
	
	static char[] friends = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
	static char[][] conditions;
	static int answer;

	public static void main(String[] args) {
		int n = 2;
		String[] data = {"N~F=0", "R~T>2"};		
		
		System.out.println(solution(n, data));
	}
	
	public static int solution(int n, String[] data) {
        conditions = new char[n][5];
        for (int i = 0; i < n; i++) {
        	conditions[i] = data[i].toCharArray();
        }
        
        answer = 0;
        permutation(0, new char[8], new boolean[8]);

        return answer;
    }
	
	private static void permutation(int count, char[] result, boolean[] selected) {
		// 매번 검사하므로 마지막으로 새로 추가된 항목만 검사하면 된다.
		if (count > 1 && !check(count - 1, result)) {
			return;
		}
		
		if (count == 8) {
			answer++;
			return;
		}
		
		for (int i = 0; i < 8; i++) {
			if (selected[i]) continue;
			
			selected[i] = true;
			result[count] = friends[i];
			permutation(count + 1, result, selected);
			selected[i] = false;
		}
	}

	private static boolean check(int targetIndex, char[] result) {
		char target = result[targetIndex]; // 이번에 검사할 프렌즈
		char friend; // target과 검사할 다른 프렌즈 
		
		for (char[] c : conditions) {
			if (target == c[0]) {
				friend = c[2];
			} else if (target == c[2]) {
				friend = c[0];
			} else { // target이 이번 검사 조건에 없다.
				continue;
			}
			
			// friend의 index를 찾는다.
			int friendIndex;
			for (friendIndex = 0; friendIndex < targetIndex; friendIndex++) {
				if (result[friendIndex] == friend) {
					break;
				}
			}
			
			// friend가 아직 result에 담기지 않았으면 이번 조건은 만족한 것으로 가정
			if (friendIndex == targetIndex) {
				continue;
			}
			
			// friend를 찾았으면
			int distance = c[4] - '0' + 1;
			char sign = c[3];
			if (sign == '=' && (targetIndex - friendIndex) != distance) {
				return false;
			}
			if (sign == '>' && (targetIndex - friendIndex) <= distance) {
				return false;
			}
			if (sign == '<' && (targetIndex - friendIndex) >= distance) {
				return false;
			}
		}
		
		// 모든 조건을 다 통과했으면 true 리턴
		return true;
	}

}
