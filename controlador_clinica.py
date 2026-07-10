from model.models import Clinica
from view.tela_clinica import TelaClinica


class ControladorClinica:
    """Controlador responsável pelo CRUD de Clínicas."""

    def __init__(self):
        self.__clinicas: list[Clinica] = []
        self.__tela = TelaClinica()

    def abrir_menu(self):
        while True:
            try:
                op = self.__tela.mostrar_opcoes()
                if op == 0:
                    break
                elif op == 1:
                    self.incluir_clinica()
                elif op == 2:
                    self.alterar_clinica()
                elif op == 3:
                    self.excluir_clinica()
                elif op == 4:
                    self.listar_clinicas()
                else:
                    self.__tela.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")

    def incluir_clinica(self):
        dados = self.__tela.pegar_dados_clinica()
        if self.buscar_por_nome(dados["nome"]):
            self.__tela.mostrar_mensagem("Já existe uma clínica com esse nome.")
            return
        clinica = Clinica(**dados)
        self.__clinicas.append(clinica)
        self.__tela.mostrar_mensagem(f"Clínica '{clinica.nome}' incluída com sucesso.")

    def alterar_clinica(self):
        self.listar_clinicas()
        nome = self.__tela.pegar_nome()
        clinica = self.buscar_por_nome(nome)
        if not clinica:
            self.__tela.mostrar_mensagem("Clínica não encontrada.")
            return
        self.__clinicas.remove(clinica)
        dados = self.__tela.pegar_dados_clinica()
        nova = Clinica(**dados)
        self.__clinicas.append(nova)
        self.__tela.mostrar_mensagem("Clínica alterada com sucesso.")

    def excluir_clinica(self):
        self.listar_clinicas()
        nome = self.__tela.pegar_nome()
        clinica = self.buscar_por_nome(nome)
        if not clinica:
            self.__tela.mostrar_mensagem("Clínica não encontrada.")
            return
        self.__clinicas.remove(clinica)
        self.__tela.mostrar_mensagem(f"Clínica '{nome}' excluída.")

    def listar_clinicas(self):
        self.__tela.mostrar_clinicas(self.__clinicas)

    def buscar_por_nome(self, nome: str):
        for c in self.__clinicas:
            if c.nome.lower() == nome.lower():
                return c
        return None

    def get_clinicas(self) -> list:
        return list(self.__clinicas)
