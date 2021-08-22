import sys
sys.stdin = open("SWExpertAcademy/1974input.txt")

def check(sudoku):
    isCheckForRow = [set() for _ in range(9)]
    for r in range(9):
        isCheckForCol = set()
        for c in range(9):
            if sudoku[r][c] in isCheckForRow[c]:
                return 0
            else:
                isCheckForRow[c].add(sudoku[r][c])

            if sudoku[r][c] in isCheckForCol:
                return 0
            else:
                isCheckForCol.add(sudoku[r][c])
    
    for start_row in range(0, 6 + 1, 3):
        for start_col in range(0, 6 + 1, 3):
            isCheck = set()
            for r in range(start_row, 3 + start_row):
                for c in range(start_col, 3 + start_col):
                    if sudoku[r][c] in isCheck:
                        return 0
                    else:
                        isCheck.add(sudoku[r][c])
    
    return 1

T = int(input()) # 테스트케이스 수
for tc in range(1, T + 1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    print("#" + str(tc), check(sudoku))
