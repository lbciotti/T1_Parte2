from model.models import Profissional
from view.tela_profissional import TelaProfissional


class ControladorProfissional:
    """Controlador responsável pelo CRUD de Profissionais."""

    def __init__(self):
        self.__profissionais: list[Profissional] = []
        self.__tela = TelaProfissional()

    def abrir_menu(self):
        while True:
            try:
                op = self.__tela.mostrar_opcoes()
                if op == 0:
                    break
                elif op == 1:
                    self.incluir_profissional()
                elif op == 2:
                    self.alterar_profissional()
                elif op == 3:
                    self.excluir_profissional()
                elif op == 4:
                    self.listar_profissionais()
                else:
                    self.__tela.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")

    def incluir_profissional(self):
        dados = self.__tela.pegar_dados_profissional()
        if self.buscar_por_cpf(dados["cpf"]):
            self.__tela.mostrar_mensagem("Já existe um profissional com esse CPF.")
            return
        prof = Profissional(**dados)
        self.__profissionais.append(prof)
        self.__tela.mostrar_mensagem(f"Profissional '{prof.nome}' incluído.")

    def alterar_profissional(self):
        self.listar_profissionais()
        cpf = self.__tela.pegar_cpf()
        prof = self.buscar_por_cpf(cpf)
        if not prof:
            self.__tela.mostrar_mensagem("Profissional não encontrado.")
            return
        self.__profissionais.remove(prof)
        dados = self.__tela.pegar_dados_profissional()
        self.__profissionais.append(Profissional(**dados))
        self.__tela.mostrar_mensagem("Profissional alterado.")

    def excluir_profissional(self):
        self.listar_profissionais()
        cpf = self.__tela.pegar_cpf()
        prof = self.buscar_por_cpf(cpf)
        if not prof:
            self.__tela.mostrar_mensagem("Profissional não encontrado.")
            return
        self.__profissionais.remove(prof)
        self.__tela.mostrar_mensagem("Profissional excluído.")

    def listar_profissionais(self):
        self.__tela.mostrar_profissionais(self.__profissionais)

    def buscar_por_cpf(self, cpf: str):
        for p in self.__profissionais:
            if p.cpf == cpf:
                return p
        return None

    def get_profissionais(self) -> list:
        return list(self.__profissionais)
