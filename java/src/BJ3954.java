import java.io.*;
import java.util.*;

public class BJ3954 {
    public static int arrSize, codeSize, inputSize, pointer, codeIndex, inputIndex;
    public static int[] arr;
    public static char[] codes, inputs;
    public static Map<Integer, Integer> bracketMap; // [ or ] 일 때 짝을 이루는 괄호의 인덱스

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ////// test
        String test1 = "4\n" + "10 4 3\n" + "+-.,\n" + "qwe\n" + "1000 5 1\n" + "+[+-]\n" + "a\n" + "100 74 4\n" + "+++++[->++<]>[-<+++++++>]<[->+>+>+>+<<<<]>+++>--->++++++++++>---<<<.>.>.>.\n" + "xxyz\n" + "9999 52 14\n" + "+++++[>+++++++++<-],+[-[>--.++>+<<-]>+.->[<.>-]<<,+]\n" + "this_is_a_test";
        String test2 = "2\n" + "3 124 1\n" + "+[-[[>+[>----------------------------------[+++]<+]++++++++++++++++++++++++++[+]<+]----------------------------------[+]]++]\n" + ".\n" + "1 8 1\n" + "+[-[]++]\n" + ".";
        String test3 = "1\n" + "1000 10 1\n" + "+[,[+-]-].\n" + "a";
        String test4 = "3\n" + "1000 7 1\n" + "+[+-]...\n" + "a\n" + "1000 10 1\n" + "+[+-].[+-]\n" + "a\n" + "1000 10 1\n" + "+[,[+-]-].\n" + "a";
        in = new BufferedReader(new StringReader(test2));
        ////// test

        int t = Integer.parseInt(in.readLine()); // 테스트케이스 수
        for (int tc = 0; tc < t; tc++) {
            // 첫째 줄 입력
            st = new StringTokenizer(in.readLine(), " ");
            arrSize = Integer.parseInt(st.nextToken()); // 메모리(배열) 크기
            codeSize = Integer.parseInt(st.nextToken()); // 명령(코드) 수
            inputSize = Integer.parseInt(st.nextToken()); // 입력 문자열 크기
            // 둘째 줄 입력
            codes = in.readLine().strip().toCharArray(); // 명령(프로그램 코드)
            // 셋째 줄 입력
            inputs = in.readLine().strip().toCharArray(); // 입력 문자열

            // 각 괄호의 짝 인덱스를 먼저 구한다.
            setBracketMap();

            pointer = 0; // arr(데이터 배열) 포인터
            codeIndex = 0; // 명령(프로그램 코드) 인덱스
            inputIndex = 0; // 입력 문자열 인덱스
            arr = new int[arrSize]; // 데이터 배열

            String result = run();
            if (!"Terminates".equals(result)) {
                result = run();
            }

            System.out.println(result);
        }
    }

    public static String run() {
        int runCount = 0; // 명령 수행 횟수
        int loopEnd = -1; // 루프 중 닫는 괄호의 위치

        while (true) {
            char code = codes[codeIndex];

            if (code == '-') {
                arr[pointer] = arr[pointer] == 0 ? 255 : arr[pointer] - 1;
            } else if (code == '+') {
                arr[pointer] = (arr[pointer] + 1) % 256;
            } else if (code == '<') {
                pointer = (pointer + arrSize - 1) % arrSize;
            } else if (code == '>') {
                pointer = (pointer + 1) % arrSize;
            } else if (code == '[') {
                if (arr[pointer] == 0) {
                    // 아래에서 1 더해주기 때문에 여기서 더해주지 않음
                    codeIndex = bracketMap.get(codeIndex);
                }
            } else if (code == ']') {
                if (arr[pointer] != 0) {
                    loopEnd = Math.max(codeIndex, loopEnd);
                    // 아래에서 1 더해주기 때문에 여기서 더해주지 않음
                    codeIndex = bracketMap.get(codeIndex);
                }
            } else if (code == ',') {
                arr[pointer] = inputIndex == inputSize ? 255 : inputs[inputIndex++];
            }

            // 명령어를 다 수행했을 경우
            if (++codeIndex >= codeSize) {
                return "Terminates";
            }
            if (++runCount >= 50000000) {
                return "Loops " + bracketMap.get(loopEnd) + " " + loopEnd;
            }
        }
    }

    // [ or ] 일 때 짝을 이루는 괄호의 인덱스를 구한다.
    public static void setBracketMap() {
        bracketMap = new HashMap<>();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < codeSize; i++) {
            if (codes[i] == '[') {
                stack.push(i);
            } else if (codes[i] == ']') {
                int openIndex = stack.pop();
                bracketMap.put(i, openIndex);
                bracketMap.put(openIndex, i);
            }
        }
    }
}
