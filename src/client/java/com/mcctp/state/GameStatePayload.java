package com.mcctp.state;

public class GameStatePayload {
    public final String type = "game_state";
    public final long timestamp;
    public final int selectedSlot;
    public final HeldItemInfo heldItem;
    public final HeldItemInfo offhandItem;
    public final PlayerStateInfo playerState;
    public final CombatContextInfo combatContext;

    public GameStatePayload(long timestamp, int selectedSlot, HeldItemInfo heldItem,
                            HeldItemInfo offhandItem, PlayerStateInfo playerState,
                            CombatContextInfo combatContext) {
        this.timestamp = timestamp;
        this.selectedSlot = selectedSlot;
        this.heldItem = heldItem;
        this.offhandItem = offhandItem;
        this.playerState = playerState;
        this.combatContext = combatContext;
    }
}
