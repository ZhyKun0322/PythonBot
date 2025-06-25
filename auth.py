# auth.py

def handle_auth(msg, client, password):
    """
    Detects LoginSecurity messages and sends /login or /register commands automatically.
    """
    try:
        msg = msg.lower()
        if "please register" in msg:
            print("[Auth] Registering...")
            client.write_chat(f"/register {password} {password}")
        elif "please login" in msg:
            print("[Auth] Logging in...")
            client.write_chat(f"/login {password}")
    except Exception as e:
        print("[Auth Error]", e)
