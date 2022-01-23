import java.util.StringTokenizer;

public class P92335 {
    public static void main(String[] args) {
        int n = (int) (Math.random() * 1000000) + 1;
        int k = (int) (Math.random() * 8) + 3;
        System.out.print("n = " + n);
        System.out.println(" k = " + k);
        System.out.println(solution(n, k));
    }

    public static int solution(int n, int k) {
        // 10진수 숫자 n을 k진수로 변환
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            sb.append(n % k);
            n = n / k;
        }
        sb.reverse();

        String knumber = sb.toString(); // n을 k진수로 변환한 문자열

        // 0으로 문자열 split
        StringTokenizer numbers = new StringTokenizer(knumber, "0");

        // split된 문자열들 소수인지 확인하고 맞으면 개수 +1
        int answer = 0;
        while (numbers.hasMoreTokens()) {
            // 자료형 주의!!
            long number = Long.parseLong(numbers.nextToken());
            if (isPrime(number)) {
                answer++;
            }
        }

        return answer;
    }

    // target이 소수인지 판별
    public static boolean isPrime(long target) {
        if (target < 2) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(target); i++) {
            if (target % i == 0) {
                return false;
            }
        }
        return true;
    }
}
