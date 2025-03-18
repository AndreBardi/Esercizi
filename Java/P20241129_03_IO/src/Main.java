import java.io.IOException;
import java.lang.Character.UnicodeScript;
import java.util.LinkedList;
import java.util.Locale;

public class Main {

    public static void main(String[] args) throws IOException {

        // Create una lista con 10 elementi Wifi casuali
        LinkedList<WiFi> lwifi = new LinkedList<WiFi>();
        for (int i = 0; i < 10; i++) {
            lwifi.add(WiFi.MakeWifi());
        }

        System.out.println(lwifi);
        
       

        // Domanda:La potreste stampare in formato CSV poiché
        // dobbiamo passarla al vostro collega Onisa?
        for (var x : lwifi) {
            String a = String.format("%s,%s,%s,%f\n", 
                    x.getId(), x.getProtocollo(), x.getPassword(), x.getFrequenza());
            System.out.print(a);

            System.out.printf("%s,%s,%s,%f\n", 
                    x.getId(), x.getProtocollo(), x.getPassword(), x.getFrequenza());
        }
        var fou = Util.OpenFileForWriting("wifi.dat");
        for(var x : lwifi) {
            String a = String.format("%s,%s,%s,%f\n", x.getId(), x.getProtocollo(), x.getPassword(), x.getFrequenza());
            fou.write(a);
        }
        fou.close();
        lwifi.clear();
        var fin = Util.OpenFileForReading("wifi.dat");
        String riga = fin.readLine();
        while (riga != null) {
        	System.out.println(riga);
        	riga = fin.readLine();
        }
        fin.close();
    }

}
