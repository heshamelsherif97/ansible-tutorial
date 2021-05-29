#!/usr/bin/python3

# Standard imports
import datetime


# Outside imports
import psutil
import pandas as pd



def save_csv(measurement, filename):
    current_timestamp = datetime.datetime.now()
    measurement = str(measurement) + "%"
    df = pd.DataFrame(
        data={"timestamp": [current_timestamp], "utilization": [measurement]}
    )
    df.to_csv(filename, mode="a", index=False, header=False)


def monitor_cpu():
    """
    Returns CPU utilization over a period of 0.4
    """
    return psutil.cpu_percent(interval=0.4)


def monitor_ram():
    """
    Returns System wide available memory %
    """
    memory_dict = dict(psutil.virtual_memory()._asdict())
    return memory_dict["free"] / memory_dict["total"] * 100.0

def monitor_disk():
    """
    Returns Root disk available space %
    """
    hdd_dict = dict(psutil.disk_usage("/")._asdict())
    return hdd_dict["free"] / hdd_dict["total"] * 100.0

if __name__ == "__main__":
    dir = '/opt/'
    monitors = {
        monitor_ram(): '{}MEM.csv'.format(dir),
        monitor_disk(): '{}DISK.csv'.format(dir),
        monitor_cpu(): '{}CPU.csv'.format(dir),
    }
    {save_csv(k, v) for k, v in monitors.items()}
