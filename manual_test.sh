#!/bin/bash

set -e

# Auto setup project for Django >=2

VIRTUALENV_DIR="envs"
PROJECTS_DIR="projects"
BASEDIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SED=sed
if [[ "$OSTYPE" == "darwin"* ]]; then
    SED=gsed
fi

echo "prepare projects for manual testing"
source "$VIRTUALENV_DIR/$1/bin/activate"

PROJECT_PATH="$PROJECTS_DIR/fb-dj$1"
rm -rf $PROJECT_PATH
mkdir -p $PROJECT_PATH
django-admin startproject fb $PROJECT_PATH
ln -s "$BASEDIR/filebrowser" "$PROJECT_PATH/filebrowser"

echo "
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filebrowser',
    #'dummy',
)

import os.path
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
" >> "$PROJECT_PATH/fb/settings.py"

echo "
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from filebrowser.sites import site

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
" > "$PROJECT_PATH/fb/urls.py"

(
    cd $PROJECT_PATH
    mkdir -p media/uploads/
    mkdir -p media/_versions/

    python manage.py test

    python manage.py startapp dummy

    echo "
from django.db import models
from filebrowser.fields import FileBrowseField, FileBrowseUploadField

class DemoItem(models.Model):
    title = models.CharField('Title', max_length=210)
    attach = FileBrowseField('Attach', max_length=200)
    upload = FileBrowseUploadField('Attach', max_length=200)
" > dummy/models.py

    echo "
from django.contrib import admin
from dummy.models import DemoItem

class DemoAdmin(admin.ModelAdmin):
    pass

admin.site.register(DemoItem, DemoAdmin)
    " > dummy/admin.py

    $SED -i "s/#'dummy/'dummy/" fb/settings.py

    python manage.py makemigrations

    python manage.py migrate
    python manage.py createsuperuser --noinput --username admin --email admin@sample.com
)