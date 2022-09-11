package randomizedtest;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdRandom;
import org.junit.Assert;
import org.junit.Test;

import java.lang.reflect.Array;
import java.util.ArrayList;

import static org.junit.Assert.*;

/**
 * Created by hug.
 */
public class TestBuggyAList {
    // YOUR TESTS HERE
    @Test
    public void thestThreeAndThreeRemove() {
        AListNoResizing<Integer> correct = new AListNoResizing<>();
        BuggyAList<Integer> broken = new BuggyAList<>();

        correct.addLast(5);
        correct.addLast(10);
        correct.addLast(15);

        broken.addLast(5);
        broken.addLast(10);
        broken.addLast(15);

        assertEquals(correct.size(), broken.size());

        assertEquals(correct.removeLast(), broken.removeLast());
        assertEquals(correct.removeLast(), broken.removeLast());
        assertEquals(correct.removeLast(), broken.removeLast());
    }

    @Test
    public void randomizedTest() {
        AListNoResizing<Integer> L = new AListNoResizing<>();
        BuggyAList<Integer> B = new BuggyAList<>();
        int N = 5000;
        for (int i = 0; i < N; i += 1) {
            int operationNumber = StdRandom.uniform(0, 4);
            if (operationNumber == 0) {
                // addLast
                int randVal = StdRandom.uniform(0, 100);
                L.addLast(randVal);
                B.addLast(randVal);
                System.out.println("addLast(" + randVal + ")");
                assertEquals(L.size(),B.size());
            } else if (operationNumber == 1) {
                // size
                int size = L.size();
                int sizeB = B.size();
                System.out.println("size: " + size);
                assertEquals(L.size(),B.size());
            } else if (operationNumber == 2 && L.size() > 0) {
                //getLast
               int last = L.getLast();
               int lastB = B.getLast();
                System.out.println("addLast() -> " + last);
                assertEquals(last,lastB);
            } else if (operationNumber == 3 && L.size() > 0) {
                //getLast
                int last = L.removeLast();
                int lastB = B.removeLast();
                System.out.println("removeLast() -> " + last);
                assertEquals(last,lastB);
        }}
    }

}

