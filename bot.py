# bot.py

import json
from minecraft.networking.connection import Connection
from minecraft.networking.packets import ChatMessagePacket
from auth import handle_auth

# Load config
with open("config.json") as f:
    config = json.load(f)

# Setup connection
client = Connection(
    server_host=config["host"],
    server_port=config["port"],
    username=config["username"],
    version=config["version"]
)

# Global bot position
bot_position = [0, 0, 0]

# On join
@client.listener()
def on_join(packet):
    print("[+] Connected to the server!")

# On chat
@client.listener()
def on_chat(packet):
    msg = packet.json_data
    print("[CHAT]", msg)
    handle_auth(msg, client, config["password"])

# Track position updates
@client.listener()
def on_position_and_look(packet):
    bot_position[0] = packet.x
    bot_position[1] = packet.y
    bot_position[2] = packet.z

# Connect to the server
try:
    client.connect()
except Exception as e:
    print("[ERROR] Failed to connect:", e)
    exit(1)

# Keep the bot alive
print("[Bot] Running... press Ctrl+C to stop.")
try:
    while True:
        pass
except KeyboardInterrupt:
    print("[Bot] Shutting down.")
    client.disconnect()
