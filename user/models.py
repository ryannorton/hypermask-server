from django.db import models
from django.contrib.auth.hashers import (
    check_password as _check_password,
    make_password
)


class HypermaskUser(models.Model):
    """
    Hypermask users set a password to locally encrypt and decrypt keys in their browser.

    A hashed version of this password is sent to this service, along with the encrypted key
    (encrypted with the original unhashed password, which never touches the server).

    Encrypted keys can be fetched from any device and are authenticated against the username and
    password hash.
    """
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=128)
    encrypted_key = models.CharField(max_length=500, null=True)

    @classmethod
    def create(cls, username, raw_password_hash, encrypted_key=None):
        # Raw password hash from client is hashed again by the server before storing in db.
        password_hash = make_password(raw_password_hash)
        user = cls(
            username=username,
            password_hash=password_hash,
            encrypted_key=encrypted_key
        )
        user.save()
        return user

    def check_password(self, raw_password_hash):
        """
        Return a boolean of whether the raw_password_hash was correct.
        """
        return _check_password(raw_password_hash, self.password_hash)
