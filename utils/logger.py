import logging
from pathlib import Path

# Importa o diretório de logs definido nas configurações do projeto
from config.config import LOGS_DIR

def setup_logger(name="MaintenanceSystem"):
    """
    Cria e configura um logger para o sistema de manutenção.
    O logger grava mensagens tanto em arquivo quanto no console.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Define o nível mínimo de log

    # Evita adicionar múltiplos handlers se o logger já estiver configurado
    if logger.handlers:
        return logger

    # Define o formato das mensagens de log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Cria o arquivo de log no diretório de logs
    log_file = Path(LOGS_DIR) / f"{name.lower()}.log"
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)

    # Cria o handler para exibir logs no console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Adiciona os handlers ao logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger