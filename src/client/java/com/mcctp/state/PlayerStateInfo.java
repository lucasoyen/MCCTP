package com.mcctp.state;

import net.minecraft.client.network.ClientPlayerEntity;

public class PlayerStateInfo {
    public final float health;
    public final float maxHealth;
    public final int hunger;
    public final float saturation;
    public final double x;
    public final double y;
    public final double z;
    public final float yaw;
    public final float pitch;
    public final boolean onGround;
    public final boolean sprinting;
    public final boolean sneaking;
    public final boolean swimming;
    public final boolean flying;
    public final boolean inWater;
    public final boolean onFire;

    public PlayerStateInfo(ClientPlayerEntity player) {
        this.health = player.getHealth();
        this.maxHealth = player.getMaxHealth();
        this.hunger = player.getHungerManager().getFoodLevel();
        this.saturation = player.getHungerManager().getSaturationLevel();
        this.x = Math.round(player.getX() * 10.0) / 10.0;
        this.y = Math.round(player.getY() * 10.0) / 10.0;
        this.z = Math.round(player.getZ() * 10.0) / 10.0;
        this.yaw = player.getYaw();
        this.pitch = player.getPitch();
        this.onGround = player.isOnGround();
        this.sprinting = player.isSprinting();
        this.sneaking = player.isSneaking();
        this.swimming = player.isSwimming();
        this.flying = player.getAbilities().flying;
        this.inWater = player.isTouchingWater();
        this.onFire = player.isOnFire();
    }
}
