#!/usr/bin/env python3
"""Verify the bounded Her Story transcript-query retrieval packet.

The corpus below is deliberately synthetic: it reproduces the documented
search, ordering, five-result cap and breadcrumb-refinement behaviour without
copying Her Story's copyrighted interview transcript.
"""

from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Clip:
    clip_id: str
    timestamp: int
    transcript: str


CLIPS = (
    Clip("CLIP-001", 10, "The murder report describes a quiet station."),
    Clip("CLIP-002", 20, "I heard the word murder beside the blue window."),
    Clip("CLIP-003", 30, "The murder question returned after midnight."),
    Clip("CLIP-004", 40, "That murder headline omitted the weather."),
    Clip("CLIP-005", 50, "The murder file remained on the desk."),
    Clip("CLIP-006", 60, "The blue window changed how the murder looked."),
    Clip("CLIP-007", 70, "The final murder note mentioned no window."),
)


def normalise(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"[a-z0-9]+", text.casefold()))


def search(query: str) -> tuple[int, tuple[Clip, ...]]:
    terms = normalise(query)
    if not terms:
        return 0, ()
    matches = [
        clip
        for clip in CLIPS
        if all(term in normalise(clip.transcript) for term in terms)
    ]
    matches.sort(key=lambda clip: clip.timestamp)
    return len(matches), tuple(matches[:5])


def verify() -> None:
    total, broad = search("murder")
    assert total == 7
    assert tuple(clip.clip_id for clip in broad) == (
        "CLIP-001",
        "CLIP-002",
        "CLIP-003",
        "CLIP-004",
        "CLIP-005",
    )

    # Repeating a broad query cannot page past the authored five-result cap.
    assert search("MURDER")[1] == broad

    # CLIP-002 supplies a rarer term. Reusing it reveals a chronologically later
    # record that the broad query counted but could not expose.
    _, refined = search("blue window")
    assert tuple(clip.clip_id for clip in refined) == ("CLIP-002", "CLIP-006")
    assert refined[-1].clip_id not in {clip.clip_id for clip in broad}

    # Matching is term-based rather than an arbitrary substring lookup.
    assert search("mur")[0] == 0
    assert search("   ") == (0, ())


if __name__ == "__main__":
    verify()
    print("PASS: Her Story capped transcript-query packet verified")
