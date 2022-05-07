
from __future__ import absolute_import


import os
import yaml
import logging.config

from subprocess import call
import click
import os
import uuid
import json
from app.app import app
from app.models import db, User



@click.group()
def cli():
    pass


@cli.command()
def run_api():
    app.run(
        host=os.environ.get('HOST', 'localhost'),
        debug=True
        # os.environ.get('DEBUG', True)
    )


@cli.command()
def migrate():
    db.drop_all()
    db.create_all()
    print('done')





@cli.command()
def generate_secret():
    with open('secret.txt', 'w') as f:
        f.write(str(uuid.uuid4()))







if __name__ == '__main__':
    cli()