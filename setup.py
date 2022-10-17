from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Maths',
    url='https://github.com/jladan/package_demo',
    author='Simon LEFRANC',
    author_email='simon.lefranc94@gmail.com',
    packages=find_packages()
    version='0.1',
    license='Archi',
    description='Module pour les mathématiques',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
