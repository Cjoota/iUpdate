import os
import ctypes
from utils.logger import setup_logger

# Cria um logger específico para a verificação de privilégios de administrador
logger = setup_logger("AdminChecker")

def check_admin_rights():
    """
    Verifica se o script está sendo executado com privilégios de administrador.
    Retorna True se for admin, False caso contrário.
    Funciona tanto em sistemas Unix quanto Windows.
    """
    try:
        # Em sistemas Unix (Linux/Mac), UID 0 é o root
        return os.getuid() == 0
    except AttributeError:
        # Em sistemas Windows, usa a API do Windows para verificar
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception as e:
            logger.error(f"Erro ao verificar privilégios de admin: {e}")
            return False