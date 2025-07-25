
                [ManufacturerData.from_json(i) for i in json["manufacturerData"]]
                bool(json["authenticatedSignedWrites"])
                bool(json["extendedProperties"])
                bool(json["writeWithoutResponse"])
                else None
                if "authenticatedSignedWrites" in json
                if "extendedProperties" in json
                if "manufacturerData" in json
                if "writeWithoutResponse" in json
            ),
            address=str(json["address"]),
            appearance=int(json["appearance"]) if "appearance" in json else None,
            authenticated_signed_writes=(
            broadcast=bool(json["broadcast"]) if "broadcast" in json else None,
            data=str(json["data"]),
            device_address=str(json["deviceAddress"]),
            extended_properties=(
            indicate=bool(json["indicate"]) if "indicate" in json else None,
            json["appearance"] = self.appearance
            json["authenticatedSignedWrites"] = self.authenticated_signed_writes
            json["broadcast"] = self.broadcast
            json["extendedProperties"] = self.extended_properties
            json["indicate"] = self.indicate
            json["manufacturerData"] = [i.to_json() for i in self.manufacturer_data]
            json["name"] = self.name
            json["notify"] = self.notify
            json["read"] = self.read
            json["txPower"] = self.tx_power
            json["uuids"] = [i for i in self.uuids]
            json["write"] = self.write
            json["writeWithoutResponse"] = self.write_without_response
            key=int(json["key"]),
            manufacturer_data=(
            name=str(json["name"]) if "name" in json else None,
            notify=bool(json["notify"]) if "notify" in json else None,
            read=bool(json["read"]) if "read" in json else None,
            rssi=int(json["rssi"]),
            scan_record=ScanRecord.from_json(json["scanRecord"]),
            tx_power=int(json["txPower"]) if "txPower" in json else None,
            type_=GATTOperationType.from_json(json["type"]),
            uuids=[str(i) for i in json["uuids"]] if "uuids" in json else None,
            write_without_response=(
            write=bool(json["write"]) if "write" in json else None,
        "method": "BluetoothEmulation.addCharacteristic",
        "method": "BluetoothEmulation.addService",
        "method": "BluetoothEmulation.disable",
        "method": "BluetoothEmulation.enable",
        "method": "BluetoothEmulation.removeCharacteristic",
        "method": "BluetoothEmulation.removeService",
        "method": "BluetoothEmulation.setSimulatedCentralState",
        "method": "BluetoothEmulation.simulateAdvertisement",
        "method": "BluetoothEmulation.simulateGATTOperationResponse",
        "method": "BluetoothEmulation.simulatePreconnectedPeripheral",
        "params": params,
        )
        if self.appearance is not None:
        if self.authenticated_signed_writes is not None:
        if self.broadcast is not None:
        if self.extended_properties is not None:
        if self.indicate is not None:
        if self.manufacturer_data is not None:
        if self.name is not None:
        if self.notify is not None:
        if self.read is not None:
        if self.tx_power is not None:
        if self.uuids is not None:
        if self.write is not None:
        if self.write_without_response is not None:
        json = dict()
        json["data"] = self.data
        json["deviceAddress"] = self.device_address
        json["key"] = self.key
        json["rssi"] = self.rssi
        json["scanRecord"] = self.scan_record.to_json()
        return cls(
        return cls(json)
        return json
        return self.value
    """
    #: Company identifier
    #: https://bitbucket.org/bluetooth-SIG/public/src/main/assigned_numbers/company_identifiers/company_identifiers.yaml
    #: https://usb.org/developers
    #: Key is the company identifier and the value is an array of bytes of
    #: manufacturer specific data.
    #: Manufacturer-specific data
    #: Stores the external appearance description of the device.
    #: Stores the transmission power of a broadcasting device.
    :param address:
    :param characteristic_id:
    :param characteristic_uuid:
    :param code:
    :param entry:
    :param known_service_uuids:
    :param le_supported: If the simulated central supports low-energy.
    :param manufacturer_data:
    :param name:
    :param properties:
    :param service_id:
    :param service_uuid:
    :param state: State of the simulated central.
    :param type_:
    :returns: An identifier that uniquely represents this characteristic.
    :returns: An identifier that uniquely represents this service.
    @classmethod
    ``address``.
    }
    ABSENT = "absent"
    address: str
    address: str,
    address: str, service_id: str
    address: str, service_id: str, characteristic_id: str
    address: str, service_uuid: str
    address: str, type_: GATTOperationType, code: int
    Adds a characteristic with ``characteristicUuid`` and ``properties`` to the
    Adds a service with ``serviceUuid`` to the peripheral with ``address``.
    appearance: int | None = None
    authenticated_signed_writes: bool | None = None
    Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes.
    broadcast: bool | None = None
    characteristic_uuid: str,
    cmd_dict: T_JSON_DICT = {
    CONNECTION = "connection"
    data: str
    def __init__(self, *args, **kwargs): pass
    def from_json(cls, json):
    def from_json(cls, json: T_JSON_DICT) -> GattOperationReceived:
    def to_json(self):
    Describes the properties of a characteristic. This follows Bluetooth Core
    device_address: str
    Disable the BluetoothEmulation domain.
    DISCOVERY = "discovery"
    Enable the BluetoothEmulation domain.
    entry: ScanEntry,
    Event for when a GATT operation of ``type`` to the peripheral with ``address``
    extended_properties: bool | None = None
    GATT operation of ``type``. The ``code`` value follows the HCI Error Codes from
    happened.
    indicate: bool | None = None
    Indicates the various states of Central.
    Indicates the various types of GATT event.
    json = yield cmd_dict
    key: int
    known_service_uuids: list[str],
    manufacturer_data: list[ManufacturerData] | None = None
    manufacturer_data: list[ManufacturerData],
    name: str | None = None
    name: str,
    notify: bool | None = None
    params: T_JSON_DICT = dict()
    params["address"] = address
    params["characteristicId"] = characteristic_id
    params["characteristicUuid"] = characteristic_uuid
    params["code"] = code
    params["entry"] = entry.to_json()
    params["knownServiceUuids"] = [i for i in known_service_uuids]
    params["leSupported"] = le_supported
    params["manufacturerData"] = [i.to_json() for i in manufacturer_data]
    params["name"] = name
    params["properties"] = properties.to_json()
    params["serviceId"] = service_id
    params["serviceUuid"] = service_uuid
    params["state"] = state.to_json()
    params["type"] = type_.to_json()
    POWERED_OFF = "powered-off"
    POWERED_ON = "powered-on"
    properties: CharacteristicProperties,
    read: bool | None = None
    Removes the characteristic respresented by ``characteristicId`` from the
    Removes the service respresented by ``serviceId`` from the peripheral with
    return str(json["characteristicId"])
    return str(json["serviceId"])
    rssi: int
    scan_record: ScanRecord
    service represented by ``serviceId`` in the peripheral with ``address``.
    service respresented by ``serviceId`` in the peripheral with ``address``.
    service_id: str,
    Set the state of the simulated central.
    Simulates a peripheral with ``address``, ``name`` and ``knownServiceUuids``
    Simulates an advertisement packet described in ``entry`` being received by
    Simulates the response code from the peripheral with ``address`` for a
    Specification BT 4.2 Vol 3 Part G 3.3.1. Characteristic Properties.
    state: CentralState,
    state: CentralState, le_supported: bool
    Stores the advertisement packet information that is sent by a Bluetooth device.
    Stores the byte data of the advertisement packet sent by a Bluetooth device.
    Stores the manufacturer data
    that has already been connected to the system.
    the central.
    tx_power: int | None = None
    type_: GATTOperationType
    uuids: list[str] | None = None
    write: bool | None = None
    write_without_response: bool | None = None
#
# CDP domain: BluetoothEmulation (experimental)
# changes, edit the generator and regenerate all of the modules.
# DO NOT EDIT THIS FILE!
# This file is generated from the CDP specification. If you need to make
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, str]:
@dataclass
@event_class("BluetoothEmulation.gattOperationReceived")
class CentralState:
class CharacteristicProperties:
class GattOperationReceived:
class GATTOperationType:
class ManufacturerData:
class ScanEntry:
class ScanRecord:
def add_characteristic(
def add_service(
def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
def enable(
def remove_characteristic(
def remove_service(
def set_simulated_central_state(
def simulate_advertisement(
def simulate_gatt_operation_response(
def simulate_preconnected_peripheral(
from .util import event_class, T_JSON_DICT
from __future__ import annotations
from dataclasses import dataclass
import typing
