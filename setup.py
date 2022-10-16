from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Maths',
    url='https://github.com/jladan/package_demo',
    author='Simon LEFRANC',
    author_email='simon.lefranc94@gmail.com',
    # Needed to actually package something
    packages=['Maths'],
    # Needed for dependencies
    install_requires=['Sympy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='Archi',
    description='Module pour les mathématiques',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
