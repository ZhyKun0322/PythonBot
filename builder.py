# builder.py

# Japanese house blueprint (3D list of block types)
blueprint = [
    [
        ["spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks"],
        ["spruce_planks", "white_wool", "white_wool", "glass_pane", "white_wool", "white_wool", "spruce_planks"],
        ["spruce_planks", "white_wool", "white_wool", "glass_pane", "white_wool", "white_wool", "spruce_planks"],
        ["spruce_planks", "white_wool", "white_wool", "glass_pane", "white_wool", "white_wool", "spruce_planks"],
        ["spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks", "spruce_planks"],
    ],
    [
        ["", "", "", "spruce_stairs", "", "", ""],
        ["", "white_wool", "white_wool", "white_wool", "white_wool", "white_wool", ""],
        ["", "white_wool", "", "", "", "white_wool", ""],
        ["", "white_wool", "", "", "", "white_wool", ""],
        ["", "white_wool", "white_wool", "white_wool", "white_wool", "white_wool", ""],
    ],
    [
        ["", "", "", "spruce_planks", "", "", ""],
        ["", "", "white_wool", "white_wool", "white_wool", "", ""],
        ["", "", "white_wool", "", "white_wool", "", ""],
        ["", "", "white_wool", "", "white_wool", "", ""],
        ["", "", "white_wool", "white_wool", "white_wool", "", ""],
    ],
    [
        ["", "", "", "spruce_slab", "", "", ""],
        ["", "", "", "spruce_slab", "", "", ""],
        ["", "", "", "spruce_slab", "", "", ""],
        ["", "", "", "spruce_slab", "", "", ""],
        ["", "", "", "spruce_slab", "", "", ""],
    ],
    [
        ["", "", "", "spruce_log", "", "", ""],
        ["", "", "", "spruce_log", "", "", ""],
        ["", "", "", "spruce_log", "", "", ""],
        ["", "", "", "spruce_log", "", "", ""],
        ["", "", "", "spruce_log", "", "", ""],
    ],
]

def build_blueprint(world, x, y, z, blueprint):
    for dy, layer in enumerate(blueprint):
        for dz, row in enumerate(layer):
            for dx, block in enumerate(row):
                if block:
                    world.setBlock(x + dx, y + dy, z + dz, block)

def count_required_blocks(blueprint):
    from collections import defaultdict
    counts = defaultdict(int)
    for layer in blueprint:
        for row in layer:
            for block in row:
                if block:
                    counts[block] += 1
    return dict(counts)
