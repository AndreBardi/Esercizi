
public class TriangoloRettangolo{

	// declare variables/attributes and methods/functions
	private double cat1;
	private double cat2;
	private double hyp;
	private double area;
	private double perimetro;
	public double getArea() {
		return area;
	}
	
	public void setArea(double area) {
		this.area = area;
	}
		
	public double getPerimetro() {
		return perimetro;
	}
	
	public void setPerimetro(double perimetro) {
		this.perimetro = perimetro;
	}
	
	public double getCat1() {
		return cat1;
	}
	public void setCat1(double cat1) {
		this.cat1 = cat1;
		UpdateFunctionalRelations();
	}
	
	private void UpdateFunctionalRelations() {
		hyp = Math.sqrt(cat2*cat2+cat1*cat1);
		area = cat1*cat2 / 2.;
		perimetro = cat1 + cat2 + hyp;		
	}
	
	public double getCat2() {
		return cat2;
	}
	
	public void setCat2( double cat2) {
		this.cat2 = cat2;
		UpdateFunctionalRelations();
	}
	
	public double getHyp() {
		return hyp;
	}
		

	public TriangoloRettangolo(double cat1, double cat2) {
		super();
		this.cat1 = cat1;
		this.cat2 = cat2;
		
		
		hyp = Math.sqrt(cat2 * cat2 + cat1 * cat1);
		area = cat1 * cat2 / cat2;
		perimetro = cat1 + cat2 + hyp;
		
		
		
		
	}
			
	

}
