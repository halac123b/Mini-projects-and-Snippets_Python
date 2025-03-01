"""
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming OAuth 2.0 RFC6749.
"""

AUTH_HEADER = 'auth_header'
URI_QUERY = 'query'
BODY = 'body'

FORM_ENC_HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

class Client:
    """Base OAuth2 client responsible for access token management.

    This class also acts as a generic interface providing methods common to all
    client types such as ``prepare_authorization_request`` and
    ``prepare_token_revocation_request``. The ``prepare_x_request`` methods are
    the recommended way of interacting with clients (as opposed to the abstract
    prepare uri/body/etc methods). They are recommended over the older set
    because they are easier to use (more consistent) and add a few additional
    security checks, such as HTTPS and state checking.

    Some of these methods require further implementation only provided by the
    specific purpose clients such as
    :py:class:`oauthlib.oauth2.MobileApplicationClient` and thus you should always
    seek to use the client class matching the OAuth workflow you need. For
    Python, this is usually :py:class:`oauthlib.oauth2.WebApplicationClient`.

    """
    refresh_token_key = 'refresh_token'

    def __init__(self, client_id,
                 default_token_placement=AUTH_HEADER,
                 token_type='Bearer',
                 access_token=None,
                 refresh_token=None,
                 mac_key=None,
                 mac_algorithm=None,
                 token=None,
                 scope=None,
                 state=None,
                 redirect_url=None,
                 state_generator=generate_token,
                 code_verifier=None,
                 code_challenge=None,
                 code_challenge_method=None,
                 **kwargs):
    
    