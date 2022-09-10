public class SLList {
    Node sentinel;

   public SLList() {
       this.sentinel = new Node();
   }

   private static class Node {
       int item;
       Node next;
   }

    /*
     * we use the helper method here because we want to hide
     * some abstractions form the user in order to make the
     * method easier to use
     * */


    public int findFirst(int n) {
        return findFirstHelper(n,0, sentinel.next);
   }


   private int findFirstHelper(int n, int index, Node curr) {
       if (curr.next == null) {
           return -1;
           }
       if (n == curr.item) {
           return index;
           } else {
           return findFirstHelper( n, index + 1, curr.next);
           }
       }

           }