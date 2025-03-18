class Carta {
    private String seme;
    private String valore;
    private double punteggio;

    public Carta(String seme, String valore, double punteggio) {
        this.seme = seme;
        this.valore = valore;
        this.punteggio = punteggio;
    }

    public double getPunteggio() {
        return punteggio;
    }

    @Override
    public String toString() {
        return valore + " di " + seme + " (" + punteggio + " punti)";
    }
}
