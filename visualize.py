import serial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import serial.tools.list_ports

def find_nucleo_port(vid=0x0483, pid=None, manufacturer_substr=None):
    """
    Auto-detect the COM port of a Nucleo or any USB device
    by VID, PID, or manufacturer substring.
    """
    ports = serial.tools.list_ports.comports()

    for p in ports:
        # Match by VID/PID if provided
        if vid is not None and p.vid != vid:
            continue
        if pid is not None and p.pid != pid:
            continue

        # Optional: match by manufacturer string
        if manufacturer_substr is not None:
            if p.manufacturer is None:
                continue
            if manufacturer_substr.lower() not in p.manufacturer.lower():
                continue

        return p.device  # e.g. "COM7"

    return None

# -----------------------------
# CONFIG
# -----------------------------
PORT = find_nucleo_port()
BAUD = 115200
GRID_W = 8
GRID_H = 8

# -----------------------------
# SERIAL SETUP
# -----------------------------
ser = serial.Serial(PORT, BAUD, timeout=1)

# -----------------------------
# PLOTTING SETUP
# -----------------------------
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Precompute pixel grid (x,y)
x = np.repeat(np.arange(GRID_W), GRID_H)
y = np.tile(np.arange(GRID_H), GRID_W)

# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    line = ser.readline().decode(errors='ignore').strip()
    if not line:
        continue

    parts = [p.strip() for p in line.split(";") if p.strip()]
    if len(parts) != 1 + GRID_W * GRID_H:
        continue

    timestamp = int(parts[0])
    values = np.array([int(v) for v in parts[1:]])
    values = np.where(values < 0, np.nan, values)

    # Save current camera view
    elev = ax.elev
    azim = ax.azim

    ax.clear()

    # Restore camera view
    ax.view_init(elev=elev, azim=azim)

    ax.set_title(f"VL53L5CX 4×4 Depth Map   t={timestamp}")
    ax.set_xlabel("X pixel")
    ax.set_ylabel("Y pixel")
    ax.set_zlabel("Distance (mm)")

    ax.scatter(x, y, values, c=values, cmap='viridis', s=80)

    ax.set_xlim(0, GRID_W - 1)
    ax.set_ylim(0, GRID_H - 1)
    ax.set_zlim(0, np.nanmax(values) * 1.1)

    plt.draw()
    plt.pause(0.01)
