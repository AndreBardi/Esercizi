
public class Cliente {
    private int idCliente;
    private String nome;
    private String cognome;
    private String email;
    private String password;

    public Cliente(int idCliente, String nome, String cognome, String email, String password) {
        this.idCliente = idCliente;
        this.nome = nome;
        this.cognome = cognome;
        this.email = email;
        this.password = password;
    }

    public void acquistaProdotto(Prodotto prodotto) {
        System.out.println(nome + " " + cognome + " ha acquistato: " + prodotto.toString());
    }

    // Getters and Setters
    public int getIdCliente() {
        return idCliente;
    }

    public String getNome() {
        return nome;
    }

    public String getCognome() {
        return cognome;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }
    
}
