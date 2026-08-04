# ♃ ☿ 𓂀 SPAM IDENTITY TESTS 𓂀 ☿ ♃

from app.core.security.identity import IdentityEngine



def test_identity_is_stable():

    engine = IdentityEngine(
        "secret"
    )


    first = engine.generate_identity(
        "123456"
    )


    second = engine.generate_identity(
        "123456"
    )


    assert first == second



def test_different_users_have_different_hash():

    engine = IdentityEngine(
        "secret"
    )


    user_a = engine.generate_identity(
        "111"
    )


    user_b = engine.generate_identity(
        "222"
    )


    assert user_a != user_b



def test_tripcode_generation():

    engine = IdentityEngine(
        "secret"
    )


    identity = engine.generate_identity(
        "123"
    )


    tripcode = engine.generate_tripcode(
        identity
    )


    assert tripcode.startswith("#")