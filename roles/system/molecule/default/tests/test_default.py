import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        cat /etc/issue
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.startswith("Debian GNU/Linux")
