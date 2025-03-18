import java.io.*;

public class Contocorrente {
	private String filePath;
	
	public Contocorrente(String filePath) {
	this.filePath = filePath;
	
	}
	
	public double getSaldo() throws IOException {
	BufferedReader br = new BufferedReader(new FileReader(filePath));
	double saldo = Double.parseDouble(br.readLine());
	br.close();
	return saldo;
	
	}
	
	public void prelievoNonSynch(double somma) throws Exception {
	Thread.sleep(3000);
	
	BufferedWriter bw = null;
	FileWriter fw = null;
	
	try {
	double nuovoSaldo = getSaldo() - somma;
	
	if (nuovoSaldo > 0) {
	fw = new FileWriter(filePath);
	bw = new BufferedWriter(fw);
	bw.write(nuovoSaldo + "");
	} else {
	throw new Exception("Saldo insufficiente!");
	}
	} catch (IOException e) {
	e.printStackTrace();
	} finally {
	if (bw != null)
	bw.close();
	if (fw != null)
	fw.close();
	}
	}
	
	public synchronized void prelievo(double somma) throws Exception {
	Thread.sleep(3000);
	
	BufferedWriter bw = null;
	FileWriter fw = null;
	
	try {
	double nuovoSaldo = getSaldo() - somma;
	
	if (nuovoSaldo > 0) {
	fw = new FileWriter(filePath);
	bw = new BufferedWriter(fw);
	bw.write(nuovoSaldo + "");
	} else {
	throw new Exception("Saldo insufficiente!");
	}
	} catch (IOException e) {
	e.printStackTrace();
	} finally {
	if (bw != null)
	bw.close();
	if (fw != null)
	fw.close();
	}
	}
	
	}
