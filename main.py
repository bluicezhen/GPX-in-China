import argparse
import gpxpy.gpx
import os
from lib import WGS84ToGCJ02


def gpx_wgs84_2_gcj02(from_path: str, to_path: str) -> None:
    with open(from_path, 'rb') as f:
        gpx_old = gpxpy.parse(f)
        gpx_new = gpxpy.gpx.GPX()

        gpx_new_track = gpxpy.gpx.GPXTrack()
        gpx_new.tracks.append(gpx_new_track)
        gpx_new_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_new_track.segments.append(gpx_new_segment)

        for track in gpx_old.tracks:
            for segment in track.segments:
                for point in segment.points:
                    new_lat, new_lon = WGS84ToGCJ02.transform(point.latitude, point.longitude)
                    gpx_new_segment.points.append(gpxpy.gpx.GPXTrackPoint(new_lat,
                                                                        new_lon,
                                                                        elevation=point.elevation,
                                                                        time=point.time))
    with open(to_path, 'wt') as f:
        f.write(gpx_new.to_xml())


def main(args: argparse.Namespace):
    from_path:str = args.from_path
    to_path:str = args.to_path

    file_extension = os.path.splitext(from_path)[1]

    if file_extension == '.gpx':
        gpx_wgs84_2_gcj02(from_path, to_path)
    else:
        print(f'Unsupported file extension: {file_extension}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='GPX-in-China')

    parser.add_argument('-f', '--from-path',
                        type=str,
                        required=True,
                        help='The path of the output GPX/KML (WGS84) file.')
    parser.add_argument('-t', '--to-path',
                        type=str,
                        required=True,
                        help='The path of the output GPX/KML (GCJ02) file.')

    args = parser.parse_args()
    main(args) 