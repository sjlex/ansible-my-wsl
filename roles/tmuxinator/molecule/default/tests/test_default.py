import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        tmuxinator version
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("ansible", "/home/ansible/.config/tmuxinator/main-wsl1.yml"),
        ("ansible", "/home/ansible/.config/tmuxinator/main-wsl2.yml"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user


@pytest.mark.parametrize("user", ["ansible"])
def test_tmuxinator_layouts(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        tmuxinator list
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.find("main-wsl1") != -1
    assert cmd.stdout.find("main-wsl2") != -1
