import psutil

def get_temperatures():
    temps = psutil.sensors_temperatures()
    result = {}

    # CPU temperature
    if "coretemp" in temps:
        for t in temps["coretemp"]:
            if "Package" in t.label:
                result["cpu"] = {
                    "current": t.current,
                    "high": t.high,
                    "critical": t.critical
                }

    # NVMe temperature
    if "nvme" in temps:
        for t in temps["nvme"]:
            if "Composite" in t.label:
                result["nvme"] = {
                    "current": t.current,
                    "high": t.high,
                    "critical": t.critical
                }

    # ACPI zone (optional)
    if "acpitz" in temps:
        result["acpi"] = temps["acpitz"][0].current

    return result
