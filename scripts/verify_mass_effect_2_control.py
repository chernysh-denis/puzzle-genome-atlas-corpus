"""Source-bounded Mass Effect 2 opening transition control, not game emulation."""

from dataclasses import dataclass, field


@dataclass
class Opening:
    phase: str = "sr1"
    squad: tuple[str, ...] = ()
    orders: dict[str, str] = field(default_factory=dict)
    paused: bool = False
    queued_powers: dict[str, str] = field(default_factory=dict)
    mech_layers: list[str] = field(default_factory=lambda: ["shield", "armour", "health"])
    collector_evidence: bool = False
    interrupt: str | None = None
    custody: str | None = None
    dossiers: bool = False
    free_ship_control: bool = False

    def advance_prologue(self) -> None:
        if self.phase != "sr1":
            raise ValueError("prologue starts on SR-1")
        self.phase = "lazarus"
        self.squad = ("Jacob",)

    def reach_colony(self) -> None:
        if self.phase != "lazarus" or "Jacob" not in self.squad:
            raise ValueError("Lazarus and Jacob precede the colony")
        self.phase = "colony"
        self.squad = ("Jacob", "Miranda")

    def order(self, member: str, target: str) -> None:
        if self.phase != "colony" or member not in self.squad:
            raise ValueError("address one present squadmate")
        self.orders[member] = target

    def open_wheel(self) -> None:
        if self.phase != "colony" or self.paused:
            raise ValueError("wheel requires live colony combat")
        self.paused = True

    def queue_power(self, member: str, power: str, effect: str) -> None:
        if not self.paused or member not in self.squad:
            raise ValueError("queue a present squadmate while paused")
        if member in self.queued_powers:
            raise ValueError("one power per squadmate per held wheel")
        if self.mech_layers and self.mech_layers[0] != "health" and effect == "health-control":
            raise ValueError("active protection blocks health-only control")
        self.queued_powers[member] = power

    def close_wheel(self) -> None:
        if not self.paused:
            raise ValueError("wheel not open")
        self.paused = False
        self.queued_powers.clear()

    def remove_current_layer(self) -> str:
        if self.phase != "colony" or self.paused or not self.mech_layers:
            raise ValueError("resolve the encounter in live combat")
        return self.mech_layers.pop(0)

    def inspect_veetor(self) -> None:
        if self.phase != "colony" or self.mech_layers:
            raise ValueError("the heavy mech must be defeated first")
        self.collector_evidence = True
        self.phase = "veetor"

    def decide_custody(self, interrupt: str, custody: str) -> None:
        if self.phase != "veetor" or not self.collector_evidence:
            raise ValueError("evidence and dialogue gate required")
        if interrupt not in {"paragon", "renegade", "none"}:
            raise ValueError("invalid offered interruption")
        if custody not in {"Tali", "Cerberus"}:
            raise ValueError("invalid custody recipient")
        self.interrupt = interrupt
        self.custody = custody
        self.phase = "report"

    def accept_ship(self) -> None:
        if self.phase != "report" or not self.custody or not self.collector_evidence:
            raise ValueError("settle the report before ship command")
        self.phase = "normandy_sr2"
        self.dossiers = True
        self.free_ship_control = True

    def positive_terminal(self) -> bool:
        return (
            self.phase == "normandy_sr2"
            and self.collector_evidence
            and self.interrupt == "paragon"
            and self.custody == "Tali"
            and self.dossiers
            and self.free_ship_control
        )


def fixed_trace() -> Opening:
    opening = Opening()
    opening.advance_prologue()
    opening.reach_colony()
    opening.order("Jacob", "left cover")
    opening.order("Miranda", "right cover")
    opening.open_wheel()
    opening.queue_power("Miranda", "Overload", "shield")
    opening.close_wheel()
    for layer in ("shield", "armour", "health"):
        assert opening.remove_current_layer() == layer
    opening.inspect_veetor()
    opening.decide_custody("paragon", "Tali")
    opening.accept_ship()
    assert opening.positive_terminal()
    return opening


if __name__ == "__main__":
    result = fixed_trace()
    print(
        "Mass Effect 2 source-model control passed: "
        f"{result.phase}, {len(result.squad)} supplied squadmates, "
        f"{len(result.orders)} independent orders, {result.custody} custody, "
        "future dossiers only"
    )
