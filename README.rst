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

Requirements
------------

FileBrowser 3.8 requires

* Django >= 3.1 (http://www.djangoproject.com)
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

* FileBrowser 3.8.1 (January 7, 2021): Compatible with Django 3.1, TinyMCE 5
* FileBrowser 3.8.2 (January 21, 2021): Azure Blob Storage Mixin added
* FileBrowser 3.8.3 (March 12, 2021): Remove Django 4.0 deprecation warnings

Older versions are available at GitHub, but are not supported anymore.
