# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from sambreville.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of sambreville.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sambreville.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('sambreville.urban.dataimport'))

    def test_uninstall(self):
        """Test if sambreville.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['sambreville.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('sambreville.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ISambrevilleUrbanDataimportLayer is registered."""
        from sambreville.urban.dataimport.interfaces import ISambrevilleUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(ISambrevilleUrbanDataimportLayer in utils.registered_layers())
