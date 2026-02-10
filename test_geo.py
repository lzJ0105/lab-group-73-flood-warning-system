"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    """Test stations_by_distance function"""

    # Create a fake station named 'A' at location (0, 0)
    # Put "None" for the data that I don't care about right now
    station_a = MonitoringStation(
        station_id="s_a",
        measure_id="m_a",
        label="Station A",
        coord=(0.0, 0.0),
        typical_range=None,
        river="River A",
        town="Town A"
    )

    # Create a fake station named 'B' at location (10, 10)
    # Further away from (0, 0) than Station A
    station_b = MonitoringStation(
        station_id="s_b",
        measure_id="m_b",
        label="Station B",
        coord=(10.0, 10.0),
        typical_range=None,
        river="River B",
        town="Town B"
    )

  
    stations = [station_b, station_a]
    p = (0.0, 0.0)
    sorted_stations = stations_by_distance(stations, p)

    assert sorted_stations[0][0] == station_a
    assert sorted_stations[1][0] == station_b





from floodsystem.geo import stations_within_radius

def test_stations_within_radius():
    """Test stations_within_radius function"""

    # Create fake stations
    # Station A is at (0, 0)
    s_a = MonitoringStation(
        station_id="s_a",
        measure_id="m_a",
        label="Station A",
        coord=(0.0, 0.0),
        typical_range=None,
        river="River A",
        town="Town A"
    )

    # Station B is at (1, 1) -> Distance way too far
    s_b = MonitoringStation(
        station_id="s_b",
        measure_id="m_b",
        label="Station B",
        coord=(1.0, 1.0),
        typical_range=None,
        river="River B",
        town="Town B"
    )

    # Station C is at (0, 0.1) -> Distance ok
    s_c = MonitoringStation(
        station_id="s_c",
        measure_id="m_c",
        label="Station C",
        coord=(0.0, 0.1),
        typical_range=None,
        river="River C",
        town="Town C"
    )

    stations = [s_a, s_b, s_c]
    centre = (0.0, 0.0)
    radius = 12.0  # 12 km radius

    # Run the function
    # We expect Station A and Station C to be inside, Station B should be outside.
    inside_stations = stations_within_radius(stations, centre, radius)

    assert len(inside_stations) == 2
    assert s_a in inside_stations
    assert s_c in inside_stations
    assert s_b not in inside_stations





from floodsystem.geo import rivers_with_station

def test_rivers_with_station():
    """Test rivers_with_station function"""

    # Create fake stations with different rivers
    s_a = MonitoringStation(
        station_id="s_a",
        measure_id="m_a",
        label="Station A",
        coord=(0.0, 0.0),
        typical_range=None,
        river="River X",
        town="Town A"
    )

    s_b = MonitoringStation(
        station_id="s_b",
        measure_id="m_b",
        label="Station B",
        coord=(1.0, 1.0),
        typical_range=None,
        river="River Y",
        town="Town B"
    )

    s_c = MonitoringStation(
        station_id="s_c",
        measure_id="m_c",
        label="Station C",
        coord=(0.0, 0.1),
        typical_range=None,
        river="River X",  # Same river as Station A
        town="Town C"
    )

    stations = [s_a, s_b, s_c]

    # Run the function
    rivers = rivers_with_station(stations)

    # Expect 2 rivers: 'River X' and 'River Y'
    # 'River X' should not appear twice.
    assert len(rivers) == 2
    assert "River X" in rivers
    assert "River Y" in rivers


from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def test_stations_by_river():
   stations=build_station_list()
   my_dict=stations_by_river(stations)
   #use river cam
   ans={'Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Weston Bampfylde'}
   assert all(x in ans for x in my_dict['River Cam'])
  




from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():
    stations=build_station_list()
    my_lst=rivers_by_station_number(stations,1)
    assert my_lst==[('Thames',55)]