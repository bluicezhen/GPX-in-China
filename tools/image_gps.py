from PIL import Image
import piexif


def modify_image_gps(file_path: str,
                     gps_latitude_ref: str,
                     gps_latitude_degrees: int,
                     gps_latitude_minutes: int,
                     gps_latitude_seconds_100: int,
                     gps_longitude_ref: str,
                     longitude_degrees: int,
                     longitude_minutes: int,
                     longitude_seconds_100: int):
    """Modify image's GPS info. if image's doesn't has GPS info, this function will insert it."""

    exif_dict = piexif.load(file_path)

    exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = gps_latitude_ref
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = ((gps_latitude_degrees, 1),
                                                   (gps_latitude_minutes, 1),
                                                   (gps_latitude_seconds_100, 100))
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = gps_longitude_ref
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = ((longitude_degrees, 1),
                                                    (longitude_minutes, 1),
                                                    (longitude_seconds_100, 100))

    exif_bytes = piexif.dump(exif_dict)
    im = Image.open(file_path)
    im.save("out.jpg", exif=exif_bytes)
