class TelaMenuPrincipal:
    """Tela do menu principal do sistema."""

    def mostrar_opcoes(self) -> int:
        print("\n===== SISTEMA DE GERENCIAMENTO DE CLÍNICAS =====")
        print("1 - Clínicas")
        print("2 - Pacientes")
        print("3 - Profissionais")
        print("4 - Tipos de Atendimento")
        print("5 - Atendimentos")
        print("6 - Pagamentos")
        print("7 - Relatórios")
        print("0 - Sair")
        return int(input("Opção: "))

    def mostrar_mensagem(self, msg: str):
        print(f"\n{msg}")
