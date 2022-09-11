package timingtest;
import edu.princeton.cs.algs4.Stopwatch;

/**
 * Created by hug.
 */
public class TimeAList {
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
        timeAListConstruction();
    }

    public static void timeAListConstruction() {
        // TODO: YOUR CODE HERE
        AList<Integer> Ns = new AList<>();
        AList<Double> times = new AList<>() ;
        AList<Integer> opCounts = Ns ;
        int i = 1;
        while (i < 500) {
            Ns.addLast(1000*i);
            i = i * 2;
        }
        for (int index = 0; index < Ns.size(); index++) {
            int j = 0;
            Stopwatch stopwatch = new Stopwatch();
            AList<Integer> timeTest = new AList<>();
            while (j<Ns.get(index) && Ns.get(index) != null) {
                timeTest.addLast(1);
                j++;
            }
            Double timeInSeconds = stopwatch.elapsedTime();
            times.addLast(timeInSeconds);
        }

        printTimingTable(Ns, times, opCounts);
    }
}
