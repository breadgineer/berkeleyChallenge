package deque;

public class ArrayDeque<T> implements Deque{

    T[] items;
    int size, maxArraySize, resizeFactor;


    public ArrayDeque() {
        this.maxArraySize = 8;
        this.items = (T[]) new Object[maxArraySize];
        this.size = 0;
        this.resizeFactor = 2;
    }

    private void resizeUp() {
            this.maxArraySize = this.maxArraySize * this.resizeFactor;
            T[] sizeAdjustedArray = (T[]) new Object[this.maxArraySize];
            System.arraycopy(this.items,0, sizeAdjustedArray, 0, this.size);
            this.items = sizeAdjustedArray;
        }
    private void resizeDown() {
            this.maxArraySize = this.maxArraySize / this.resizeFactor;
            T[] sizeAdjustedArray = (T[]) new Object[this.maxArraySize];
            System.arraycopy(this.items,0, sizeAdjustedArray, 0, this.size);
            this.items = sizeAdjustedArray;
        }




    @Override
    public void addFirst(Object item) {
        if (this.size == this.maxArraySize) {
            resizeUp();
        }
        if (size>0) {System.arraycopy(this.items, 0, this.items, 1, size);}
        this.items[0] = (T) item;
        size++;
    }

    @Override
    public void addLast(Object item) {
        if (this.size == this.maxArraySize) {
            resizeUp();
        }
        this.items[this.size] = (T) item;
        size ++;

    }

    @Override
    public boolean isEmpty() {
        return (this.size == 0 || this.items[0] == null);
    }

    @Override
    public int size() {
        return this.size;
    }

    @Override
    public void printDeque() {
        StringBuilder stringArray = new StringBuilder("[ ");
        for (T item : this.items) {
            if (item == null){ break; }
            stringArray.append(item);
            stringArray.append(" ");
        }
        stringArray.append("]");
        System.out.println(stringArray);
    }

    @Override
    public Object removeFirst() {
        if (isEmpty()) {
            return null;
        }
        T removed = this.items[0];
        T[] pArray = (T[]) new Object[this.maxArraySize];
        System.arraycopy(this.items, 1, pArray, 0, size-1 );
        this.items = pArray;
        size--;
        if (this.size == (this.maxArraySize/this.resizeFactor)) {
            resizeDown();
        }

        return removed;
    }

    @Override
    public Object removeLast() {
        if (isEmpty()) {
            return null;
        }
        T removed = this.items[size-1];
        T[] pArray = (T[]) new Object[this.maxArraySize];
        System.arraycopy(this.items, 0, pArray, 0, size-1 );
        this.items = pArray;
        size--;
        if (this.size == (this.maxArraySize/this.resizeFactor)) {
            resizeDown();
        }

        return removed;
    }

    @Override
    public Object get(int index) {
        T arrayItem = this.items[index];
        return arrayItem;
    }
}
