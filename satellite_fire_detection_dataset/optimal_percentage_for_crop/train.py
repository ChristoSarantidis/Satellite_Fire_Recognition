import torch
from ultralytics import YOLO

# Load the pre-trained YOLO model
model = YOLO('yolov9t.pt')

# Check if CUDA is available and specify device manually
if torch.cuda.is_available():
    device_ids = [0, 1, 2]  # Specify the GPUs you want to use
    model = model.to(f'cuda:{device_ids[0]}')  # Move model to the first GPU

    # Train the model with a specified batch size
    model.train(data='fold6.yaml', epochs=100, imgsz=640, device=[0,1,2], batch=30, save_txt=True)
else:
    print("CUDA not available. Using CPU.")
