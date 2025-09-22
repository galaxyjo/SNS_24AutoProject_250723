"""SSL Handler module for verifying domain SSL status."""

import ssl
import socket


class SSLHandler:
    """Handles SSL verification for domains."""

    def verify_ssl(self, domain: str) -> bool:
        """
        Verify if the given domain has valid SSL.

        Args:
            domain (str): The domain to verify.

        Returns:
            bool: True if SSL is valid, False otherwise.
        """
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=3) as sock:
                with context.wrap_socket(sock, server_hostname=domain):
                    return True
        except Exception:
            return False
