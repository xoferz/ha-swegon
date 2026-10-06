import logging

from .casa_base import CasaBase
from ..swegon import (
    COMMANDS,
    R7_CONFIG,
    R7_STATUSES,
    SENSORS,
    SENSORS2,
    SETPOINTS,
    Modbus_Datapoint,
)

_LOGGER = logging.getLogger(__name__)


class CasaR7(CasaBase):
    """Datapoints for the Swegon CASA R7."""

    def __init__(self):
        super().__init__()

        # The R7 reports its temperature setpoint in whole degrees.
        self.Datapoints[SETPOINTS]["Temp_SP"] = Modbus_Datapoint(5100, 1)

        # R7 cooker hood runtime command (4x5005, zero-based address 5004).
        self.Datapoints[COMMANDS]["Cooker_Hood"] = Modbus_Datapoint(5004, 1)

        # Absolute humidity uses 0.01 g/m³ resolution on the R7.
        self.Datapoints[SENSORS]["AH"] = Modbus_Datapoint(6214, 0.01)
        self.Datapoints[SENSORS]["AH_SP"] = Modbus_Datapoint(6215, 0.01)

        # 3x6234: rotor speed in RPM (zero-based address 6233).
        self.Datapoints[SENSORS2]["Heat_Exchanger"] = Modbus_Datapoint(6233, 1)

        # R7-specific settings use non-contiguous holding registers.
        self.Datapoints[R7_CONFIG] = {
            "Summer_Night_Cooling": Modbus_Datapoint(5163, 1),
            "Temperature_Control_Mode": Modbus_Datapoint(5173, 1),
        }

        # R7-specific status uses a non-contiguous input register.
        self.Datapoints[R7_STATUSES] = {
            "Summer_Cooling_Active": Modbus_Datapoint(6333, 1),
        }

        _LOGGER.debug("Loaded datapoints for Swegon Casa R7")
