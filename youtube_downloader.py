import yt_dlp

# ダウンロードしたいYouTubeのURLを指定してください
video_url = 'https://youtu.be/nkcDXq1Uwv0?si=S_kiV3-DBTnk12a3'

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', # 最高画質の映像と音声をダウンロードして結合する設定
        'outtmpl': '%(title)s.%(ext)s', # 保存するファイル名の形式（動画のタイトル.拡張子）
        'merge_output_format': 'mp4', # mp4に変換・結合する
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"ダウンロードを開始します: {url}")
            ydl.download([url])
            print("ダウンロードが完了しました！")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# 実行
download_youtube_video(video_url)