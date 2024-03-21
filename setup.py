from setuptools import setup, find_packages

setup(
    name='telegram-message',
    version='0.1.0',
    description='Simple library to send Telegram messages',
    author='kstka',
    author_email='me@kstka.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
