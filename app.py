import gradio as gr
from src_model.model import MattingNetwork
from inference import convert_video
import torch
import os
import shutil

# Load the model
model = MattingNetwork(variant="mobilenetv3").cuda()
model.load_state_dict(torch.load("models/rvm_mobilenetv3.pth"))


def video_matting(video):
    basename = os.path.splitext(os.path.basename(video))[0]
    output_dir = os.path.join("output", basename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_composition = os.path.join(output_dir, "com.mp4")
    output_alpha = os.path.join(output_dir, "pha.mp4")
    output_foreground = os.path.join(output_dir, "fgr.mp4")

    convert_video(
        model=model,
        input_source=video,
        output_type="video",
        output_composition=output_composition,
        output_alpha=output_alpha,
        output_foreground=output_foreground,
        output_video_mbps=4,
        downsample_ratio=None,
        seq_chunk=12,
    )
    return output_composition, output_alpha, output_foreground


iface = gr.Interface(
    fn=video_matting,
    inputs=gr.Video(),
    outputs=[
        gr.Video(label="Composition"),
        gr.Video(label="Alpha"),
        gr.Video(label="Foreground"),
    ],
    title="Robust Video Matting",
    description="Upload a video to apply video matting.",
)

if __name__ == "__main__":
    iface.launch()
