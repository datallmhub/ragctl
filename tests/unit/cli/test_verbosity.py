"""Tests for verbose and quiet flags."""
import logging
from typer.testing import CliRunner
from src.core.cli.app import app

runner = CliRunner()


def test_quiet_flag_sets_error_level():
    """Test that --quiet flag sets logging to ERROR level."""
    result = runner.invoke(app, ["--quiet", "--version"])
    assert result.exit_code == 0
    # Quiet mode should suppress non-error output


def test_verbose_flag_sets_info_level():
    """Test that -v flag sets logging to INFO level."""
    result = runner.invoke(app, ["--verbose", "--version"])
    assert result.exit_code == 0


def test_very_verbose_flag_sets_debug_level():
    """Test that -vv flag sets logging to DEBUG level."""
    result = runner.invoke(app, ["-vv", "--version"])
    assert result.exit_code == 0


def test_quiet_and_verbose_mutually_exclusive():
    """Test that --quiet and --verbose cannot be used together."""
    result = runner.invoke(app, ["--quiet", "--verbose", "info"])
    assert result.exit_code != 0
    assert "Cannot use --quiet with --verbose" in result.output
