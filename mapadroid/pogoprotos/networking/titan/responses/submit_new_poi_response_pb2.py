# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/titan/responses/submit_new_poi_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/titan/responses/submit_new_poi_response.proto',
  package='pogoprotos.networking.titan.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nCpogoprotos/networking/titan/responses/submit_new_poi_response.proto\x12%pogoprotos.networking.titan.responses\"\x97\x02\n\x14SubmitNewPoiResponse\x12R\n\x06status\x18\x01 \x01(\x0e\x32\x42.pogoprotos.networking.titan.responses.SubmitNewPoiResponse.Status\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\"\x93\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x12\x12\n\x0eINTERNAL_ERROR\x10\x03\x12\x1f\n\x1bTOO_MANY_RECENT_SUBMISSIONS\x10\x04\x12\x11\n\rINVALID_INPUT\x10\x05\x12\t\n\x05MINOR\x10\x06\x12\x11\n\rNOT_AVAILABLE\x10\x07\x62\x06proto3'
)



_SUBMITNEWPOIRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.titan.responses.SubmitNewPoiResponse.Status',
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
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_RECENT_SUBMISSIONS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_INPUT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINOR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_AVAILABLE', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=243,
  serialized_end=390,
)
_sym_db.RegisterEnumDescriptor(_SUBMITNEWPOIRESPONSE_STATUS)


_SUBMITNEWPOIRESPONSE = _descriptor.Descriptor(
  name='SubmitNewPoiResponse',
  full_name='pogoprotos.networking.titan.responses.SubmitNewPoiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.titan.responses.SubmitNewPoiResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submission_id', full_name='pogoprotos.networking.titan.responses.SubmitNewPoiResponse.submission_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SUBMITNEWPOIRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=390,
)

_SUBMITNEWPOIRESPONSE.fields_by_name['status'].enum_type = _SUBMITNEWPOIRESPONSE_STATUS
_SUBMITNEWPOIRESPONSE_STATUS.containing_type = _SUBMITNEWPOIRESPONSE
DESCRIPTOR.message_types_by_name['SubmitNewPoiResponse'] = _SUBMITNEWPOIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitNewPoiResponse = _reflection.GeneratedProtocolMessageType('SubmitNewPoiResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITNEWPOIRESPONSE,
  '__module__' : 'pogoprotos.networking.titan.responses.submit_new_poi_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.titan.responses.SubmitNewPoiResponse)
  })
_sym_db.RegisterMessage(SubmitNewPoiResponse)


# @@protoc_insertion_point(module_scope)
