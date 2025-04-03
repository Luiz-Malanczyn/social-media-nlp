import yaml
from abc import ABC, abstractmethod
import os

class IConfigLoader(ABC):
    """Interface para carregamento de configurações."""

    @abstractmethod
    def get_config(self, key: str, default=None):
        pass

    @abstractmethod
    def get_secret(self, section: str, key: str, default=None):
        pass

class YAMLConfigLoader(IConfigLoader):
    """Carrega configurações gerais e secrets do projeto a partir de arquivos YAML."""

    def __init__(self, config_path="config/config.yaml"):
        self.config_path = config_path
        self.config = self._load_yaml(config_path)
        self.secrets = self._load_yaml(self.config.get("secret_path", "secret/secret.yaml"))

    def _load_yaml(self, path):
        """Carrega um arquivo YAML."""
        try:
            with open(path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file) or {}
        except FileNotFoundError:
            print(f"⚠️ Aviso: Arquivo {path} não encontrado. Retornando configuração vazia.")
            return {}

    def get_config(self, key: str, default=None):
        """Retorna uma configuração geral."""
        return self.config.get(key, default)

    def get_secret(self, section: str, key: str, default=None):
        """Retorna um segredo específico."""
        return self.secrets.get(section, {}).get(key, default)

class ConfigLoaderFactory:
    """Factory para instanciar um carregador de configuração."""

    @staticmethod
    def create_loader(loader_type="yaml"):
        if loader_type == "yaml":
            return YAMLConfigLoader()
        raise ValueError(f"Loader {loader_type} não suportado.")
