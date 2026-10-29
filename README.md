# Transcription & Content Toolkit

A practical toolkit for turning audio and video into clear written deliverables: transcripts, subtitles, captions, and voiceover-ready scripts.

> **Status:** Usable service MVP with templates, fictional formatting demonstrations, quality checklists, and a Python caption-file validator.

## Start here

1. Review the [transcript style guide](templates/transcript-style-guide.md).
2. Use the [project intake questionnaire](templates/intake-questionnaire.md) to confirm scope.
3. Use the [voiceover script template](templates/voiceover-script-template.md) for narration projects.
4. Review the [multi-speaker transcript example](examples/sample-transcript-multi-speaker.md).
5. Compare [verbatim vs. clean transcript editing](examples/before-after-edit.md).
6. Inspect the SRT and WebVTT examples, including [short-form SRT](examples/short-form-captions.srt) and [short-form WebVTT](examples/short-form-captions.vtt).
7. Run the [quality-control checklist](checklists/quality-control.md) and [delivery checklist](checklists/delivery-checklist.md).

## Functional utility

The [caption validator](tools/README.md) checks basic SRT/WebVTT structure, cue numbering, blank text, invalid time ranges, chronology, and overlapping cues.

Run from the repository root:

```bash
python tools/validate_captions.py examples/sample-captions.srt examples/sample-captions.vtt
python -m unittest discover -s tests -v
```

A structural pass does not prove transcription accuracy or exact synchronization with the recording; human review against the source media is still required.

## Services this toolkit supports

- Verbatim or clean transcription
- Speaker labels and timestamps
- SRT subtitles and WebVTT captions
- Proofreading and transcript formatting
- Voiceover / narration script formatting
- Clear delivery packaging and quality checks

See [starter service packages](SERVICE_PACKAGES.md) for proposed scope, turnaround, and intake requirements.

## Quality principles

- Accuracy over polish: do not invent unclear words.
- Mark uncertainty transparently.
- Verify names, numbers, terminology, speaker labels, and timestamps against the media.
- Keep verbatim, clean transcript, and summary deliverables distinct.
- Follow client permissions and privacy requirements.
- Confirm caption timing and platform requirements against the actual source.

## Current limitations

The existing transcript examples are fictional formatting demonstrations, not transcripts of real recordings. A portfolio-ready service sample still needs an end-to-end review against a permitted source recording. Automated checks are structural only.

## Quality checks

Automated tests run through GitHub Actions on pushes and pull requests. See the [test workflow](.github/workflows/test.yml).
