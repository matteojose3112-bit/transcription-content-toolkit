# Tools

## Caption validator

The `validate_captions.py` utility checks basic SRT and WebVTT formatting, sequential SRT cue numbers, non-empty cue text, valid start/end order, chronological order, and overlapping cues. It uses only the Python standard library.

From the repository root:

```bash
python tools/validate_captions.py examples/sample-captions.srt examples/sample-captions.vtt
python -m unittest discover -s tests -v
```

A passing result is a structural check only. It does not prove that the words match the recording or that caption timing is synchronized to the media.
