public class QuikMaths {

    public static void multiplyBy3(int[] A) {
        for (int x: A) {
            x = x * 3;
        }
        System.out.println(A[0]);
    }

    public static void multiplyBy2(int[] A) {
        int[] B = A;
              for (int i = 0; i < B.length; i+= 1) {
                  B[i] *= 2;
                  }
        System.out.println(A[0]);

              }


      public static void swap(int A, int B ) {
          int temp = B;
          B = A;
          A = temp;
          System.out.println(A);
          System.out.println(B);
      }

      public static void main(String[] args) {
              int[] arr;
              arr = new int[]{2, 3, 3, 4};
              multiplyBy3(arr);

              /* Value of arr: {2, 3, 3, 4} */

              arr = new int[]{2, 3, 3, 4};
              multiplyBy2(arr);

              /* Value of arr: {4, 6, 6, 8} */

              int a = 6;
              int b = 7;
              swap(a, b);
          System.out.println(a);
              /* Value of a: 6 Value of b: 7 */
              }
  }