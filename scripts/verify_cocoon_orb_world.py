#!/usr/bin/env python3
"""Verify a synthetic early world-orb packet from Cocoon.

The control models only the sourced rules used by the bounded analysis: one
world remains the same identity while carried or mounted, a compatible jump
pedestal makes its contained world enterable, and the first unlocked orb
ability manifests an otherwise absent bridge only while that orb is carried.
Names and route geometry are original fixtures rather than copied level data.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class WorldOrb:
    identity: str
    world: str
    ability: str
    ability_unlocked: bool = False
    location: str = "outer-ground"


@dataclass
class Packet:
    orb: WorldOrb
    avatar_world: str = "outer"
    avatar_marker: str = "start"
    carried_orb: str | None = None
    mounted_orb: str | None = None

    def pick_up(self) -> bool:
        if self.avatar_world != "outer" or self.carried_orb is not None:
            return False
        if self.orb.location not in {"outer-ground", "jump-pedestal"}:
            return False
        if self.orb.location == "jump-pedestal":
            self.mounted_orb = None
        self.orb.location = "carried"
        self.carried_orb = self.orb.identity
        return True

    def mount(self, pedestal_accepts: str) -> bool:
        if (
            self.avatar_world != "outer"
            or self.carried_orb != self.orb.identity
            or pedestal_accepts != self.orb.identity
        ):
            return False
        self.carried_orb = None
        self.mounted_orb = self.orb.identity
        self.orb.location = "jump-pedestal"
        return True

    def enter_or_exit(self) -> bool:
        if self.mounted_orb != self.orb.identity:
            return False
        if self.avatar_world == "outer":
            self.avatar_world = self.orb.world
            self.avatar_marker = "arrival"
        elif self.avatar_world == self.orb.world:
            self.avatar_world = "outer"
            self.avatar_marker = "jump-pedestal"
        else:
            return False
        return True

    def unlock_ability(self) -> bool:
        if self.avatar_world != self.orb.world or self.avatar_marker != "world-core":
            return False
        self.orb.ability_unlocked = True
        return True

    def bridge_is_present(self) -> bool:
        return (
            self.avatar_world == "outer"
            and self.avatar_marker == "bridge-locus"
            and self.carried_orb == self.orb.identity
            and self.orb.ability_unlocked
            and self.orb.ability == "manifest-bridge"
        )


def verify() -> None:
    orb = WorldOrb("orange-orb", "orange-world", "manifest-bridge")
    packet = Packet(orb)

    # A loose or merely carried orb is still a world, but it is not an active
    # jump destination until mounted on its compatible pedestal.
    assert packet.pick_up()
    assert not packet.enter_or_exit()
    assert not packet.mount("green-orb")
    assert packet.carried_orb == "orange-orb"
    assert packet.mount("orange-orb")
    assert packet.orb.identity == "orange-orb"
    assert packet.orb.world == "orange-world"

    # Entering and leaving transfers the avatar, not the orb.  The externally
    # mounted object and its contained world retain one stable identity.
    assert packet.enter_or_exit()
    assert packet.avatar_world == "orange-world"
    assert packet.orb.location == "jump-pedestal"
    assert not packet.unlock_ability()
    packet.avatar_marker = "world-core"
    assert packet.unlock_ability()
    assert packet.enter_or_exit()
    assert packet.avatar_world == "outer"
    assert packet.orb.identity == "orange-orb"

    # The first ability belongs to the unlocked orb but is available in the
    # outer route only while that exact orb is carried at its compatible locus.
    assert packet.pick_up()
    packet.avatar_marker = "bridge-locus"
    assert packet.bridge_is_present()
    packet.orb.location = "outer-ground"
    packet.carried_orb = None
    assert not packet.bridge_is_present()


if __name__ == "__main__":
    verify()
    print("PASS: Cocoon world-orb packet verified")
