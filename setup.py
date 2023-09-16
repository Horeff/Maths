from setuptools import setup, find_packages

setup(
    name='Maths',
    author='Simon LEFRANC',
    author_email='simon.lefranc94@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'sympy',
        'Algorithmique @ git+https://github.com/Horeff/Algorithmique.git'
    ],
)
