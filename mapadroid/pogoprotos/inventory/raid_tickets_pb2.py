# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/raid_tickets.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import raid_ticket_pb2 as pogoprotos_dot_inventory_dot_raid__ticket__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/raid_tickets.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\'pogoprotos/inventory/raid_tickets.proto\x12\x14pogoprotos.inventory\x1a&pogoprotos/inventory/raid_ticket.proto\"D\n\x0bRaidTickets\x12\x35\n\x0braid_ticket\x18\x01 \x03(\x0b\x32 .pogoprotos.inventory.RaidTicketb\x06proto3'
  ,
  dependencies=[pogoprotos_dot_inventory_dot_raid__ticket__pb2.DESCRIPTOR,])




_RAIDTICKETS = _descriptor.Descriptor(
  name='RaidTickets',
  full_name='pogoprotos.inventory.RaidTickets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raid_ticket', full_name='pogoprotos.inventory.RaidTickets.raid_ticket', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=105,
  serialized_end=173,
)

_RAIDTICKETS.fields_by_name['raid_ticket'].message_type = pogoprotos_dot_inventory_dot_raid__ticket__pb2._RAIDTICKET
DESCRIPTOR.message_types_by_name['RaidTickets'] = _RAIDTICKETS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidTickets = _reflection.GeneratedProtocolMessageType('RaidTickets', (_message.Message,), {
  'DESCRIPTOR' : _RAIDTICKETS,
  '__module__' : 'pogoprotos.inventory.raid_tickets_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.RaidTickets)
  })
_sym_db.RegisterMessage(RaidTickets)


# @@protoc_insertion_point(module_scope)
