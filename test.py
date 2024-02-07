from flask import Flask, request, jsonify
import mimetypes

app = Flask(__name__)

def is_video(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    if mime_type is not None:
        return mime_type.startswith('video/')
    return False

@app.route('/check_video', methods=['POST'])
def check_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and is_video(file.filename):
        return jsonify({'result': True, 'message': 'The file is a video'})
    else:
        return jsonify({'result': False, 'message': 'The file is not a video'})

if __name__ == '__main__':
    app.run(debug=True)
