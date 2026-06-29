import sounddevice as sd

print("=" * 60)
print("SoundDevice Version:", sd.__version__)
print("=" * 60)

# 查找 WASAPI HostAPI
wasapi = None
for i, api in enumerate(sd.query_hostapis()):
    print(f"{i}: {api['name']}")

    if "WASAPI" in api["name"]:
        wasapi = i

print("=" * 60)

if wasapi is None:
    print("❌ WASAPI NOT FOUND")
    exit()

print(f"✅ WASAPI HostAPI Index: {wasapi}")

print("=" * 60)

# 列出 WASAPI 设备
devices = sd.query_devices()

for index, dev in enumerate(devices):

    if dev["hostapi"] != wasapi:
        continue

    print(
        f"{index:2d} | "
        f"In:{dev['max_input_channels']} "
        f"Out:{dev['max_output_channels']} | "
        f"{dev['name']}"
    )

print("=" * 60)

print("Trying WasapiSettings...")

try:

    ws = sd.WasapiSettings()

    print("✅ WasapiSettings OK")
    print(ws)

except Exception as e:

    print("❌ WasapiSettings FAILED")
    print(e)