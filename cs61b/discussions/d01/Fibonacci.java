public class Fibonacci {

    public static int fib(int n) {
        if (n==0){
            return 1;
        } else if (n == 1) {
            return 1;
        } else {
            return n + fib(n - 1);
        }
    }


    public static void main(String[] args) {
        System.out.println(fib(2));
    }

}
