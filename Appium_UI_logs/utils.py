import subprocess

def get_logcat_output(lines=50):
    try:
        subprocess.run(["adb", "logcat", "-c"])
        result = subprocess.run(
            ["adb", "logcat", "-d", "-t", str(lines)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"⚠️ Failed to get logcat logs: {e}"
