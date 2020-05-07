from setuptools import setup, find_packages

setup(
    name='coddeiapi',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'waitress',
        'pyramid',
        'pyramid_services',
        'pymongo'
    ],
    entry_points={
        'paste.app_factory': [
            'main = coddeiapi:main',
        ],
    }
)
