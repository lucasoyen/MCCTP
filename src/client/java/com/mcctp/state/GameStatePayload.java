package com.mcctp.state;

public class GameStatePayload {
    public final String type = "game_state";
    public final long timestamp;
    public final int selectedSlot;
    public final HeldItemInfo heldItem;
    public final HeldItemInfo offhandItem;
    public final PlayerStateInfo playerState;
    public final CombatContextInfo combatContext;
    public final PlayerInputInfo playerInput;
    public final ScreenStateInfo screenState;
    public final StatusEffectInfo statusEffects;
    public final ThreatInfo threats;
    public final long timeOfDay;
    public final String gameMode;

    public GameStatePayload(long timestamp, int selectedSlot, HeldItemInfo heldItem,
                            HeldItemInfo offhandItem, PlayerStateInfo playerState,
                            CombatContextInfo combatContext, PlayerInputInfo playerInput,
                            ScreenStateInfo screenState, StatusEffectInfo statusEffects,
                            ThreatInfo threats, long timeOfDay, String gameMode) {
        this.timestamp = timestamp;
        this.selectedSlot = selectedSlot;
        this.heldItem = heldItem;
        this.offhandItem = offhandItem;
        this.playerState = playerState;
        this.combatContext = combatContext;
        this.playerInput = playerInput;
        this.screenState = screenState;
        this.statusEffects = statusEffects;
        this.threats = threats;
        this.timeOfDay = timeOfDay;
        this.gameMode = gameMode;
    }
}
