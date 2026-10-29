import tempfile
import unittest
from pathlib import Path
from tools.validate_captions import parse

class CaptionValidatorTests(unittest.TestCase):
    def write(self, text: str, suffix: str) -> Path:
        tmp = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=suffix, delete=False)
        tmp.write(text)
        tmp.close()
        self.addCleanup(lambda: Path(tmp.name).unlink(missing_ok=True))
        return Path(tmp.name)

    def test_valid_srt(self):
        path = self.write("1\n00:00:00,000 --> 00:00:01,000\nHello.\n\n2\n00:00:01,000 --> 00:00:02,000\nGoodbye.\n", ".srt")
        cues, errors = parse(path)
        self.assertEqual(len(cues), 2)
        self.assertEqual(errors, [])

    def test_valid_vtt(self):
        path = self.write("WEBVTT\n\n00:00:00.000 --> 00:00:01.000\nHello.\n", ".vtt")
        cues, errors = parse(path)
        self.assertEqual(len(cues), 1)
        self.assertEqual(errors, [])

    def test_rejects_overlap(self):
        path = self.write("1\n00:00:00,000 --> 00:00:02,000\nFirst.\n\n2\n00:00:01,000 --> 00:00:03,000\nSecond.\n", ".srt")
        _, errors = parse(path)
        self.assertTrue(any("overlaps" in e for e in errors))

    def test_rejects_empty_cue(self):
        path = self.write("1\n00:00:00,000 --> 00:00:01,000\n\n", ".srt")
        _, errors = parse(path)
        self.assertTrue(errors)

if __name__ == "__main__":
    unittest.main()
