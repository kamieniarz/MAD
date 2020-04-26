# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/quest_precondition.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import badge_type_pb2 as pogoprotos_dot_enums_dot_badge__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/quest_precondition.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n/pogoprotos/data/quests/quest_precondition.proto\x12\x16pogoprotos.data.quests\x1a!pogoprotos/enums/badge_type.proto\"\xed\n\n\x11QuestPrecondition\x12M\n\x04type\x18\x01 \x01(\x0e\x32?.pogoprotos.data.quests.QuestPrecondition.QuestPreconditionType\x12\x1b\n\x11quest_template_id\x18\x02 \x01(\tH\x00\x12@\n\x05level\x18\x03 \x01(\x0b\x32/.pogoprotos.data.quests.QuestPrecondition.LevelH\x00\x12@\n\x05medal\x18\x04 \x01(\x0b\x32/.pogoprotos.data.quests.QuestPrecondition.MedalH\x00\x12\x42\n\x06quests\x18\x05 \x01(\x0b\x32\x30.pogoprotos.data.quests.QuestPrecondition.QuestsH\x00\x12V\n\x11month_year_bucket\x18\x06 \x01(\x0b\x32\x39.pogoprotos.data.quests.QuestPrecondition.MonthYearBucketH\x00\x12@\n\x05group\x18\x07 \x01(\x0b\x32/.pogoprotos.data.quests.QuestPrecondition.GroupH\x00\x1al\n\x05Group\x12\x42\n\x04name\x18\x01 \x01(\x0e\x32\x34.pogoprotos.data.quests.QuestPrecondition.Group.Name\"\x1f\n\x04Name\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08GIOVANNI\x10\x01\x1a.\n\x0fMonthYearBucket\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x1a$\n\x06Quests\x12\x1a\n\x12quest_template_ids\x18\x01 \x03(\t\x1a\\\n\x05Level\x12\x44\n\x08operator\x18\x01 \x01(\x0e\x32\x32.pogoprotos.data.quests.QuestPrecondition.Operator\x12\r\n\x05level\x18\x02 \x01(\x05\x1a\x8c\x01\n\x05Medal\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.BadgeType\x12\x44\n\x08operator\x18\x02 \x01(\x0e\x32\x32.pogoprotos.data.quests.QuestPrecondition.Operator\x12\x12\n\nbadge_rank\x18\x03 \x01(\x05\"B\n\x08Operator\x12\t\n\x05UNSET\x10\x00\x12\n\n\x06\x45QUALS\x10\x01\x12\x10\n\x0cGREATER_THAN\x10\x02\x12\r\n\tLESS_THAN\x10\x03\"\x87\x03\n\x15QuestPreconditionType\x12\x1c\n\x18QUEST_PRECONDITION_UNSET\x10\x00\x12\x1c\n\x18QUEST_PRECONDITION_QUEST\x10\x01\x12\x1c\n\x18QUEST_PRECONDITION_LEVEL\x10\x02\x12\x1c\n\x18QUEST_PRECONDITION_MEDAL\x10\x03\x12\x1f\n\x1bQUEST_PRECONDITION_IS_MINOR\x10\x04\x12\'\n#QUEST_PRECONDITION_EXCLUSIVE_QUESTS\x10\x05\x12\x1c\n\x18QUEST_PRECONDITION_NEVER\x10\x06\x12\x30\n,QUEST_PRECONDITION_RECEIVED_ANY_LISTED_QUEST\x10\x07\x12(\n$QUEST_PRECONDITION_MONTH_YEAR_BUCKET\x10\x08\x12\x32\n.QUEST_PRECONDITION_EXCLUSIVE_IN_PROGRESS_GROUP\x10\tB\x0b\n\tConditionb\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_badge__type__pb2.DESCRIPTOR,])



_QUESTPRECONDITION_GROUP_NAME = _descriptor.EnumDescriptor(
  name='Name',
  full_name='pogoprotos.data.quests.QuestPrecondition.Group.Name',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIOVANNI', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=671,
  serialized_end=702,
)
_sym_db.RegisterEnumDescriptor(_QUESTPRECONDITION_GROUP_NAME)

_QUESTPRECONDITION_OPERATOR = _descriptor.EnumDescriptor(
  name='Operator',
  full_name='pogoprotos.data.quests.QuestPrecondition.Operator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQUALS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREATER_THAN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1027,
  serialized_end=1093,
)
_sym_db.RegisterEnumDescriptor(_QUESTPRECONDITION_OPERATOR)

_QUESTPRECONDITION_QUESTPRECONDITIONTYPE = _descriptor.EnumDescriptor(
  name='QuestPreconditionType',
  full_name='pogoprotos.data.quests.QuestPrecondition.QuestPreconditionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_QUEST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_LEVEL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_MEDAL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_IS_MINOR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_EXCLUSIVE_QUESTS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_NEVER', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_RECEIVED_ANY_LISTED_QUEST', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_MONTH_YEAR_BUCKET', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PRECONDITION_EXCLUSIVE_IN_PROGRESS_GROUP', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1096,
  serialized_end=1487,
)
_sym_db.RegisterEnumDescriptor(_QUESTPRECONDITION_QUESTPRECONDITIONTYPE)


_QUESTPRECONDITION_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='pogoprotos.data.quests.QuestPrecondition.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.data.quests.QuestPrecondition.Group.name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _QUESTPRECONDITION_GROUP_NAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=702,
)

_QUESTPRECONDITION_MONTHYEARBUCKET = _descriptor.Descriptor(
  name='MonthYearBucket',
  full_name='pogoprotos.data.quests.QuestPrecondition.MonthYearBucket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='pogoprotos.data.quests.QuestPrecondition.MonthYearBucket.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='pogoprotos.data.quests.QuestPrecondition.MonthYearBucket.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=704,
  serialized_end=750,
)

_QUESTPRECONDITION_QUESTS = _descriptor.Descriptor(
  name='Quests',
  full_name='pogoprotos.data.quests.QuestPrecondition.Quests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest_template_ids', full_name='pogoprotos.data.quests.QuestPrecondition.Quests.quest_template_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=752,
  serialized_end=788,
)

_QUESTPRECONDITION_LEVEL = _descriptor.Descriptor(
  name='Level',
  full_name='pogoprotos.data.quests.QuestPrecondition.Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operator', full_name='pogoprotos.data.quests.QuestPrecondition.Level.operator', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.data.quests.QuestPrecondition.Level.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=790,
  serialized_end=882,
)

_QUESTPRECONDITION_MEDAL = _descriptor.Descriptor(
  name='Medal',
  full_name='pogoprotos.data.quests.QuestPrecondition.Medal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.quests.QuestPrecondition.Medal.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='pogoprotos.data.quests.QuestPrecondition.Medal.operator', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='badge_rank', full_name='pogoprotos.data.quests.QuestPrecondition.Medal.badge_rank', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=885,
  serialized_end=1025,
)

_QUESTPRECONDITION = _descriptor.Descriptor(
  name='QuestPrecondition',
  full_name='pogoprotos.data.quests.QuestPrecondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.quests.QuestPrecondition.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quest_template_id', full_name='pogoprotos.data.quests.QuestPrecondition.quest_template_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.data.quests.QuestPrecondition.level', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='medal', full_name='pogoprotos.data.quests.QuestPrecondition.medal', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quests', full_name='pogoprotos.data.quests.QuestPrecondition.quests', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month_year_bucket', full_name='pogoprotos.data.quests.QuestPrecondition.month_year_bucket', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='pogoprotos.data.quests.QuestPrecondition.group', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_QUESTPRECONDITION_GROUP, _QUESTPRECONDITION_MONTHYEARBUCKET, _QUESTPRECONDITION_QUESTS, _QUESTPRECONDITION_LEVEL, _QUESTPRECONDITION_MEDAL, ],
  enum_types=[
    _QUESTPRECONDITION_OPERATOR,
    _QUESTPRECONDITION_QUESTPRECONDITIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Condition', full_name='pogoprotos.data.quests.QuestPrecondition.Condition',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=111,
  serialized_end=1500,
)

_QUESTPRECONDITION_GROUP.fields_by_name['name'].enum_type = _QUESTPRECONDITION_GROUP_NAME
_QUESTPRECONDITION_GROUP.containing_type = _QUESTPRECONDITION
_QUESTPRECONDITION_GROUP_NAME.containing_type = _QUESTPRECONDITION_GROUP
_QUESTPRECONDITION_MONTHYEARBUCKET.containing_type = _QUESTPRECONDITION
_QUESTPRECONDITION_QUESTS.containing_type = _QUESTPRECONDITION
_QUESTPRECONDITION_LEVEL.fields_by_name['operator'].enum_type = _QUESTPRECONDITION_OPERATOR
_QUESTPRECONDITION_LEVEL.containing_type = _QUESTPRECONDITION
_QUESTPRECONDITION_MEDAL.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_badge__type__pb2._BADGETYPE
_QUESTPRECONDITION_MEDAL.fields_by_name['operator'].enum_type = _QUESTPRECONDITION_OPERATOR
_QUESTPRECONDITION_MEDAL.containing_type = _QUESTPRECONDITION
_QUESTPRECONDITION.fields_by_name['type'].enum_type = _QUESTPRECONDITION_QUESTPRECONDITIONTYPE
_QUESTPRECONDITION.fields_by_name['level'].message_type = _QUESTPRECONDITION_LEVEL
_QUESTPRECONDITION.fields_by_name['medal'].message_type = _QUESTPRECONDITION_MEDAL
_QUESTPRECONDITION.fields_by_name['quests'].message_type = _QUESTPRECONDITION_QUESTS
_QUESTPRECONDITION.fields_by_name['month_year_bucket'].message_type = _QUESTPRECONDITION_MONTHYEARBUCKET
_QUESTPRECONDITION.fields_by_name['group'].message_type = _QUESTPRECONDITION_GROUP
_QUESTPRECONDITION_OPERATOR.containing_type = _QUESTPRECONDITION
_QUESTPRECONDITION_QUESTPRECONDITIONTYPE.containing_type = _QUESTPRECONDITION
_QUESTPRECONDITION.oneofs_by_name['Condition'].fields.append(
  _QUESTPRECONDITION.fields_by_name['quest_template_id'])
_QUESTPRECONDITION.fields_by_name['quest_template_id'].containing_oneof = _QUESTPRECONDITION.oneofs_by_name['Condition']
_QUESTPRECONDITION.oneofs_by_name['Condition'].fields.append(
  _QUESTPRECONDITION.fields_by_name['level'])
_QUESTPRECONDITION.fields_by_name['level'].containing_oneof = _QUESTPRECONDITION.oneofs_by_name['Condition']
_QUESTPRECONDITION.oneofs_by_name['Condition'].fields.append(
  _QUESTPRECONDITION.fields_by_name['medal'])
_QUESTPRECONDITION.fields_by_name['medal'].containing_oneof = _QUESTPRECONDITION.oneofs_by_name['Condition']
_QUESTPRECONDITION.oneofs_by_name['Condition'].fields.append(
  _QUESTPRECONDITION.fields_by_name['quests'])
_QUESTPRECONDITION.fields_by_name['quests'].containing_oneof = _QUESTPRECONDITION.oneofs_by_name['Condition']
_QUESTPRECONDITION.oneofs_by_name['Condition'].fields.append(
  _QUESTPRECONDITION.fields_by_name['month_year_bucket'])
_QUESTPRECONDITION.fields_by_name['month_year_bucket'].containing_oneof = _QUESTPRECONDITION.oneofs_by_name['Condition']
_QUESTPRECONDITION.oneofs_by_name['Condition'].fields.append(
  _QUESTPRECONDITION.fields_by_name['group'])
_QUESTPRECONDITION.fields_by_name['group'].containing_oneof = _QUESTPRECONDITION.oneofs_by_name['Condition']
DESCRIPTOR.message_types_by_name['QuestPrecondition'] = _QUESTPRECONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestPrecondition = _reflection.GeneratedProtocolMessageType('QuestPrecondition', (_message.Message,), {

  'Group' : _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), {
    'DESCRIPTOR' : _QUESTPRECONDITION_GROUP,
    '__module__' : 'pogoprotos.data.quests.quest_precondition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestPrecondition.Group)
    })
  ,

  'MonthYearBucket' : _reflection.GeneratedProtocolMessageType('MonthYearBucket', (_message.Message,), {
    'DESCRIPTOR' : _QUESTPRECONDITION_MONTHYEARBUCKET,
    '__module__' : 'pogoprotos.data.quests.quest_precondition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestPrecondition.MonthYearBucket)
    })
  ,

  'Quests' : _reflection.GeneratedProtocolMessageType('Quests', (_message.Message,), {
    'DESCRIPTOR' : _QUESTPRECONDITION_QUESTS,
    '__module__' : 'pogoprotos.data.quests.quest_precondition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestPrecondition.Quests)
    })
  ,

  'Level' : _reflection.GeneratedProtocolMessageType('Level', (_message.Message,), {
    'DESCRIPTOR' : _QUESTPRECONDITION_LEVEL,
    '__module__' : 'pogoprotos.data.quests.quest_precondition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestPrecondition.Level)
    })
  ,

  'Medal' : _reflection.GeneratedProtocolMessageType('Medal', (_message.Message,), {
    'DESCRIPTOR' : _QUESTPRECONDITION_MEDAL,
    '__module__' : 'pogoprotos.data.quests.quest_precondition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestPrecondition.Medal)
    })
  ,
  'DESCRIPTOR' : _QUESTPRECONDITION,
  '__module__' : 'pogoprotos.data.quests.quest_precondition_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestPrecondition)
  })
_sym_db.RegisterMessage(QuestPrecondition)
_sym_db.RegisterMessage(QuestPrecondition.Group)
_sym_db.RegisterMessage(QuestPrecondition.MonthYearBucket)
_sym_db.RegisterMessage(QuestPrecondition.Quests)
_sym_db.RegisterMessage(QuestPrecondition.Level)
_sym_db.RegisterMessage(QuestPrecondition.Medal)


# @@protoc_insertion_point(module_scope)
