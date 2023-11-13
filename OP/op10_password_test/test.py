"""Password validation tests."""
import password


def test__is_correct_length__too_short():
    """Test whether password of length 7 is not correct."""
    assert password.is_correct_length("passwor") is False


def test__is_correct_length__too_long():
    """Test whether password of length > 64 is incorrect."""
    assert password.is_correct_length("pass" * 18) is False


def test__is_correct_length__correct_length():
    """Test whether password of length 8 is correct."""
    assert password.is_correct_length("password") is True


def test__is_correct_length__empty():
    """Test whether empty password is incorrect."""
    assert password.is_correct_length("") is False


def test__is_correct_length__correct_length_only_numbers():
    """Test whether password of length 64 is correct."""
    assert password.is_correct_length("12345678" * 8) is True


def test__is_correct_length__correct_length_64():
    """Test whether password of length 64 is correct."""
    assert password.is_correct_length("pass" * 16) is True


def test__includes_uppercase__no_uppercase():
    """Test whether password without uppercase is incorrect."""
    assert password.includes_uppercase("password") is False


def test__includes_uppercase__with_uppercase():
    """Test whether password with uppercase is correct."""
    assert password.includes_uppercase("Password") is True


def test__includes_uppercase__with_uppercase_and_lowercase():
    """Test whether password with uppercase and lowercase is correct."""
    assert password.includes_uppercase("PassWord") is True


def test__includes_uppercase__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_uppercase("") is False


def test__includes_uppercase__only_uppercase():
    """Test whether password with only uppercase is correct."""
    assert password.includes_uppercase("PASSWORD") is True


def test__includes_uppercase__only_numbers():
    """Test whether password with only numbers is incorrect."""
    assert password.includes_uppercase("12345678") is False


def test__includes_lowercase__no_lowercase():
    """Test whether password without lowercase is incorrect."""
    assert password.includes_lowercase("PASSWORD") is False


def test__includes_lowercase__with_lowercase():
    """Test whether password with lowercase is correct."""
    assert password.includes_lowercase("Password") is True


def test_includes_lowercase__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_lowercase("") is False


def test__includes_lowercase__only_numbers():
    """Test whether password with only numbers is incorrect."""
    assert password.includes_lowercase("12345678") is False


def test__includes_special__no_special():
    """Test whether password without special is incorrect."""
    assert password.includes_special("Password") is False


def test__includes_special__with_special():
    """Test whether password with special is correct."""
    assert password.includes_special("Password!") is True


def test__includes_special__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_special("") is False


def test__includes_special__only_special():
    """Test whether password with only special is correct."""
    assert password.includes_special("!@#$%^&*()") is True


def test__includes_special__only_numbers():
    """Test whether password with only numbers is incorrect."""
    assert password.includes_special("12345678") is False


def test__includes_number__no_number():
    """Test whether password without number is incorrect."""
    assert password.includes_number("Password!") is False


def test__includes_number__with_number():
    """Test whether password with number is correct."""
    assert password.includes_number("Password1") is True


def test__includes_number__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_number("") is False


def test__includes_number__only_special():
    """Test whether password with only special is incorrect."""
    assert password.includes_number("!@#$%^&*()") is False


def test__is_different_from_old_password__same():
    """Test whether password is same as old password."""
    assert password.is_different_from_old_password("Password", "Password") is False


def test__is_different_from_old_password__different():
    """Test whether password is different from old password."""
    assert password.is_different_from_old_password("Password", "Password1") is True


def test__is_different_from_old_password__empty_old_pass():
    """Test whether password is different from empty old password."""
    assert password.is_different_from_old_password("", "Password") is True


def test__is_different_from_old_password__empty_new_pass():
    """Test whether password is different from empty new password."""
    assert password.is_different_from_old_password("Password", "") is False
