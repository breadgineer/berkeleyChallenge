public class Mystery {
    public static int mystery(int[] inputArray, int k) {
         int x = inputArray[k]; //4
         int answer = k; //2
         int index = k + 1; //3
         while (index < inputArray.length) { //5
             if (inputArray[index] < x) {
                 x = inputArray[index];
                 answer = index;
                 }
             index = index + 1;
             }
         return answer;
         }

public static void mystery2(int[] inputArray) {
        int index = 0;
        while (index < inputArray.length) {
            int targetIndex = mystery(inputArray, index);
            int temp = inputArray[targetIndex];
            inputArray[targetIndex] = inputArray[index];
            inputArray[index] = temp;
            index = index + 1;
            }
         }

    public static void main(String[] args) {
        int[] inputArray = {3, 0, 4, 6, 10};
        System.out.println(mystery(inputArray,2));

    }
}
