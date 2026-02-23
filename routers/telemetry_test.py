from fastapi.testclient import TestClient
from main import app
from store import telemetrystore
import copy

from utils import dateutils

client = TestClient(app)

# Copy rows each time to preserve data in store
rows = lambda: copy.deepcopy(telemetrystore.rows)

json_rows = lambda xs: [x.model_dump() for x in xs]

default_sorted_rows = sorted(rows(), key=lambda x: x.timestamp, reverse=True)

def paging_test(page: int, pageSize: int):
    response = client.get("/telemetry?page=" + str(page) + "&pageSize=" + str(pageSize))
    assert response.status_code == 200
    assert response.json() == {
        "items": json_rows(default_sorted_rows[page * pageSize : (page + 1) * pageSize]),
        "length": len(rows())
    }

def sorting_test(sortBy: str, sortDirection: str):
    response = client.get("/telemetry?sortBy=" + sortBy + "&sortDirection=" + sortDirection)

    if (sortBy == 'altitude'):
        sorted_rows = sorted(rows(), key=lambda x: x.altitude, reverse=sortDirection == 'descending')
    elif (sortBy == 'velocity'):
        sorted_rows = sorted(rows(), key=lambda x: x.velocity, reverse=sortDirection == 'descending')
    else:
        sorted_rows = sorted(rows(), key=lambda x: x.timestamp, reverse=sortDirection == 'descending')

    assert response.status_code == 200
    assert response.json() == {
        "items": json_rows(sorted_rows),
        "length": len(rows())
    }

def filtering_test(satelliteId: str = None, status: str = None):
    params = []
    if satelliteId != None:
        params.append('satelliteId=' + satelliteId)
    if status != None:
        params.append('status=' + status)
    response = client.get("/telemetry?" + str.join('&', params))
    
    filtered_rows = [x for x in rows()]
    if satelliteId != None:
        filtered_rows = [x for x in filtered_rows if x.satelliteId == satelliteId]
    if status != None:
        filtered_rows = [x for x in filtered_rows if x.status == status]

    assert response.status_code == 200
    assert response.json() == {
        "items": json_rows(filtered_rows),
        "length": len(filtered_rows)
    }

def test_list_telemetry():
    response = client.get("/telemetry")
    assert response.status_code == 200
    assert response.json() == {
        "items": json_rows(default_sorted_rows),
        "length": len(rows())
    }

def test_list_telemetry_paged_0_10():
    paging_test(0, 10)
def test_list_telemetry_paged_1_10():
    paging_test(1, 10)
def test_list_telemetry_paged_0_50():
    paging_test(0, 50)
def test_list_telemetry_paged_0_100():
    paging_test(0, 100)
def test_list_telemetry_paged_1_100():
    paging_test(1, 100)
def test_list_telemetry_paged_0_3():
    paging_test(0, 3)

def test_list_telemetry_sorted_direction_only():
    response = client.get("/telemetry")
    assert response.status_code == 200
    # Expect sortDirection to be ignored if there's no sortBy
    assert response.json() == {
        "items": json_rows(default_sorted_rows),
        "length": len(rows())
    }

def test_list_telemetry_sorted_timestamp_asc():
    sorting_test('timestamp', 'ascending')
def test_list_telemetry_sorted_timestamp_desc():
    sorting_test('timestamp', 'descending')
def test_list_telemetry_sorted_altitude_asc():
    sorting_test('altitude', 'ascending')
def test_list_telemetry_sorted_altitude_desc():
    sorting_test('altitude', 'descending')
def test_list_telemetry_sorted_velocity_asc():
    sorting_test('velocity', 'ascending')
def test_list_telemetry_sorted_velocity_desc():
    sorting_test('velocity', 'descending')

def test_list_telemetry_filtered_satelliteId():
    filtering_test('SAT001', None)
def test_list_telemetry_filtered_status():
    filtering_test(None, 'interrupt')
def test_list_telemetry_filtered_satelliteId_status():
    filtering_test('SAT001', 'interrupt')

def test_list_telemetry_paged_sorted_filtered_1():
    response = client.get("/telemetry?page=0&pageSize=20&sortBy=timestamp&sortDirection=ascending&satelliteId=SAT001&status=healthy")
    
    filtered_rows = [x for x in rows() if x.satelliteId == 'SAT001' and x.status == 'healthy']
    expected_rows = [x for x in sorted(filtered_rows, key=lambda y: y.timestamp, reverse=False)][0 : 20]

    assert response.status_code == 200
    assert response.json() == {
        "items": json_rows(expected_rows),
        "length": len(filtered_rows)
    }

def test_list_telemetry_paged_sorted_filtered_2():
    response = client.get("/telemetry?page=1&pageSize=10&sortBy=velocity&sortDirection=descending&satelliteId=SAT002&status=critical")
    
    filtered_rows = [x for x in rows() if x.satelliteId == 'SAT002' and x.status == 'critical']
    expected_rows = [x for x in sorted(filtered_rows, key=lambda y: y.timestamp, reverse=False)][10 : 20]

    assert response.status_code == 200
    assert response.json() == {
        "items": json_rows(expected_rows),
        "length": len(filtered_rows)
    }

def test_get_telemetry_point():
    response = client.get("/telemetry/" + rows()[0].id)
    assert response.status_code == 200
    assert response.json() == rows()[0].model_dump()

def test_post_telemetry_point():
    response = client.post("/telemetry", json={
        "satelliteId": 'SAT001',
        "timestamp": dateutils.getTimestamp(10),
        "altitude": '10',
        "velocity": '10',
        "status": 'healthy'
    })

    assert response.status_code == 200

    try:
        index = [x.id for x in telemetrystore.rows].index(response.json())
    except ValueError:
        index = None

    assert index != None

def test_post_telemetry_point_invalid_satelliteId():
    response = client.post("/telemetry", json={
        "satelliteId": 'invalid',
        "timestamp": dateutils.getTimestamp(10),
        "altitude": '10',
        "velocity": '10',
        "status": 'healthy'
    })

    assert response.status_code == 400

def test_post_telemetry_point_invalid_timestamp():
    response = client.post("/telemetry", json={
        "satelliteId": 'SAT001',
        "timestamp": '1/1/2026 10:00:00',
        "altitude": '10',
        "velocity": '10',
        "status": 'healthy'
    })

    assert response.status_code == 400

def test_post_telemetry_point_invalid_altitude():
    response = client.post("/telemetry", json={
        "satelliteId": 'SAT001',
        "timestamp": dateutils.getTimestamp(10),
        "altitude": '0',
        "velocity": '10',
        "status": 'healthy'
    })

    assert response.status_code == 400

def test_post_telemetry_point_invalid_velocity():
    response = client.post("/telemetry", json={
        "satelliteId": 'SAT001',
        "timestamp": dateutils.getTimestamp(10),
        "altitude": '10',
        "velocity": '0',
        "status": 'healthy'
    })

    assert response.status_code == 400

def test_post_telemetry_point_invalid_status():
    response = client.post("/telemetry", json={
        "satelliteId": 'SAT001',
        "timestamp": dateutils.getTimestamp(10),
        "altitude": '10',
        "velocity": '10',
        "status": 'invalid'
    })

    assert response.status_code == 400

def test_delete_telemetry_point():
    delete_id = rows()[0].id
    response = client.delete("/telemetry/" + delete_id)

    assert response.status_code == 200

    try:
        index = [x.id for x in telemetrystore.rows].index(delete_id)
    except ValueError:
        index = None

    assert index == None