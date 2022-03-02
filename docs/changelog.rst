:tocdepth: 1

.. |grappelli| replace:: Grappelli
.. |filebrowser| replace:: FileBrowser

.. _changelog:

Changelog
=========

4.0.0 (February 2nd, 2022)
---------------------------

* Django 4.0 support, drop Django <3. Thanks to @pulse-mind.
* Support for TinyMCE v5. Thanks to @rmaceissoft.
* Dropbox storage support. Thanks to @rmaceissoft.

3.8.0 (Novermber 4th, 2019)
---------------------------

* Django 3.0 support, drop Django <1.11. Thanks to @lpomfrey.

3.7.9 (Novermber 3rd, 2019)
---------------------------

* FileObject should implement os.PathLike protocol

3.7.8 (Match 25th, 2019)
------------------------

* Fix Chinese locale language code to match the one in Django 1.9+

3.7.7 (February 2nd, 2019)
--------------------------

* Fix of the previous release removing dependency on six

3.7.6 (February 1st, 2019)
--------------------------

* Fix default value for FileBrowserField (thanks @carlosgeos for report)

3.7.5 (September 12th, 2018)
----------------------------

* Support for Django 2.1 (by @orbitvu)

3.7.4 (January 27th, 2018)
--------------------------

* Fix manage dumpdata command for Django 2.0 (by @waustin)

3.7.3 (December 4th, 2017)
--------------------------

* Compatibility with Django 2.0
* Add config for use admin_custom

3.7.2 (Jun 8th, 2017)
---------------------

* Fix AttributeError in Django 1.11 when saving

3.7.1 (May 28th, 2017)
----------------------

* New: Compatibility with Django 1.11
* Folders being listed as selectable and 'format' not working correctly. (#29)
* UI improvements

3.7.0 (Febrary 11th, 2017)
--------------------------

* New: Compatibility with Django 1.10
* Dropped support for Django < 1.8
* Based on filebrowser v3.7.2


For further information, see :ref:`releasenotes`.
