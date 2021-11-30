private static int[][] initializeBoard(int[][] board) {
    // TODO Auto-generated method stub
    Random random = new Random();
    int candy1 = 0;
    int candy2 = 0;

    for(int r = 0; r < board.length; r++){
        for(int c = 0; c < board[0].length; c++){
            int candy3 = random.nextInt(5)+1;
            while((candy3 == candy1 && candy3 == candy2) || (r > 2 && candy3 == board[r-1][c] && candy3 == board[r-2][c])){
                candy3 = random.nextInt(5)+1;
            }
            board[r][c] = candy3;
            candy1 = candy2;
            candy2 = candy3;
        }
    }
    
    return board;
}