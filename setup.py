import setuptools

setuptools.setup(
    name='django-makesuperuser',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
