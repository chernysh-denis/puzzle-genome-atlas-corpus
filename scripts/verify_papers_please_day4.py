#!/usr/bin/env python3
"""Executable control for the bounded Papers, Please Day 4 packet."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Entrant:
    nation: str
    passport_present: bool
    passport_expiry: str
    entry_ticket_date: Optional[str]
    entry_permit_present: bool
    id_card_present: bool
    wanted: bool = False


DAY = "1982-11-26"
FOREIGN_NATIONS = {"Kolechia", "Impor", "Antegria", "Obristan", "Republia", "United Federation"}


def active_rules(day: int) -> tuple[str, ...]:
    common = ("passport", "current", "wanted")
    if day == 3:
        return common + ("foreigner_ticket",)
    if day == 4:
        return common + ("foreigner_permit", "arstotzkan_id")
    raise ValueError("Control models only Days 3 and 4")


def violations(entrant: Entrant, day: int) -> tuple[str, ...]:
    rules = active_rules(day)
    found: list[str] = []
    if "passport" in rules and not entrant.passport_present:
        found.append("missing passport")
    if "current" in rules and entrant.passport_expiry < DAY:
        found.append("expired passport")
    if "wanted" in rules and entrant.wanted:
        found.append("wanted criminal")
    if entrant.nation in FOREIGN_NATIONS:
        if "foreigner_ticket" in rules and entrant.entry_ticket_date != DAY:
            found.append("missing or invalid entry ticket")
        if "foreigner_permit" in rules and not entrant.entry_permit_present:
            found.append("missing entry permit")
    if entrant.nation == "Arstotzka" and "arstotzkan_id" in rules and not entrant.id_card_present:
        found.append("missing identity card")
    return tuple(found)


def correlate(left: str, right: str, entrant: Entrant, day: int) -> str:
    pair = {left, right}
    if pair == {"empty permit area", "foreigners require entry permit"}:
        return "discrepancy" if "missing entry permit" in violations(entrant, day) else "matching"
    if pair == {"passport expiry", "inspection date"}:
        return "discrepancy" if "expired passport" in violations(entrant, day) else "matching"
    return "no correlation"


def citation(entrant: Entrant, day: int, verdict: str) -> bool:
    expected = "deny" if violations(entrant, day) else "approve"
    return verdict != expected


def can_call_next(clock_minutes: int, minimum_scripted_processed: bool) -> bool:
    return clock_minutes < 12 * 60 or not minimum_scripted_processed


def run() -> None:
    control = Entrant(
        nation="Kolechia",
        passport_present=True,
        passport_expiry="1983-05-10",
        entry_ticket_date=DAY,
        entry_permit_present=False,
        id_card_present=False,
    )

    assert violations(control, 3) == ()
    assert violations(control, 4) == ("missing entry permit",)
    assert correlate("empty permit area", "foreigners require entry permit", control, 4) == "discrepancy"
    assert correlate("passport expiry", "inspection date", control, 4) == "matching"
    assert correlate("passport expiry", "foreigners require entry permit", control, 4) == "no correlation"
    assert citation(control, 4, "deny") is False
    assert citation(control, 4, "approve") is True
    assert can_call_next(11 * 60 + 59, True) is True
    assert can_call_next(12 * 60, True) is False
    assert can_call_next(12 * 60, False) is True

    print("Papers, Please control passed: policy swap, discrepancy, verdict, citation, and shift gate.")


if __name__ == "__main__":
    run()
