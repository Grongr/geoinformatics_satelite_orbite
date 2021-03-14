#! Geoinformatics is my life. All my time is geoinformatics

# All we need is blood. Or some python libraries
import math

# I love stackoverflow :)
def get_coord_in_ecef(xyz):
    from astropy import coordinates as coord
    from astropy import units as u
    from astropy.time import Time
    now = Time('2021-03-15 00:36:00')
    # position of satellite in GCRS or J20000 ECI:
    cartrep = coord.CartesianRepresentation(*xyz, unit=u.m)
    gcrs = coord.GCRS(cartrep, obstime=now)
    itrs = gcrs.transform_to(coord.ITRS(obstime=now))
    loc = coord.EarthLocation(*itrs.cartesian.xyz)
    return [loc.lat, loc.lon, loc.height]

def get_coords_in_eci():
    dolg_vosh_uzl = 247.4627
    arg_per       = 130.5360
    tr_anom       = 325.0288
    nakl_orb      = 51.6416
    sredn_dvij    = 15.72125391
    grav_potent   = 398603 * 10e9
    eccentricity  = 0.0006703

    # Auxillary angle
    u = arg_per + tr_anom

    # firstly big poluos
    a = grav_potent / sredn_dvij**2
    a = a ** (1/3)

    # It means Фокальный параметр on major language
    foc_param = a * (1 - eccentricity**2)

    radius_vec = foc_param / ( 1 + eccentricity * math.cos(tr_anom * math.pi / 180) )

    # Rewrite in radian
    U = u * math.pi / 180
    Dolg_vosh_uzl = dolg_vosh_uzl * math.pi / 180
    i = nakl_orb * math.pi / 180

    # Now coords!!!
    x  = radius_vec
    x *= math.cos(U) * math.cos(Dolg_vosh_uzl) - math.sin(Dolg_vosh_uzl) * math.cos(i)
    
    y  = radius_vec
    y *= math.sin(Dolg_vosh_uzl) * math.cos(U) + math.cos(Dolg_vosh_uzl) * math.cos(i)

    z  = radius_vec
    z *= math.sin(U) * math.sin(i)
    
    return [x, y, z]

l = get_coords_in_eci()

l = get_coord_in_ecef(l)

print(l)


