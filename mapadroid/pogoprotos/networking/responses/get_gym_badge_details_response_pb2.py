# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_gym_badge_details_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.badge import awarded_gym_badge_pb2 as pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2
from pogoprotos.data.gym import gym_defender_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__defender__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_gym_badge_details_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nDpogoprotos/networking/responses/get_gym_badge_details_response.proto\x12\x1fpogoprotos.networking.responses\x1a-pogoprotos/data/badge/awarded_gym_badge.proto\x1a&pogoprotos/data/gym/gym_defender.proto\"\xa0\x01\n\x1aGetGymBadgeDetailsResponse\x12\x39\n\tgym_badge\x18\x01 \x01(\x0b\x32&.pogoprotos.data.badge.AwardedGymBadge\x12\x36\n\x0cgym_defender\x18\x02 \x01(\x0b\x32 .pogoprotos.data.gym.GymDefender\x12\x0f\n\x07success\x18\x03 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_gym_dot_gym__defender__pb2.DESCRIPTOR,])




_GETGYMBADGEDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetGymBadgeDetailsResponse',
  full_name='pogoprotos.networking.responses.GetGymBadgeDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_badge', full_name='pogoprotos.networking.responses.GetGymBadgeDetailsResponse.gym_badge', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_defender', full_name='pogoprotos.networking.responses.GetGymBadgeDetailsResponse.gym_defender', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.networking.responses.GetGymBadgeDetailsResponse.success', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=193,
  serialized_end=353,
)

_GETGYMBADGEDETAILSRESPONSE.fields_by_name['gym_badge'].message_type = pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2._AWARDEDGYMBADGE
_GETGYMBADGEDETAILSRESPONSE.fields_by_name['gym_defender'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__defender__pb2._GYMDEFENDER
DESCRIPTOR.message_types_by_name['GetGymBadgeDetailsResponse'] = _GETGYMBADGEDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGymBadgeDetailsResponse = _reflection.GeneratedProtocolMessageType('GetGymBadgeDetailsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGYMBADGEDETAILSRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.get_gym_badge_details_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetGymBadgeDetailsResponse)
  })
_sym_db.RegisterMessage(GetGymBadgeDetailsResponse)


# @@protoc_insertion_point(module_scope)
