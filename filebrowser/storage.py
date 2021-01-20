# coding: utf-8

import os
import shutil

from django.core.files.move import file_move_safe
from django.utils.encoding import smart_text

from filebrowser.base import FileObject
from filebrowser.settings import DEFAULT_PERMISSIONS


class StorageMixin(object):
    """
    Adds some useful methods to the Storage class.
    """

    def isdir(self, name):
        """
        Returns true if name exists and is a directory.
        """
        raise NotImplementedError()

    def isfile(self, name):
        """
        Returns true if name exists and is a regular file.
        """
        raise NotImplementedError()

    def move(self, old_file_name, new_file_name, allow_overwrite=False):
        """
        Moves safely a file from one location to another.

        If allow_ovewrite==False and new_file_name exists, raises an exception.
        """
        print('move', old_file_name, new_file_name, allow_overwrite)
        raise NotImplementedError()

    def makedirs(self, name):
        """
        Creates all missing directories specified by name. Analogue to os.mkdirs().
        """
        raise NotImplementedError()

    def rmtree(self, name):
        """
        Deletes a directory and everything it contains. Analogue to shutil.rmtree().
        """
        raise NotImplementedError()

    def setpermission(self, name):
        """
        Sets file permission
        """
        raise NotImplementedError()


class FileSystemStorageMixin(StorageMixin):

    def isdir(self, name):
        return os.path.isdir(self.path(name))

    def isfile(self, name):
        return os.path.isfile(self.path(name))

    def move(self, old_file_name, new_file_name, allow_overwrite=False):
        file_move_safe(self.path(old_file_name), self.path(new_file_name), allow_overwrite=True)

    def makedirs(self, name):
        os.makedirs(self.path(name))

    def rmtree(self, name):
        shutil.rmtree(self.path(name))

    def setpermission(self, name):
        full_path = FileObject(smart_text(name), site=self).path_full
        os.chmod(full_path, DEFAULT_PERMISSIONS)


class S3BotoStorageMixin(StorageMixin):

    def isfile(self, name):
        return self.exists(name)

    def isdir(self, name):
        # That's some inefficient implementation...
        # If there are some files having 'name' as their prefix, then
        # the name is considered to be a directory
        if not name:  # Empty name is a directory
            return True

        if self.isfile(name):
            return False

        name = self._normalize_name(self._clean_name(name))
        dirlist = self.bucket.list(self._encode_name(name))

        # Check whether the iterator is empty
        for item in dirlist:
            return True
        return False

    def move(self, old_file_name, new_file_name, allow_overwrite=False):

        if self.exists(new_file_name):
            if allow_overwrite:
                self.delete(new_file_name)
            else:
                raise "The destination file '%s' exists and allow_overwrite is False" % new_file_name

        old_key_name = self._encode_name(self._normalize_name(self._clean_name(old_file_name)))
        new_key_name = self._encode_name(self._normalize_name(self._clean_name(new_file_name)))

        k = self.bucket.copy_key(new_key_name, self.bucket.name, old_key_name)

        if not k:
            raise "Couldn't copy '%s' to '%s'" % (old_file_name, new_file_name)

        self.delete(old_file_name)

    def makedirs(self, name):
        pass

    def rmtree(self, name):
        name = self._normalize_name(self._clean_name(name))
        dirlist = self.bucket.list(self._encode_name(name))
        for item in dirlist:
            item.delete()

    def setpermission(self, name):
        # Permissions for S3 uploads with django-storages
        # is set in settings.py with AWS_DEFAULT_ACL.
        # More info: http://django-common-configs.readthedocs.org/en/latest/configs/storage.html
        pass


class AzureStorageMixin(StorageMixin):
    """

        Filebrowser storage class for Azure storage blob.

        This mixin depends on django-storage dependency.
        Note that the latest version of django-storages
        only supports the Azure python sdk version 2.1.0!

        Follow the configuration instructions at
        https://django-storages.readthedocs.io/en/latest/backends/azure.html

        Add the following class to your 'storage_backend.py':

        class AzureFilebrowserStorage(AzureStorageMixin, AzureMediaStorage):
            pass

        and set the correct storage class (i.e. in your urls.py):

        from filebrowser.sites import site as fb_site
        from <your_project>.storage_backend import AzureFilebrowserStorage
        fb_site.storage = AzureFilebrowserStorage(
            location='',
        )

        Note: Permissions are not supported by Azure.
              Set FILEBROWSER_DEFAULT_PERMISSIONS to None

        Azure storage blob is only flat, so all directory
        structures are fake. To create an empty directory
        a file named 'dir.azr' with no content is created,
        which has the desired path.
        To hide these files in GUI add this to settings.py:
        FILEBROWSER_EXCLUDE = ['azr']

    """
    storage_type = 'azure'

    def sys_file(self):
        return 'dir.azr'

    def isdir(self, name):
        """
        Returns true if name exists and is a directory.
        """
        if name.endswith('/'):
            return True

        result = self.listdir(name)
        # if name contains dirs (result[0]) or files (result[1]) its a directory
        return len(result[0]) > 0 or len(result[1]) > 0

    def isfile(self, name):
        """
        Returns true if name exists and is a regular file.
        """
        # print('isfile', name, self.exists(name))
        return self.exists(name)

    def listdir(self, path=''):
        files = []
        dirs = []

        path_parts = path.split('/')

        # remove blank parts of path
        if path_parts[-1] == '':
            path_parts = path_parts[:-1]

        for name in self.list_all(path):
            name_parts = name.split('/')

            # check dir level of files
            if len(name_parts) == len(path_parts) + 1:
                files.append(name_parts[-1])
            # check dir level of dirs
            elif len(name_parts) == len(path_parts) + 2:
                if name_parts[-2] not in dirs:
                    dirs.append(name_parts[-2])
            else:
                pass
        return dirs, files

    def path(self, name):
        """
        Azure storage doesn't support Python's open() function.
        """
        return False

    def move(self, old_file_name, new_file_name, allow_overwrite=True):
        """
        Moves safely a file from one location to another.

        If allow_ovewrite==False and new_file_name exists, raises an exception.
        """
        print('move')
        pass

    def makedirs(self, name):
        """
        Creates all missing directories specified by name. Analogue to os.mkdirs().
        """
        self.service.create_blob_from_text(
            self.azure_container,
            name+'/'+self.sys_file(),
            '.'
        )
        pass

    def rmtree(self, name):
        """
        Deletes a directory and everything it contains. Analogue to shutil.rmtree().
        """
        print('rmtree')
        raise NotImplementedError()

    def setpermission(self, name):
        """
        # Permissions for Azure uploads with django-storages
        # is set in settings.py.
        # More info: http://django-common-configs.readthedocs.org/en/latest/configs/storage.html
        """
        pass