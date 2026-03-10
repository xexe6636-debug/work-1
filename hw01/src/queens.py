"""
N-Queens Problem Solver
使用回溯法（Backtracking）求解 N 皇后问题。
"""


def solve_n_queens(n: int) -> list[list[int]]:
    """
    求解 N 皇后问题，返回所有合法摆放方案。

    Args:
        n: 棋盘大小（N×N），同时也是皇后数量

    Returns:
        所有解的列表，每个解是长度为 n 的列表，
        其中 solution[row] = col 表示第 row 行的皇后放在第 col 列。

    Example:
        >>> solutions = solve_n_queens(4)
        >>> len(solutions)
        2
    """
    solutions = []
    board = [-1] * n  # board[row] = col，表示每行皇后所在的列

    def is_safe(row: int, col: int) -> bool:
        """检查在 (row, col) 放置皇后是否安全。"""
        for prev_row in range(row):
            prev_col = board[prev_row]
            # 同列冲突
            if prev_col == col:
                return False
            # 对角线冲突：行差等于列差
            if abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row: int) -> None:
        """从第 row 行开始递归回溯。"""
        if row == n:
            # 找到一个完整解，记录
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # 回溯：撤销选择

    backtrack(0)
    return solutions


def format_board(solution: list[int]) -> str:
    """
    将一个解格式化为棋盘字符串，便于可视化。

    Args:
        solution: 皇后位置列表

    Returns:
        可打印的棋盘字符串
    """
    n = len(solution)
    rows = []
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        rows.append(line.strip())
    return "\n".join(rows)


if __name__ == "__main__":
    for n in [4, 8]:
        solutions = solve_n_queens(n)
        print(f"\n{'='*40}")
        print(f"N={n} 共有 {len(solutions)} 个解")
        print(f"{'='*40}")
        if solutions:
            print(f"\n第一个解：\n{format_board(solutions[0])}")
