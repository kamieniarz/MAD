# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/send_raid_invitation_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/send_raid_invitation_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nJpogoprotos/networking/requests/messages/send_raid_invitation_message.proto\x12\'pogoprotos.networking.requests.messages\"}\n\x12SendRaidInvitation\x12\x13\n\x0binvitee_ids\x18\x01 \x03(\t\x12\x0e\n\x06gym_id\x18\x02 \x01(\t\x12\x10\n\x08lobby_id\x18\x03 \x03(\x05\x12\x17\n\x0fgym_lat_degrees\x18\x04 \x01(\x01\x12\x17\n\x0fgym_lng_degrees\x18\x05 \x01(\x01\x62\x06proto3'
)




_SENDRAIDINVITATION = _descriptor.Descriptor(
  name='SendRaidInvitation',
  full_name='pogoprotos.networking.requests.messages.SendRaidInvitation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invitee_ids', full_name='pogoprotos.networking.requests.messages.SendRaidInvitation.invitee_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.networking.requests.messages.SendRaidInvitation.gym_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobby_id', full_name='pogoprotos.networking.requests.messages.SendRaidInvitation.lobby_id', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_lat_degrees', full_name='pogoprotos.networking.requests.messages.SendRaidInvitation.gym_lat_degrees', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_lng_degrees', full_name='pogoprotos.networking.requests.messages.SendRaidInvitation.gym_lng_degrees', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=119,
  serialized_end=244,
)

DESCRIPTOR.message_types_by_name['SendRaidInvitation'] = _SENDRAIDINVITATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendRaidInvitation = _reflection.GeneratedProtocolMessageType('SendRaidInvitation', (_message.Message,), {
  'DESCRIPTOR' : _SENDRAIDINVITATION,
  '__module__' : 'pogoprotos.networking.requests.messages.send_raid_invitation_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SendRaidInvitation)
  })
_sym_db.RegisterMessage(SendRaidInvitation)


# @@protoc_insertion_point(module_scope)
