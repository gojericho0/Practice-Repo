import sys
import os


def main():
    print("=== Environment Setup Check ===\n")

    # Python version
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")

    # Virtual environment check
    in_venv = sys.prefix != sys.base_prefix
    print(f"\nVirtual environment active: {in_venv}")
    if in_venv:
        print(f"  Virtual env path: {sys.prefix}")

    # Check for requirements.txt
    req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_path):
        print(f"\nrequirements.txt found at: {req_path}")
        with open(req_path, "r") as f:
            deps = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        print(f"  Listed dependencies: {len(deps)}")
        for dep in deps:
            print(f"    - {dep}")
    else:
        print("\nrequirements.txt not found.")

    # Installed packages
    try:
        import pkg_resources
        installed = sorted(
            [f"{pkg.key}=={pkg.version}" for pkg in pkg_resources.working_set],
            key=str.lower,
        )
        print(f"\nInstalled packages ({len(installed)}):")
        for pkg in installed:
            print(f"  - {pkg}")
    except ImportError:
        print("\nCould not list installed packages (pkg_resources not available).")

    print("\n=== Setup check complete ===")


if __name__ == "__main__":
    main()
