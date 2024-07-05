class Document:

    def __init__(self, text) -> None:
        self.text = text

    def getText(self):
        return self.text
    
    def setText(self, text):
        self.text = text
    
    def IsInText(self, p_chiave):
        return p_chiave in self.text
    
class Email(Document):
    def __init__(self, text, mittente, destinatario, titolo) -> None:
        super().__init__(text)

        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo

    def getMittente(self):
        return self.mittente
    def setText(self, mittente):
        self.mittente = mittente
    def getDestinatario(self):
        return self.destinatario
    def setDestinatario(self, destinatario):
        self.destinatario = destinatario
    def getTitolo(self):
        return self.titolo
    def setTitolo(self, titolo):
        self.titolo = titolo

    