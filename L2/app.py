import os
import subprocess
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# This route serves the converted video files
@app.route('/converted_files/<filename>')
def download_file(filename):
    # Define the path to the 'converted_files' directory
    converted_dir = os.path.join(app.root_path, 'converted_files')
    return send_from_directory(converted_dir, filename)

@app.route('/convert_to_format', methods=['POST'])
def convert_to_format():
    video = request.files['input_file']
    format = request.form['format']
    filename = video.filename
    input_path = os.path.join('uploads', filename)
    os.makedirs('uploads', exist_ok=True)
    video.save(input_path)

    # Define output directory for converted files
    output_dir = 'converted_files'
    os.makedirs(output_dir, exist_ok=True)

    # Define correct file extensions based on the format
    output_filename = f"converted_video.{format}"
    if format == 'vp8' or format == 'vp9':
        output_filename = f"converted_video.webm"
    elif format == 'h265':
        output_filename = f"converted_video.mp4"

    output_file = os.path.join(output_dir, output_filename)

    codec_map = {
        'vp8': 'libvpx',
        'vp9': 'libvpx-vp9',
        'h265': 'libx265',
    }

    audio_codec_map = {
        'vp8': 'libvorbis',
        'vp9': 'libvorbis',
        'h265': 'aac',
    }

    codec = codec_map.get(format)
    audio_codec = audio_codec_map.get(format)
    if not codec:
        return jsonify({'error': 'Unsupported format'}), 400

    # ffmpeg command to convert the video
    command = [
        'ffmpeg', '-y',  # -y ensures overwriting of the output file without asking
        '-i', input_path, '-c:v', codec,
        '-b:v', '1M', '-c:a', audio_codec, output_file
    ]

    try:
        subprocess.run(command, check=True)
        return jsonify({'message': 'Conversion successful!', 'output_file': output_filename})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f"FFmpeg failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)