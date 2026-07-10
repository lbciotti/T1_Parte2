from model.models import TipoAtendimento
from view.tela_tipo_atendimento import TelaTipoAtendimento


class ControladorTipoAtendimento:
    """Controlador responsável pelo CRUD de Tipos de Atendimento."""

    def __init__(self):
        self.__tipos: list[TipoAtendimento] = []
        self.__tela = TelaTipoAtendimento()

    def abrir_menu(self):
        while True:
            try:
                op = self.__tela.mostrar_opcoes()
                if op == 0:
                    break
                elif op == 1:
                    self.incluir_tipo()
                elif op == 2:
                    self.alterar_tipo()
                elif op == 3:
                    self.excluir_tipo()
                elif op == 4:
                    self.listar_tipos()
                else:
                    self.__tela.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")

    def incluir_tipo(self):
        dados = self.__tela.pegar_dados_tipo()
        if self.buscar_por_descricao(dados["descricao"]):
            self.__tela.mostrar_mensagem("Tipo já cadastrado.")
            return
        tipo = TipoAtendimento(**dados)
        self.__tipos.append(tipo)
        self.__tela.mostrar_mensagem(f"Tipo '{tipo.descricao}' incluído.")

    def alterar_tipo(self):
        self.listar_tipos()
        desc = self.__tela.pegar_descricao()
        tipo = self.buscar_por_descricao(desc)
        if not tipo:
            self.__tela.mostrar_mensagem("Tipo não encontrado.")
            return
        self.__tipos.remove(tipo)
        dados = self.__tela.pegar_dados_tipo()
        self.__tipos.append(TipoAtendimento(**dados))
        self.__tela.mostrar_mensagem("Tipo alterado.")

    def excluir_tipo(self):
        self.listar_tipos()
        desc = self.__tela.pegar_descricao()
        tipo = self.buscar_por_descricao(desc)
        if not tipo:
            self.__tela.mostrar_mensagem("Tipo não encontrado.")
            return
        self.__tipos.remove(tipo)
        self.__tela.mostrar_mensagem("Tipo excluído.")

    def listar_tipos(self):
        self.__tela.mostrar_tipos(self.__tipos)

    def buscar_por_descricao(self, descricao: str):
        for t in self.__tipos:
            if t.descricao.lower() == descricao.lower():
                return t
        return None

    def get_tipos(self) -> list:
        return list(self.__tipos)
