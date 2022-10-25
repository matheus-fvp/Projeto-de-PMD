class User: 
    
    def __init__(self, id, nome, telefone, email, anuncios_feitos=None, anuncios_recebidos=None):
        self.Id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.anuncios_feitos = anuncios_feitos
        self.anuncios_recebidos = anuncios_recebidos
    
    def anunciar(self, book_ad):
        if book_ad is not None:
            self.meus_anuncios.append(book_ad);
    
    def receber_anuncio(self, book_ad):
        if book_ad is not None:
            self.amigos_anuncios.append(book_ad)