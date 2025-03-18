
public class Test {
    public static void main(String[] args) {
        CasellaPosta casella = new CasellaPosta();

        Thread scrittore = new Scrittore(casella);
        Thread lettore = new Lettore(casella);

        scrittore.start();
        lettore.start();
    }
}
