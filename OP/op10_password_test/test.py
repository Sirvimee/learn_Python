"""Password validation tests."""
import password


def test__is_correct_length__too_short():
    """Test whether password of length < 8 is not correct."""
    assert password.is_correct_length("p") is False
    assert password.is_correct_length("passwor") is False
    assert password.is_correct_length("pas") is False


def test__is_correct_length__too_long():
    """Test whether password of length > 64 is incorrect."""
    assert password.is_correct_length("pass" * 18) is False
    assert password.is_correct_length("p" * 65) is False


def test__is_correct_length__correct_length():
    """Test whether password of length between 8 and 64 is correct."""
    assert password.is_correct_length("password") is True
    assert password.is_correct_length("passwordaaaaa") is True
    assert password.is_correct_length("p" * 64) is True


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
    assert password.includes_uppercase("lowercase") is False


def test__includes_uppercase__with_uppercase():
    """Test whether password with uppercase is correct."""
    assert password.includes_uppercase("Password") is True


def test__includes_uppercase__with_uppercase_and_lowercase():
    """Test whether password with uppercase and lowercase is correct."""
    assert password.includes_uppercase("PassWord") is True
    assert password.includes_uppercase("Password123") is True
    assert password.includes_uppercase("AbCdEfGhIjKlMnOpQrStUvWxYz") is True


def test__includes_uppercase__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_uppercase("") is False


def test__includes_uppercase__only_uppercase():
    """Test whether password with only uppercase is correct."""
    assert password.includes_uppercase("PASSWORD") is True


def test__includes_uppercase__only_numbers():
    """Test whether password with only numbers is incorrect."""
    assert password.includes_uppercase("12345678") is False


def test_includes_uppercase__every_uppercase_letter():
    """Test whether password with every uppercase letter is correct."""
    assert password.includes_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ") is True


def test__includes_lowercase__no_lowercase():
    """Test whether password without lowercase is incorrect."""
    assert password.includes_lowercase("PASSWORD") is False


def test__includes_lowercase__with_lowercase():
    """Test whether password with lowercase is correct."""
    assert password.includes_lowercase("Password") is True


def test__includes_lowercase__only_lowercase_letters():
    """Test whether password with only lowercase is correct."""
    assert password.includes_lowercase("asdfghjk") is True


def test__includes_lowercase__every_lowercase_letter():
    """Test whether password with every lowercase letter is correct."""
    assert password.includes_lowercase("abcdefghijklmnopqrstuvwxyz") is True


def test_includes_lowercase__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_lowercase("") is False


def test__includes_lowercase__only_numbers():
    """Test whether password with only numbers is incorrect."""
    assert password.includes_lowercase("12345678") is False


def test__includes_special__no_special():
    """Test whether password without special is incorrect."""
    assert password.includes_special("NoSpecial123") is False


def test__includes_special__with_special():
    """Test whether password with special is correct."""
    assert password.includes_special("Password!") is True
    assert password.includes_special("Hello@World") is True


def test__includes_special__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_special("") is False


def test__includes_special__only_special():
    """Test whether password with only special is correct."""
    assert password.includes_special("!@#$%^&*()") is True


def test__includes_special__includes_whitespace():
    """Test whether password with whitespace is correct."""
    assert password.includes_special("Password 123") is True
    assert password.includes_special("Hello World") is True


def test__includes_special__only_numbers():
    """Test whether password with only numbers is incorrect."""
    assert password.includes_special("12345678") is False


def test__includes_number__no_number():
    """Test whether password without number is incorrect."""
    assert password.includes_number("NoNumbers!") is False


def test__includes_number__with_number():
    """Test whether password with number is correct."""
    assert password.includes_number("Password123") is True
    assert password.includes_number("12345AbC") is True


def test__includes_number__every_number():
    """Test whether password with every number is correct."""
    assert password.includes_number("1234567890") is True


def test__includes_number__empty():
    """Test whether empty password is incorrect."""
    assert password.includes_number("") is False


def test__includes_number__only_special():
    """Test whether password with only special is incorrect."""
    assert password.includes_number("!@#$%^&*()") is False


def test__is_different_from_old_password__same():
    """Test whether password is same as old password."""
    assert password.is_different_from_old_password("Password", "Password") is False
    assert password.is_different_from_old_password("Password1", "Password") is False
    assert password.is_different_from_old_password("Password", "password") is False
    assert password.is_different_from_old_password("password", "Password") is False
    assert password.is_different_from_old_password("Password", "Passwod") is False
    assert password.is_different_from_old_password("Password1", "Passwor1") is False
    assert password.is_different_from_old_password("Password1", "Pssword1") is False
    assert password.is_different_from_old_password("Password", "assword") is False
    assert password.is_different_from_old_password("Password1", "sswor1") is False
    assert password.is_different_from_old_password("Password1", "ssword1") is False
    assert password.is_different_from_old_password("Password", "Passw") is False
    assert password.is_different_from_old_password("Password1", "Password") is False
    assert password.is_different_from_old_password("Password1", "Passwod") is False
    assert password.is_different_from_old_password("Password", "drowssaP") is False
    assert password.is_different_from_old_password("Password1", "1drowssap") is False
    assert password.is_different_from_old_password("Password1", "1drowsswop") is False
    assert password.is_different_from_old_password("Password", "drowss") is False
    assert password.is_different_from_old_password("Password1", "1drows") is False
    assert password.is_different_from_old_password("Password1", "1drowsso") is False


def test__is_different_from_old_password__different():
    """Test whether password is different from old password."""
    assert password.is_different_from_old_password("IamNewPass123", "Password1") is True


def test__is_different_from_old_password__empty_old_pass():
    """Test whether password is different from empty old password."""
    assert password.is_different_from_old_password("", "Password") is True


def test__is_different_from_old_password__empty_new_pass():
    """Test whether password is different from empty new password."""
    assert password.is_different_from_old_password("Password", "") is False
