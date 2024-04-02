class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0;
        
        // Sum of main diagonal
        for(int i = 0; i < mat.length; i++) {
            sum += mat[i][i];
        }
        
        // Sum of anti-diagonal
        for(int i = 0, j = mat.length - 1; i < mat.length && j >= 0; i++, j--) {
            sum += mat[i][j];
        }
        
        // If matrix size is odd, subtract the value at the center to avoid double counting
        if(mat.length % 2 == 1) {
            int mid = mat.length / 2;
            sum -= mat[mid][mid];
        }
        
        return sum;
    }
}
