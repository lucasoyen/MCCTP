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
    fall_distance: float = 0.0
    velocity_y: float = 0.0
    armor: int = 0
    is_climbing: bool = False
    recently_hurt: bool = False
    horizontal_collision: bool = False

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
            fall_distance=data.get("fallDistance", 0.0),
            velocity_y=data.get("velocityY", 0.0),
            armor=data.get("armor", 0),
            is_climbing=data.get("isClimbing", False),
            recently_hurt=data.get("recentlyHurt", False),
            horizontal_collision=data.get("horizontalCollision", False),
        )


@dataclass
class CombatContext:
    is_using_item: bool = False
    is_blocking: bool = False
    active_hand: str = "MAIN_HAND"
    crosshair_target: str = "MISS"
    crosshair_entity_type: Optional[str] = None
    crosshair_block_pos: Optional[list[int]] = None
    attack_cooldown: float = 1.0
    item_use_progress: float = 0.0

    @classmethod
    def from_dict(cls, data: dict) -> CombatContext:
        return cls(
            is_using_item=data.get("isUsingItem", False),
            is_blocking=data.get("isBlocking", False),
            active_hand=data.get("activeHand", "MAIN_HAND"),
            crosshair_target=data.get("crosshairTarget", "MISS"),
            crosshair_entity_type=data.get("crosshairEntityType"),
            crosshair_block_pos=data.get("crosshairBlockPos"),
            attack_cooldown=data.get("attackCooldown", 1.0),
            item_use_progress=data.get("itemUseProgress", 0.0),
        )


@dataclass
class PlayerInputInfo:
    movement_forward: float = 0.0
    movement_sideways: float = 0.0
    jump: bool = False
    sprint: bool = False
    sneak: bool = False
    attack: bool = False
    use_item: bool = False
    drop: bool = False
    swap_offhand: bool = False
    open_inventory: bool = False
    yaw_delta: float = 0.0
    pitch_delta: float = 0.0

    @classmethod
    def from_dict(cls, data: dict) -> PlayerInputInfo:
        return cls(
            movement_forward=data.get("movementForward", 0.0),
            movement_sideways=data.get("movementSideways", 0.0),
            jump=data.get("jump", False),
            sprint=data.get("sprint", False),
            sneak=data.get("sneak", False),
            attack=data.get("attack", False),
            use_item=data.get("useItem", False),
            drop=data.get("drop", False),
            swap_offhand=data.get("swapOffhand", False),
            open_inventory=data.get("openInventory", False),
            yaw_delta=data.get("yawDelta", 0.0),
            pitch_delta=data.get("pitchDelta", 0.0),
        )


@dataclass
class ScreenStateInfo:
    screen_open: bool = False
    screen_type: str = "none"
    cursor_x: float = -1.0
    cursor_y: float = -1.0
    mouse_left: bool = False
    mouse_right: bool = False
    shift_held: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> ScreenStateInfo:
        return cls(
            screen_open=data.get("screenOpen", False),
            screen_type=data.get("screenType", "none"),
            cursor_x=data.get("cursorX", -1.0),
            cursor_y=data.get("cursorY", -1.0),
            mouse_left=data.get("mouseLeft", False),
            mouse_right=data.get("mouseRight", False),
            shift_held=data.get("shiftHeld", False),
        )


@dataclass
class StatusEffectInfo:
    has_speed: bool = False
    has_slowness: bool = False
    has_strength: bool = False
    has_fire_resistance: bool = False
    has_poison: bool = False
    has_wither: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> StatusEffectInfo:
        return cls(
            has_speed=data.get("hasSpeed", False),
            has_slowness=data.get("hasSlowness", False),
            has_strength=data.get("hasStrength", False),
            has_fire_resistance=data.get("hasFireResistance", False),
            has_poison=data.get("hasPoison", False),
            has_wither=data.get("hasWither", False),
        )


@dataclass
class ThreatInfo:
    target_entity_hostile: bool = False
    target_distance: float = 0.0
    nearest_hostile_dist: float = 0.0
    nearest_hostile_yaw: float = 0.0
    hostile_count: int = 0

    @classmethod
    def from_dict(cls, data: dict) -> ThreatInfo:
        return cls(
            target_entity_hostile=data.get("targetEntityHostile", False),
            target_distance=data.get("targetDistance", 0.0),
            nearest_hostile_dist=data.get("nearestHostileDist", 0.0),
            nearest_hostile_yaw=data.get("nearestHostileYaw", 0.0),
            hostile_count=data.get("hostileCount", 0),
        )


@dataclass
class GameState:
    timestamp: int = 0
    selected_slot: int = 0
    held_item: HeldItemInfo = field(default_factory=HeldItemInfo)
    offhand_item: HeldItemInfo = field(default_factory=HeldItemInfo)
    player_state: PlayerState = field(default_factory=PlayerState)
    combat_context: CombatContext = field(default_factory=CombatContext)
    player_input: PlayerInputInfo = field(default_factory=PlayerInputInfo)
    screen_state: ScreenStateInfo = field(default_factory=ScreenStateInfo)
    status_effects: StatusEffectInfo = field(default_factory=StatusEffectInfo)
    threats: ThreatInfo = field(default_factory=ThreatInfo)
    time_of_day: int = 0
    game_mode: str = "survival"

    @classmethod
    def from_dict(cls, data: dict) -> GameState:
        return cls(
            timestamp=data.get("timestamp", 0),
            selected_slot=data.get("selectedSlot", 0),
            held_item=HeldItemInfo.from_dict(data.get("heldItem", {})),
            offhand_item=HeldItemInfo.from_dict(data.get("offhandItem", {})),
            player_state=PlayerState.from_dict(data.get("playerState", {})),
            combat_context=CombatContext.from_dict(data.get("combatContext", {})),
            player_input=PlayerInputInfo.from_dict(data.get("playerInput", {})),
            screen_state=ScreenStateInfo.from_dict(data.get("screenState", {})),
            status_effects=StatusEffectInfo.from_dict(data.get("statusEffects", {})),
            threats=ThreatInfo.from_dict(data.get("threats", {})),
            time_of_day=data.get("timeOfDay", 0),
            game_mode=data.get("gameMode", "survival"),
        )

    def to_control_dict(self) -> dict:
        """Flatten into the dict format expected by encode_game_state_v2().

        Returns a dict with all fields needed for the 46-dim game state vector
        plus resolved inputs for recording.
        """
        # Compute screen_open_type for the v2 game state encoder
        if not self.screen_state.screen_open:
            screen_open_type = "none"
        else:
            st = self.screen_state.screen_type.lower()
            if "inventory" in st:
                screen_open_type = "inventory"
            elif "container" in st or "chest" in st:
                screen_open_type = "chest"
            else:
                screen_open_type = self.screen_state.screen_type

        return {
            # Item context
            "held_item": self.held_item.name,
            "held_item_category": self.held_item.category,
            "offhand_category": self.offhand_item.category,

            # Vitals
            "health": self.player_state.health,
            "hunger": float(self.player_state.hunger),
            "armor": self.player_state.armor,

            # Movement flags
            "on_ground": self.player_state.on_ground,
            "in_water": self.player_state.in_water,
            "swimming": self.player_state.swimming,
            "flying": self.player_state.flying,
            "is_climbing": self.player_state.is_climbing,
            "on_fire": self.player_state.on_fire,
            "is_sprinting": self.player_state.sprinting,
            "is_sneaking": self.player_state.sneaking,
            "fall_distance": self.player_state.fall_distance,
            "velocity_y": self.player_state.velocity_y,

            # Combat
            "attack_cooldown": self.combat_context.attack_cooldown,
            "is_using_item": self.combat_context.is_using_item,
            "is_blocking": self.combat_context.is_blocking,
            "item_use_progress": self.combat_context.item_use_progress,
            "recently_hurt": self.player_state.recently_hurt,

            # Crosshair
            "crosshair_target": self.combat_context.crosshair_target,
            "crosshair_entity_type": self.combat_context.crosshair_entity_type,

            # Threats
            "target_entity_hostile": self.threats.target_entity_hostile,
            "target_distance": self.threats.target_distance,
            "nearest_hostile_dist": self.threats.nearest_hostile_dist,
            "nearest_hostile_yaw": self.threats.nearest_hostile_yaw,
            "hostile_count": self.threats.hostile_count,

            # Environment
            "time_of_day": self.time_of_day,
            "game_mode": self.game_mode,
            "screen_open": self.screen_state.screen_open,
            "screen_type": self.screen_state.screen_type,
            "screen_open_type": screen_open_type,

            # Status effects
            "has_speed": self.status_effects.has_speed,
            "has_slowness": self.status_effects.has_slowness,
            "has_strength": self.status_effects.has_strength,
            "has_fire_resistance": self.status_effects.has_fire_resistance,
            "has_fire_resist": self.status_effects.has_fire_resistance,
            "has_poison": self.status_effects.has_poison,
            "has_wither": self.status_effects.has_wither,

            # Extra
            "selected_slot": self.selected_slot,
            "horizontal_collision": self.player_state.horizontal_collision,

            # Position + look (for recorder, not part of 46-dim)
            "yaw": self.player_state.yaw,
            "pitch": self.player_state.pitch,
            "x": self.player_state.x,
            "y": self.player_state.y,
            "z": self.player_state.z,

            # Resolved player input (for recording)
            "movement_forward": self.player_input.movement_forward,
            "movement_sideways": self.player_input.movement_sideways,
            "input_jump": self.player_input.jump,
            "input_sprint": self.player_input.sprint,
            "input_sneak": self.player_input.sneak,
            "input_attack": self.player_input.attack,
            "input_use_item": self.player_input.use_item,
            "input_drop": self.player_input.drop,
            "input_swap_offhand": self.player_input.swap_offhand,
            "input_open_inventory": self.player_input.open_inventory,
            "yaw_delta": self.player_input.yaw_delta,
            "pitch_delta": self.player_input.pitch_delta,

            # Screen interaction (for recording)
            "cursor_x": self.screen_state.cursor_x,
            "cursor_y": self.screen_state.cursor_y,
            "mouse_left": self.screen_state.mouse_left,
            "mouse_right": self.screen_state.mouse_right,
            "shift_held": self.screen_state.shift_held,
        }
