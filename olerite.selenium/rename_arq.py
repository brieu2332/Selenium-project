import os
import time

def renomear_pdf(download_dir, novo_nome):
    """
    Função para renomear o arquivo PDF baixado no diretório especificado, adicionando um número sequencial.

    Parameters:
    download_dir (str): O diretório onde o arquivo foi salvo.
    novo_nome (str): O novo nome base desejado para o arquivo PDF.

    Retorna:
    str: Caminho completo do arquivo renomeado ou uma mensagem de erro.
    """
    try:
        # Aguardar o download (ajuste o tempo conforme necessário)
        time.sleep(5)

        # Obter os arquivos no diretório
        arquivos = os.listdir(download_dir)
        
        if not arquivos:
            return "Nenhum arquivo encontrado no diretório de download."

        # Ordenar os arquivos por data de modificação
        arquivos.sort(key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)
        
        # Identificar o arquivo mais recente
        arquivo_baixado = arquivos[0]  # Arquivo mais recente
        caminho_arquivo_baixado = os.path.join(download_dir, arquivo_baixado)

        # Verificar se o nome do arquivo já existe com o número sequencial
        num = 1
        novo_nome_com_num = f"{novo_nome}{num}.pdf"  # Formato inicial do nome
        caminho_novo_arquivo = os.path.join(download_dir, novo_nome_com_num)
        
        # Incrementar o número até encontrar um nome único
        while os.path.exists(caminho_novo_arquivo):
            num += 1
            novo_nome_com_num = f"{novo_nome}{num}.pdf"
            caminho_novo_arquivo = os.path.join(download_dir, novo_nome_com_num)

        # Renomear o arquivo
        os.rename(caminho_arquivo_baixado, caminho_novo_arquivo)
        return f"Arquivo renomeado para: {caminho_novo_arquivo}"

    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

# Exemplo de uso
download_dir = r"C:\Users\gabri\Desktop\olerite"  # Diretório de download
novo_nome = "holerite"  # Novo nome base desejado para o arquivo

# Chamar a função
resultado = renomear_pdf(download_dir, novo_nome)
print(resultado)
