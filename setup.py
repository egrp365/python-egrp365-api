from setuptools import setup

setup(
    name='egrp365',
    version='0.0.1',
    packages=['egrp365'],
    url='https://github.com/egrp365/python-egrp365-api',
    license='LICENSE',
    author='egrp365',
    author_email='mail@egrp365.ru',
    description='Клиент API https://egrp365.ru для получения данных из ЕГРН Росреестра.',
    install_requires=[
        "requests",
    ],
)
