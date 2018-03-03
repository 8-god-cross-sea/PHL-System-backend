from models import *
import click
import uuid


@click.group()
def cli():
    pass


@click.command()
def init_db():
    """initialize database and create schema"""
    db.connect()

    # create tables
    db.drop_tables(models)
    db.create_tables(models)

    # initialize data
    admin = User.create(id=uuid.uuid4(), username='admin', password='admin')
    admin.save()

    click.echo('db initialization finished')
    db.close()


@click.command()
def drop_db():
    """drop database"""
    click.echo('Dropped the database')


cli.add_command(init_db)
cli.add_command(drop_db)

if __name__ == '__main__':
    cli()
