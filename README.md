# PowerBI

## GENERATE POWER BI SECRETS

1. Go to the Azure Portal:
Navigate to Azure Portal.

2. Register a New Application:
In the left-hand navigation pane, select Azure Active Directory.
Under Manage, select App registrations.
Select New registration.

3. Configure the Application:
Enter a name for your application.
Select the supported account types (e.g., Accounts in this organizational directory only).
For the Redirect URI, you can leave it empty for now or set it to a placeholder (you can configure it later if needed).
Click Register.

4. Get the Client ID:
After registering the application, you will be redirected to the application's overview page.
Copy the Application (client) ID. This is your Power BI Client ID.

5. Add API Permissions:
In the application's overview page, select API permissions.
Click Add a permission.
Select Power BI Service.
Select Delegated permissions and choose the necessary permissions (e.g., Dataset.ReadWrite.All).
Click Add permissions.

6. Generate a Client Secret:
In the application's overview page, select Certificates & secrets.
Under Client secrets, click New client secret.
Add a description and set an expiration period.
Click Add.
Copy the generated client secret value. This is your Power BI Client Secret.


## GET WORKSAPCE ID

1. Go to Power BI Service:

2. Navigate to Power BI Service.

3. Open the Workspace:
In the left-hand navigation pane, select the workspace you want to deploy to.
Get the Workspace ID:

4. Look at the URL in your browser. It will look something like this: https://app.powerbi.com/groups/{workspace_id}/
The {workspace_id} part of the URL is your Workspace ID.