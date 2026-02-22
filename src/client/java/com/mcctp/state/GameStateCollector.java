package com.mcctp.state;

import com.google.gson.Gson;
import net.minecraft.client.MinecraftClient;
import net.minecraft.client.network.ClientPlayerEntity;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Hand;

public class GameStateCollector {
    private final Gson gson = new com.google.gson.GsonBuilder()
            .serializeSpecialFloatingPointValues()
            .create();

    public String collect(MinecraftClient client) {
        ClientPlayerEntity player = client.player;
        if (player == null) return null;

        int selectedSlot = player.getInventory().getSelectedSlot();
        ItemStack mainHand = player.getMainHandStack();
        ItemStack offHand = player.getStackInHand(Hand.OFF_HAND);

        long timeOfDay = client.world != null ? client.world.getTimeOfDay() % 24000 : 0;
        String gameMode = client.interactionManager != null
                ? client.interactionManager.getCurrentGameMode().getId()
                : "survival";

        GameStatePayload payload = new GameStatePayload(
                System.currentTimeMillis(),
                selectedSlot,
                new HeldItemInfo(mainHand),
                new HeldItemInfo(offHand),
                new PlayerStateInfo(player),
                new CombatContextInfo(player),
                new PlayerInputInfo(player),
                new ScreenStateInfo(client),
                new StatusEffectInfo(player),
                new ThreatInfo(player),
                timeOfDay,
                gameMode
        );

        return gson.toJson(payload);
    }
}
