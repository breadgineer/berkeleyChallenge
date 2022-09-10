public class IntList {
    public int first;
    public IntList rest;
    public IntList (int f, IntList r) {
        this.first = f;
        this.rest = r;
    }

    public static void evenOdd(IntList lst) {

        int max = 0;
        IntList _lst = lst;

        while (_lst.rest != null) {
            max = 0;
            sortIntList(_lst, max);
            _lst = _lst.rest;
        }

    }

    private static void sortIntList(IntList lst, int max) {
        if (lst.rest == null) {
            lst.first = max;
            return;
        } else if (lst.first > max) {
            max = lst.first;
            sortIntList(lst.rest, max);
        } else {
            sortIntList(lst.rest,max);
        }
    }



public static IntList[] partition(IntList lst, int k) {
        IntList[] array = new IntList[k];
        int index = 0;
        IntList L = reverse(lst);
        while (L != null) {
            IntList prevAtIndex = array[index];
            IntList next = L.rest;
            array[index] = L;
            array[index].rest = prevAtIndex;
             L = next;
             index = (index + 1) % array.length;
             }
         return array;
         }


    public static void main(String[] args) {

        IntList lst = new IntList(1, null);
         lst = new IntList(3, lst);
         lst = new IntList(2, lst);
         lst = new IntList(5, lst);
        evenOdd( lst);

        System.out.println(lst.first);
        System.out.println(lst.rest.first);
        System.out.println(lst.rest.rest.first);
        System.out.println(lst.rest.rest.rest.first);
    }
    }