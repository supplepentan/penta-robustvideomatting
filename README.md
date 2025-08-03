# Usage (Windows)

1.  **Clone the repository**
    ```
    git clone https://github.com/supplepentan/penta-robustvideomatting
    cd penta-robustvideomatting
    ```

2.  **Create a virtual environment**
    ```
    python -m venv venv
    venv\scripts\activate
    ```

3.  **Install dependencies**
    -   First, upgrade `pip` and install `wheel`:
        ```
        python -m pip install --upgrade pip wheel
        ```
    -   Install the packages from `requirements.txt`:
        ```
        python -m pip install -r requirements.txt
        ```
    -   Install `torch` and `torchvision`:
        ```
        python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
        ```
    -   Upgrade `typing_extensions` to resolve compatibility issues:
        ```
        venv\Scripts\pip.exe install --upgrade typing_extensions
        ```

4.  **Download and place the pre-trained model**
    -   Run `run.py` once to download the model. You can stop it once the download starts.
        ```
        venv\Scripts\python.exe run.py
        ```
    -   The model `rvm_mobilenetv3.pth` will be downloaded to `C:\Users\YOUR_USERNAME\.cache\torch\hub\checkpoints`.
    -   Move `rvm_mobilenetv3.pth` from `C:\Users\YOUR_USERNAME\.cache\torch\hub\checkpoints` to the `models` folder in this project (`D:\projects-d\penta-robustvideomatting\models`).
        ```
        move C:\Users\YOUR_USERNAME\.cache\torch\hub\checkpoints\rvm_mobilenetv3.pth models\rvm_mobilenetv3.pth
        ```
    -   Create `src_model` directory and copy necessary files:
        ```
        mkdir src_model
        copy C:\Users\YOUR_USERNAME\.cache\torch\hub\PeterL1n_RobustVideoMatting_master\model\* src_model\
        ```

5.  **Place your video in the `input` folder**
    -   For example, `input/example.mp4`.

6.  **Run the application**
    
    There are two ways to run the application:
    
    **A) Command-line interface**
    ```
    venv\Scripts\python.exe run.py
    ```
    -   Processed videos will be saved in the `output` folder.

    **B) Web UI (Gradio)**
    ```
    venv\Scripts\python.exe app.py
    ```
    -   This will launch a web interface. Open the URL displayed in the console in your browser.
    -   Upload a video and the processed videos will be available for download.

# Original

[Robust High-Resolution Video Matting with Temporal Guidance](https://peterl1n.github.io/RobustVideoMatting/)