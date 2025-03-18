import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class CalcolatriceTest {

	@Test
	void testSomma() {
		Calcolatrice c = new Calcolatrice();
		assertEquals(3, c.somma(2, 1));
		
	}
	@Test
	void testSottrazione() {
		Calcolatrice c = new Calcolatrice();
		assertEquals(1, c.sottrazione(2, 1));
		
	}
	@Test
	void testMoltiplicazione() {
		Calcolatrice c = new Calcolatrice();
		assertEquals(2, c.moltiplicazione(2, 1));
		
	}
	@Test
	void testDivizione() {
		Calcolatrice c = new Calcolatrice();
		assertEquals(1, c.divisione(2, 2));
		
	}

}
