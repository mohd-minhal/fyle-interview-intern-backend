import pytest
from core.libs.assertions import assert_auth, assert_true

def test_assert_auth_unauthorized():
    with pytest.raises(Exception) as exc_info:
        assert_auth(False)
    assert str(exc_info.value) == "UNAUTHORIZED"

def test_assert_auth_custom_message():
    with pytest.raises(Exception) as exc_info:
        assert_auth(False, msg='Custom Unauthorized Message')
    assert str(exc_info.value) == "Custom Unauthorized Message"

def test_assert_true_forbidden():
    with pytest.raises(Exception) as exc_info:
        assert_true(False)
    assert str(exc_info.value) == "FORBIDDEN"

def test_assert_true_custom_message():
    with pytest.raises(Exception) as exc_info:
        assert_true(False, msg='Custom Forbidden Message')
    assert str(exc_info.value) == "Custom Forbidden Message"
