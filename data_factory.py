import pulumi
from pulumi_azure import datafactory
from environments import get_env

def provission_data_factory(resource_group):
    env = get_env()
    datafactory.Factory('factory{env}'.format(env=env),
                         location=resource_group.location,
                         resource_group_name=resource_group.name)