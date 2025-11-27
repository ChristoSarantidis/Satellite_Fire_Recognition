import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
from glob import glob
from tqdm import tqdm

# === Parameters ===
model_path = "/home/sarantidis/fire_vol2/for_crop/best.pt"
val_images_dir = "/home/sarantidis/fire_vol2/for_crop/fold6/test/images"
crop_scales = [ 0.05, 0.1 ,0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
image_size = 640  # All images are assumed to be 640x640

# === Load model ===
model = YOLO(model_path)

# === Collect all image paths ===
image_paths = glob(os.path.join(val_images_dir, "*.jpg"))  # or .png depending on your format

average_confidences = []

for scale in crop_scales:
    confidences = []

    for img_path in tqdm(image_paths, desc=f"Processing scale {scale}"):
        img = cv2.imread(img_path)
        h, w = img.shape[:2]
        crop_size = int(scale * min(h, w))

        x1 = (w - crop_size) // 2
        y1 = (h - crop_size) // 2
        x2 = x1 + crop_size
        y2 = y1 + crop_size

        crop = img[y1:y2, x1:x2]
        resized_crop = cv2.resize(crop, (image_size, image_size))

        # Run inference
        results = model(resized_crop, verbose=False)
        detections = results[0].boxes

        # Collect confidence scores
        for det in detections:
            conf = float(det.conf)
            confidences.append(conf)

    avg_conf = np.mean(confidences) if confidences else 0.0
    average_confidences.append(avg_conf)

# === Plot results ===
plt.figure(figsize=(10, 6))
plt.plot([int(s * 100) for s in crop_scales], average_confidences, marker='o')
plt.xlabel("Crop size (% of original)")
plt.ylabel("Average confidence")
plt.title("Average Confidence vs Crop Percentage (YOLO Inference)")
plt.grid(True)
plt.tight_layout()
plt.savefig("confidence_vs_crop.png")
plt.show()

# === Report best crop percentage ===
max_index = np.argmax(average_confidences)
best_crop_percentage = crop_scales[max_index] * 100
print(f"\n✅ Best crop percentage: {best_crop_percentage:.1f}% with average confidence: {average_confidences[max_index]:.4f}")
