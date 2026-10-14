"""
Entrypoint for Cloud Platforms (Railway, Render, Fly.io, etc.)
Automatically detected by Nixpacks and standard Python buildpacks.
"""
from bot import main

if __name__ == "__main__":
    main()
