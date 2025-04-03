if __name__ == "__main__":
    config_loader = ConfigLoaderFactory.create_loader()
    print("🔹 Configuração do Twitter:", config_loader.get_config("twitter"))
    print("🔹 Secret do Twitter (bearer_token):", config_loader.get_secret("twitter", "bearer_token"))
