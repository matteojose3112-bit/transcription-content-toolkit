# Transcription & Content Toolkit

A practical toolkit for turning audio and video into clear written deliverables: transcripts, subtitles, captions, and voiceover-ready scripts.

> **Status:** Usable service MVP with templates, fictional formatting examples, a Python caption-file validator, automated tests, and a prepared synthetic-voice workflow demonstration.

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

A structural pass does not prove transcription accuracy or exact synchronization with a recording; human review against the source media is still required.

## Portfolio demonstration

A separate portfolio pack includes an original synthetic-voice WAV, matching speaker-labeled transcript, SRT captions, and WebVTT captions. The dialogue was written first and then rendered with text-to-speech; this demonstrates delivery formats and a workflow, **not** blind transcription accuracy on naturally recorded audio. The accompanying fictional transcript PDF also uses illustrative timestamps.

Before presenting the service as proven on real-world audio, complete and review a sample transcribed from a naturally spoken, public-domain or explicitly authorized recording. Verify every word, speaker label, and caption boundary against the actual media.

## Services and marketplace setup

See [starter service packages](SERVICE_PACKAGES.md) for scope, turnaround, and intake requirements, and the [Fiverr/Upwork listing draft](GIG_LISTING_DRAFT.md) for title, description, suggested pricing, FAQ, and buyer requirements. Listing copy and prices are drafts; the gigs are not published by this repository.

## Quality principles

- Accuracy over polish: do not invent unclear words.
- Mark uncertainty transparently.
- Verify names, numbers, terminology, speaker labels, and timestamps against the media.
- Keep verbatim, clean transcript, and summary deliverables distinct.
- Follow client permissions and privacy requirements.
- Confirm caption timing and platform requirements against the actual source.

## Current limitations

The current repository examples are fictional formatting demonstrations. The separate synthetic-voice sample uses a known script, so it is not a real-world transcription accuracy test. Automated checks are structural only. A real-media end-to-end sample and marketplace publication remain open launch tasks.

## Quality checks

Automated tests run through GitHub Actions on pushes and pull requests. See the [test workflow](.github/workflows/test.yml).
