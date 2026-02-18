package com.mcctp;

import com.mcctp.action.ActionDispatcher;
import com.mcctp.action.KeyReleaseScheduler;
import com.mcctp.config.MCCTPConfig;
import com.mcctp.hud.HotbarWheelRenderer;
import com.mcctp.hud.HotbarWheelState;
import com.mcctp.network.ConnectionManager;
import com.mcctp.network.WebSocketServer;
import com.mcctp.state.GameStateCollector;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.event.lifecycle.v1.ClientTickEvents;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayConnectionEvents;
import net.fabricmc.fabric.api.client.keybinding.v1.KeyBindingHelper;
import net.fabricmc.fabric.api.client.rendering.v1.HudRenderCallback;
import net.minecraft.client.option.KeyBinding;
import org.lwjgl.glfw.GLFW;

public class MCCTPClient implements ClientModInitializer {
    private WebSocketServer webSocketServer;
    private GameStateCollector stateCollector;
    private ActionDispatcher actionDispatcher;
    private int tickCounter;

    private static final KeyBinding TOGGLE_WHEEL = KeyBindingHelper.registerKeyBinding(
            new KeyBinding("key.mcctp.toggle_wheel", GLFW.GLFW_KEY_V, KeyBinding.Category.MISC)
    );

    @Override
    public void onInitializeClient() {
        MCCTPConfig config = MCCTPConfig.load();
        ConnectionManager connectionManager = new ConnectionManager();
        stateCollector = new GameStateCollector();
        actionDispatcher = new ActionDispatcher();
        webSocketServer = new WebSocketServer(config.getPort(), connectionManager, actionDispatcher);

        ClientPlayConnectionEvents.JOIN.register((handler, sender, client) -> {
            MCCTPMod.LOGGER.info("Joined world, starting MCCTP WebSocket server on port {}", config.getPort());
            webSocketServer.start();
        });

        ClientPlayConnectionEvents.DISCONNECT.register((handler, client) -> {
            MCCTPMod.LOGGER.info("Disconnected, stopping MCCTP WebSocket server");
            webSocketServer.stop();
        });

        ClientTickEvents.END_CLIENT_TICK.register(client -> {
            KeyReleaseScheduler.tick();
            if (client.player == null) return;

            if (TOGGLE_WHEEL.wasPressed()) {
                HotbarWheelState.toggle();
            }

            tickCounter++;
            if (tickCounter >= config.getTickInterval()) {
                tickCounter = 0;
                String stateJson = stateCollector.collect(client);
                if (stateJson != null) {
                    connectionManager.broadcast(stateJson);
                }
            }
        });

        HudRenderCallback.EVENT.register((drawContext, renderTickCounter) -> {
            HotbarWheelRenderer.render(drawContext);
        });

        MCCTPMod.LOGGER.info("MCCTP client initialized");
    }
}
