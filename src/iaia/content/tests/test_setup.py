# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from iaia.content.testing import IAIA_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that iaia.content is properly installed."""

    layer = IAIA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if iaia.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'iaia.content'))

    def test_browserlayer(self):
        """Test that IIaiaContentLayer is registered."""
        from iaia.content.interfaces import (
            IIaiaContentLayer)
        from plone.browserlayer import utils
        self.assertIn(IIaiaContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IAIA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['iaia.content'])

    def test_product_uninstalled(self):
        """Test if iaia.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'iaia.content'))

    def test_browserlayer_removed(self):
        """Test that IIaiaContentLayer is removed."""
        from iaia.content.interfaces import \
            IIaiaContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IIaiaContentLayer, utils.registered_layers())
