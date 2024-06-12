"""Unit Tests for the Base Engine and specialised Engines classes.

This module contains unit tests for the Base Engine and specialised Engines."""

import unittest
from abc import ABC
from engine.base_engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    """Tests for the Engine Class.

    This tests that the Engine base class is correctly implemented according to specification.
    """
    def test_engine_is_subclass_of_abstract_base_class(self):
        """Test that the Engine class is an instance of the ABC class."""
        self.assertTrue(issubclass(Engine, ABC))

    def test_engine_needs_service(self):
        """Test that the Engine class has a needs_service method."""
        self.assertTrue(hasattr(Engine, 'needs_service'))


class TestCapuletEngine(unittest.TestCase):
    """Tests for the CapuletEngine Class.

    This tests that the CapuletEngine class is correctly implemented.
    """
    def test_capulet_engine_is_subclass_of_engine(self):
        """Test that the CapuletEngine class is an instance of the Engine class."""
        self.assertTrue(issubclass(CapuletEngine, Engine))

    def test_capulet_engine_needs_service(self):
        """Test that the CapuletEngine class has a needs_service method"""
        self.assertTrue(hasattr(CapuletEngine, 'needs_service'))

    def test_capulet_engine_needs_service_returns_bool(self):
        """Test that the needs_service method returns a boolean"""
        self.assertIsInstance(CapuletEngine(0, 0).needs_service(), bool)

    def test_capulet_engine_needs_service_returns_true(self):
        """Test that the needs_service method returns True when the engine needs service"""
        self.assertTrue(CapuletEngine(30001, 0).needs_service())

    def test_capulet_engine_needs_service_returns_false(self):
        """Test that the needs_service method returns False when the engine does not need service"""
        self.assertFalse(CapuletEngine(30000, 0).needs_service())


class TestSternmanEngine(unittest.TestCase):
    """Tests for the SternmanEngine Class.

    This tests that the SternmanEngine class is correctly implemented.
    """
    def test_sternman_engine_is_subclass_of_engine(self):
        """Test that the SternmanEngine class is an instance of the Engine class."""
        self.assertTrue(issubclass(SternmanEngine, Engine))

    def test_sternman_engine_needs_service(self):
        """Test that the SternmanEngine class has a needs_service method."""
        self.assertTrue(hasattr(SternmanEngine, 'needs_service'))

    def test_sternman_engine_needs_service_returns_bool(self):
        """Test that the needs_service method returns a boolean"""
        self.assertIsInstance(SternmanEngine(True).needs_service(), bool)

    def test_sternman_engine_needs_service_returns_true(self):
        """Test that the needs_service method returns True when the engine needs service."""
        self.assertTrue(SternmanEngine(True).needs_service())

    def test_sternman_engine_needs_service_returns_false(self):
        """Test that the needs_service method returns False when the engine does not need service."""
        self.assertFalse(SternmanEngine(False).needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    """Tests for the WilloughbyEngine Class.

    This tests that the WilloughbyEngine class is correctly implemented.
    """
    def test_willoughby_engine_is_subclass_of_engine(self):
        """Test that the WilloughbyEngine class is an instance of the Engine class."""
        self.assertTrue(issubclass(WilloughbyEngine, Engine))

    def test_willoughby_engine_needs_service(self):
        """Test that the WilloughbyEngine class has a needs_service method."""
        self.assertTrue(hasattr(WilloughbyEngine, 'needs_service'))

    def test_willoughby_engine_needs_service_returns_bool(self):
        """Test that the needs_service method returns a boolean."""
        self.assertIsInstance(WilloughbyEngine(0, 0).needs_service(), bool)

    def test_willoughby_engine_needs_service_returns_true(self):
        """Test that the needs_service method returns True when the engine needs service."""
        self.assertTrue(WilloughbyEngine(60001, 0).needs_service())

    def test_willoughby_engine_needs_service_returns_false(self):
        """Test that the needs_service method returns False when the engine does not need service."""
        self.assertFalse(WilloughbyEngine(60000, 0).needs_service())



if __name__ == '__main__':
    unittest.main()
