# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/invasion_open_combat_session_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map.fort import incident_lookup_pb2 as pogoprotos_dot_map_dot_fort_dot_incident__lookup__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/invasion_open_combat_session_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nRpogoprotos/networking/requests/messages/invasion_open_combat_session_message.proto\x12\'pogoprotos.networking.requests.messages\x1a)pogoprotos/map/fort/incident_lookup.proto\"\x8c\x01\n InvasionOpenCombatSessionMessage\x12<\n\x0fincident_lookup\x18\x01 \x01(\x0b\x32#.pogoprotos.map.fort.IncidentLookup\x12\x0c\n\x04step\x18\x02 \x01(\x05\x12\x1c\n\x14\x61ttacking_pokemon_id\x18\x03 \x03(\x06\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_map_dot_fort_dot_incident__lookup__pb2.DESCRIPTOR,])




_INVASIONOPENCOMBATSESSIONMESSAGE = _descriptor.Descriptor(
  name='InvasionOpenCombatSessionMessage',
  full_name='pogoprotos.networking.requests.messages.InvasionOpenCombatSessionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incident_lookup', full_name='pogoprotos.networking.requests.messages.InvasionOpenCombatSessionMessage.incident_lookup', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='pogoprotos.networking.requests.messages.InvasionOpenCombatSessionMessage.step', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attacking_pokemon_id', full_name='pogoprotos.networking.requests.messages.InvasionOpenCombatSessionMessage.attacking_pokemon_id', index=2,
      number=3, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=171,
  serialized_end=311,
)

_INVASIONOPENCOMBATSESSIONMESSAGE.fields_by_name['incident_lookup'].message_type = pogoprotos_dot_map_dot_fort_dot_incident__lookup__pb2._INCIDENTLOOKUP
DESCRIPTOR.message_types_by_name['InvasionOpenCombatSessionMessage'] = _INVASIONOPENCOMBATSESSIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InvasionOpenCombatSessionMessage = _reflection.GeneratedProtocolMessageType('InvasionOpenCombatSessionMessage', (_message.Message,), {
  'DESCRIPTOR' : _INVASIONOPENCOMBATSESSIONMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.invasion_open_combat_session_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.InvasionOpenCombatSessionMessage)
  })
_sym_db.RegisterMessage(InvasionOpenCombatSessionMessage)


# @@protoc_insertion_point(module_scope)
