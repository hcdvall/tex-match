import argparse

from image_inspector import ImageInspector
from observation_saver import ObservationSaver


def compare_images():
    parser = argparse.ArgumentParser(
        description="Compare two images and return a similarity percentage."
    )
    parser.add_argument("image1", help="Path to the first image.")
    parser.add_argument("image2", help="Path to the second image.")

    args = parser.parse_args()

    inspector = ImageInspector(args.image1, args.image2)

    ssim_value, image_1, image_2, delta_image = inspector.image_similarity()

    saver = ObservationSaver(image_1, image_2, delta_image, ssim_value)
    saver.save(args.image1, args.image2)

    print(f"Similarity using SSIM: {ssim_value:.4f}")


if __name__ == "__main__":
    compare_images()
