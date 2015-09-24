import os
import shutil

from django.conf import settings
from django.test import TestCase

from filebrowser.settings import DIRECTORY, VERSIONS_BASEDIR
from filebrowser.base import FileObject
from filebrowser.sites import site


class FilebrowserTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(FilebrowserTestCase, cls).setUpClass()

        cls.TEST_PATH = os.path.join(site.storage.location, '_test')
        cls.DIRECTORY_PATH = os.path.join(site.storage.location, DIRECTORY)
        cls.VERSIONS_PATH = os.path.join(site.storage.location, VERSIONS_BASEDIR)

        cls.FOLDER_PATH = os.path.join(cls.DIRECTORY_PATH, 'subfolder')
        cls.PLACEHOLDER_PATH = os.path.join(cls.DIRECTORY_PATH, 'placeholders')

        cls.STATIC_IMG_PATH = os.path.join(settings.BASE_DIR, 'filebrowser', "static", "filebrowser", "img", "testimage.jpg")
        cls.F_IMG = FileObject(os.path.join(DIRECTORY, 'subfolder', "testimage.jpg"), site=site)
        cls.F_MISSING = FileObject(os.path.join(DIRECTORY, 'subfolder', "missing.jpg"), site=site)

        os.makedirs(cls.FOLDER_PATH)
        os.makedirs(cls.PLACEHOLDER_PATH)

        shutil.copy(cls.STATIC_IMG_PATH, cls.FOLDER_PATH)
        shutil.copy(cls.STATIC_IMG_PATH, cls.PLACEHOLDER_PATH)

    @classmethod
    def tearDownClass(cls):
        super(FilebrowserTestCase, cls).tearDownClass()
        shutil.rmtree(cls.TEST_PATH)
