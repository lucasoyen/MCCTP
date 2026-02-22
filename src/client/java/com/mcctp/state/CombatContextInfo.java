package com.mcctp.state;

import net.minecraft.client.MinecraftClient;
import net.minecraft.client.network.ClientPlayerEntity;
import net.minecraft.entity.Entity;
import net.minecraft.registry.Registries;
import net.minecraft.util.Hand;
import net.minecraft.util.hit.BlockHitResult;
import net.minecraft.util.hit.EntityHitResult;
import net.minecraft.util.hit.HitResult;
import net.minecraft.util.math.BlockPos;

public class CombatContextInfo {
    public final boolean isUsingItem;
    public final boolean isBlocking;
    public final String activeHand;
    public final String crosshairTarget;
    public final String crosshairEntityType;
    public final int[] crosshairBlockPos;
    public final float attackCooldown;
    public final float itemUseProgress;

    public CombatContextInfo(ClientPlayerEntity player) {
        this.isUsingItem = player.isUsingItem();
        this.isBlocking = player.isBlocking();
        this.activeHand = player.getActiveHand() == Hand.MAIN_HAND ? "MAIN_HAND" : "OFF_HAND";
        this.attackCooldown = player.getAttackCooldownProgress(0.0f);

        if (player.isUsingItem()) {
            int maxUse = player.getActiveItem().getMaxUseTime(player);
            this.itemUseProgress = maxUse > 0
                ? Math.min(1.0f, (float) player.getItemUseTime() / (float) maxUse)
                : 0.0f;
        } else {
            this.itemUseProgress = 0.0f;
        }

        MinecraftClient client = MinecraftClient.getInstance();
        HitResult hitResult = client.crosshairTarget;

        if (hitResult instanceof EntityHitResult entityHit) {
            this.crosshairTarget = "ENTITY";
            Entity entity = entityHit.getEntity();
            this.crosshairEntityType = Registries.ENTITY_TYPE.getId(entity.getType()).toString();
            this.crosshairBlockPos = null;
        } else if (hitResult instanceof BlockHitResult blockHit) {
            this.crosshairTarget = "BLOCK";
            this.crosshairEntityType = null;
            BlockPos pos = blockHit.getBlockPos();
            this.crosshairBlockPos = new int[]{pos.getX(), pos.getY(), pos.getZ()};
        } else {
            this.crosshairTarget = "MISS";
            this.crosshairEntityType = null;
            this.crosshairBlockPos = null;
        }
    }
}
