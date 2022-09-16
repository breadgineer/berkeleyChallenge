import java.util.Iterator;
import java.util.NoSuchElementException;

public class OHIterator implements Iterator<OHRequest> {
    OHRequest curr;

    public OHIterator(OHRequest queue) {
    }

    public boolean isGood(String description) {
        return description != null && description.length() > 5;

    }

    @Override
    public boolean hasNext() {
        OHRequest curru = curr;
        while (curru != null && !isGood(curr.description)) {
            curru = curru.next;
        }
        return curru != null;
    }


    @Override
    public OHRequest next() {

        if (!hasNext()) {
            throw new NoSuchElementException();
        };
        OHRequest currentElement = this.curr;
        curr = curr.next;
        return currentElement;
    }
}
