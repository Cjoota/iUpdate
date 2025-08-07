from utils.logger import setup_logger
from utils.file_utils import clean_directory
from config.config import TEMP_DIRECTORIES

class SystemClear:
    def __init__(self):

        self.logger = setup_logger("SystemCleaner")

    def clean_temp(self):
        """
        Limpa arquivos temporários do sistema.
        """
        
        for temp_dir in TEMP_DIRECTORIES:
            self.logger.info(f"Limpando Diretório temporário: {temp_dir}")
            self.logger.info(f"Limpeza em: {temp_dir} - {clean_directory(temp_dir)} bytes liberados")
            self.logger.info(f"Limpeza Concluida em: {temp_dir}")
