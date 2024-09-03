import argparse
import json
import pathlib
import shutil


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
        - input_dir (str): Directory containing the comparison data.
        - output_dir (str): Directory to save filtered data.
        - threshold (float): Minimum similarity score required to not get filtered.
    """
    parser = argparse.ArgumentParser(
        description="Aggregate and filter results from the image comparison."
    )
    parser.add_argument(
        "input_dir", type=str, help="Directory containing the comparison data."
    )
    parser.add_argument(
        "output_dir", type=str, help="Directory to save the filtered observations."
    )
    parser.add_argument(
        "threshold",
        type=float,
        help="Minimum similarity score to include in the results.",
    )
    return parser.parse_args()


def process_data(input_dir: str, output_dir: str, threshold: float) -> None:
    """
    Process and filter image comparison data based on a similarity threshold.
    Copy the whole directory of a comparison if the threshold is met.

    Args:
        input_dir (str): Directory containing the comparison data.
        output_dir (str): Directory to save filtered data.
        threshold (float): Minimum similarity score required to not get filtered.

    Returns:
        None
    """
    input_path = pathlib.Path(input_dir)
    output_path = pathlib.Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for comparison_folder in input_path.iterdir():
        if not comparison_folder.is_dir():
            continue

        similarity_file = comparison_folder / "similarity.json"
        if not similarity_file.exists():
            continue

        with open(similarity_file, "r") as f:
            similarity_data = json.load(f)
            similarity = similarity_data.get("metric", {}).get("similarity", 0)

        if similarity >= threshold:
            destination_folder = output_path / comparison_folder.name
            shutil.copytree(comparison_folder, destination_folder, dirs_exist_ok=True)

    print(f"Filtered data has been saved to {output_dir}")


def aggregate_data() -> None:
    args = parse_arguments()
    process_data(args.input_dir, args.output_dir, args.threshold)


if __name__ == "__main__":
    aggregate_data()
