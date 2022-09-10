import java.util.Arrays;

public class FillGrid {

    public static void fillGrid(int[] LL, int[] UR, int[][] S) {
        int N = S.length; //5
        int kL, kR;
        kL = kR = 0;
        for (int row = 0; row < N; row += 1) {
            for (int col = 0; col < N; col += 1) {
                if (row == col) {
                    S[row][col] = 0;
                } else if (col > row) {
                    S[row][col] = UR[kR];
                    kR++;
                } else {
                    S[row][col] = LL[kL];
                    kL++;
                }



            }

        }
    }

    public static void main(String[] args) {
        int[] LL = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0 };
        int[] UR = { 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 };
        int[][] S = {
                { 0, 0, 0, 0, 0},
                { 0, 0, 0, 0, 0},
                { 0, 0, 0, 0, 0},
                { 0, 0, 0, 0, 0},
                { 0, 0, 0, 0, 0}
        };
        fillGrid( LL, UR, S);
        for(int[] i:S) {
            System.out.println(Arrays.toString(i));



        }

    }

}
