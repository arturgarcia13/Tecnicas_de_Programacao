class UJCException(Exception):
    """
    Exceção levantada quando se tenta cadastrar um usuário com um nome já existente.
    """
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f'Erro: O usuário "{self.usuario}" já foi cadastrado.')


class UNCException(Exception):
    """
    Exceção levantada quando o perfil do usuário informado não existe.
    """
    def __init__(self, perfil):
        self.perfil = perfil
        super().__init__(f'Erro: O perfil informado ({self.perfil}) não existe.')


class PEException(Exception):
    """
    Exceção levantada quando já existe um perfil com o mesmo nome de usuário.
    """
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f'Erro: O nome de usuário "{self.usuario}" já existe.')


class PDException(Exception):
    """
    Exceção levantada quando o perfil do usuário existe, mas está inativo.
    """
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f'Erro: O usuário "{self.usuario}" existe, mas foi desativado.')


class PIException(Exception):
    """
    Exceção levantada quando o perfil do nome de usuário informado não existe.
    """
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f'Erro: O nome de usuário "{self.usuario}" não existe.')


class MFPException(Exception):
    """
    Exceção levantada quando a mensagem não está dentro do limite de 1 a 140 caracteres.
    """
    def __init__(self, mensagem):
        self.tamanho = len(mensagem)
        super().__init__(f'Erro: A mensagem excedeu o limite de caracteres (1 a 140). '
                         f'Tamanho atual: {self.tamanho} caracteres.')


class SIException(Exception):
    """
    Exceção levantada quando o nome de usuário do seguidor é o mesmo do seguido.
    """
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f'Erro: O usuário "{self.usuario}" não pode seguir a si mesmo.')
