# PIP

## Topics

* Create a Hello World script
* Connect the CLI in the script
* Connect the API in the script
* Compile the package using python setup.py bdist_wheel
* Install from local
* Commit to Git
* Install from Git (https://github.com/armandomiani/python-package-sample.git)


## Internal References

* https://dzone.com/articles/executable-package-pip-install

## Help 

```
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
```