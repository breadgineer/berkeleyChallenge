class Book {
    public static String title;
    public Library library;
    public static Book last = null;
    public Book(String name) {
        title = name;
        last = this;
        library = null;
    }
    public static String lastBookTitle() {
        return last.title;
    }
    public static String getTitle() {
        return title;
    }
}