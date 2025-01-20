# coding: utf-8

"""
    Todo API

    A simple Todo API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from todosdk.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_todos_get(self) -> None:
        """Test case for todos_get

        Get all todos
        """
        pass

    def test_todos_post(self) -> None:
        """Test case for todos_post

        Create a new todo
        """
        pass

    def test_todos_todo_id_get(self) -> None:
        """Test case for todos_todo_id_get

        Get a specific todo
        """
        pass


if __name__ == '__main__':
    unittest.main()
