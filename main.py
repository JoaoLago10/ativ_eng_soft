from config_manager import ConfigManager

if __name__ == "__main__":
    # Instância inicial do Singleton
    config1 = ConfigManager("config.json")

    # Lendo configurações existentes
    print("Host atual:", config1.get("host", "localhost"))
    print("Porta atual:", config1.get("port", 8000))

    # Atualizando configurações
    config1.set("host", "127.0.0.1")
    config1.set("port", 8080)

    # Criando outra instância para verificar se é a mesma
    config2 = ConfigManager("another_config.json")
    print("Host da segunda instância:", config2.get("host"))
    print("Porta da segunda instância:", config2.get("port"))

    # Verificando se as instâncias são as mesmas
    print("Config1 é Config2?", config1 is config2)
