from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class HeldItemInfo:
    name: str = "minecraft:air"
    category: str = "EMPTY"
    stack_count: int = 0
    max_durability: int = 0
    current_durability: int = 0

    @classmethod
    def from_dict(cls, data: dict) -> HeldItemInfo:
        return cls(
            name=data.get("name", "minecraft:air"),
            category=data.get("category", "EMPTY"),
            stack_count=data.get("stackCount", 0),
            max_durability=data.get("maxDurability", 0),
            current_durability=data.get("currentDurability", 0),
        )


@dataclass
class PlayerState:
    health: float = 20
    max_health: float = 20
    hunger: int = 20
    saturation: float = 5
    x: float = 0
    y: float = 0
    z: float = 0
    yaw: float = 0
    pitch: float = 0
    on_ground: bool = True
    sprinting: bool = False
    sneaking: bool = False
    swimming: bool = False
    flying: bool = False
    in_water: bool = False
    on_fire: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> PlayerState:
        return cls(
            health=data.get("health", 20),
            max_health=data.get("maxHealth", 20),
            hunger=data.get("hunger", 20),
            saturation=data.get("saturation", 5),
            x=data.get("x", 0),
            y=data.get("y", 0),
            z=data.get("z", 0),
            yaw=data.get("yaw", 0),
            pitch=data.get("pitch", 0),
            on_ground=data.get("onGround", True),
            sprinting=data.get("sprinting", False),
            sneaking=data.get("sneaking", False),
            swimming=data.get("swimming", False),
            flying=data.get("flying", False),
            in_water=data.get("inWater", False),
            on_fire=data.get("onFire", False),
        )


@dataclass
class CombatContext:
    is_using_item: bool = False
    is_blocking: bool = False
    active_hand: str = "MAIN_HAND"
    crosshair_target: str = "MISS"
    crosshair_entity_type: Optional[str] = None
    crosshair_block_pos: Optional[list[int]] = None

    @classmethod
    def from_dict(cls, data: dict) -> CombatContext:
        return cls(
            is_using_item=data.get("isUsingItem", False),
            is_blocking=data.get("isBlocking", False),
            active_hand=data.get("activeHand", "MAIN_HAND"),
            crosshair_target=data.get("crosshairTarget", "MISS"),
            crosshair_entity_type=data.get("crosshairEntityType"),
            crosshair_block_pos=data.get("crosshairBlockPos"),
        )


@dataclass
class GameState:
    timestamp: int = 0
    selected_slot: int = 0
    held_item: HeldItemInfo = field(default_factory=HeldItemInfo)
    offhand_item: HeldItemInfo = field(default_factory=HeldItemInfo)
    player_state: PlayerState = field(default_factory=PlayerState)
    combat_context: CombatContext = field(default_factory=CombatContext)

    @classmethod
    def from_dict(cls, data: dict) -> GameState:
        return cls(
            timestamp=data.get("timestamp", 0),
            selected_slot=data.get("selectedSlot", 0),
            held_item=HeldItemInfo.from_dict(data.get("heldItem", {})),
            offhand_item=HeldItemInfo.from_dict(data.get("offhandItem", {})),
            player_state=PlayerState.from_dict(data.get("playerState", {})),
            combat_context=CombatContext.from_dict(data.get("combatContext", {})),
        )
