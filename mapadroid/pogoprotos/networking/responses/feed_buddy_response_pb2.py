# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/feed_buddy_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.buddy import buddy_observed_data_pb2 as pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2
from pogoprotos.data.buddy import buddy_stats_shown_hearts_pb2 as pogoprotos_dot_data_dot_buddy_dot_buddy__stats__shown__hearts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/feed_buddy_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n9pogoprotos/networking/responses/feed_buddy_response.proto\x12\x1fpogoprotos.networking.responses\x1a/pogoprotos/data/buddy/buddy_observed_data.proto\x1a\x34pogoprotos/data/buddy/buddy_stats_shown_hearts.proto\"\xa6\x03\n\x11\x46\x65\x65\x64\x42uddyResponse\x12I\n\x06result\x18\x01 \x01(\x0e\x32\x39.pogoprotos.networking.responses.FeedBuddyResponse.Result\x12?\n\robserved_data\x18\x03 \x01(\x0b\x32(.pogoprotos.data.buddy.BuddyObservedData\x12V\n\x0cshown_hearts\x18\x04 \x01(\x0e\x32@.pogoprotos.data.buddy.BuddyStatsShownHearts.BuddyShownHeartType\"\xac\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x19\n\x15\x45RROR_BUDDY_NOT_VALID\x10\x02\x12!\n\x1d\x46\x41ILED_INSUFFICIENT_RESOURCES\x10\x03\x12#\n\x1f\x46\x41ILED_INVALID_ITEM_REQUIREMENT\x10\x04\x12\'\n#FAILED_BUDDY_STILL_FULL_FROM_POFFIN\x10\x05\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_buddy_dot_buddy__stats__shown__hearts__pb2.DESCRIPTOR,])



_FEEDBUDDYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.FeedBuddyResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_BUDDY_NOT_VALID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_INSUFFICIENT_RESOURCES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_INVALID_ITEM_REQUIREMENT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_BUDDY_STILL_FULL_FROM_POFFIN', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=448,
  serialized_end=620,
)
_sym_db.RegisterEnumDescriptor(_FEEDBUDDYRESPONSE_RESULT)


_FEEDBUDDYRESPONSE = _descriptor.Descriptor(
  name='FeedBuddyResponse',
  full_name='pogoprotos.networking.responses.FeedBuddyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.FeedBuddyResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observed_data', full_name='pogoprotos.networking.responses.FeedBuddyResponse.observed_data', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shown_hearts', full_name='pogoprotos.networking.responses.FeedBuddyResponse.shown_hearts', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDBUDDYRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=620,
)

_FEEDBUDDYRESPONSE.fields_by_name['result'].enum_type = _FEEDBUDDYRESPONSE_RESULT
_FEEDBUDDYRESPONSE.fields_by_name['observed_data'].message_type = pogoprotos_dot_data_dot_buddy_dot_buddy__observed__data__pb2._BUDDYOBSERVEDDATA
_FEEDBUDDYRESPONSE.fields_by_name['shown_hearts'].enum_type = pogoprotos_dot_data_dot_buddy_dot_buddy__stats__shown__hearts__pb2._BUDDYSTATSSHOWNHEARTS_BUDDYSHOWNHEARTTYPE
_FEEDBUDDYRESPONSE_RESULT.containing_type = _FEEDBUDDYRESPONSE
DESCRIPTOR.message_types_by_name['FeedBuddyResponse'] = _FEEDBUDDYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedBuddyResponse = _reflection.GeneratedProtocolMessageType('FeedBuddyResponse', (_message.Message,), {
  'DESCRIPTOR' : _FEEDBUDDYRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.feed_buddy_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.FeedBuddyResponse)
  })
_sym_db.RegisterMessage(FeedBuddyResponse)


# @@protoc_insertion_point(module_scope)
