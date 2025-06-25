from typing import List from mcpi.minecraft import Minecraft from mcpi import block import time

Block codes for clarity

W = "white_wool"        # Wall panel S = "spruce_planks"     # Flooring or porch L = "spruce_log"        # Pillars / frame G = "glass_pane"        # Window A = "air"               # Nothing T = "spruce_stairs"     # Roof tile B = "spruce_slab"       # Roof flat top

3D Blueprint: [Y][Z][X]

blueprint = [ [  # Layer 0 - Floor base [A, A, S, S, S, S, S, A, A], [A, S, S, S, S, S, S, S, A], [S, S, S, S, S, S, S, S, S], [S, S, S, S, S, S, S, S, S], [S, S, S, S, S, S, S, S, S], [A, S, S, S, S, S, S, S, A], [A, A, S, S, S, S, S, A, A] ], [  # Layer 1 - Pillars and base walls [A, A, L, A, A, A, L, A, A], [A, L, W, W, W, W, W, L, A], [L, W, W, G, G, G, W, W, L], [L, W, W, W, W, W, W, W, L], [L, W, W, G, G, G, W, W, L], [A, L, W, W, W, W, W, L, A], [A, A, L, A, A, A, L, A, A], ], [  # Layer 2 - Upper walls [A, A, L, A, A, A, L, A, A], [A, L, W, W, W, W, W, L, A], [L, W, A, A, G, A, A, W, L], [L, W, A, A, A, A, A, W, L], [L, W, A, A, G, A, A, W, L], [A, L, W, W, W, W, W, L, A], [A, A, L, A, A, A, L, A, A], ], [  # Layer 3 - Roof base (stairs layer) [A, T, A, A, A, A, A, T, A], [T, A, A, A, A, A, A, A, T], [A, A, A, A, A, A, A, A, A], [A, A, A, A, A, A, A, A, A], [A, A, A, A, A, A, A, A, A], [T, A, A, A, A, A, A, A, T], [A, T, A, A, A, A, A, T, A], ], [  # Layer 4 - Roof top (slabs) [A, A, A, A, B, A, A, A, A], [A, A, A, B, B, B, A, A, A], [A, A, B, B, B, B, B, A, A], [A, B, B, B, B, B, B, B, A], [A, A, B, B, B, B, B, A, A], [A, A, A, B, B, B, A, A, A], [A, A, A, A, B, A, A, A, A] ] ]

Dictionary mapping from block name to Minecraft block ID (simplified version)

block_map = { "air": block.AIR.id, "spruce_log": 17,        # block.WOOD.id with metadata needed "spruce_planks": 5, "white_wool": 35, "glass_pane": 102, "spruce_stairs": 53,     # Regular stairs, might vary in real builds "spruce_slab": 44        # Slabs, same note }

def build_blueprint(mc: Minecraft, x: int, y: int, z: int, blueprint: List[List[List[str]]]): height = len(blueprint) depth = len(blueprint[0]) width = len(blueprint[0][0])

for dy in range(height):
    for dz in range(depth):
        for dx in range(width):
            block_name = blueprint[dy][dz][dx]
            if block_name == "air":
                continue
            block_id = block_map.get(block_name, block.AIR.id)
            mc.setBlock(x + dx, y + dy, z + dz, block_id)
            time.sleep(0.01)  # slight delay to reduce server strain

Example usage:

mc = Minecraft.create()

pos = mc.player.getTilePos()

build_blueprint(mc, pos.x, pos.y, pos.z, blueprint)

You can replace the example usage with a bot command handler or socket trigger.

This code assumes a local Minecraft Pi or modded Java environment with mcpi API.

