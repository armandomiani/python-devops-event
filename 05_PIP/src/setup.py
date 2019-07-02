import setuptools

setuptools.setup(
    name='first_cli',
    version='1.0',
    author='Armando Miani',
    author_email='armando.miani@gmail.com',
    description='First CLI',
    packages=setuptools.find_packages(),
    scripts=['first-cli'],
    install_requires=[
        'flask'
    ]
)