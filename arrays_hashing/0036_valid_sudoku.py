class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        brute force: check all rows, then cols, then subgrids

        T: O(n^2) [triple pass]
        S: O(n)   [one set per pass]
        """
        n = len(board)

        # check rows
        for r in range(n):
            seen = set()

            for c in range(n):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False

                seen.add(board[r][c])

        # check cols
        for c in range(n):
            seen = set()

            for r in range(n):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False

                seen.add(board[r][c])

        # check subgrids
        for subgrid in range(n):
            seen = set()

            for row in range(n // 3):
                for col in range(n // 3):
                    r = (subgrid // 3) * (n // 3) + row
                    c = (subgrid % 3) * (n // 3) + col

                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in seen:
                        return False

                    seen.add(board[r][c])
        
        return True


    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        optimization: one-pass

        use sets for each row, column, and sub-grid to determine
        if a value 1-9 has been used already

        whenever we have a conflict (i.e., constraint violation), we
        can conclude the board is automatically invalid

        if all checks pass, then board is valid

        approach: check each position on the grid and confirm that these pass:
            - row doesn't have this value
            - col doesn't have this value
            - subgrid doesn't have this value

        T: O(n^2)
        S: O(n^2)
            - worst-case: grid is filled; each dict has n keys, each with
            a set filled with n values; n*n*3 ~= n^2
        """
        n = len(board)

        # dicts where r/c/sg: set[int]
        rows = dict()
        cols = dict()
        subgrids = dict()

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":  # skip
                    continue

                subgrid = (r // 3, c // 3)

                if r not in rows: rows[r] = set()
                if c not in cols: cols[c] = set()
                if subgrid not in subgrids: subgrids[subgrid] = set()

                val = board[r][c]

                # check that val is not repeated elsewhere
                if (
                    val in rows[r] or
                    val in cols[c] or
                    val in subgrids[subgrid]
                ):
                    return False

                # add val to each set
                rows[r].add(val)
                cols[c].add(val)
                subgrids[subgrid].add(val)

        return True
