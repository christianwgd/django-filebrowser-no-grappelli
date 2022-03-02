Django FileBrowser
==================
.. image:: https://img.shields.io/pypi/v/django-filebrowser-no-grappelli2.svg
    :target: https://pypi.python.org/pypi/django-filebrowser-no-grappelli2

.. image:: https://img.shields.io/pypi/l/django-filebrowser-no-grappelli2.svg
    :target: https://pypi.python.org/pypi/django-filebrowser-no-grappelli2

.. image:: https://img.shields.io/pypi/dm/django-filebrowser-no-grappelli2
    :alt: PyPI - Downloads
    :target: https://pypi.python.org/pypi/django-filebrowser-no-grappelli2

**Media-Management**. (based on https://github.com/sehmaschine/django-filebrowser)

The FileBrowser is an extension to the `Django <http://www.djangoproject.com>`_ administration interface in order to:

* browse directories on your server and upload/delete/edit/rename files.
* include images/documents to your models/database using the ``FileBrowseField``.
* select images/documents with TinyMCE.

The only difference by now to the original smacker/django-filebrowser-no-grappelli
is the additional Azure storage class.

Requirements
------------

FileBrowser 4.0 requires

* Django 2/3/4 (http://www.djangoproject.com)
* Pillow (https://github.com/python-imaging/Pillow)

No Grappelli
------------

This fork removes the dependency on Grappelli.

.. figure:: docs/_static/Screenshot.png
   :scale: 50 %
   :alt: django filebrowser no grappelli

Installation
------------

Latest version:

    pip install -e git+git://github.com/christianwgd/django-filebrowser-no-grappelli.git#egg=django-filebrowser-no-grappelli

Stable version:

    pip install django-filebrowser-no-grappelli2

Documentation
-------------

http://readthedocs.org/docs/django-filebrowser/

It also has fake model to show filebrowser in admin dashboard, but you can disable it by setting ``FILEBROWSER_SHOW_IN_DASHBOARD = False``.

Translation
-----------

https://www.transifex.com/projects/p/django-filebrowser/

Releases
--------

* FileBrowser 4.0.1 (March 2nd, 2022): Compatible with Django 3/4, merge back smacker/master
* FileBrowser 3.8.0 (November 4th, 2019): Compatible with Django 1.11/2.0/2.1/2.2/3.0
* FileBrowser 3.7.9 (November 3rd, 2019): Compatible with Django 1.8/1.9/1.10/1.11/2.0/2.1/2.2
* FileBrowser 3.6.2 (March 7th, 2016): Compatible with Django 1.4/1.5/1.6/1.7/1.8/1.9

Older versions are available at GitHub, but are not supported anymore.
