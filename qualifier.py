from random import choice


def generate_password(
    password_length: int = 8,
    has_symbols: bool = False,
    has_uppercase: bool = False,
    ignored_chars: list = [],
    allowed_chars: list = [],
) -> str:
    """Generates a random password.

    The password will be exactly `password_length` characters, but cannot be more than 1,000,000 characters.
    If `has_symbols` is True, the password will contain at least one symbol, such as #, !, or @.
    If `has_uppercase` is True, the password will contain at least one upper case letter.
    If `ignored_chars` is used, characters in that list will not be in the password.
    If `allowed_chars` is used, only charactrers from this list will be used, has_upper and has_symbols is satisfied.
    `allowed_chars` and `ignored_chars` cannot be used together
    """
    # Check for correct usage
    assert password_length < 1000000, "`password_length` must be < 1,000,000 chars"

    # make sure both `allowed_chars` and `ignored_chars` are not being used
    if ignored_chars:
        if allowed_chars:
            raise UserWarning(
                "Using both `allowed_chars` and `ignored_chars` is not allowed"
            )

    # make sure that the boolean conditions are met if using allowed_chars
    if allowed_chars:
        if has_symbols:
            for c in allowed_chars:
                assert (
                    c in has_all_params["symbols"]
                ), "Error, mismatched arguments. You want a symbol but there is not a symbol in `allowed_chars`"
        if has_uppercase:
            for c in allowed_chars:
                assert (
                    c in has_all_params["uppers"]
                ), "Error, mismatched arguments. You want a uppercase but there is not a uppercase in `allowed_chars`"

    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = """`~!@#$%^&*()-_=+[{]}\|/?.>,<;:'"]"""
    upchoice = lowers + uppers
    symchoice = lowers + symbols
    allchoice = lowers + uppers + symbols

    # has only symbols and lowers
    if has_symbols:
        if not has_uppercase:
            password = ""
            while not any(char in symbols for char in password):
                password = ""
                if ignored_chars:
                    for c in ignored_chars:
                        symchoice = symchoice.replace(c, "")

                    for i in range(password_length):
                        char = choice(symchoice)
                        password += char

                elif allowed_chars:
                    for i in range(password_length):
                        char = choice(allowed_chars)
                        password += char

                else:
                    for i in range(password_length):
                        char = choice(symchoice)
                        password += char

    # has only uppers and lowers
    if has_uppercase:
        if not has_symbols:
            password = ""
            while not any(char in uppers for char in password):
                password = ""
                if ignored_chars:
                    for c in ignored_chars:
                        upchoice = upchoice.replace(c, "")

                    for i in range(password_length):
                        char = choice(upchoice)
                        password += char

                elif allowed_chars:
                    for i in range(password_length):
                        char = choice(allowed_chars)
                        password += char

                else:
                    for i in range(password_length):
                        char = choice(upchoice)
                        password += char

    # has symbols, uppers and lowers
    if has_symbols:
        if has_uppercase:
            check = True
            while check:
                password = ""
                if ignored_chars:
                    for c in ignored_chars:
                        allchoice = allchoice.replace(c, "")

                    for i in range(password_length):
                        char = choice(allchoice)
                        password += char

                elif allowed_chars:
                    for i in range(password_length):
                        char = choice(allowed_chars)
                        password += char

                else:
                    for i in range(password_length):
                        char = choice(allchoice)
                        password += char

                if any(char in uppers for char in password):
                    if any(char in symbols for char in password):
                        check = False

    # has only lowercase
    else:
        password = ""
        if ignored_chars:
            for c in ignored_chars:
                lowers = lowers.replace(c, "")

            for i in range(password_length):
                char = choice(lowers)
                password += char

        elif allowed_chars:
            for i in range(password_length):
                char = choice(allowed_chars)
                password += char

        else:
            for i in range(password_length):
                char = choice(lowers)
                password += char

    return password
