#!/usr/bin/env python

"""Tests for `create_meson_app` package."""


import unittest
from click.testing import CliRunner

from create_meson_app import create_meson_app
from create_meson_app import cli


class TestCreate_meson_app(unittest.TestCase):
    """Tests for `create_meson_app` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'create_meson_app.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
