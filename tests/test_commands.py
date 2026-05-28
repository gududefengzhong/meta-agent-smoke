import shlex

from commands import build_archive_command


def test_build_archive_command_quotes_paths_with_spaces() -> None:
    command = build_archive_command("/tmp/my archive.tgz", "/tmp/source dir")

    assert shlex.split(command) == [
        "tar",
        "-czf",
        "/tmp/my archive.tgz",
        "/tmp/source dir",
    ]
