BatchImageEditor
=================

BatchImageEditor is a small command-line tool for batch editing images.
It is designed as a personal side project to quickly apply simple
transformations to many files at once.

Planned features include:
- Resize multiple images to a fixed width or height
- Convert formats (for example, PNG to JPEG)
- Apply simple filters such as grayscale
- Run dry-runs to preview what will be changed

Example usage
-------------

Resize a folder of photos to a maximum width of 1280 pixels:

    python -m batch_image_editor ./photos ./resized --width 1280

Show which files would be processed without writing anything:

    python -m batch_image_editor ./photos ./resized --width 1280 --dry-run

Development notes
-----------------

This project is intentionally small and opinionated. If something feels
too clever for what it does, it probably should be simplified instead.

The tests are kept lightweight and focus on exercising small pieces of
logic rather than end-to-end behaviour.

This project is intentionally simple and focused on learning and
experimentation rather than production use.
