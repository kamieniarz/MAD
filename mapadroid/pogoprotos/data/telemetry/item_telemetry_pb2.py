# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/item_telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/item_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n.pogoprotos/data/telemetry/item_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\xa4\x01\n\rItemTelemetry\x12@\n\x11item_use_click_id\x18\x01 \x01(\x0e\x32%.pogoprotos.enums.ItemUseTelemetryIds\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\x12\x10\n\x08\x65quipped\x18\x03 \x01(\x08\x12\x16\n\x0e\x66rom_inventory\x18\x04 \x01(\x08\x12\x16\n\x0eitem_id_string\x18\x05 \x01(\tb\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_ITEMTELEMETRY = _descriptor.Descriptor(
  name='ItemTelemetry',
  full_name='pogoprotos.data.telemetry.ItemTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_use_click_id', full_name='pogoprotos.data.telemetry.ItemTelemetry.item_use_click_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.data.telemetry.ItemTelemetry.item_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='equipped', full_name='pogoprotos.data.telemetry.ItemTelemetry.equipped', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_inventory', full_name='pogoprotos.data.telemetry.ItemTelemetry.from_inventory', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id_string', full_name='pogoprotos.data.telemetry.ItemTelemetry.item_id_string', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=280,
)

_ITEMTELEMETRY.fields_by_name['item_use_click_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._ITEMUSETELEMETRYIDS
DESCRIPTOR.message_types_by_name['ItemTelemetry'] = _ITEMTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemTelemetry = _reflection.GeneratedProtocolMessageType('ItemTelemetry', (_message.Message,), {
  'DESCRIPTOR' : _ITEMTELEMETRY,
  '__module__' : 'pogoprotos.data.telemetry.item_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ItemTelemetry)
  })
_sym_db.RegisterMessage(ItemTelemetry)


# @@protoc_insertion_point(module_scope)
