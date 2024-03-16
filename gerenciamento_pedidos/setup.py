from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_microsservico',
    version='0.0',
    description='Exercício de microsservico',
    author='Lucas-sgarioni',
    author_email='lsgarioni@ucs.br',
    keywords='flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)