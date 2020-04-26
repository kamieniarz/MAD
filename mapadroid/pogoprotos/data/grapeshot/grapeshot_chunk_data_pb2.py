# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/grapeshot/grapeshot_chunk_data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.grapeshot import grapeshot_authentication_data_pb2 as pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__authentication__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/grapeshot/grapeshot_chunk_data.proto',
  package='pogoprotos.data.grapeshot',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n4pogoprotos/data/grapeshot/grapeshot_chunk_data.proto\x12\x19pogoprotos.data.grapeshot\x1a=pogoprotos/data/grapeshot/grapeshot_authentication_data.proto\"\xf1\x01\n\x12GrapeshotChunkData\x12\x17\n\x0f\x63hunk_file_path\x18\x01 \x01(\t\x12\x14\n\x0c\x63hunk_number\x18\x02 \x01(\r\x12U\n\x15upload_authentication\x18\x03 \x01(\x0b\x32\x36.pogoprotos.data.grapeshot.GrapeshotAuthenticationData\x12U\n\x15\x64\x65lete_authentication\x18\x04 \x01(\x0b\x32\x36.pogoprotos.data.grapeshot.GrapeshotAuthenticationDatab\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__authentication__data__pb2.DESCRIPTOR,])




_GRAPESHOTCHUNKDATA = _descriptor.Descriptor(
  name='GrapeshotChunkData',
  full_name='pogoprotos.data.grapeshot.GrapeshotChunkData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_file_path', full_name='pogoprotos.data.grapeshot.GrapeshotChunkData.chunk_file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_number', full_name='pogoprotos.data.grapeshot.GrapeshotChunkData.chunk_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_authentication', full_name='pogoprotos.data.grapeshot.GrapeshotChunkData.upload_authentication', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_authentication', full_name='pogoprotos.data.grapeshot.GrapeshotChunkData.delete_authentication', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=147,
  serialized_end=388,
)

_GRAPESHOTCHUNKDATA.fields_by_name['upload_authentication'].message_type = pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__authentication__data__pb2._GRAPESHOTAUTHENTICATIONDATA
_GRAPESHOTCHUNKDATA.fields_by_name['delete_authentication'].message_type = pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__authentication__data__pb2._GRAPESHOTAUTHENTICATIONDATA
DESCRIPTOR.message_types_by_name['GrapeshotChunkData'] = _GRAPESHOTCHUNKDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GrapeshotChunkData = _reflection.GeneratedProtocolMessageType('GrapeshotChunkData', (_message.Message,), {
  'DESCRIPTOR' : _GRAPESHOTCHUNKDATA,
  '__module__' : 'pogoprotos.data.grapeshot.grapeshot_chunk_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.grapeshot.GrapeshotChunkData)
  })
_sym_db.RegisterMessage(GrapeshotChunkData)


# @@protoc_insertion_point(module_scope)
