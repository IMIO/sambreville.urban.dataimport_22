# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.csv.settings import CSVImporterFromImportSettings


class SambrevilleImporterSettingsForm(ImporterSettingsForm):
    """ """


class SambrevilleImporterSettings(ImporterSettings):
    """ """
    form = SambrevilleImporterSettingsForm


class SambrevilleImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = SambrevilleImporterSettings


class SambrevilleImporterFromImportSettings(CSVImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(SambrevilleImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
