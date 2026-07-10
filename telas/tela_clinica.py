from datetime import time


class TelaClinica:
    """Tela para operações de Clínica."""

    def mostrar_opcoes(self) -> int:
        print("\n--- CLÍNICAS ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return int(input("Opção: "))

    def pegar_dados_clinica(self) -> dict:
        print("\n--- Dados da Clínica ---")
        nome    = input("Nome: ")
        cidade  = input("Cidade: ")
        descricao = input("Descrição: ")
        h_ab  = input("Horário de abertura (HH:MM): ")
        h_fec = input("Horário de fechamento (HH:MM): ")
        ab  = time(*map(int, h_ab.split(":")))
        fec = time(*map(int, h_fec.split(":")))
        return {"nome": nome, "cidade": cidade, "descricao": descricao,
                "horario_abertura": ab, "horario_fechamento": fec}

    def pegar_nome(self) -> str:
        return input("Nome da clínica: ")

    def mostrar_clinicas(self, lista: list):
        if not lista:
            print("Nenhuma clínica cadastrada.")
            return
        print("\n--- Clínicas cadastradas ---")
        for c in lista:
            print(f"  {c.nome} | {c.cidade} | {c.horario_abertura}-{c.horario_fechamento}")

    def mostrar_mensagem(self, msg: str):
        print(f"\n{msg}")
