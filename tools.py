from PIL import Image
import piexif


def modify_image_gps(file_path: str,
                     gps_latitude_ref: str,
                     gps_latitude_degrees: float,
                     gps_latitude_minutes: float,
                     gps_latitude_seconds_100: float,
                     gps_longitude_ref: str,
                     longitude_degrees: float,
                     longitude_minutes: float,
                     longitude_seconds_100: float):
    """Modify image's GPS info. if image's doesn't has GPS info, this function will insert it."""

    exif_dict = piexif.load(file_path)

    exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = gps_latitude_ref
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = ((gps_latitude_degrees, 1),
                                                   (gps_latitude_minutes, 1),
                                                   (gps_latitude_seconds_100, 100))
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = gps_longitude_ref
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = ((longitude_degrees, 1),
                                                    (longitude_minutes, 1),
                                                    (longitude_seconds_100, 1))

    exif_bytes = piexif.dump(exif_dict)
    im = Image.open("file_path")
    im.save("out.jpg", exif=exif_bytes)
