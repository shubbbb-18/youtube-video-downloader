from flask import Flask, request, send_file
import youtube_dl
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form['videoUrl']
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            video_title = info_dict.get('title', 'video')  # Default title if not found
            video_file = f'downloads/{video_title}.mp4'

        return send_file(video_file, as_attachment=True)
    except youtube_dl.utils.DownloadError as e:
        return f"Error downloading video: {str(e)}", 500
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
