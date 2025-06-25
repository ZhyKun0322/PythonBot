# gathering.py

import time

# Placeholder for pathfinding/movement (you can replace this with real logic)
def walk_to(x, y, z, client):
    print(f"[Gather] Walking to ({x}, {y}, {z})")
    time.sleep(1)

def find_nearest_tree(bot_position):
    x, y, z = bot_position
    return (x + 5, y, z + 5)

def find_nearest_sheep(bot_position):
    x, y, z = bot_position
    return (x + 8, y, z + 3)

def find_nearest_sand(bot_position):
    x, y, z = bot_position
    return (x + 4, y, z - 6)

def walk_to_furnace(bot_position):
    x, y, z = bot_position
    return (x + 2, y, z + 2)  # Simulated furnace spot

def chop_tree(x, y, z, inventory):
    print(f"[Gather] Chopping spruce log at ({x}, {y}, {z})")
    inventory['spruce_log'] = inventory.get('spruce_log', 0) + 5
    time.sleep(2)

def kill_sheep(x, y, z, inventory):
    print(f"[Gather] Killing sheep at ({x}, {y}, {z})")
    inventory['white_wool'] = inventory.get('white_wool', 0) + 2
    time.sleep(1)

def mine_sand(x, y, z, inventory):
    print(f"[Gather] Mining sand at ({x}, {y}, {z})")
    inventory['sand'] = inventory.get('sand', 0) + 4
    time.sleep(1)

def smelt_sand(inventory):
    print("[Gather] Smelting sand into glass...")
    sand = inventory.get('sand', 0)
    smelted = min(sand, 10)  # Simulate smelting 10 max
    inventory['glass'] = inventory.get('glass', 0) + smelted
    inventory['sand'] -= smelted
    time.sleep(2)

def craft_glass_panes(inventory):
    print("[Gather] Crafting glass panes from glass")
    glass = inventory.get('glass', 0)
    panes = (glass // 6) * 16
    if panes > 0:
        inventory['glass_pane'] = inventory.get('glass_pane', 0) + panes
        inventory['glass'] -= (panes // 16) * 6
    time.sleep(1)

def gather_materials(required, client, bot_position, inventory):
    print("[Gather] Starting material collection...")

    # GATHER LOGS
    needed_logs = required.get("spruce_log", 0)
    logs_have = inventory.get("spruce_log", 0)
    if logs_have < needed_logs:
        while inventory.get("spruce_log", 0) < needed_logs:
            tx, ty, tz = find_nearest_tree(bot_position)
            walk_to(tx, ty, tz, client)
            chop_tree(tx, ty, tz, inventory)
            client.write_chat(f"Chopped a tree. Logs: {inventory['spruce_log']}")

    # GATHER WOOL
    needed_wool = required.get("white_wool", 0)
    wool_have = inventory.get("white_wool", 0)
    if wool_have < needed_wool:
        while inventory.get("white_wool", 0) < needed_wool:
            sx, sy, sz = find_nearest_sheep(bot_position)
            walk_to(sx, sy, sz, client)
            kill_sheep(sx, sy, sz, inventory)
            client.write_chat(f"Killed sheep. Wool: {inventory['white_wool']}")

    # GATHER GLASS PANES
    needed_panes = required.get("glass_pane", 0)
    panes_have = inventory.get("glass_pane", 0)
    if panes_have < needed_panes:
        while inventory.get("glass_pane", 0) < needed_panes:
            sand_x, sand_y, sand_z = find_nearest_sand(bot_position)
            walk_to(sand_x, sand_y, sand_z, client)
            mine_sand(sand_x, sand_y, sand_z, inventory)
            fx, fy, fz = walk_to_furnace(bot_position)
            walk_to(fx, fy, fz, client)
            smelt_sand(inventory)
            craft_glass_panes(inventory)
            client.write_chat(f"Crafted panes. Panes: {inventory['glass_pane']}")

    client.write_chat("Done gathering logs, wool, and glass panes!")
    print("[Gather] All essential materials collected.")
    
