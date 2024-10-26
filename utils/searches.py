import ssl
import socket


def get_ssl_certificate(
    hostname: str,
) -> dict[str, str | tuple[tuple[tuple[str, str], ...], ...] | tuple[tuple[str, str], ...]] | None:
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # Get the certificate from the SSL connection
            cert = ssock.getpeercert()
            return cert
