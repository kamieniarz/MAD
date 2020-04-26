# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/game_master_decoder.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.responses import download_item_templates_response_pb2 as pogoprotos_dot_networking_dot_responses_dot_download__item__templates__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/game_master_decoder.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n)pogoprotos/data/game_master_decoder.proto\x12\x0fpogoprotos.data\x1a\x46pogoprotos/networking/responses/download_item_templates_response.proto\"\x8d\x04\n\x11GameMasterDecoder\x12\x39\n\x06result\x18\x01 \x01(\x0e\x32).pogoprotos.data.GameMasterDecoder.Result\x12M\n\x08template\x18\x02 \x03(\x0b\x32;.pogoprotos.data.GameMasterDecoder.ClientGameMasterTemplate\x12\x18\n\x10\x64\x65leted_template\x18\x03 \x03(\t\x12\x10\n\x08\x62\x61tch_id\x18\x04 \x01(\x04\x12\x13\n\x0bpage_offset\x18\x05 \x01(\x05\x12\x15\n\rexperiment_id\x18\x06 \x03(\x05\x1a\x96\x01\n\x18\x43lientGameMasterTemplate\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\x12\x65\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32W.pogoprotos.networking.responses.DownloadItemTemplatesResponse.GameMasterClientTemplate\"}\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x43OMPLETE\x10\x01\x12\x10\n\x0cMORE_RESULTS\x10\x02\x12\x15\n\x11\x42\x41TCH_ID_NOT_LIVE\x10\x03\x12\x1a\n\x16INVALID_BASIS_BATCH_ID\x10\x04\x12\x15\n\x11WRONG_EXPERIMENTS\x10\x05\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_networking_dot_responses_dot_download__item__templates__response__pb2.DESCRIPTOR,])



_GAMEMASTERDECODER_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.GameMasterDecoder.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MORE_RESULTS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATCH_ID_NOT_LIVE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_BASIS_BATCH_ID', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_EXPERIMENTS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=535,
  serialized_end=660,
)
_sym_db.RegisterEnumDescriptor(_GAMEMASTERDECODER_RESULT)


_GAMEMASTERDECODER_CLIENTGAMEMASTERTEMPLATE = _descriptor.Descriptor(
  name='ClientGameMasterTemplate',
  full_name='pogoprotos.data.GameMasterDecoder.ClientGameMasterTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='pogoprotos.data.GameMasterDecoder.ClientGameMasterTemplate.template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pogoprotos.data.GameMasterDecoder.ClientGameMasterTemplate.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=383,
  serialized_end=533,
)

_GAMEMASTERDECODER = _descriptor.Descriptor(
  name='GameMasterDecoder',
  full_name='pogoprotos.data.GameMasterDecoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.GameMasterDecoder.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template', full_name='pogoprotos.data.GameMasterDecoder.template', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted_template', full_name='pogoprotos.data.GameMasterDecoder.deleted_template', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='pogoprotos.data.GameMasterDecoder.batch_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_offset', full_name='pogoprotos.data.GameMasterDecoder.page_offset', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='pogoprotos.data.GameMasterDecoder.experiment_id', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GAMEMASTERDECODER_CLIENTGAMEMASTERTEMPLATE, ],
  enum_types=[
    _GAMEMASTERDECODER_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=660,
)

_GAMEMASTERDECODER_CLIENTGAMEMASTERTEMPLATE.fields_by_name['data'].message_type = pogoprotos_dot_networking_dot_responses_dot_download__item__templates__response__pb2._DOWNLOADITEMTEMPLATESRESPONSE_GAMEMASTERCLIENTTEMPLATE
_GAMEMASTERDECODER_CLIENTGAMEMASTERTEMPLATE.containing_type = _GAMEMASTERDECODER
_GAMEMASTERDECODER.fields_by_name['result'].enum_type = _GAMEMASTERDECODER_RESULT
_GAMEMASTERDECODER.fields_by_name['template'].message_type = _GAMEMASTERDECODER_CLIENTGAMEMASTERTEMPLATE
_GAMEMASTERDECODER_RESULT.containing_type = _GAMEMASTERDECODER
DESCRIPTOR.message_types_by_name['GameMasterDecoder'] = _GAMEMASTERDECODER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameMasterDecoder = _reflection.GeneratedProtocolMessageType('GameMasterDecoder', (_message.Message,), {

  'ClientGameMasterTemplate' : _reflection.GeneratedProtocolMessageType('ClientGameMasterTemplate', (_message.Message,), {
    'DESCRIPTOR' : _GAMEMASTERDECODER_CLIENTGAMEMASTERTEMPLATE,
    '__module__' : 'pogoprotos.data.game_master_decoder_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.GameMasterDecoder.ClientGameMasterTemplate)
    })
  ,
  'DESCRIPTOR' : _GAMEMASTERDECODER,
  '__module__' : 'pogoprotos.data.game_master_decoder_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.GameMasterDecoder)
  })
_sym_db.RegisterMessage(GameMasterDecoder)
_sym_db.RegisterMessage(GameMasterDecoder.ClientGameMasterTemplate)


# @@protoc_insertion_point(module_scope)
