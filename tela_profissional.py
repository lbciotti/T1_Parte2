class TelaProfissional:
    """Tela para operações de Profissional."""

    def mostrar_opcoes(self) -> int:
        print("\n--- PROFISSIONAIS ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return int(input("Opção: "))

    def pegar_dados_profissional(self) -> dict:
        print("\n--- Dados do Profissional ---")
        nome     = input("Nome: ")
        celular  = input("Celular: ")
        cpf      = input("CPF: ")
        esp      = input("Especialidade: ")
        registro = input("Registro profissional (CRM/CRO/etc): ")
        return {"nome": nome, "celular": celular, "cpf": cpf,
                "especialidade": esp, "registro_profissional": registro}

    def pegar_cpf(self) -> str:
        return input("CPF do profissional: ")

    def mostrar_profissionais(self, lista: list):
        if not lista:
            print("Nenhum profissional cadastrado.")
            return
        print("\n--- Profissionais cadastrados ---")
        for p in lista:
            print(f"  {p.nome} | {p.especialidade} | Reg: {p.registro_profissional}")

    def mostrar_mensagem(self, msg: str):
        print(f"\n{msg}")
