# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, utils

from ..algorithm import SignatureAlgorithm
from ..transform import SignatureTransform
from ..._enums import SignatureAlgorithm as KeyVaultSignatureAlgorithm


class RsaSignatureTransform(SignatureTransform):
    def __init__(self, key, padding_function, hash_algorithm):
        super(RsaSignatureTransform, self).__init__()
        self._key = key
        self._padding_function = padding_function
        self._hash_algorithm = hash_algorithm

    def sign(self, digest):
        return self._key.sign(digest, self._padding_function(digest), utils.Prehashed(self._hash_algorithm))

    def verify(self, digest, signature):
        self._key.verify(signature, digest, self._padding_function(digest), utils.Prehashed(self._hash_algorithm))


class RsaSsaPkcs1v15(SignatureAlgorithm):
    def create_signature_transform(self, key):
        return RsaSignatureTransform(key, lambda _: padding.PKCS1v15(), self._default_hash_algorithm)


class RsaSsaPss(SignatureAlgorithm):
    def create_signature_transform(self, key):
        return RsaSignatureTransform(key, self._get_padding, self._default_hash_algorithm)

    def _get_padding(self, digest):
        return padding.PSS(mgf=padding.MGF1(self._default_hash_algorithm), salt_length=len(digest))


class Ps256(RsaSsaPss):
    _name = KeyVaultSignatureAlgorithm.ps256
    _default_hash_algorithm = hashes.SHA256()


class Ps384(RsaSsaPss):
    _name = KeyVaultSignatureAlgorithm.ps384
    _default_hash_algorithm = hashes.SHA384()


class Ps512(RsaSsaPss):
    _name = KeyVaultSignatureAlgorithm.ps512
    _default_hash_algorithm = hashes.SHA512()


class Rs256(RsaSsaPkcs1v15):
    _name = KeyVaultSignatureAlgorithm.rs256
    _default_hash_algorithm = hashes.SHA256()


class Rs384(RsaSsaPkcs1v15):
    _name = KeyVaultSignatureAlgorithm.rs384
    _default_hash_algorithm = hashes.SHA384()


class Rs512(RsaSsaPkcs1v15):
    _name = KeyVaultSignatureAlgorithm.rs512
    _default_hash_algorithm = hashes.SHA512()


Ps256.register()
Ps384.register()
Ps512.register()
Rs256.register()
Rs384.register()
Rs512.register()
