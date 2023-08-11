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


@pytest.mark.parametrize(
    "package_name",
    [
        "curl",
        "wget",
        "gnupg",
        "build-essential",
    ],
)
def test_package_is_installed(host, package_name):
    host_package = host.package(package_name)

    assert host_package.is_installed
