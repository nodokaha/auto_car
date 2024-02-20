(ffmpeg -video_size 40x40 -framerate 8 -i /dev/video0 -f hls -c:v libx264 -hls_time 1 -hls_list_size 10 -hls_flags delete_segments stream/out.m3u8; python3 -m http.server --cgi) &
