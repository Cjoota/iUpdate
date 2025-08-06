import os
from pathlib import Path

#Diretórios base do projeto
BASE_DIR = Path(__file__).parent.parent
LOGS_DIR = BASE_DIR / "logs"
CONFIG_DIR = BASE_DIR/ "config"

#Criar Directorios caso não exista
LOGS_DIR.mkdir(exist_ok=True)


#Configuração de limpeza de arquivos temporarios
TEMP_DIRECTORIES = [
    os.path.expandvars(r'%TEMP%'),
    os.path.expandvars(r'%WINDIR\Temp%'),
    os.path.expandvars(r'%LOCALAPPDATA\Temp%'),
]

#Configurações de agendamento
DEFAULT_SCHEDULE_TIME = "00:00" #Definindo o horario para meia noite
DEFAULT_SCHEDULE_DAY = "sunday" #Definindo o dia para Domingo


#Configurações de timeout(em segundos)
UPDATE_TIMEOUT = 1800 #30 Minutos para Update
CLEANUP_TIMEOUT = 600 # 10 Minutos para limpeza

#Configuração de logging
LOG_LEVEL = "INFO"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

