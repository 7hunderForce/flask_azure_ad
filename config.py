
CLIENT_ID = 'app_client_id'
CLIENT_SECRET = 'app_client_secret'
REDIRECT_URI = 'http://localhost:5000/login/authorized'

AUTHORITY_URL = 'https://login.microsoftonline.us/some_code'

AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
TOKEN_ENDPOINT = '/oauth2/v2.0/token'

RESOURCE = 'https://graph.microsoft.us/'
API_VERSION = 'v1.0'
SECURITYAPI_VERSION = 'v1.0'
SECURESCORE_VERSION = 'v1.0'
SECURITYACTION_VERSION = 'beta'
SECURITYAPI_URL = RESOURCE + SECURITYAPI_VERSION + '/security/'
SCOPES = ['User.Read']  




WEBHOOK_DATA = {'changeType': 'updated',
                'notificationUrl': 'https://{ ENTER_YOUR_NGROK_URL }/listen',
                'resource': 'security/alerts',
                'clientState': 'cLIENTsTATEfORvALIDATION'}
