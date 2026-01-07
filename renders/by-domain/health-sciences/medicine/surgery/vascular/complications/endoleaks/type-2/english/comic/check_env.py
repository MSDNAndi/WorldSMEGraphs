import os

REQUIRED = [
    "AI_FOUNDRY_API_KEY",
    "AI_FOUNDRY_ENDPOINT",
    "GPT_IMAGE_1DOT5_ENDPOINT_URL",
]


def main():
    missing = [k for k in REQUIRED if not os.environ.get(k)]
    for key in REQUIRED:
        val = os.environ.get(key)
        print(f"{key}: {'set' if val else 'missing'}")
    if missing:
        print("❌ Missing required secrets:", ", ".join(missing))
        return 1
    print("✅ All required secrets available")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
