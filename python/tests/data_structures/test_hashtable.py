import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashtable
    for item in hashtable.buckets:
        if item:
            keys = []
            current = item
            while current:
                keys.append([current.key, current.value])
                current = current.next
            keys.sort()  # Sort the key-value pairs
            actual.append(keys)

    expected = [[["listen", "to me"], ["silent", True]], [["ahmad", 30]]]

    assert actual == expected

def test_hash_in_range():
    hashtable = Hashtable(size=1024)

    # Hash several keys and check if they are within the range [0, size-1]
    for key in ["apple", "banana", "cherry", "orange"]:
        hashed_index = hashtable.hash(key)
        assert 0 <= hashed_index < 1024


