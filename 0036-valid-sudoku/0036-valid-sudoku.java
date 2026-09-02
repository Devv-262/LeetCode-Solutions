class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            HashSet<Character> row = new HashSet<>();
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '.') 
                    continue;
                if (row.contains(board[i][j])) {
                    return false;
                }
                row.add(board[i][j]);
            }
        }
        for (int j = 0; j < board[0].length; j++) {
            HashSet<Character> column = new HashSet<>();
            for (int i = 0; i < board.length; i++) {
                if (board[i][j] == '.')
                    continue;
                if (column.contains(board[i][j])) {
                    return false;
                }
                column.add(board[i][j]);
            }
        }
        for (int boxRow = 0; boxRow < 9; boxRow += 3) {
            for (int boxCol = 0; boxCol < 9; boxCol += 3) {
                HashSet<Character> box = new HashSet<>();
                for (int i = boxRow; i < boxRow + 3; i++) {
                    for (int j = boxCol; j < boxCol + 3; j++) {

                        if (board[i][j] == '.')
                            continue;

                        if (box.contains(board[i][j])) {
                            return false;
                        }
                        box.add(board[i][j]);
                    }
                }
            }
        }

        return true;
    }
}