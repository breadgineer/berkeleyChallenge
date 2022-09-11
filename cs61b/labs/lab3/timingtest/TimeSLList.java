package timingtest;
import edu.princeton.cs.algs4.Stopwatch;

/**
 * Created by hug.
 */
public class TimeSLList {
    private static void printTimingTable(AList<Integer> Ns, AList<Double> times, AList<Integer> opCounts) {
        System.out.printf("%12s %12s %12s %12s\n", "N", "time (s)", "# ops", "microsec/op");
        System.out.printf("------------------------------------------------------------\n");
        for (int i = 0; i < Ns.size(); i += 1) {
            int N = Ns.get(i);
            double time = times.get(i);
            int opCount = opCounts.get(i);
            double timePerOp = time / opCount * 1e6;
            System.out.printf("%12d %12.2f %12d %12.2f\n", N, time, opCount, timePerOp);
        }
    }

    public static void main(String[] args) {
        timeGetLast();
    }

    public static void timeGetLast() {
//        AList<Integer> Ns = new AList<>();
//        AList<Double> times = new AList<>() ;
//        AList<Integer> opCounts = new AList<>() ;
//
//        int i = 1;
//
//        while (i < 500) {
//            Ns.addLast(1000*i);
//            opCounts.addLast(10000);
//            i = i * 2;
//        }


        AList<Integer> Ns = new AList<>();
        AList<Double> times = new AList<>() ;
        AList<Integer> opCounts = new AList<>() ;
        int i = 1;
        while (i < 100) {
            Ns.addLast(1000*i);
            opCounts.addLast(10000);
            i = i * 2;
        }
        for (int index = 0; index < Ns.size(); index++) {
            int j = 0;

            SLList<Integer> timeTest = new SLList<>();
            while (j<Ns.get(index) && Ns.get(index) != null) {
                timeTest.addLast(1);
                j++;
            }
            int k = 0;
            Stopwatch stopwatch = new Stopwatch();
            while (k < opCounts.get(index)) {
                timeTest.getLast();
                k++;
            }
            Double timeInSeconds = stopwatch.elapsedTime();
            times.addLast(timeInSeconds);
        }

        printTimingTable(Ns, times, opCounts);
    }




}
