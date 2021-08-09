# Algorithm Study

- [Visual Studio Code markdown preview](https://code.visualstudio.com/docs/languages/markdown)
    - Ctrl + Shift + V

- `표시되어있는 문제` 다시 풀어보기



- - -
## [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
- [reference blog](https://wayhome25.github.io/python/2017/06/14/time-complexity/)

> ### List

Operation | Big-O | Example
  :---:   | :---: |  :---:
Slice | O(end-start) | list[start:end]
Compare | O(N) | list1 == list2
Insert | O(N) | list.insert(location, value)
Delete | O(N) | del list[index]
Remove | O(N) | list.remove(value)
Containment |	O(N) | target in list
Copy | O(N) | list.copy()
Extreme value | O(N) | min(list) / max(list)
Reverse | O(N) | list.reverse()
Sort | O(NlogN) | list.sort()  


- - -
- - -
## BaekJoon

> ### - BFS & DFS
- 1260 (DFS와 BFS)  
  : dfs와 bfs를 구현하는 기본 문제

- 2178 (미로 탐색)  
  : bfs를 이용한 미로찾기  

- 2606 (바이러스)  
  : dfs를 이용해 연결된 노드의 수 구하기  

- 2667 (단지번호붙이기)  
  : dfs를 이용해 2차원 행렬 내 1로 연결된 단지의 수, 각 단지 내의 1 개수 구하기  

- 2644 (촌수계산)  
  : bfs를 이용해 노드 간 최단거리 구하기  

- `7569 (토마토)`  
  : bfs를 이용한 탐색 최소 시간 구하기  
  -> 메모리 제한 주의  

- 7576 (토마토)  
  : bfs를 이용한 탐색 최소 시간 구하기  

- `1697 (숨바꼭질)`  
  : bfs를 이용한 탐색 최소 시간 구하기  
  -> 메모리, 시간 줄이는 방법 생각  

- 5014 (스타트링크)  
  : bfs를 이용한 탐색 최소 시간 구하기  

- 2468 (안전 영역)  
  : dfs를 이용해 행렬에서 섬 영역이 가장 많아질 때의 섬 영역 개수 구하기  

- 10451 (순열 사이클)  
  : dfs를 이용해 사이클의 개수 구하기  

- 9466 (텀 프로젝트)  
  : dfs를 이용해 팀에 속하지 않는 학생 수 구하기  
  -> 시간초과 주의  

- 4963 (섬의 개수)  
  : dfs를 이용해 섬의 개수 구하기  

- 7576 (토마토)  
  : bfs를 이용한 탐색 최소 시간 구하기  
  -> 시간초과 주의  
  -> 2021-05-19 재채점 결과 런타임 에러 발생으로 2021-05-20 재풀이  

- 2146 (다리 만들기)  
  : bfs를 이용한 섬과 섬을 잇는 최단 경로 구하기  

- 5427 (불)  
  : bfs를 이용해 불과 만나지 않는 탈출 경로 구하기  
  -> 다양한 테스트 케이스 실행 필요  

- 1068 (트리)  
  : dfs를 이용해 리프 노드 개수 구하기  

- `5719 (거의 최단 경로)`  
  : 다익스트라 알고리즘과 bfs를 사용해 두 번째 최단 경로 구하기 

- `9205 (맥주 마시면서 걸어가기)`  
  : bfs를 사용해 목적지까지 도착 가능 여부 찾기

- `2573 (빙산)`  
  : 빙산이 녹아서 분리되는 최초의 시간 구하기  
  -> 현재 python 시간초과로 pypy3 으로 제출

- 1012 (유기농 배추)  
  : bfs나 dfs를 사용해 영역의 개수 구하기

- 11724 (연결 요소의 개수)  
  : dfs를 사용해 연결된 요소 집합의 수 구하기  
  -> 간선에 연결되지 않은 노드도 하나의 집합으로 여긴다.

- 2583 (영역 구하기)  
  : bfs를 사용해 영역의 수 구하기  

- `7562 (나이트의 이동)`  
  : bfs를 이용해 목적지로 이동할 수 있는 최소 시간 구하기  
  `-> 목적지를 현재 위치의 가까이로 변경해 풀이 시간 단축 가능`  

- `9019 (DSLR)`  
  : bfs를 이용해 4개의 연산을 통해 목적 숫자까지의 최소 연산 구하기  
  `-> pypy3로 제출, python3 시간초과`  



> ### - Union Find
- 16562 (친구비)  
  : union find를 이용해 최소 친구 비용 구하기  


> ### - MST(Minimum Spanning Tree, 최소 신장 트리)
- 1922 (네트워크 연결)  
  : 크루스칼(& Union Find)을 이용해 컴퓨터들을 연결하는 데 드는 최소 비용 구하기

- 6497 (전력난)  
  : 프림 알고리즘을 이용해 도시들을 연결하는 최소 거리 구하기


> ### - Dijkstra
- 1753 (최단경로)  
  : 기본 다익스트라 알고리즘  

- 1916 (최소비용 구하기)  
  : 기본 다익스트라 알고리즘  

- 1238 (파티)  
  : 다익스트라 알고리즘을 사용해 왕복 최단거리 중 가장 큰 값 찾기  

- `11779 (최소비용 구하기 2)`  
  : 다익스트라 알고리즘을 사용해 최소 비용 경로 구하기  

- 2211 (네트워크 복구)  
  : 다익스트라 알고리즘을 사용해 1번 노드와 모든 노드와의 최소 비용 연결 경로 구하기  

- `5719 (거의 최단 경로)`  
  : 다익스트라 알고리즘과 bfs를 사용해 두 번째 최단 경로 구하기  
  

> ### - Floyd-Warshall
- 11404 (플로이드)  
  : 모든 도시의 쌍에 대해 버스 비용의 최솟값 구하기

- 1956 (운동)  
  : 최소 사이클의 길이의 합 구하기


> ### - Dynamic Programming
- 2839 (설탕 배달)  
- 1463 (1로 만들기)  
- 9095 (1, 2, 3 더하기)  
- 1003 (피보나치 함수)  
- 11726 (2xn 타일링)  
- 11053 (가장 긴 증가하는 부분 수열)  
- 3687 (성냥개비)  
- 2579 (계단 오르기)  
- 1904 (01타일)  
- 1932 (정수 삼각형)  
- 1912 (연속합)  
- 2156 (포도주 시식)  
- `9251 (LCS)`  
- 1446 (지름길)  
- 2193 (이친수)  
- 10844 (쉬운 계단 수)  
- `12865 (평범한 배낭)`  
- 11727 (2xn타일링2)  


> ### - Else
- 2331 (반복수열)  
  : 특정 연산을 통해 반복되는 수를 제외한 나머지 수들 구하기  

- 1000 (A+B)  
  : 기본 입출력  

- 1026 (보물)  
  : 리스트 정렬로 두 리스트의 곱 중 최솟값 구하기  

- 17478 (재귀함수가 뭔가요?)  
  : 재귀함수를 이용한 문자열 출력  

- 1244 (스위치 켜고 끄기)  
  : 구현, 시뮬레이션

- 2493 (탑)  
  : 스택  

- - -
## Programmers

> ### - SQL
- [오랜 기간 보호한 동물(2)](https://programmers.co.kr/learn/courses/30/lessons/59411)  
  : MySQL, Oracle

- [우유와 요거트가 담긴 장바구니](https://programmers.co.kr/learn/courses/30/lessons/62284)  
  : MySQL(INNER JOIN 사용), Oracle(INTERSECT 사용)

- [`입양 시각 구하기(2)`](https://programmers.co.kr/learn/courses/30/lessons/59413)  
  : MySQL(WITH RECURSIVE 사용), Oracle(DUAL, CONNECT BY 사용)

- [`보호소에서 중성화한 동물`](https://programmers.co.kr/learn/courses/30/lessons/59045)  
  : MySQL(INNER JOIN 사용)


> ### - Stack & Queue
- [크레인 인형뽑기 게임](https://programmers.co.kr/learn/courses/30/lessons/64061)  


> ### - Union Find
- [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)  
  : union find 사용해서 네트워크 수 구하기


> ### - Dijkstra
- [가장 먼 노드](https://programmers.co.kr/learn/courses/30/lessons/49189)  
  : dijkstra 알고리즘 사용해서 최단거리 중 가장 멀리 있는 노드의 수 구하기


> ### - Dynamic Programming
- [정수 삼각형](https://programmers.co.kr/learn/courses/30/lessons/43105)  
- [등굣길](https://programmers.co.kr/learn/courses/30/lessons/42898)  
- [도둑질](https://programmers.co.kr/learn/courses/30/lessons/42897)  


> ### - Greedy
- [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)  


> ### - Else
- 다단계 칫솔 판매  



- - -
## LeetCode

> ### - DFS & BFS
- [200. number of islands](https://leetcode.com/problems/number-of-islands)  
  -> Submission Detail : https://leetcode.com/submissions/detail/477283404/  
  : dfs 사용해서 섬의 개수 구하기  

- [17. letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)  
  -> Submission 1 Detail : https://leetcode.com/submissions/detail/478811528/  
  -> Submission 2 Detail : https://leetcode.com/submissions/detail/465584076/  
  : dfs를 사용해 번호에 해당하는 문자들의 조합 만들기 (1: stack 사용 / 2: 재귀 사용)

- [46. Permutations](https://leetcode.com/problems/permutations)  
  -> Submission 1 Detail : https://leetcode.com/submissions/detail/478906183/  
  -> Submission 2 Detail : https://leetcode.com/submissions/detail/478908313/  
  :  dfs를 사용한 순열 만들기


> ### - Hash Table
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)  
  -> Submission 1 Detail : https://leetcode.com/submissions/detail/478144422/  
  -> Submission 2 Detail : https://leetcode.com/submissions/detail/478146900/  
  : 슬라이딩 윈도우, 투 포인터, 해시 테이블을 사용해 중복된 문자가 없는 가장 긴 부분 문자열 구하기  

> ### - Dynamic Programming
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number)  
  -> Submission Detail : https://leetcode.com/submissions/detail/487938604/  
  : Dynamic Programming을 통해 피보나치 수열 구하기  


- - -
## SW Expert Academy

> ### - Two Pointer  
- 9229 (한빈이와 Spot Mart)  

> ### - Else  
- 1228 (암호문1)  