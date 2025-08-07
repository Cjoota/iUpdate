import os
from utils.logger import setup_logger

# Cria um logger específico para operações com arquivos
logger = setup_logger("FileUtils")

def clean_directory(directory):
    """
    Limpa todos os arquivos de um diretório e retorna o total de bytes liberados.
    Se o diretório não existir, retorna 0.
    """
    freed_bytes = 0
    if not os.path.exists(directory):
        return freed_bytes

    logger.info(f"Limpando diretório: {directory}")

    # Percorre todos os arquivos do diretório (e subdiretórios)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)  # Tamanho do arquivo antes de deletar
                os.remove(file_path)  # Remove o arquivo
                freed_bytes += file_size  # Soma o espaço liberado
            except (OSError, PermissionError, FileNotFoundError):
                # Ignora arquivos que não podem ser removidos
                continue
    return freed_bytes

def format_bytes(bytes_value):
    """
    Converte um valor em bytes para uma string legível (KB, MB, GB, etc).
    Exemplo: 1048576 -> '1.00 MB'
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} TB"