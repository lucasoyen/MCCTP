"""Remote play - control Minecraft from another computer using keyboard and mouse."""

import sys
import threading
import time
from pynput import keyboard, mouse
from mcctp import SyncMCCTPClient, Actions

HOST = "129.21.148.235"
PORT = 8765
MOUSE_SENSITIVITY = 0.15

# Track key states to avoid spamming start/stop
held_keys = set()
running = True
locked = False  # mouse look enabled


def on_state(state):
    line = (f"[State] HP: {state.player_state.health} | "
            f"Pos: ({state.player_state.x}, {state.player_state.y}, {state.player_state.z}) | "
            f"Held: {state.held_item.name} ({state.held_item.category})")
    sys.stdout.write(f"\r\033[K{line}")
    sys.stdout.flush()


def log(msg):
    sys.stdout.write(f"\r\033[K{msg}\n")
    sys.stdout.flush()


def main():
    global running, locked

    client = SyncMCCTPClient(HOST, PORT)
    client.on_state(on_state)
    client.connect()
    log(f"Connected to MCCTP at {HOST}:{PORT}")
    log("Controls:")
    log("  WASD = Move | Space = Jump | Shift = Sneak | Ctrl = Sprint")
    log("  Mouse Move = Look (click window first) | Left Click = Attack | Right Click = Use")
    log("  1-9 = Select slot | Q = Drop | E = Inventory | F = Swap hands")
    log("  V = Toggle hotbar wheel")
    log("  ESC = Quit")
    log("")
    log("Press F1 to toggle mouse look on/off")
    log("")

    # --- Keyboard ---
    key_map = {
        'w': ("move", "forward"),
        's': ("move", "backward"),
        'a': ("move", "left"),
        'd': ("move", "right"),
    }

    def on_key_press(key):
        global running, locked
        try:
            if key == keyboard.Key.esc:
                running = False
                return False

            if key == keyboard.Key.f1:
                locked = not locked
                log(f"Mouse look: {'ON' if locked else 'OFF'}")
                return

            if key == keyboard.Key.space:
                client.send(Actions.jump())
                return

            if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                if 'sneak' not in held_keys:
                    held_keys.add('sneak')
                    client.send(Actions.sneak("start"))
                return

            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                if 'sprint' not in held_keys:
                    held_keys.add('sprint')
                    client.send(Actions.sprint("start"))
                return

            c = key.char if hasattr(key, 'char') and key.char else None
            if c is None:
                return

            # Movement keys
            if c in key_map:
                action_type, direction = key_map[c]
                if c not in held_keys:
                    held_keys.add(c)
                    client.send(Actions.move(direction, "start"))
                return

            # Hotbar slots 1-9
            if c in '123456789':
                client.send(Actions.select_slot(int(c) - 1))
                return

            if c == 'q':
                client.send(Actions.drop_item(full_stack=False))
            elif c == 'e':
                client.send(Actions.open_inventory())
            elif c == 'f':
                client.send(Actions.swap_hands())
            elif c == 'v':
                client.send(Actions.toggle_wheel())

        except Exception as e:
            log(f"Error: {e}")

    def on_key_release(key):
        try:
            if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                held_keys.discard('sneak')
                client.send(Actions.sneak("stop"))
                return

            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                held_keys.discard('sprint')
                client.send(Actions.sprint("stop"))
                return

            c = key.char if hasattr(key, 'char') and key.char else None
            if c and c in key_map:
                held_keys.discard(c)
                _, direction = key_map[c]
                client.send(Actions.move(direction, "stop"))

        except Exception as e:
            log(f"Error: {e}")

    # --- Mouse ---
    last_pos = [None, None]

    def on_mouse_move(x, y):
        if not locked:
            return
        if last_pos[0] is None:
            last_pos[0] = x
            last_pos[1] = y
            return

        dx = (x - last_pos[0]) * MOUSE_SENSITIVITY
        dy = (y - last_pos[1]) * MOUSE_SENSITIVITY
        last_pos[0] = x
        last_pos[1] = y

        if abs(dx) > 0.1 or abs(dy) > 0.1:
            try:
                client.send(Actions.look(yaw=dx, pitch=dy, relative=True))
            except Exception:
                pass

    def on_mouse_click(x, y, button, pressed):
        try:
            if button == mouse.Button.left:
                if pressed:
                    client.send(Actions.attack())
            elif button == mouse.Button.right:
                if pressed:
                    client.send(Actions.use_item("start"))
                else:
                    client.send(Actions.use_item("stop"))
        except Exception as e:
            log(f"Error: {e}")

    # Start listeners
    kb_listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
    ms_listener = mouse.Listener(on_move=on_mouse_move, on_click=on_mouse_click)
    kb_listener.start()
    ms_listener.start()

    try:
        while running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    log("\nDisconnecting...")
    # Release all held keys
    for c in list(held_keys):
        if c in key_map:
            _, direction = key_map[c]
            client.send(Actions.move(direction, "stop"))
        elif c == 'sneak':
            client.send(Actions.sneak("stop"))
        elif c == 'sprint':
            client.send(Actions.sprint("stop"))

    kb_listener.stop()
    ms_listener.stop()
    client.disconnect()
    print("\nBye!")


if __name__ == "__main__":
    main()
