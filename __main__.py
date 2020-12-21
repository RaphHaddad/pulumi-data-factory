"""An Azure Python Pulumi program"""

import pulumi
from pulumi_azure import core, storage

def get_env():
    config = pulumi.Config()
    return config.require('env')

def get_resource_group():
    env = get_env()
    return core.ResourceGroup('resource_group_{env}'.format(env=env))

resource_group = get_resource_group()
account = storage.Account('storage{env}'.format(env=env),
                          # The location for the storage account will be derived automatically from the resource group.
                          resource_group_name=resource_group.name,
                          account_tier='Standard',
                          account_replication_type='LRS')

pulumi.export('connection_string', account.primary_connection_string)
