from pathlib import Path

def finalize_dist(dist, path='pyproject.toml'):
    path = Path(path)
    if not (path.exists() and path.is_file()):
        return

    print(f" ============================= finalize_dist")
