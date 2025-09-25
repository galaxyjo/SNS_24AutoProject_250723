# modules/common/handshake.py
from typing import List, Optional


class HandshakeError(Exception):
    """Raised when the handshake process fails."""


class Handshake:
    def __init__(self, client: bool):
        self.client = client
        self.accepted_protocol: Optional[str] = None

    def initiate(self, protocols: List[str]) -> str:
        """Initiate handshake by choosing a protocol."""
        if not protocols:
            raise HandshakeError("No protocols provided")
        self.accepted_protocol = protocols[0]
        return self.accepted_protocol

    def is_complete(self) -> bool:
        """Return True if handshake completed successfully."""
        return self.accepted_protocol is not None

    def reset(self):
        """Reset handshake state."""
        self.accepted_protocol = None
