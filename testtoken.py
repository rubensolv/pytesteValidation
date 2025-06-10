import os
AUTH_TOKEN = os.environ.get("AUTH_TOKEN_JAMES_OFICIAL2")#os.environ['AUTH_TOKEN_JAMES_OFICIAL']
if not AUTH_TOKEN:
    raise ValueError("AUTH_TOKEN_JAMES_OFICIAL2 environment variable is not set.")

print(AUTH_TOKEN)


AUTH_TOKEN = os.environ.get("AUTH_TOKEN_JAMES_OFICIAL")#os.environ['AUTH_TOKEN_JAMES_OFICIAL']
if not AUTH_TOKEN:
    raise ValueError("AUTH_TOKEN_JAMES_OFICIAL environment variable is not set.")

print(AUTH_TOKEN)
