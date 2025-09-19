from utils import read_video, save_video
from trackers import Tracker
def main():
    # Read Video
    video_frames = read_video('/Users/akremhd/Desktop/My_projects/Football_Project/Input_Videos/Video from Google Drive.mp4')

    tracker=Tracker('/Users/akremhd/Desktop/My_projects/Football_Project/Football_training_yolo/models/Football Training YOLO v5.pt')
    
    
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    save_video(output_video_frames, 'output_videos/output_video.mp4')

if __name__ == '__main__':
    main()