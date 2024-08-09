import requests
import os
from msal import ConfidentialClientApplication

# Constants
TENANT_ID = os.getenv('POWERBI_TENANT_ID')
CLIENT_ID = os.getenv('POWERBI_CLIENT_ID')
CLIENT_SECRET = os.getenv('POWERBI_CLIENT_SECRET')
WORKSPACE_ID = 123 #os.getenv('POWERBI_WORKSPACE_ID')
PBIX_FILE_PATH = 'HumanResources\HumanResourcesSamplePBIX.pbix'
GROUP_ID = WORKSPACE_ID

# Function to get access token
def get_access_token():
    try:
        authority_url = f'https://login.microsoftonline.com/{TENANT_ID}'
        app = ConfidentialClientApplication(
            CLIENT_ID,
            authority=authority_url,
            client_credential=CLIENT_SECRET
        )
        scopes = ['https://analysis.windows.net/powerbi/api/.default']
        result = app.acquire_token_for_client(scopes=scopes)
        if 'access_token' in result:
            return result['access_token']
        else:
            raise Exception('Could not obtain access token')
    except Exception as e:
        with open('error.log', 'w') as f:
            f.write(f'Error obtaining access token: {e}')
        raise

# Function to upload .pbix file
def upload_pbix_file(access_token):
    try:
        url = f'https://api.powerbi.com/v1.0/myorg/groups/{GROUP_ID}/imports?datasetDisplayName=MyDataset'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        files = {
            'file': open(PBIX_FILE_PATH, 'rb')
        }
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 202:
            print('File uploaded successfully')
        else:
            with open('error.log', 'w') as f:
                f.write(f'Failed to upload file: {response.content}')
            response.raise_for_status()
    except Exception as e:
        with open('error.log', 'w') as f:
            f.write(f'Error uploading PBIX file: {e}')
        raise

# Main deployment process
if __name__ == '__main__':
    try:
        token = get_access_token()
        upload_pbix_file(token)
    except Exception as e:
        with open('error.log', 'w') as f:
            f.write(f'Deployment failed: {e}')
        print(f'Deployment failed: {e}')