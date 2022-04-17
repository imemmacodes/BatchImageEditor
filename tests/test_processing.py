from pathlib import Path

from batch_image_editor.processing import SUPPORTED_SUFFIXES, build_output_path


def test_supported_suffixes_are_lowercase():
    for suffix in SUPPORTED_SUFFIXES:
        assert suffix == suffix.lower()


def test_build_output_path_preserves_structure(tmp_path: Path):
    input_root = tmp_path / "input"
    input_root.mkdir()
    file_path = input_root / "nested" / "photo.jpg"
    file_path.parent.mkdir()
    file_path.touch()

    output_root = tmp_path / "output"
    result = build_output_path(input_root, output_root, file_path)

    expected = output_root / "nested" / "photo.jpg"
    assert result == expected

