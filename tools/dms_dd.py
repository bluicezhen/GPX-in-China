def dd2dms(latitude: float, longitude: float):
    """
    convert DD to DMS
    https://en.wikipedia.org/wiki/Decimal_degrees
    """
    north_or_south = 'N' if longitude >= 0 else 'S'
    east_or_west = 'E' if latitude >= 0 else 'W'

    longitude = abs(longitude)
    latitude = abs(latitude)

    longitude_degrees = int(longitude)
    longitude_minutes = int((longitude - longitude_degrees) * 60)
    longitude_seconds = (longitude - longitude_degrees - longitude_minutes / 60) * 3600

    latitude_degrees = int(latitude)
    latitude_minutes = int((latitude - latitude_degrees) * 60)
    latitude_seconds = (latitude - latitude_degrees - latitude_minutes / 60) * 3600

    return north_or_south, longitude_degrees, longitude_minutes, longitude_seconds, east_or_west, latitude_degrees, \
        latitude_minutes, latitude_seconds


if __name__ == "__main__":
    print(dd2dms(38.8897, -77.0089))
