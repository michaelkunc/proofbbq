from proofbbq.models.user import User


def test_user_init():
    user = User()
    assert user
