# gathering.py

import time

# Placeholder for pathfinding/movement (you can replace this with real logic)
def walk_to(x, y, z, client):
    print(f"[Gather] Walking to ({x}, {y}, {z})")
    # TODO: Replace with real pathfinding or movement commands
    time.sleep(1)  # Simulate delay

# Simulated block detection (replace with real raycast or world scanning)
def find_nearest_tree(bot_position):
    x, y, z = bot_position
    return (x + 5, y, z + 5)  # Simulated tree location

def find_nearest_sheep(bot_position):
    x, y, z = bot_position
    return (x + 8, y, z + 3)  # Simulated sheep location

def chop_tree(x, y, z, inventory):
    print(f"[Gather] Chopping spruce log at ({x}, {y}, {z})")
    inventory['spruce_log'] = inventory.get('spruce_log', 0) + 5
    time.sleep(2)

def kill_sheep(x, y, z, inventory):
    print(f"[Gather] Killing sheep at ({x}, {y}, {z})")
    inventory['white_wool'] = inventory.get('white_wool', 0) + 2
    time.sleep(1)

def gather_materials(required, client, bot_position, inventory):
    print("[Gather] Starting material collection...")

    # GATHER LOGS
    needed_logs = required.get("spruce_log", 0)
    logs_have = inventory.get("spruce_log", 0)
    if logs_have < needed_logs:
        logs_needed = needed_logs - logs_have
        print(f"[Gather] Need {logs_needed} more spruce logs.")
        while inventory.get("spruce_log", 0) < needed_logs:
            tx, ty, tz = find_nearest_tree(bot_position)
            walk_to(tx, ty, tz, client)
            chop_tree(tx, ty, tz, inventory)
            client.write_chat(f"Chopped a tree. Current logs: {inventory['spruce_log']}")

    # GATHER WOOL
    needed_wool = required.get("white_wool", 0)
    wool_have = inventory.get("white_wool", 0)
    if wool_have < needed_wool:
        wool_needed = needed_wool - wool_have
        print(f"[Gather] Need {wool_needed} more white wool.")
        while inventory.get("white_wool", 0) < needed_wool:
            sx, sy, sz = find_nearest_sheep(bot_position)
            walk_to(sx, sy, sz, client)
            kill_sheep(sx, sy, sz, inventory)
            client.write_chat(f"Killed a sheep. Current wool: {inventory['white_wool']}")

    client.write_chat("Done gathering materials (logs + wool)!")
    print("[Gather] All logs and wool collected.")
            
