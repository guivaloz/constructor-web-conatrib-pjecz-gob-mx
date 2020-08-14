from setuptools import setup

setup(
    name='Archivista',
    version='0.4',
    py_modules=['archivista'],
    install_requires=[
        'click',
        'jinja2',
        'markdown',
    ],
    entry_points="""
        [console_scripts]
        archivista=archivista:cli
    """,
)
