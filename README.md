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

- 2146 (다리 만들기)  
  : bfs를 이용한 섬과 섬을 잇는 최단 경로 구하기

- 5427 (불)  
  : bfs를 이용해 불과 만나지 않는 탈출 경로 구하기
  -> 다양한 테스트 케이스 실행 필요


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


> ### - Else
- 2331 (반복수열)
  : 특정 연산을 통해 반복되는 수를 제외한 나머지 수들 구하기

- 1000 (A+B)  
  : 기본 입출력

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


> ### - Union Find
- [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)  
  : union find 사용해서 네트워크 수 구하기


> ### - Dynamic Programming
- 정수 삼각형  


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
