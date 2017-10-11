# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer

from imio.urban.dataimport.interfaces import IUrbanDataImporter


class ISambrevilleUrbanDataimportLayer(IDefaultPloneLayer):
    """ Marker interface that defines a Zope 3 browser layer."""


class ISambrevilleDataImporter(IUrbanDataImporter):
    """ Marker interface for ISambreville csv importer """
