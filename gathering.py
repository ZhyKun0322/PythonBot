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
    # Simulate a spruce tree nearby (offset)
    return (x + 5, y, z + 5)

def chop_tree(x, y, z, inventory):
    print(f"[Gather] Chopping spruce log at ({x}, {y}, {z})")
    # Simulate getting 5 logs per tree
    inventory['spruce_log'] = inventory.get('spruce_log', 0) + 5
    time.sleep(2)  # Simulate chopping time

def gather_materials(required, client, bot_position, inventory):
    print("[Gather] Starting material collection...")

    # Get how many spruce logs are needed
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

    client.write_chat("Done gathering spruce logs!")
    print("[Gather] All required logs collected.")
