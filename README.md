# ⚽ YOLOv8 Football Player Tracker

This project uses a custom-trained YOLOv8 model to perform object tracking on football video clips. It identifies and tracks players and the ball, applying bounding boxes and tracking IDs to the video output.

---

## ✨ Key Features

* **Custom Object Tracking:** Utilizes a YOLOv8 model custom-trained (via Roboflow) to recognize and track football players and the ball.
* **Video Processing:** Reads video files from an input directory and outputs a new video file with tracking annotations.
* **Advanced Annotation:** Uses the `supervision` library to apply clean, professional-looking bounding boxes and tracking IDs.
* **OOP Structure:** Built with an Object-Oriented approach for clean and maintainable code.

---

## 🛠️ Technologies Used

* **Python**
* **Ultralytics (YOLOv8):** For the core object detection and tracking model.
* **Supervision:** For high-level video processing and annotation.
* **Numpy:** For numerical operations.
* **Roboflow:** Used for dataset management and model training.
* **Pickle, OS, Sys:** Standard Python libraries for file and system operations.

---

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

You must have **Python 3.8** or newer installed on your system.

### Installation

1.  Clone the repo:
    ```bash
    git clone [https://github.com/TheAkrem/hassoub_repo.git](https://github.com/TheAkrem/hassoub_repo.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd hassoub_repo
    ```
3.  Install the required Python libraries:
    ```bash
    pip install ultralytics supervision numpy roboflow
    ```

---

## 🏃‍♂️ How to Run

1.  Place the football video clip you want to process inside the `Input_Videos` folder.
2.  Run the `main.py` script from your terminal:
    ```bash
    python main.py
    ```
3.  The processed video will be saved in the designated output folder (you can specify this in the code).

---

## 📜 License

Distributed under the MIT License. See `LICENSE.txt` for more information. (You may need to add a `LICENSE.txt` file to your repo for this to be accurate).
