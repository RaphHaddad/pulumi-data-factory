# Pulumi Example

## Setup

### Configure Azure CLI

```cmd
$ az login # Login to Azure
The default web browser has been opened at https://login.microsoftonline.com/common/oauth2/authorize. Please continue the login in the web browser.
$ az account list # Get list of available azure subscriptions
[
  {
    "cloudName": "AzureCloud",
    "id": "a-guid-here",
    "isDefault": false,
    "name": "Visual Studio Professional with MSDN",
    "state": "Enabled",
    "tenantId": "a-guid-here",
    "user": {
      "name": "raphael.haddad@something.net",
      "type": "user"
    }
  }
...
...
...
]
$ az account set -s a-guid
```

### Install Dependencies

```cmd
$ python -m venv ./venv
$ pip install -r requirements.txt
Collecting pulumi<3.0.0,>=2.0.0
  Using cached pulumi-2.15.6-py2.py3-none-any.whl (114 kB)
Collecting pulumi-azure<4.0.0,>=3.0.0
  Using cached pulumi_azure-3.40.0.tar.gz (1.3 MB)
...
...
...
```

### Upload infrastructure

```cmd
$ pulumi preview # For quick validation
$ pulumi up --yes # Upload the infrastructure and automatically approve.
```

## TODO

[x] Run the default project and get it going locally into a subscription;
[x] Link Pulumi to an Azure DevOps project and run the same template
into another subscription;
[] Paramertise the template (stack) so that it can be used across different
environments; and
[] Create mutable infrastructure, modify the data inside it, and redeploy.
