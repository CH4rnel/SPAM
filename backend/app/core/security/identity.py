# ♃ ☿ 𓂀 SPAM IDENTITY ENGINE 𓂀 ☿ ♃

"""
Anonymous identity generation layer.

No Telegram IDs.
No usernames.
No personal metadata.

Only deterministic cryptographic fingerprints.
"""


import hashlib
import hmac
import secrets


class IdentityEngine:
    """
    Generates anonymous identities.

    Uses HMAC-SHA256 instead of plain hashing
    to prevent rainbow table attacks.
    """


    def __init__(self, secret: str):
        self.secret = secret.encode("utf-8")


    def generate_identity(
        self,
        external_id: str,
    ) -> str:
        """
        Generates stable anonymous hash.

        external_id:
            Temporary external identifier.
            Example:
            Telegram user ID.

        It is never stored.
        """

        digest = hmac.new(
            self.secret,
            external_id.encode("utf-8"),
            hashlib.sha256,
        )

        return digest.hexdigest()


    def generate_tripcode(
        self,
        anonymous_hash: str,
        length: int = 8,
    ) -> str:
        """
        Creates public anonymous nickname.

        Example:

        #A7F91BCD
        """

        return (
            "#"
            + anonymous_hash[:length]
            .upper()
        )


    @staticmethod
    def generate_secret() -> str:
        """
        Creates cryptographic secret.
        """

        return secrets.token_hex(32)