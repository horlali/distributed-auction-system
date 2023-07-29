import datetime
import os
import ssl

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from auction_system.utils.constants import HOST, KEY_FILE_DIR

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)


# Create a self-signed certificate
subject = issuer = x509.Name([x509.NameAttribute(x509.NameOID.COMMON_NAME, HOST)])
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName(HOST)]),
        critical=False,
    )
    .sign(private_key, hashes.SHA256(), default_backend())
)


# Write the private key and certificate to files
def create_key_files():
    with open(os.path.join(KEY_FILE_DIR, "privateKey.pem"), "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    with open(os.path.join(KEY_FILE_DIR, "certificate.pem"), "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def ssl_context():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(
        certfile=os.path.join(KEY_FILE_DIR, "certificate.pem"),
        keyfile=os.path.join(KEY_FILE_DIR, "privateKey.pem"),
    )

    return context
