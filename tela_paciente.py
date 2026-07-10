from datetime import date


class TelaPaciente:
    """Tela para operações de Paciente."""

    def mostrar_opcoes(self) -> int:
        print("\n--- PACIENTES ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return int(input("Opção: "))

    def pegar_dados_paciente(self) -> dict:
        print("\n--- Dados do Paciente ---")
        nome    = input("Nome: ")
        celular = input("Celular: ")
        cpf     = input("CPF: ")
        nasc    = input("Data de nascimento (AAAA-MM-DD): ")
        d = date(*map(int, nasc.split("-")))
        return {"nome": nome, "celular": celular, "cpf": cpf, "data_nascimento": d}

    def pegar_cpf(self) -> str:
        return input("CPF do paciente: ")

    def mostrar_pacientes(self, lista: list):
        if not lista:
            print("Nenhum paciente cadastrado.")
            return
        print("\n--- Pacientes cadastrados ---")
        for p in lista:
            print(f"  {p.nome} | CPF: {p.cpf} | {p.idade} anos")

    def mostrar_mensagem(self, msg: str):
        print(f"\n{msg}")
