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



- - -
## Programmers

> ### - SQL
- [오랜 기간 보호한 동물(2)](https://programmers.co.kr/learn/courses/30/lessons/59411)  
  : MySQL, Oracle

> ### - Union Find
- [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)  
  : union find 사용해서 네트워크 수 구하기