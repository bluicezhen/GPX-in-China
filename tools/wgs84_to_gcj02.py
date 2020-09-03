from __future__ import division
from math import pi, sqrt, sin, cos

a = 6378245.0
ee = 0.00669342162296594323


def _transform_lat(x, y):
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * sqrt(abs(x))
    ret += (20.0 * sin(6.0 * x * pi) + 20.0 * sin(2.0 * x * pi)) * 2.0 / 3.0
    ret += (20.0 * sin(y * pi) + 40.0 * sin(y / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * sin(y / 12.0 * pi) + 320 * sin(y * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transform_lon(x, y):
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * sqrt(abs(x))
    ret += (20.0 * sin(6.0 * x * pi) + 20.0 * sin(2.0 * x * pi)) * 2.0 / 3.0
    ret += (20.0 * sin(x * pi) + 40.0 * sin(x / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * sin(x / 12.0 * pi) + 300.0 * sin(x / 30.0 * pi)) * 2.0 / 3.0
    return ret


# World Geodetic System ==> Mars Geodetic System
def wgs84_to_gcj02(wg_lat, wg_lon):
    """
    transform(latitude,longitude) , WGS84
    return (latitude,longitude) , GCJ02
    """

    d_lat = _transform_lat(wg_lon - 105.0, wg_lat - 35.0)
    d_lon = _transform_lon(wg_lon - 105.0, wg_lat - 35.0)
    rad_lat = wg_lat / 180.0 * pi
    magic = sin(rad_lat)
    magic = 1 - ee * magic * magic
    sqrt_magic = sqrt(magic)
    d_lat = (d_lat * 180.0) / ((a * (1 - ee)) / (magic * sqrt_magic) * pi)
    d_lon = (d_lon * 180.0) / (a / sqrt_magic * cos(rad_lat) * pi)
    mg_lat = wg_lat + d_lat
    mg_lon = wg_lon + d_lon
    return mg_lat, mg_lon


if __name__ == "__main__":
    WGS84_Lat = 39.990205
    WGS84_Long = 116.327847
    print(wgs84_to_gcj02(WGS84_Lat, WGS84_Long))
