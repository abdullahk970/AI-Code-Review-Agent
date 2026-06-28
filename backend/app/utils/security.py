import hashlib

import hmac


def verify_github_signature(

    payload: bytes,

    signature: str,

    secret: str

):

    if not signature:

        return False


    try:

        sha_name, github_signature = signature.split("=")

    except ValueError:

        return False


    if sha_name != "sha256":

        return False


    digest = hmac.new(

        secret.encode(),

        msg=payload,

        digestmod=hashlib.sha256

    ).hexdigest()


    return hmac.compare_digest(

        digest,

        github_signature

    )