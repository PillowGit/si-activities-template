import yaml
import sys
import os

from pathlib import Path

working_dir: Path = Path(__file__).parent
activities_yaml: Path = working_dir / "activities.yaml"


def run(activity_name: str) -> None:
    # Load activities yaml file
    activities: dict = {}
    if not activities_yaml.exists() or not activities_yaml.is_file():
        raise RuntimeError(f"Activities file not found in: {str(activities_yaml)}")
    with activities_yaml.open("r") as f:
        try:
            activities = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise RuntimeError(f"Error loading activities file from: {str(activities_yaml)}")
    # Call the given activity
    activity_entry = activities.get(activity_name)
    if activity_entry is None:
        raise RuntimeError(f"Activity not found: {activity_name}")
    if "cmd" not in activity_entry:
        raise RuntimeError(f"Command not found for the following activity: {activity_name}")
    move_cmd: str = f"cd {working_dir / activity_name}"
    run_cmd = activity_entry["cmd"]
    os.system("clear")
    print(run_cmd + "\n")
    os.system(f"{move_cmd} && {run_cmd}")

if __name__ == "__main__":
    if not activities_yaml.exists() or not activities_yaml.is_file():
        raise RuntimeError(f"Activities file not found in: {str(activities_yaml)}")
    if len(sys.argv) != 2:
        print("Usage: ./runner <activity_name>")
        sys.exit(1)
    activity_name = sys.argv[1]
    run(activity_name)
