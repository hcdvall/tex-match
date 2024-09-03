import cv2
import imageio.v3 as imageio
import numpy as np
from skimage.metrics import structural_similarity


class ImageInspector:
    def __init__(self, image1_path: str, image2_path: str):
        """
        Initializes the ImageInspector class by reading the images from the provided paths.

        Args:
            image1_path (str): Path to the first image.
            image2_path (str): Path to the second image.
        """
        self.image1 = imageio.imread(image1_path)
        self.image2 = imageio.imread(image2_path)

        if self.image1 is None or self.image2 is None:
            raise ValueError("One or both images could not be loaded. Check the paths.")


    def _format_images(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Convert images to RGB and resizes them to the same size.

        Returns:
            tuple[np.ndarray, np.ndarray]: The formatted grayscale images.
        """
        # Convert images to RGB
        image1_rgb = cv2.cvtColor(self.image1, cv2.COLOR_BGR2RGB)
        image2_rgb = cv2.cvtColor(self.image2, cv2.COLOR_BGR2RGB)

        # Resize the images to the same size
        height = min(image1_rgb.shape[0], image2_rgb.shape[0])
        width = min(image1_rgb.shape[1], image2_rgb.shape[1])
        image1_rgb = cv2.resize(image1_rgb, (width, height))
        image2_rgb = cv2.resize(image2_rgb, (width, height))

        return image1_rgb, image2_rgb


    def image_similarity(
        self,
    ) -> tuple[float, np.ndarray, np.ndarray, np.ndarray]:
        """
        Computes the similarity between the two images using SSIM.

        Returns:
            tuple[, float, np.ndarray, np.ndarray, np.ndarray]:
            - Structural Similarity Index (SSIM)
            - Original image 1
            - Original image 2
            - Delta image
        """
        image1_rgb, image2_rgb = self._format_images()

        # Compute the Structural Similarity Index (SSI) and Delta
        ssim_value, _ = structural_similarity(
            image1_rgb, image2_rgb, channel_axis=2, full=True
        )
        # Calculate the difference (delta) between images
        delta_image = cv2.absdiff(image1_rgb, image2_rgb)

        return ssim_value, self.image1, self.image2, delta_image
