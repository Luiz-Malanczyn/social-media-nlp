import unittest
from unittest.mock import patch, MagicMock
from connection.twitter_connection import TwitterConnection 

class TestTwitterConnection(unittest.TestCase):

    @patch("connection.twitter_connection.tweepy.API")
    @patch("connection.twitter_connection.tweepy.OAuth1UserHandler")
    @patch("script.load_config.load_config")
    def test_twitter_connection_success(self, mock_load_config, mock_auth, mock_api):
        """Testa se a conexão com a API do Twitter é bem-sucedida"""

        # Mockando as credenciais de autenticação
        mock_load_config.return_value = {
            "twitter": {
                "api_key": "fake_key",
                "api_secret": "fake_secret",
                "access_token": "fake_token",
                "access_secret": "fake_access_secret"
            }
        }

        # Mockando a autenticação
        mock_auth.return_value = MagicMock()
        mock_api.return_value = MagicMock()

        # Criando instância da conexão
        twitter_conn = TwitterConnection()
        client = twitter_conn.get_client()

        # Verificações
        mock_auth.assert_called_once()
        mock_api.assert_called_once()
        self.assertIsNotNone(client)

    @patch("script.load_config.load_config")
    def test_twitter_connection_failure(self, mock_load_config):
        """Testa se a conexão falha ao não fornecer credenciais"""
        mock_load_config.return_value = {"twitter": {}}

        with self.assertRaises(ConnectionError):
            TwitterConnection()

if __name__ == "__main__":
    unittest.main()
