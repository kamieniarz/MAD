# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gameiap/responses/redeem_samsung_receipt_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gameiap/responses/redeem_samsung_receipt_response.proto',
  package='pogoprotos.networking.game.gameiap.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nRpogoprotos/networking/game/gameiap/responses/redeem_samsung_receipt_response.proto\x12,pogoprotos.networking.game.gameiap.responses\"b\n\x1cRedeemSamsungReceiptResponse\x12\x13\n\x0bpurchase_id\x18\x01 \x01(\t\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3'
)



_REDEEMSAMSUNGRECEIPTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.game.gameiap.responses.RedeemSamsungReceiptResponse.Status',
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
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=185,
  serialized_end=230,
)
_sym_db.RegisterEnumDescriptor(_REDEEMSAMSUNGRECEIPTRESPONSE_STATUS)


_REDEEMSAMSUNGRECEIPTRESPONSE = _descriptor.Descriptor(
  name='RedeemSamsungReceiptResponse',
  full_name='pogoprotos.networking.game.gameiap.responses.RedeemSamsungReceiptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='purchase_id', full_name='pogoprotos.networking.game.gameiap.responses.RedeemSamsungReceiptResponse.purchase_id', index=0,
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
    _REDEEMSAMSUNGRECEIPTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=230,
)

_REDEEMSAMSUNGRECEIPTRESPONSE_STATUS.containing_type = _REDEEMSAMSUNGRECEIPTRESPONSE
DESCRIPTOR.message_types_by_name['RedeemSamsungReceiptResponse'] = _REDEEMSAMSUNGRECEIPTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedeemSamsungReceiptResponse = _reflection.GeneratedProtocolMessageType('RedeemSamsungReceiptResponse', (_message.Message,), {
  'DESCRIPTOR' : _REDEEMSAMSUNGRECEIPTRESPONSE,
  '__module__' : 'pogoprotos.networking.game.gameiap.responses.redeem_samsung_receipt_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.game.gameiap.responses.RedeemSamsungReceiptResponse)
  })
_sym_db.RegisterMessage(RedeemSamsungReceiptResponse)


# @@protoc_insertion_point(module_scope)
