"""
N-Queens 问题求解器的单元测试。
运行方式：在 hw01/ 目录下执行 pytest tests/ -v
"""
import sys
import os

# 将 src 目录加入路径，使测试能够导入 queens 模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from queens import solve_n_queens, format_board


# ──────────────────────────────────────────────
# 辅助函数
# ──────────────────────────────────────────────

def is_valid_solution(solution: list[int]) -> bool:
    """验证一个解是否合法（无冲突）。"""
    n = len(solution)
    for i in range(n):
        for j in range(i + 1, n):
            # 同列
            if solution[i] == solution[j]:
                return False
            # 对角线
            if abs(solution[i] - solution[j]) == abs(i - j):
                return False
    return True


# ──────────────────────────────────────────────
# 测试：已知解的数量
# ──────────────────────────────────────────────

class TestSolutionCount:
    """测试各规模下的解数量是否与数学结论一致。"""

    def test_n1(self):
        """N=1 有 1 个解。"""
        assert len(solve_n_queens(1)) == 1

    def test_n2(self):
        """N=2 无解。"""
        assert len(solve_n_queens(2)) == 0

    def test_n3(self):
        """N=3 无解。"""
        assert len(solve_n_queens(3)) == 0

    def test_n4(self):
        """N=4 有 2 个解（核心测试）。"""
        assert len(solve_n_queens(4)) == 2

    def test_n5(self):
        """N=5 有 10 个解。"""
        assert len(solve_n_queens(5)) == 10

    def test_n6(self):
        """N=6 有 4 个解。"""
        assert len(solve_n_queens(6)) == 4

    def test_n7(self):
        """N=7 有 40 个解。"""
        assert len(solve_n_queens(7)) == 40

    def test_n8(self):
        """N=8 有 92 个解（核心测试）。"""
        assert len(solve_n_queens(8)) == 92


# ──────────────────────────────────────────────
# 测试：解的合法性
# ──────────────────────────────────────────────

class TestSolutionValidity:
    """测试每个解是否真正合法（无皇后互相攻击）。"""

    @pytest.mark.parametrize("n", [1, 4, 5, 6, 8])
    def test_all_solutions_valid(self, n):
        """对每个 N，所有解都应通过合法性检验。"""
        solutions = solve_n_queens(n)
        for sol in solutions:
            assert is_valid_solution(sol), f"N={n} 存在非法解: {sol}"

    @pytest.mark.parametrize("n", [1, 4, 5, 6, 8])
    def test_solution_length(self, n):
        """每个解的长度应等于 N。"""
        solutions = solve_n_queens(n)
        for sol in solutions:
            assert len(sol) == n

    @pytest.mark.parametrize("n", [1, 4, 5, 6, 8])
    def test_no_duplicate_solutions(self, n):
        """不应有重复的解。"""
        solutions = solve_n_queens(n)
        unique = {tuple(s) for s in solutions}
        assert len(unique) == len(solutions)


# ──────────────────────────────────────────────
# 测试：N=4 具体解内容
# ──────────────────────────────────────────────

class TestN4Specifics:
    """N=4 的两个已知解：[1,3,0,2] 和 [2,0,3,1]。"""

    def test_n4_known_solutions(self):
        solutions = solve_n_queens(4)
        solution_set = {tuple(s) for s in solutions}
        assert (1, 3, 0, 2) in solution_set
        assert (2, 0, 3, 1) in solution_set

    def test_n4_column_values_in_range(self):
        """列号必须在 [0, N-1] 范围内。"""
        for sol in solve_n_queens(4):
            for col in sol:
                assert 0 <= col < 4


# ──────────────────────────────────────────────
# 测试：format_board 可视化函数
# ──────────────────────────────────────────────

class TestFormatBoard:
    def test_format_n4_first_solution(self):
        """测试 N=4 第一个解的棋盘格式。"""
        solution = [1, 3, 0, 2]
        board = format_board(solution)
        lines = board.split("\n")
        assert len(lines) == 4
        # 第 0 行皇后在列 1
        assert lines[0].split()[1] == "Q"

    def test_format_board_has_one_queen_per_row(self):
        """每行棋盘应恰好有一个 Q。"""
        for sol in solve_n_queens(4):
            board = format_board(sol)
            for line in board.split("\n"):
                assert line.count("Q") == 1
