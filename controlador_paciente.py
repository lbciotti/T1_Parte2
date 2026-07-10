from model.models import Paciente
from view.tela_paciente import TelaPaciente


class ControladorPaciente:
    """Controlador responsável pelo CRUD de Pacientes."""

    def __init__(self):
        self.__pacientes: list[Paciente] = []
        self.__tela = TelaPaciente()

    def abrir_menu(self):
        while True:
            try:
                op = self.__tela.mostrar_opcoes()
                if op == 0:
                    break
                elif op == 1:
                    self.incluir_paciente()
                elif op == 2:
                    self.alterar_paciente()
                elif op == 3:
                    self.excluir_paciente()
                elif op == 4:
                    self.listar_pacientes()
                else:
                    self.__tela.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")

    def incluir_paciente(self):
        dados = self.__tela.pegar_dados_paciente()
        if self.buscar_por_cpf(dados["cpf"]):
            self.__tela.mostrar_mensagem("Já existe um paciente com esse CPF.")
            return
        paciente = Paciente(**dados)
        self.__pacientes.append(paciente)
        self.__tela.mostrar_mensagem(f"Paciente '{paciente.nome}' incluído.")

    def alterar_paciente(self):
        self.listar_pacientes()
        cpf = self.__tela.pegar_cpf()
        paciente = self.buscar_por_cpf(cpf)
        if not paciente:
            self.__tela.mostrar_mensagem("Paciente não encontrado.")
            return
        self.__pacientes.remove(paciente)
        dados = self.__tela.pegar_dados_paciente()
        self.__pacientes.append(Paciente(**dados))
        self.__tela.mostrar_mensagem("Paciente alterado com sucesso.")

    def excluir_paciente(self):
        self.listar_pacientes()
        cpf = self.__tela.pegar_cpf()
        paciente = self.buscar_por_cpf(cpf)
        if not paciente:
            self.__tela.mostrar_mensagem("Paciente não encontrado.")
            return
        self.__pacientes.remove(paciente)
        self.__tela.mostrar_mensagem("Paciente excluído.")

    def listar_pacientes(self):
        self.__tela.mostrar_pacientes(self.__pacientes)

    def buscar_por_cpf(self, cpf: str):
        for p in self.__pacientes:
            if p.cpf == cpf:
                return p
        return None

    def get_pacientes(self) -> list:
        return list(self.__pacientes)
