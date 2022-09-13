package deque;

import java.util.Iterator;

public class LinkedListDeque<T> implements Deque {

    private class SimpleList {
        private T item;
        private SimpleList next;
        private SimpleList prev;

        public SimpleList(T item, SimpleList prev, SimpleList next) {
            this.item = item;
            this.prev = prev;
            this.next = next;
        }
    }
    private SimpleList sentinel;
    private int size;

    public LinkedListDeque() {
        sentinel = new SimpleList(null, null, null);
        sentinel.next = sentinel;
        sentinel.prev = sentinel;
        size = 0;

    }

    @Override
    public void addFirst(Object item) {
        size++;
        sentinel.next = new SimpleList((T) item,sentinel, sentinel.next);
        sentinel.next.next.prev = sentinel.next;


    }

    @Override
    public void addLast(Object item) {
        size++;
        sentinel.prev.next = new SimpleList((T) item, sentinel.prev, sentinel);
        sentinel.prev = sentinel.prev.next;


    }

    @Override
    public boolean isEmpty() {
        return sentinel.prev.item == null && sentinel.next.item == null;
    }

    @Override
    public int size() {
        return this.size;
    }

    @Override
    public void printDeque() {
        SimpleList p = sentinel.next;

        for (int i = 0; i < this.size; i++) {
            if (i == this.size - 1) {
                System.out.print(p.item);
            } else {
                System.out.print(p.item + "<->");
            }
            p=p.next;
        }
        System.out.println();

    }

    public void printDeque(int x) {
        SimpleList p = sentinel.next;

        for (int i = 0; i < x; i++) {
            if (i == x - 1) {
                System.out.print(p.item);
            } else {
                System.out.print(p.item + "<->");
            }
            p = p.next;
        }
        System.out.println();

    }

    @Override
    public Object removeFirst() {
        if (this.size == 0) {
            return null;
        }
        size --;
        T deletedItem = sentinel.next.item;
        sentinel.next.item = null;
        sentinel.next = sentinel.next.next;
        sentinel.next.next.prev = sentinel;
        return deletedItem;
    }

    @Override
    public Object removeLast() {
        if (this.size == 0) {
            return null;
        }
        size --;
        T deletedItem = sentinel.prev.item;
        sentinel.prev.item = null;
        sentinel.prev = sentinel.prev.prev;
        sentinel.prev.prev.next = sentinel;
        return deletedItem;
    }

    @Override
    public Object get(int index) {

        if (index < 0 || index > this.size - 1) {
            return null;
        }

        SimpleList p = sentinel;
        for (int i = 0; i <= index; i++) {
            p = p.next;
        }
        return p.item;
    }

}
