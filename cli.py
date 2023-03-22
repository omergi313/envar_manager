#!/usr/bin/env python

import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('-p', '--envfile_path', required=True, help='Path to the .env file')
@click.option('-u', '--users', multiple=True, required=True, help='Users to add to the bucket')
def init(envfile_path, users):
    from envar_manager.provider import GoogleCloudStorage

    # Authenticate with the cloud provider
    provider = GoogleCloudStorage()
    provider.authenticate()

    # Create a bucket and env file from local path
    provider.create_bucket_from_local(envfile_path)

    # Add specified users to the bucket
    provider.add_users_to_bucket(users)

if __name__ == '__main__':
    cli()
