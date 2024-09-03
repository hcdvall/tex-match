import json
import os
from datetime import datetime

import imageio.v3 as imageio
import numpy as np

OBSERVATIONS_FOLDER = "observations"
COMPARISON_NAME = "comparison_"


class ObservationSaver:
    def __init__(
        self,
        image1: np.ndarray,
        image2: np.ndarray,
        delta_image: np.ndarray,
        similarity: float,
    ):
        """
        Initializes ObservationSaver with the necessary data and output directory settings.

        Args:
            image1 (np.ndarray): First input image.
            image2 (np.ndarray): Second input image.
            delta_image (np.ndarray): The delta image showing differences between image1 and image2.
            similarity (float): The computed similarity metric between image1 and image2.
            output_folder (str): The base directory where comparisons are saved.
            comparison_name (str): The prefix name for each comparison folder.
        """
        self.image1 = image1
        self.image2 = image2
        self.delta_image = delta_image
        self.similarity = similarity
        self.output_folder = OBSERVATIONS_FOLDER
        self.comparison_name = COMPARISON_NAME


    def _create_directories(self) -> str:
        """
        Creates and returns the directory structure for saving comparison results.

        Returns:
            str: The path to the comparison folder.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        comparison_folder = os.path.join(
            self.output_folder, f"{self.comparison_name}{timestamp}"
        )
        os.makedirs(comparison_folder, exist_ok=True)

        return comparison_folder


    def save(self, image1_path: str, image2_path: str) -> None:
        """
        Saves the comparison results including the original images, delta image, and similarity score.
        """
        comparison_folder = self._create_directories()

        # Extract the filenames and ensure the paths are created in the output folder
        image1_filename = os.path.basename(image1_path)
        image2_filename = os.path.basename(image2_path)

        # Set save paths
        image1_save_path = os.path.join(comparison_folder, image1_filename)
        image2_save_path = os.path.join(comparison_folder, image2_filename)
        delta_save_path = os.path.join(comparison_folder, "delta.dds")
        similarity_path = os.path.join(comparison_folder, "similarity.json")

        # Save images
        imageio.imwrite(image1_save_path, self.image1)
        imageio.imwrite(image2_save_path, self.image2)
        imageio.imwrite(delta_save_path, self.delta_image, extension=".dds")

        # Save similarity metric and paths
        similarity_data = {
            "metric": {"similarity": round(self.similarity, 4)},
            "images": {
                "image1": image1_save_path,
                "image2": image2_save_path,
                "delta": delta_save_path,
            },
        }
        with open(similarity_path, "w") as f:
            json.dump(similarity_data, f, indent=4)
