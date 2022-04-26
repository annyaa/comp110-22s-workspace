"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale

__author__ = "730478408"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty Linked List should raise an IndexError for any index value."""
    list_index: int = 3
    with pytest.raises(IndexError):
        value_at(None, list_index)


def test_value_at_zero_index() -> None:
    """Value_at with index 0 should return the data of the current Node being processed on the list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_value_at_non_zero_index() -> None:
    """Value_at with a non-zero index should return the data of the Node stored at the given index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_value_at_another_non_zero_index() -> None:
    """Value_at with a non-zero index should return the data of the Node stored at the given index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def max_empty() -> None:
    """Calling max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_last_value_in_list() -> None:
    """Calling max when it is the last value in the linked list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_inside_list() -> None:
    """Calling max when it is one of the inner values in the linked list."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30


def test_max_value_first_in_list() -> None:
    """Calling max when it is the first value in the linked list."""
    linked_list = Node(30, Node(20, Node(10, None)))
    assert max(linked_list) == 30


def test_linkify_empty() -> None:
    """Calling linkify on an empty list."""
    item_list: list[int] = []
    assert linkify(item_list) is None


def test_linkify_multiple() -> None:
    """Calling linkify on a list with many items."""
    item_list: list[int] = [10, 20, 30, 40]
    assert is_equal(linkify(item_list), Node(10, Node(20, Node(30, Node(40, None)))))


def test_scale_non_empty() -> None:
    """Scale returns a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
    assert is_equal(scale(linkify([1, 2, 3]), 2), Node(2, Node(4, Node(6, None))))


def test_scale_empty() -> None:
    """Scale returns None when input of Optional[Node] is None."""
    assert is_equal(scale(None, 2), None)
    