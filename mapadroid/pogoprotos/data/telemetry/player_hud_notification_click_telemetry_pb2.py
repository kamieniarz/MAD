# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/player_hud_notification_click_telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/player_hud_notification_click_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nGpogoprotos/data/telemetry/player_hud_notification_click_telemetry.proto\x12\x19pogoprotos.data.telemetry\"D\n#PlayerHudNotificationClickTelemetry\x12\x1d\n\x15notification_category\x18\x01 \x01(\tb\x06proto3'
)




_PLAYERHUDNOTIFICATIONCLICKTELEMETRY = _descriptor.Descriptor(
  name='PlayerHudNotificationClickTelemetry',
  full_name='pogoprotos.data.telemetry.PlayerHudNotificationClickTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_category', full_name='pogoprotos.data.telemetry.PlayerHudNotificationClickTelemetry.notification_category', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=102,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['PlayerHudNotificationClickTelemetry'] = _PLAYERHUDNOTIFICATIONCLICKTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerHudNotificationClickTelemetry = _reflection.GeneratedProtocolMessageType('PlayerHudNotificationClickTelemetry', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERHUDNOTIFICATIONCLICKTELEMETRY,
  '__module__' : 'pogoprotos.data.telemetry.player_hud_notification_click_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.PlayerHudNotificationClickTelemetry)
  })
_sym_db.RegisterMessage(PlayerHudNotificationClickTelemetry)


# @@protoc_insertion_point(module_scope)
