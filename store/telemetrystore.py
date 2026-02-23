import uuid
from utils import dateutils
from models import telemetrypoint

rows: list[telemetrypoint.TelemetryPoint] = [
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(1),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(2),
        altitude = 351461,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(3),
        altitude = 351461,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(4),
        altitude = 351460,
        velocity = 7701,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(5),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(6),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(7),
        altitude = 351461,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(8),
        altitude = 351461,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(9),
        altitude = 351460,
        velocity = 7701,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(10),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(11),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(12),
        altitude = 351460,
        velocity = 7700,
        status = "interruption"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(13),
        altitude = 351460,
        velocity = 7700,
        status = "interruption"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(14),
        altitude = 351460,
        velocity = 7701,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(15),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(16),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(17),
        altitude = 351461,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(18),
        altitude = 351461,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(19),
        altitude = 351460,
        velocity = 7701,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT001",
        timestamp = dateutils.getTimestamp(20),
        altitude = 351460,
        velocity = 7700,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(1),
        altitude = 1,
        velocity = 1,
        status = "critical"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(2),
        altitude = 1,
        velocity = 1,
        status = "critical"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(3),
        altitude = 1,
        velocity = 1,
        status = "critical"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(4),
        altitude = 1,
        velocity = 1,
        status = "critical"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(5),
        altitude = 306587,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(6),
        altitude = 306587,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(7),
        altitude = 306588,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(8),
        altitude = 306588,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(9),
        altitude = 306588,
        velocity = 7724,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(10),
        altitude = 306588,
        velocity = 7725,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(11),
        altitude = 306588,
        velocity = 7725,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(12),
        altitude = 306588,
        velocity = 7724,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(13),
        altitude = 306588,
        velocity = 7725,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(14),
        altitude = 306587,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(15),
        altitude = 306587,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(16),
        altitude = 306587,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(17),
        altitude = 306586,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(18),
        altitude = 306586,
        velocity = 7726,
        status = "interruption"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(19),
        altitude = 306586,
        velocity = 7726,
        status = "healthy"
    ),
    telemetrypoint.TelemetryPoint(
        id = str(uuid.uuid4()),
        satelliteId = "SAT002",
        timestamp = dateutils.getTimestamp(20),
        altitude = 306586,
        velocity = 7726,
        status = "healthy"
    )
]
