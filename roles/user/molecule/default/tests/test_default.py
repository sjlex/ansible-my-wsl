import pytest


@pytest.mark.parametrize("user", ["root", "user"])
def test_user_is_exist(host, user):
    passwd = host.file("/etc/passwd")
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        id -a
        """,
    )

    if user == "user":
        assert cmd.stdout.startswith("uid=1000(user)")
        assert passwd.contains("user:x:1000:1000::/home/user:/bin/bash")
    elif user == "root":
        assert cmd.stdout.startswith("uid=0(root)")
        assert passwd.contains("root:x:0:0:root:/root:/bin/bash")

    assert cmd.rc == 0
