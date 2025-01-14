import json

class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def _initialize(self, config_file):
        """Carrega as configurações do arquivo JSON."""
        self.config_file = config_file
        self._load_config()

    def _load_config(self):
        """Lê as configurações do arquivo JSON."""
        try:
            with open(self.config_file, "r") as file:
                self.config = json.load(file)
                print(f"Configurações carregadas de '{self.config_file}'.")
        except FileNotFoundError:
            self.config = {}
            print(f"Arquivo de configuração '{self.config_file}' não encontrado. Usando valores padrão.")

    def get(self, key, default=None):
        """Obtém o valor de uma configuração."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Define uma nova configuração e atualiza o arquivo."""
        self.config[key] = value
        self._save_config()

    def _save_config(self):
        """Salva as configurações no arquivo JSON."""
        with open(self.config_file, "w") as file:
            json.dump(self.config, file, indent=4)
            print(f"Configurações salvas em '{self.config_file}'.")
