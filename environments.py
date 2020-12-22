import pulumi

def get_env():
    config = pulumi.Config()
    return config.require('env')