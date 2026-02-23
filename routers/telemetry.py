from fastapi import APIRouter, HTTPException
import uuid
from models import telemetrypoint
from utils import dateutils
from store import telemetrystore, satellitestore
import copy

router = APIRouter(prefix="/telemetry", tags=["telemetry"])

@router.get("/")
async def list_telemetry(page: int = None, pageSize: int = None, sortBy: str = None, sortDirection: str = None, satelliteId: str = None, status: str = None):
    # Copy first to preserve data
    rows = copy.deepcopy(telemetrystore.rows)

    # Filtering
    filtered_rows = [x for x in rows]
    if satelliteId != None:
        filtered_rows = [x for x in filtered_rows if x.satelliteId == satelliteId]
    if status != None:
        filtered_rows = [x for x in filtered_rows if x.status == status]
    
    # Sorting
    sorted_rows = filtered_rows
    # If sortBy is None, ignore sortDirection and use default
    if sortBy == None:
        sorted_rows.sort(key=lambda x: x.timestamp, reverse=True)
    # Else, sort by sortBy
    else:
        if sortBy == 'timestamp':
            sorted_rows.sort(key=lambda x: x.timestamp, reverse=sortDirection == 'descending')
        elif sortBy == 'altitude':
            sorted_rows.sort(key=lambda x: x.altitude, reverse=sortDirection == 'descending')
        elif sortBy == 'velocity':
            sorted_rows.sort(key=lambda x: x.velocity, reverse=sortDirection == 'descending')

    # Paging
    paged_rows = sorted_rows
    if (page != None and pageSize != None):
        paged_rows = paged_rows[page * pageSize : (page + 1) * pageSize]

    return {
        "items": paged_rows,
        "length": len(filtered_rows)
    }

@router.get("/{id}")
async def get_telemetry_point(id):
    try:
        index = [x.id for x in telemetrystore.rows].index(id)
        return telemetrystore.rows[index]
    except ValueError:
        raise HTTPException(status_code=404, detail="Not found")

@router.post("/")
async def create_telemetry_point(info: telemetrypoint.TelemetryPointInfo):
    # Convert info to point class
    point = info
    point.__class__ = telemetrypoint.TelemetryPoint

    # Validation
    if point.satelliteId not in [x.id for x in satellitestore.rows]:
        raise HTTPException(status_code=400, detail="Invalid satellite ID")
    if not dateutils.isValidISO8601(point.timestamp):
        raise HTTPException(status_code=400, detail="Not a valid ISO 8601 timestamp")
    if point.altitude <= 0:
        raise HTTPException(status_code=400, detail="Altitude must be positive")
    if point.velocity <= 0:
        raise HTTPException(status_code=400, detail="Velocity must be positive")
    if point.status not in ['healthy', 'interruption', 'critical']:
        raise HTTPException(status_code=400, detail="Invalid status")

    # Assign ID
    point.id = str(uuid.uuid4())

    telemetrystore.rows.append(point)
    return point.id # Return new ID

@router.delete("/{id}")
async def delete_telemetry_point(id):
    try:
        index = [x.id for x in telemetrystore.rows].index(id)
        telemetrystore.rows = telemetrystore.rows[:index] + telemetrystore.rows[index + 1:]
        return
    except ValueError:
        raise HTTPException(status_code=404, detail="Not found")