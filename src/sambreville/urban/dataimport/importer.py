# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.csv.importer import CsvDataImporter
from sambreville.urban.dataimport.interfaces import ISambrevilleDataImporter


class SambrevilleDataImporter(CsvDataImporter):
    """ """

    implements(ISambrevilleDataImporter)
