from setuptools import setup, find_packages

setup(name='nts',
    version='1.0',
    author='HMST Solution',
    author_email='samommitas@gmail.com',
    url='https://github.com/TIS2016/Narodna-transfuzna-sluzba.git',
    packages=find_packages(),
    include_package_data=True,
    description='Non commercial application for NTS',
    install_requires=['Django==1.10','django-jquery==3.1.0','psycopg2==2.6.2', 'whitenoise==3.2.2'],
)
