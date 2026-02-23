MOVE = "move"
LOOK = "look"
JUMP = "jump"
SNEAK = "sneak"
SPRINT = "sprint"
ATTACK = "attack"
USE_ITEM = "use_item"
THROW_ITEM = "throw_item"
DROP_ITEM = "drop_item"
SELECT_SLOT = "select_slot"
SWAP_HANDS = "swap_hands"
OPEN_INVENTORY = "open_inventory"
CLOSE_SCREEN = "close_screen"
TOGGLE_WHEEL = "toggle_wheel"


class Actions:
    """Pre-built action message constructors."""

    @staticmethod
    def move(direction: str = "forward", state: str = "start") -> dict:
        return {"action": MOVE, "params": {"direction": direction, "state": state}}

    @staticmethod
    def look(yaw: float = 0, pitch: float = 0, relative: bool = True) -> dict:
        return {"action": LOOK, "params": {"yaw": yaw, "pitch": pitch, "relative": relative}}

    @staticmethod
    def jump() -> dict:
        return {"action": JUMP, "params": {}}

    @staticmethod
    def sneak(state: str = "start") -> dict:
        return {"action": SNEAK, "params": {"state": state}}

    @staticmethod
    def sprint(state: str = "start") -> dict:
        return {"action": SPRINT, "params": {"state": state}}

    @staticmethod
    def attack() -> dict:
        return {"action": ATTACK, "params": {}}

    @staticmethod
    def use_item(state: str = "start") -> dict:
        return {"action": USE_ITEM, "params": {"state": state}}

    @staticmethod
    def throw_item() -> dict:
        return {"action": THROW_ITEM, "params": {}}

    @staticmethod
    def drop_item(full_stack: bool = False) -> dict:
        return {"action": DROP_ITEM, "params": {"full_stack": full_stack}}

    @staticmethod
    def select_slot(slot: int) -> dict:
        return {"action": SELECT_SLOT, "params": {"slot": slot}}

    @staticmethod
    def swap_hands() -> dict:
        return {"action": SWAP_HANDS, "params": {}}

    @staticmethod
    def open_inventory() -> dict:
        return {"action": OPEN_INVENTORY, "params": {}}

    @staticmethod
    def close_screen() -> dict:
        """Close the currently open screen (equivalent to pressing Escape)."""
        return {"action": CLOSE_SCREEN, "params": {}}

    @staticmethod
    def toggle_wheel() -> dict:
        return {"action": TOGGLE_WHEEL, "params": {}}
