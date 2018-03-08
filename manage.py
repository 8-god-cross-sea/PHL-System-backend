from models import *
import click


@click.group()
def cli():
    pass


@click.command()
def init_db():
    """initialize database and create schema"""
    db.database.connect()

    # drop tables
    db.database.drop_tables(tables)

    # create tables
    db.database.create_tables(tables)

    # initialize data
    User.create(username='admin', password='admin', email='', admin=True, active=True)

    click.echo('db initialization finished')
    db.database.close()


@click.command()
def drop_db():
    """drop database"""
    click.echo('Dropped the database')


cli.add_command(init_db)
cli.add_command(drop_db)

if __name__ == '__main__':
    cli()
