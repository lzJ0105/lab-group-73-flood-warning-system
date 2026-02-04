"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    """Test stations_level_over_threshold function"""

    # Create fake station 'A'
    # Range is 0.0 to 1.0
    # Make Current level 1.5 which is clearly flooding
    station_a = MonitoringStation(
        station_id="s_a",
        measure_id="m_a",
        label="Station A",
        coord=(0.0, 0.0),
        typical_range=(0.0, 1.0),
        river="River A",
        town="Town A"
    )
    station_a.latest_level = 1.5  #set the water level

    # Create a fake station 'B'
    # Range is 0.0 to 1.0
    # Current level 0.5 which is normal, half full
    station_b = MonitoringStation(
        station_id="s_b",
        measure_id="m_b",
        label="Station B",
        coord=(1.0, 1.0),
        typical_range=(0.0, 1.0),
        river="River B",
        town="Town B"
    )
    station_b.latest_level = 0.5

    stations = [station_a, station_b]
    
    # Ask for stations where the level is over 0.8 (80% full)
    # Station A (1.5) should be in the list
    # Station B (0.5) should NOT be in the list
    result = stations_level_over_threshold(stations, 0.8)

    assert len(result) == 1
    assert result[0][0] == station_a



from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():
    """Test stations_highest_rel_level function"""

    # Create 3 stations with different levels
    s_a = MonitoringStation("s_a", "m_a", "Station A", (0, 0), (0, 1), "River A", "Town A")
    s_a.latest_level = 10.0 

    s_b = MonitoringStation("s_b", "m_b", "Station B", (0, 0), (0, 1), "River B", "Town B")
    s_b.latest_level = 0.5  

    s_c = MonitoringStation("s_c", "m_c", "Station C", (0, 0), (0, 1), "River C", "Town C")
    s_c.latest_level = 5.0 

    stations = [s_a, s_b, s_c]

    # Ask for the top 2
    result = stations_highest_rel_level(stations, 2)

    assert len(result) == 2
    
    # Check first item (Station A, 10.0)
    assert result[0][0] == s_a
    assert result[0][1] == 10.0
    
    # Check second item (Station C, 5.0)
    assert result[1][0] == s_c
    assert result[1][1] == 5.0
