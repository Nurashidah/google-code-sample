"""A video player class."""
import video
from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self.pause_vid = None
        self._video_playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here are all the videos available: ")
        for video in self._video_library.get_all_videos():
            print(video.title,video.video_id,  video.tags)

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)

        if not video:
            print("Cannot play video: Video does not exist")
            return

        if self._current_video != None:
            print(f"Stopping video: {self._current_video}")
            print(f"Playing video: {video.title}")
            self._current_video = video.title
            return

        print(f"Playing video: {video.title}")
        self._current_video = video.title

    def stop_video(self):
        """Stops the current video."""

        print("Stopped: ", self._current_video)
        self._current_video = None

        print("Cannot stop: no video are playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        rand_video = random.choice(self._video_library.get_all_videos())

        print("Playing video: ", rand_video.title)
        self._current_video = rand_video.title

    def pause_video(self):
        """Pauses the current video."""

        if video:
            if self.pause_vid is False:
                print(f'Pausing video: {self._current_video}')
                self._current_video = video
                self.pause_vid = True
            elif self.pause_vid is True:
                print(f'Video already paused: {self._current_video}')

        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video == False:
            print("No video is currently playing")
        else:
            print(f'Currently playing: {video.title}, ({self._current_video.video_id}), [{self._current_video.tags}]')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        print("Here are all the playlist available: ")
        for playlist in self._video_playlist.get_all_playlist():
            print(playlist)


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        video_term = self._video_library.get_video(search_term)
        if video_term:
            print(f"Here are the results for {search_term}")


    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """
        video_tag_search = self._video_library.get_video(video_tag)
        if video_tag_search:
            print(f"Here are the results for {video_tag}")


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")