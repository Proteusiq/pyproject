from {{cookiecutter.project_slug}}.echo import echo


def test_echo():
    assert echo("ping") == "pong"
