commands.py

from builder import build_blueprint, blueprint

build_location = None  # Global build spot

def handle_command(msg, client, bot_position, world): global build_location

# Get plain text
if isinstance(msg, dict) and "text" in msg:
    msg = msg["text"]
elif isinstance(msg, str):
    pass
else:
    return

msg = msg.strip().lower()

if msg == "!buildhere":
    build_location = tuple(bot_position)
    print(f"[Command] Build location set to {build_location}")
    client.write_chat("Got it! I’ll build here next time you say !buildhouse.")

elif msg == "!buildwhere":
    if build_location:
        client.write_chat(f"I'm set to build at: {build_location}")
    else:
        client.write_chat("No build location set. Use !buildhere first.")

elif msg == "!buildhouse":
    if not build_location:
        client.write_chat("No build location set. Use !buildhere first.")
        return
    x, y, z = build_location
    client.write_chat("Building Japanese house... This might take a moment.")
    build_blueprint(world, x, y, z, blueprint)
    client.write_chat("Done! Japanese house has been built.")

elif msg == "!status":
    client.write_chat("I'm online, connected, and listening!")

elif msg == "!stop":
    client.write_chat("Okay, stopping what I’m doing.")
    # TODO: Hook this to movement/gather/build stop

# You can add more commands here later (e.g., !gohome, !buildfarm, !patrol)

