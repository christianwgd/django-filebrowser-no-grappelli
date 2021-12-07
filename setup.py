import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-filebrowser-no-grappelli2',
    version='3.8.5',
    description='Media-Management no Grappelli',
    long_description=read('README.rst'),
    url='https://github.com/christianwgd/django-filebrowser-no-grappelli',
    download_url='',
    author='Patrick Kranzlmueller, Axel Swoboda (vonautomatisch), Maxim Sukharev, Christian Wiegand',
    author_email='christianwgd@gmail.com',
    maintainer='Christian Wiegand',
    maintainer_email='christianwgd@gmail.com',
    license='BSD',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    zip_safe=False,
)