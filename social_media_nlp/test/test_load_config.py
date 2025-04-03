import unittest
from script.load_config import ConfigLoaderFactory

class TestYAMLConfigLoader(unittest.TestCase):
    def setUp(self):
        """Cria uma instância do ConfigLoader para os testes."""
        self.config_loader = ConfigLoaderFactory.create_loader()

    def test_get_config(self):
        """Testa se conseguimos recuperar uma configuração."""
        self.assertEqual(self.config_loader.get_config("twitter")["max_results"], 10)

    def test_get_secret(self):
        """Testa se conseguimos recuperar um segredo."""
        bearer_token = self.config_loader.get_secret("twitter", "bearer_token")
        self.assertIsNotNone(bearer_token)

if __name__ == '__main__':
    unittest.main()
