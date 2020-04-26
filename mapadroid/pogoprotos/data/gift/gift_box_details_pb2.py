# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/gift/gift_box_details.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/gift/gift_box_details.proto',
  package='pogoprotos.data.gift',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n+pogoprotos/data/gift/gift_box_details.proto\x12\x14pogoprotos.data.gift\"\xc7\x02\n\x0eGiftBoxDetails\x12\x12\n\ngiftbox_id\x18\x01 \x01(\x06\x12\x11\n\tsender_id\x18\x02 \x01(\t\x12\x17\n\x0fsender_codename\x18\x03 \x01(\t\x12\x13\n\x0breceiver_id\x18\x04 \x01(\t\x12\x19\n\x11receiver_codename\x18\x05 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x06 \x01(\t\x12\x11\n\tfort_name\x18\x07 \x01(\t\x12\x10\n\x08\x66ort_lat\x18\x08 \x01(\x01\x12\x10\n\x08\x66ort_lng\x18\t \x01(\x01\x12\x16\n\x0e\x66ort_image_url\x18\n \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x0b \x01(\x03\x12\x16\n\x0esent_timestamp\x18\x0c \x01(\x03\x12\x1b\n\x13\x64\x65livery_pokemon_id\x18\r \x01(\x06\x12\x14\n\x0cis_sponsored\x18\x0e \x01(\x08\x62\x06proto3'
)




_GIFTBOXDETAILS = _descriptor.Descriptor(
  name='GiftBoxDetails',
  full_name='pogoprotos.data.gift.GiftBoxDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='giftbox_id', full_name='pogoprotos.data.gift.GiftBoxDetails.giftbox_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='pogoprotos.data.gift.GiftBoxDetails.sender_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_codename', full_name='pogoprotos.data.gift.GiftBoxDetails.sender_codename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_id', full_name='pogoprotos.data.gift.GiftBoxDetails.receiver_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_codename', full_name='pogoprotos.data.gift.GiftBoxDetails.receiver_codename', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.gift.GiftBoxDetails.fort_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_name', full_name='pogoprotos.data.gift.GiftBoxDetails.fort_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_lat', full_name='pogoprotos.data.gift.GiftBoxDetails.fort_lat', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_lng', full_name='pogoprotos.data.gift.GiftBoxDetails.fort_lng', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_image_url', full_name='pogoprotos.data.gift.GiftBoxDetails.fort_image_url', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_timestamp', full_name='pogoprotos.data.gift.GiftBoxDetails.creation_timestamp', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sent_timestamp', full_name='pogoprotos.data.gift.GiftBoxDetails.sent_timestamp', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delivery_pokemon_id', full_name='pogoprotos.data.gift.GiftBoxDetails.delivery_pokemon_id', index=12,
      number=13, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_sponsored', full_name='pogoprotos.data.gift.GiftBoxDetails.is_sponsored', index=13,
      number=14, type=8, cpp_type=7, label=1,
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
  serialized_start=70,
  serialized_end=397,
)

DESCRIPTOR.message_types_by_name['GiftBoxDetails'] = _GIFTBOXDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GiftBoxDetails = _reflection.GeneratedProtocolMessageType('GiftBoxDetails', (_message.Message,), {
  'DESCRIPTOR' : _GIFTBOXDETAILS,
  '__module__' : 'pogoprotos.data.gift.gift_box_details_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.gift.GiftBoxDetails)
  })
_sym_db.RegisterMessage(GiftBoxDetails)


# @@protoc_insertion_point(module_scope)
