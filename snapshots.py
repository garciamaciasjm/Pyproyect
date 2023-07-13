#!/bin/python3
from tools import cli, service_instance, pchelper
from pyVmomi import vim
from influxdb import InfluxDBClient
from datetime import datetime
import time

def influx_connection():
    """
    Function where we are connecting to influxdb.
    """
    host ='Influx_IP'
    port = '8086'
    user = 'anyuser'
    password = 'anypass'
    dbname = 'anydb'

    client = InfluxDBClient(host, port, user, password, dbname)

    return client


def influx_data(vm_name, snapshot_name, since):
    """
    Function where we are defining all data to send to influxdb.
    """
    data_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    json_body = [
        {
        "measurement": "current_snapshot",
        # "tags": {
        #     "tag_srv": "vm_name",
        #     "tag_name": "snapshot_name"
        # },
        "time": data_time,
        "fields": {
            "Virtual Machine": vm_name,
            "Snapshot": snapshot_name,
            "Since": since
        }
        }
    ]

    return json_body


def catch_snapshot(content):
    """
    Function where we are taking all the snapshot content of every virtual machine.
    """
    container = content.rootFolder
    view_type = [vim.VirtualMachine]
    recursive = True
    container_view = content.viewManager.CreateContainerView(
            container, view_type, recursive)
    machine_objects_list = container_view.view

    for vm in machine_objects_list:

        if vm.snapshot is not None and vm.config.template == False:

            snapshot_lists = vm.snapshot.rootSnapshotList
            snapshot_output(snapshot_lists, vm.config)


def snapshot_output(snapshot_lists, vm_config):
    """
    Function where we are defining the structure to print or data to deal with and sending to influxdb.
    """
    client = influx_connection()

    time1 = snapshot_lists[0].createTime

    day = time1.strftime("%d-%m-%Y  %H:%M")

    json_data = influx_data(vm_config.name, snapshot_lists[0].name, day)

    print(json_data) # line for logs in icinga

    client.write_points(json_data)

    time.sleep(1)

    snapshotchild = snapshot_lists[0].childSnapshotList

    if snapshotchild:
        snapshot_output(snapshotchild, vm_config)

    return


def main():
    """
    Function where we are starting the py program with vcenter
    """
    parser = cli.Parser()
    args = parser.get_args()
    si = service_instance.connect(args)

    content = si.RetrieveContent()

    catch_snapshot(content)


# Starting the program:
if __name__ == "__main__":
    main()