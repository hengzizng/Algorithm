import java.util.HashMap;
import java.util.Map;

public class P77486 {

    public static void main(String[] args) {
        // enroll: 조직 구성도 (조직에 먼저 참여한 순)
        // referral: 추천인 (enroll[i]의 추천인은 referral[i])
        // seller: 판매한 사람, amount: 판매량
        // 이익은 칫솔 한 개당 100원 -> 판매량 * 100

        String[] enroll = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
        String[] referral = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] seller = {"young", "john", "tod", "emily", "mary"};
        int[] amount = {12, 4, 2, 5, 10};
        int[] answer = solution(enroll, referral, seller, amount);

        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }
    }

    public static int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        // profits: 사람별로 배분된 이익금의 총합
        Map<String, Integer> profits = new HashMap<>();
        // referralMap: {판매원 : 추천인} 형태의 추천인 정보
        Map<String, String> referralMap = new HashMap<>();

        // 기본 수익 값을 0으로 설정한다.
        profits.put("-", 0);
        for (String person : enroll) {
            profits.put(person, 0);
        }

        // 추천인 정보를 설정한다.
        for (int i = 0; i < referral.length; i++) {
            referralMap.put(enroll[i], referral[i]);
        }

        // 각 사람별로 이익을 구한다.
        for (int i = 0; i < seller.length; i++) {
            String person = seller[i]; // 이익을 구할 판매원
            String parent = referralMap.get(person); // 추천인
            int profit = amount[i] * 100; // 이번에 발생한 이익
            int value = profit / 10; // 배분할 금액

            profits.put(person, profits.get(person) + profit);

            // center가 될 때까지 반복해서 이익을 나눈다.
            while (!"-".equals(person) && value > 0) {
                profits.put(person, profits.get(person) - value);
                profits.put(parent, profits.get(parent) + value);

                person = parent;
                parent = referralMap.get(person);

                value /= 10;
            }
        }

        int[] answer = new int[enroll.length];
        for (int i = 0; i < enroll.length; i++) {
            answer[i] = profits.get(enroll[i]);
        }

        return answer;
    }

}
