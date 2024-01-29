import os
import subprocess
import sys
from typing import List, Dict, Union

# Define the type for environment dictionaries
EnvironmentDict = Dict[str, str]

# List of environments to process
environments: List[EnvironmentDict] = [
    {"NAME": "latest", "PYTHON_VERSION": "3.11"},
    {"NAME": "python3.11", "PYTHON_VERSION": "3.11"},
    {"NAME": "python3.10", "PYTHON_VERSION": "3.10"},
    {"NAME": "python3.9", "PYTHON_VERSION": "3.9"},
    {"NAME": "python3.8", "PYTHON_VERSION": "3.8"},
    {"NAME": "python3.7", "PYTHON_VERSION": "3.7"},
    {"NAME": "python3.11-slim", "PYTHON_VERSION": "3.11"},
    {"NAME": "python3.10-slim", "PYTHON_VERSION": "3.10"},
    {"NAME": "python3.9-slim", "PYTHON_VERSION": "3.9"},
    {"NAME": "python3.8-slim", "PYTHON_VERSION": "3.8"},
    {"NAME": "python3.9-alpine3.14", "PYTHON_VERSION": "3.9"},
    {"NAME": "python3.8-alpine3.10", "PYTHON_VERSION": "3.8"},
    {"NAME": "python3.7-alpine3.8", "PYTHON_VERSION": "3.7"},
]

# Environment variables
start_with: Union[None, str] = os.environ.get("START_WITH")
build_push: Union[None, str] = os.environ.get("BUILD_PUSH")


def process_tag(*, env: EnvironmentDict) -> None:
    """Process a tag by executing a script."""
    use_env = {**os.environ, **env}
    script = "scripts/test.sh"
    if build_push:
        script = "scripts/build-push.sh"
    return_code = subprocess.call(["bash", script], env=use_env)
    if return_code != 0:
        sys.exit(return_code)


def print_version_envs() -> None:
    """Print version environments."""
    env_lines = []
    for env in environments:
        env_vars = [f"{key}='{value}'" for key, value in env.items()]
        env_lines.append(" ".join(env_vars))
    for line in env_lines:
        print(line)


def main() -> None:
    """Main entry point."""
    start_at = 0
    if start_with:
        start_at = next(
            (i for i, env in enumerate(environments) if env["NAME"] == start_with), 0
        )
    for i, env in enumerate(environments[start_at:]):
        print(f"Processing tag: {env['NAME']}")
        process_tag(env=env)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--print-envs":
        print_version_envs()
    else:
        main()
