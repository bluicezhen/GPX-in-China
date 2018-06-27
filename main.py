import click
import gpxpy.gpx
from lib import WGS84ToGCJ02

@click.command()
@click.option("--f", help="from GPX(WGS84) file")
@click.option("--t", help="from GPX(GCJ02) file")
def main(f: str, t: str):
    gpx_file = open(f, 'r')
    gpx_old = gpxpy.parse(gpx_file)
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
    gpx_new_file = open(t, 'w')
    gpx_new_file.write(gpx_new.to_xml())


if __name__ == "__main__":
    main()
