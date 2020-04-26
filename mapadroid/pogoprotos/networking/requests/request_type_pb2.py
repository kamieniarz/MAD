# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/request_type.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/request_type.proto',
  package='pogoprotos.networking.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n1pogoprotos/networking/requests/request_type.proto\x12\x1epogoprotos.networking.requests*\xc1#\n\x0bRequestType\x12\x10\n\x0cMETHOD_UNSET\x10\x00\x12\x0e\n\nGET_PLAYER\x10\x02\x12\x16\n\x12GET_HOLO_INVENTORY\x10\x04\x12\x15\n\x11\x44OWNLOAD_SETTINGS\x10\x05\x12\x1b\n\x17\x44OWNLOAD_ITEM_TEMPLATES\x10\x06\x12\"\n\x1e\x44OWNLOAD_REMOTE_CONFIG_VERSION\x10\x07\x12\x1e\n\x1aREGISTER_BACKGROUND_DEVICE\x10\x08\x12\x12\n\x0eGET_PLAYER_DAY\x10\t\x12\x1a\n\x16\x41\x43KNOWLEDGE_PUNISHMENT\x10\n\x12\x13\n\x0fGET_SERVER_TIME\x10\x0b\x12\x12\n\x0eGET_LOCAL_TIME\x10\x0c\x12\x0f\n\x0b\x46ORT_SEARCH\x10\x65\x12\r\n\tENCOUNTER\x10\x66\x12\x11\n\rCATCH_POKEMON\x10g\x12\x10\n\x0c\x46ORT_DETAILS\x10h\x12\x13\n\x0fGET_MAP_OBJECTS\x10j\x12\x17\n\x13\x46ORT_DEPLOY_POKEMON\x10n\x12\x17\n\x13\x46ORT_RECALL_POKEMON\x10o\x12\x13\n\x0fRELEASE_POKEMON\x10p\x12\x13\n\x0fUSE_ITEM_POTION\x10q\x12\x14\n\x10USE_ITEM_CAPTURE\x10r\x12\x11\n\rUSE_ITEM_FLEE\x10s\x12\x13\n\x0fUSE_ITEM_REVIVE\x10t\x12\x16\n\x12GET_PLAYER_PROFILE\x10y\x12\x12\n\x0e\x45VOLVE_POKEMON\x10}\x12\x14\n\x10GET_HATCHED_EGGS\x10~\x12\x1f\n\x1b\x45NCOUNTER_TUTORIAL_COMPLETE\x10\x7f\x12\x15\n\x10LEVEL_UP_REWARDS\x10\x80\x01\x12\x19\n\x14\x43HECK_AWARDED_BADGES\x10\x81\x01\x12\x11\n\x0cUSE_ITEM_GYM\x10\x85\x01\x12\x14\n\x0fGET_GYM_DETAILS\x10\x86\x01\x12\x15\n\x10START_GYM_BATTLE\x10\x87\x01\x12\x0f\n\nATTACK_GYM\x10\x88\x01\x12\x1b\n\x16RECYCLE_INVENTORY_ITEM\x10\x89\x01\x12\x18\n\x13\x43OLLECT_DAILY_BONUS\x10\x8a\x01\x12\x16\n\x11USE_ITEM_XP_BOOST\x10\x8b\x01\x12\x1b\n\x16USE_ITEM_EGG_INCUBATOR\x10\x8c\x01\x12\x10\n\x0bUSE_INCENSE\x10\x8d\x01\x12\x18\n\x13GET_INCENSE_POKEMON\x10\x8e\x01\x12\x16\n\x11INCENSE_ENCOUNTER\x10\x8f\x01\x12\x16\n\x11\x41\x44\x44_FORT_MODIFIER\x10\x90\x01\x12\x13\n\x0e\x44ISK_ENCOUNTER\x10\x91\x01\x12!\n\x1c\x43OLLECT_DAILY_DEFENDER_BONUS\x10\x92\x01\x12\x14\n\x0fUPGRADE_POKEMON\x10\x93\x01\x12\x19\n\x14SET_FAVORITE_POKEMON\x10\x94\x01\x12\x15\n\x10NICKNAME_POKEMON\x10\x95\x01\x12\x10\n\x0b\x45QUIP_BADGE\x10\x96\x01\x12\x19\n\x14SET_CONTACT_SETTINGS\x10\x97\x01\x12\x16\n\x11SET_BUDDY_POKEMON\x10\x98\x01\x12\x15\n\x10GET_BUDDY_WALKED\x10\x99\x01\x12\x17\n\x12USE_ITEM_ENCOUNTER\x10\x9a\x01\x12\x0f\n\nGYM_DEPLOY\x10\x9b\x01\x12\x11\n\x0cGYM_GET_INFO\x10\x9c\x01\x12\x16\n\x11GYM_START_SESSION\x10\x9d\x01\x12\x16\n\x11GYM_BATTLE_ATTACK\x10\x9e\x01\x12\x0f\n\nJOIN_LOBBY\x10\x9f\x01\x12\x10\n\x0bLEAVE_LOBBY\x10\xa0\x01\x12\x19\n\x14SET_LOBBY_VISIBILITY\x10\xa1\x01\x12\x16\n\x11SET_LOBBY_POKEMON\x10\xa2\x01\x12\x15\n\x10GET_RAID_DETAILS\x10\xa3\x01\x12\x15\n\x10GYM_FEED_POKEMON\x10\xa4\x01\x12\x16\n\x11START_RAID_BATTLE\x10\xa5\x01\x12\x10\n\x0b\x41TTACK_RAID\x10\xa6\x01\x12\x13\n\x0e\x41WARD_POKECOIN\x10\xa7\x01\x12\x1c\n\x17USE_ITEM_STARDUST_BOOST\x10\xa8\x01\x12\x14\n\x0fREASSIGN_PLAYER\x10\xa9\x01\x12\x18\n\x13REDEEM_POI_PASSCODE\x10\xaa\x01\x12\x15\n\x10GET_ASSET_DIGEST\x10\xac\x02\x12\x16\n\x11GET_DOWNLOAD_URLS\x10\xad\x02\x12\x16\n\x11GET_ASSET_VERSION\x10\xae\x02\x12\x13\n\x0e\x43LAIM_CODENAME\x10\x93\x03\x12\x0f\n\nSET_AVATAR\x10\x94\x03\x12\x14\n\x0fSET_PLAYER_TEAM\x10\x95\x03\x12\x1b\n\x16MARK_TUTORIAL_COMPLETE\x10\x96\x03\x12\x1f\n\x1aUPDATE_PERFORMANCE_METRICS\x10\x97\x03\x12\x14\n\x0f\x43HECK_CHALLENGE\x10\xd8\x04\x12\x15\n\x10VERIFY_CHALLENGE\x10\xd9\x04\x12\t\n\x04\x45\x43HO\x10\x9a\x05\x12\x17\n\x12SFIDA_REGISTRATION\x10\xa0\x06\x12\x15\n\x10SFIDA_ACTION_LOG\x10\xa1\x06\x12\x18\n\x13SFIDA_CERTIFICATION\x10\xa2\x06\x12\x11\n\x0cSFIDA_UPDATE\x10\xa3\x06\x12\x11\n\x0cSFIDA_ACTION\x10\xa4\x06\x12\x11\n\x0cSFIDA_DOWSER\x10\xa5\x06\x12\x12\n\rSFIDA_CAPTURE\x10\xa6\x06\x12\x1f\n\x1aLIST_AVATAR_CUSTOMIZATIONS\x10\xa7\x06\x12\x1e\n\x19SET_AVATAR_ITEM_AS_VIEWED\x10\xa8\x06\x12\x0e\n\tGET_INBOX\x10\xa9\x06\x12\x14\n\x0fLIST_GYM_BADGES\x10\xab\x06\x12\x1a\n\x15GET_GYM_BADGE_DETAILS\x10\xac\x06\x12\x19\n\x14USE_ITEM_MOVE_REROLL\x10\xad\x06\x12\x18\n\x13USE_ITEM_RARE_CANDY\x10\xae\x06\x12\x1b\n\x16\x41WARD_FREE_RAID_TICKET\x10\xaf\x06\x12\x13\n\x0e\x46\x45TCH_ALL_NEWS\x10\xb0\x06\x12\x1b\n\x16MARK_READ_NEWS_ARTICLE\x10\xb1\x06\x12\x1c\n\x17GET_PLAYER_DISPLAY_INFO\x10\xb2\x06\x12\x1d\n\x18\x42\x45LUGA_TRANSACTION_START\x10\xb3\x06\x12 \n\x1b\x42\x45LUGA_TRANSACTION_COMPLETE\x10\xb4\x06\x12\x13\n\x0eGET_NEW_QUESTS\x10\x84\x07\x12\x16\n\x11GET_QUEST_DETAILS\x10\x85\x07\x12\x13\n\x0e\x43OMPLETE_QUEST\x10\x86\x07\x12\x11\n\x0cREMOVE_QUEST\x10\x87\x07\x12\x14\n\x0fQUEST_ENCOUNTER\x10\x88\x07\x12\x1e\n\x19\x43OMPLETE_QUEST_STAMP_CARD\x10\x89\x07\x12\x0e\n\tSEND_GIFT\x10\xb6\x07\x12\x0e\n\tOPEN_GIFT\x10\xb7\x07\x12\x11\n\x0cGIFT_DETAILS\x10\xb8\x07\x12\x10\n\x0b\x44\x45LETE_GIFT\x10\xb9\x07\x12\x19\n\x14SAVE_PLAYER_SNAPSHOT\x10\xba\x07\x12%\n GET_FRIENDSHIP_MILESTONE_REWARDS\x10\xbb\x07\x12\x14\n\x0f\x43HECK_SEND_GIFT\x10\xbc\x07\x12\x18\n\x13SET_FRIEND_NICKNAME\x10\xbd\x07\x12\x1f\n\x1a\x44\x45LETE_GIFT_FROM_INVENTORY\x10\xbe\x07\x12 \n\x1bSAVE_SOCIAL_PLAYER_SETTINGS\x10\xbf\x07\x12\x17\n\x12SHARE_EX_RAID_PASS\x10\xc0\x07\x12\x1d\n\x18\x43HECK_SHARE_EX_RAID_PASS\x10\xc1\x07\x12 \n\x1b\x44\x45\x43LINE_SHARED_EX_RAID_PASS\x10\xc2\x07\x12\x11\n\x0cOPEN_TRADING\x10\xca\x07\x12\x13\n\x0eUPDATE_TRADING\x10\xcb\x07\x12\x14\n\x0f\x43ONFIRM_TRADING\x10\xcc\x07\x12\x13\n\x0e\x43\x41NCEL_TRADING\x10\xcd\x07\x12\x10\n\x0bGET_TRADING\x10\xce\x07\x12\x18\n\x13GET_FITNESS_REWARDS\x10\xd4\x07\x12\x1e\n\x19GET_COMBAT_PLAYER_PROFILE\x10\xde\x07\x12!\n\x1cGENERATE_COMBAT_CHALLENGE_ID\x10\xdf\x07\x12\x1c\n\x17\x43REATE_COMBAT_CHALLENGE\x10\xe0\x07\x12\x1a\n\x15OPEN_COMBAT_CHALLENGE\x10\xe1\x07\x12\x19\n\x14GET_COMBAT_CHALLENGE\x10\xe2\x07\x12\x1c\n\x17\x41\x43\x43\x45PT_COMBAT_CHALLENGE\x10\xe3\x07\x12\x1d\n\x18\x44\x45\x43LINE_COMBAT_CHALLENGE\x10\xe4\x07\x12\x1c\n\x17\x43\x41NCEL_COMBAT_CHALLENGE\x10\xe5\x07\x12%\n SUBMIT_COMBAT_CHALLENGE_POKEMONS\x10\xe6\x07\x12#\n\x1eSAVE_COMBAT_PLAYER_PREFERENCES\x10\xe7\x07\x12\x18\n\x13OPEN_COMBAT_SESSION\x10\xe8\x07\x12\x12\n\rUPDATE_COMBAT\x10\xe9\x07\x12\x10\n\x0bQUIT_COMBAT\x10\xea\x07\x12\x17\n\x12GET_COMBAT_RESULTS\x10\xeb\x07\x12\x18\n\x13UNLOCK_SPECIAL_MOVE\x10\xec\x07\x12\x1b\n\x16GET_NPC_COMBAT_REWARDS\x10\xed\x07\x12\x1a\n\x15\x43OMBAT_FRIEND_REQUEST\x10\xee\x07\x12\x1c\n\x17OPEN_NPC_COMBAT_SESSION\x10\xef\x07\x12\x1a\n\x15START_TUTORIAL_ACTION\x10\xf0\x07\x12\x1c\n\x17GET_TUTORIAL_EGG_ACTION\x10\xf1\x07\x12\x0f\n\nSEND_PROBE\x10\xfc\x07\x12\x0f\n\nPROBE_DATA\x10\xfd\x07\x12\x10\n\x0b\x43OMBAT_DATA\x10\xfe\x07\x12\x1a\n\x15\x43OMBAT_CHALLENGE_DATA\x10\xff\x07\x12\x14\n\x0f\x43HECK_PHOTOBOMB\x10\xcd\x08\x12\x16\n\x11\x43ONFIRM_PHOTOBOMB\x10\xce\x08\x12\x12\n\rGET_PHOTOBOMB\x10\xcf\x08\x12\x18\n\x13\x45NCOUNTER_PHOTOBOMB\x10\xd0\x08\x12#\n\x1eGET_SIGNED_GMAP_URL_DEPRECATED\x10\xd1\x08\x12\x10\n\x0b\x43HANGE_TEAM\x10\xd2\x08\x12\x12\n\rGET_WEB_TOKEN\x10\xd3\x08\x12\x1e\n\x19\x43OMPLETE_SNAPSHOT_SESSION\x10\xd6\x08\x12\x13\n\x0eSTART_INCIDENT\x10\xb0\t\x12\x1f\n\x1aINVASION_COMPLETE_DIALOGUE\x10\xb1\t\x12!\n\x1cINVASION_OPEN_COMBAT_SESSION\x10\xb2\t\x12\x1b\n\x16INVASION_BATTLE_UPDATE\x10\xb3\t\x12\x17\n\x12INVASION_ENCOUNTER\x10\xb4\t\x12\x13\n\x0ePURIFY_POKEMON\x10\xb5\t\x12 \n\x1bVS_SEEKER_START_MATCHMAKING\x10\x94\n\x12\x17\n\x12\x43\x41NCEL_MATCHMAKING\x10\x95\n\x12\x1b\n\x16GET_MATCHMAKING_STATUS\x10\x96\n\x12,\n\'COMPLETE_VS_SEEKER_AND_RESTART_CHARGING\x10\x97\n\x12\x19\n\x14GET_VS_SEEKER_STATUS\x10\x98\n\x12.\n)COMPLETE_COMBAT_COMPETITIVE_SEASON_ACTION\x10\x99\n\x12\x1c\n\x17\x43LAIM_VS_SEEKER_REWARDS\x10\x9a\n\x12\x1f\n\x1aVS_SEEKER_REWARD_ENCOUNTER\x10\x9b\n\x12\x17\n\x12\x41\x43TIVATE_VS_SEEKER\x10\x9c\n\x12\x12\n\rGET_BUDDY_MAP\x10\xc6\n\x12\x14\n\x0fGET_BUDDY_STATS\x10\xc7\n\x12\x0f\n\nFEED_BUDDY\x10\xc8\n\x12\x14\n\x0fOPEN_BUDDY_GIFT\x10\xc9\n\x12\x0e\n\tPET_BUDDY\x10\xca\n\x12\x16\n\x11GET_BUDDY_HISTORY\x10\xcb\n\x12%\n CREATE_BUDDY_MUTLIPLAYER_SESSION\x10\xb0\x0b\x12#\n\x1eJOIN_BUDDY_MULTIPLAYER_SESSION\x10\xb1\x0b\x12$\n\x1fLEAVE_BUDDY_MULTIPLAYER_SESSION\x10\xb2\x0b\x12\x13\n\x0eGET_TODAY_VIEW\x10\xdd\x0b\x12\x15\n\x10REMOTE_GIFT_PING\x10\xdf\x0b\x12\x19\n\x14SEND_RAID_INVITATION\x10\xe0\x0b\x62\x06proto3'
)

_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='pogoprotos.networking.requests.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METHOD_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PLAYER', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_HOLO_INVENTORY', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_SETTINGS', index=3, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_ITEM_TEMPLATES', index=4, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_REMOTE_CONFIG_VERSION', index=5, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_BACKGROUND_DEVICE', index=6, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PLAYER_DAY', index=7, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACKNOWLEDGE_PUNISHMENT', index=8, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SERVER_TIME', index=9, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_LOCAL_TIME', index=10, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_SEARCH', index=11, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER', index=12, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATCH_POKEMON', index=13, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_DETAILS', index=14, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_MAP_OBJECTS', index=15, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_DEPLOY_POKEMON', index=16, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_RECALL_POKEMON', index=17, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELEASE_POKEMON', index=18, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_POTION', index=19, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_CAPTURE', index=20, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_FLEE', index=21, number=115,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_REVIVE', index=22, number=116,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PLAYER_PROFILE', index=23, number=121,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVOLVE_POKEMON', index=24, number=125,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_HATCHED_EGGS', index=25, number=126,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_TUTORIAL_COMPLETE', index=26, number=127,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_UP_REWARDS', index=27, number=128,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_AWARDED_BADGES', index=28, number=129,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_GYM', index=29, number=133,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_GYM_DETAILS', index=30, number=134,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_GYM_BATTLE', index=31, number=135,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTACK_GYM', index=32, number=136,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECYCLE_INVENTORY_ITEM', index=33, number=137,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECT_DAILY_BONUS', index=34, number=138,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_XP_BOOST', index=35, number=139,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_EGG_INCUBATOR', index=36, number=140,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_INCENSE', index=37, number=141,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INCENSE_POKEMON', index=38, number=142,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCENSE_ENCOUNTER', index=39, number=143,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_FORT_MODIFIER', index=40, number=144,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISK_ENCOUNTER', index=41, number=145,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECT_DAILY_DEFENDER_BONUS', index=42, number=146,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPGRADE_POKEMON', index=43, number=147,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_FAVORITE_POKEMON', index=44, number=148,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NICKNAME_POKEMON', index=45, number=149,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQUIP_BADGE', index=46, number=150,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_CONTACT_SETTINGS', index=47, number=151,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_BUDDY_POKEMON', index=48, number=152,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_BUDDY_WALKED', index=49, number=153,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_ENCOUNTER', index=50, number=154,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_DEPLOY', index=51, number=155,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_GET_INFO', index=52, number=156,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_START_SESSION', index=53, number=157,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BATTLE_ATTACK', index=54, number=158,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN_LOBBY', index=55, number=159,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAVE_LOBBY', index=56, number=160,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_LOBBY_VISIBILITY', index=57, number=161,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_LOBBY_POKEMON', index=58, number=162,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_RAID_DETAILS', index=59, number=163,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_FEED_POKEMON', index=60, number=164,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_RAID_BATTLE', index=61, number=165,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTACK_RAID', index=62, number=166,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AWARD_POKECOIN', index=63, number=167,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_STARDUST_BOOST', index=64, number=168,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REASSIGN_PLAYER', index=65, number=169,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_POI_PASSCODE', index=66, number=170,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_ASSET_DIGEST', index=67, number=300,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_DOWNLOAD_URLS', index=68, number=301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_ASSET_VERSION', index=69, number=302,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_CODENAME', index=70, number=403,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_AVATAR', index=71, number=404,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_PLAYER_TEAM', index=72, number=405,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARK_TUTORIAL_COMPLETE', index=73, number=406,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_PERFORMANCE_METRICS', index=74, number=407,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_CHALLENGE', index=75, number=600,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFY_CHALLENGE', index=76, number=601,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECHO', index=77, number=666,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_REGISTRATION', index=78, number=800,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_ACTION_LOG', index=79, number=801,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_CERTIFICATION', index=80, number=802,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_UPDATE', index=81, number=803,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_ACTION', index=82, number=804,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_DOWSER', index=83, number=805,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_CAPTURE', index=84, number=806,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_AVATAR_CUSTOMIZATIONS', index=85, number=807,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_AVATAR_ITEM_AS_VIEWED', index=86, number=808,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INBOX', index=87, number=809,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_GYM_BADGES', index=88, number=811,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_GYM_BADGE_DETAILS', index=89, number=812,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_MOVE_REROLL', index=90, number=813,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_RARE_CANDY', index=91, number=814,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AWARD_FREE_RAID_TICKET', index=92, number=815,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FETCH_ALL_NEWS', index=93, number=816,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARK_READ_NEWS_ARTICLE', index=94, number=817,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PLAYER_DISPLAY_INFO', index=95, number=818,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BELUGA_TRANSACTION_START', index=96, number=819,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BELUGA_TRANSACTION_COMPLETE', index=97, number=820,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_NEW_QUESTS', index=98, number=900,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_QUEST_DETAILS', index=99, number=901,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE_QUEST', index=100, number=902,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_QUEST', index=101, number=903,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_ENCOUNTER', index=102, number=904,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE_QUEST_STAMP_CARD', index=103, number=905,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_GIFT', index=104, number=950,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_GIFT', index=105, number=951,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIFT_DETAILS', index=106, number=952,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_GIFT', index=107, number=953,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAVE_PLAYER_SNAPSHOT', index=108, number=954,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FRIENDSHIP_MILESTONE_REWARDS', index=109, number=955,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_SEND_GIFT', index=110, number=956,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_FRIEND_NICKNAME', index=111, number=957,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_GIFT_FROM_INVENTORY', index=112, number=958,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAVE_SOCIAL_PLAYER_SETTINGS', index=113, number=959,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_EX_RAID_PASS', index=114, number=960,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_SHARE_EX_RAID_PASS', index=115, number=961,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLINE_SHARED_EX_RAID_PASS', index=116, number=962,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_TRADING', index=117, number=970,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_TRADING', index=118, number=971,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_TRADING', index=119, number=972,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_TRADING', index=120, number=973,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_TRADING', index=121, number=974,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FITNESS_REWARDS', index=122, number=980,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_COMBAT_PLAYER_PROFILE', index=123, number=990,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERATE_COMBAT_CHALLENGE_ID', index=124, number=991,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_COMBAT_CHALLENGE', index=125, number=992,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_COMBAT_CHALLENGE', index=126, number=993,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_COMBAT_CHALLENGE', index=127, number=994,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEPT_COMBAT_CHALLENGE', index=128, number=995,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLINE_COMBAT_CHALLENGE', index=129, number=996,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_COMBAT_CHALLENGE', index=130, number=997,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_COMBAT_CHALLENGE_POKEMONS', index=131, number=998,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAVE_COMBAT_PLAYER_PREFERENCES', index=132, number=999,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_COMBAT_SESSION', index=133, number=1000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_COMBAT', index=134, number=1001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUIT_COMBAT', index=135, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_COMBAT_RESULTS', index=136, number=1003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNLOCK_SPECIAL_MOVE', index=137, number=1004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_NPC_COMBAT_REWARDS', index=138, number=1005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_FRIEND_REQUEST', index=139, number=1006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_NPC_COMBAT_SESSION', index=140, number=1007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_TUTORIAL_ACTION', index=141, number=1008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_TUTORIAL_EGG_ACTION', index=142, number=1009,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_PROBE', index=143, number=1020,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROBE_DATA', index=144, number=1021,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_DATA', index=145, number=1022,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_CHALLENGE_DATA', index=146, number=1023,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_PHOTOBOMB', index=147, number=1101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_PHOTOBOMB', index=148, number=1102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PHOTOBOMB', index=149, number=1103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_PHOTOBOMB', index=150, number=1104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SIGNED_GMAP_URL_DEPRECATED', index=151, number=1105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_TEAM', index=152, number=1106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_WEB_TOKEN', index=153, number=1107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE_SNAPSHOT_SESSION', index=154, number=1110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_INCIDENT', index=155, number=1200,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_COMPLETE_DIALOGUE', index=156, number=1201,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_OPEN_COMBAT_SESSION', index=157, number=1202,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_BATTLE_UPDATE', index=158, number=1203,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_ENCOUNTER', index=159, number=1204,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURIFY_POKEMON', index=160, number=1205,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VS_SEEKER_START_MATCHMAKING', index=161, number=1300,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_MATCHMAKING', index=162, number=1301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_MATCHMAKING_STATUS', index=163, number=1302,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE_VS_SEEKER_AND_RESTART_CHARGING', index=164, number=1303,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_VS_SEEKER_STATUS', index=165, number=1304,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE_COMBAT_COMPETITIVE_SEASON_ACTION', index=166, number=1305,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_VS_SEEKER_REWARDS', index=167, number=1306,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VS_SEEKER_REWARD_ENCOUNTER', index=168, number=1307,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVATE_VS_SEEKER', index=169, number=1308,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_BUDDY_MAP', index=170, number=1350,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_BUDDY_STATS', index=171, number=1351,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_BUDDY', index=172, number=1352,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_BUDDY_GIFT', index=173, number=1353,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PET_BUDDY', index=174, number=1354,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_BUDDY_HISTORY', index=175, number=1355,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_BUDDY_MUTLIPLAYER_SESSION', index=176, number=1456,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN_BUDDY_MULTIPLAYER_SESSION', index=177, number=1457,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAVE_BUDDY_MULTIPLAYER_SESSION', index=178, number=1458,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_TODAY_VIEW', index=179, number=1501,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_GIFT_PING', index=180, number=1503,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_RAID_INVITATION', index=181, number=1504,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=86,
  serialized_end=4631,
)
_sym_db.RegisterEnumDescriptor(_REQUESTTYPE)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
METHOD_UNSET = 0
GET_PLAYER = 2
GET_HOLO_INVENTORY = 4
DOWNLOAD_SETTINGS = 5
DOWNLOAD_ITEM_TEMPLATES = 6
DOWNLOAD_REMOTE_CONFIG_VERSION = 7
REGISTER_BACKGROUND_DEVICE = 8
GET_PLAYER_DAY = 9
ACKNOWLEDGE_PUNISHMENT = 10
GET_SERVER_TIME = 11
GET_LOCAL_TIME = 12
FORT_SEARCH = 101
ENCOUNTER = 102
CATCH_POKEMON = 103
FORT_DETAILS = 104
GET_MAP_OBJECTS = 106
FORT_DEPLOY_POKEMON = 110
FORT_RECALL_POKEMON = 111
RELEASE_POKEMON = 112
USE_ITEM_POTION = 113
USE_ITEM_CAPTURE = 114
USE_ITEM_FLEE = 115
USE_ITEM_REVIVE = 116
GET_PLAYER_PROFILE = 121
EVOLVE_POKEMON = 125
GET_HATCHED_EGGS = 126
ENCOUNTER_TUTORIAL_COMPLETE = 127
LEVEL_UP_REWARDS = 128
CHECK_AWARDED_BADGES = 129
USE_ITEM_GYM = 133
GET_GYM_DETAILS = 134
START_GYM_BATTLE = 135
ATTACK_GYM = 136
RECYCLE_INVENTORY_ITEM = 137
COLLECT_DAILY_BONUS = 138
USE_ITEM_XP_BOOST = 139
USE_ITEM_EGG_INCUBATOR = 140
USE_INCENSE = 141
GET_INCENSE_POKEMON = 142
INCENSE_ENCOUNTER = 143
ADD_FORT_MODIFIER = 144
DISK_ENCOUNTER = 145
COLLECT_DAILY_DEFENDER_BONUS = 146
UPGRADE_POKEMON = 147
SET_FAVORITE_POKEMON = 148
NICKNAME_POKEMON = 149
EQUIP_BADGE = 150
SET_CONTACT_SETTINGS = 151
SET_BUDDY_POKEMON = 152
GET_BUDDY_WALKED = 153
USE_ITEM_ENCOUNTER = 154
GYM_DEPLOY = 155
GYM_GET_INFO = 156
GYM_START_SESSION = 157
GYM_BATTLE_ATTACK = 158
JOIN_LOBBY = 159
LEAVE_LOBBY = 160
SET_LOBBY_VISIBILITY = 161
SET_LOBBY_POKEMON = 162
GET_RAID_DETAILS = 163
GYM_FEED_POKEMON = 164
START_RAID_BATTLE = 165
ATTACK_RAID = 166
AWARD_POKECOIN = 167
USE_ITEM_STARDUST_BOOST = 168
REASSIGN_PLAYER = 169
REDEEM_POI_PASSCODE = 170
GET_ASSET_DIGEST = 300
GET_DOWNLOAD_URLS = 301
GET_ASSET_VERSION = 302
CLAIM_CODENAME = 403
SET_AVATAR = 404
SET_PLAYER_TEAM = 405
MARK_TUTORIAL_COMPLETE = 406
UPDATE_PERFORMANCE_METRICS = 407
CHECK_CHALLENGE = 600
VERIFY_CHALLENGE = 601
ECHO = 666
SFIDA_REGISTRATION = 800
SFIDA_ACTION_LOG = 801
SFIDA_CERTIFICATION = 802
SFIDA_UPDATE = 803
SFIDA_ACTION = 804
SFIDA_DOWSER = 805
SFIDA_CAPTURE = 806
LIST_AVATAR_CUSTOMIZATIONS = 807
SET_AVATAR_ITEM_AS_VIEWED = 808
GET_INBOX = 809
LIST_GYM_BADGES = 811
GET_GYM_BADGE_DETAILS = 812
USE_ITEM_MOVE_REROLL = 813
USE_ITEM_RARE_CANDY = 814
AWARD_FREE_RAID_TICKET = 815
FETCH_ALL_NEWS = 816
MARK_READ_NEWS_ARTICLE = 817
GET_PLAYER_DISPLAY_INFO = 818
BELUGA_TRANSACTION_START = 819
BELUGA_TRANSACTION_COMPLETE = 820
GET_NEW_QUESTS = 900
GET_QUEST_DETAILS = 901
COMPLETE_QUEST = 902
REMOVE_QUEST = 903
QUEST_ENCOUNTER = 904
COMPLETE_QUEST_STAMP_CARD = 905
SEND_GIFT = 950
OPEN_GIFT = 951
GIFT_DETAILS = 952
DELETE_GIFT = 953
SAVE_PLAYER_SNAPSHOT = 954
GET_FRIENDSHIP_MILESTONE_REWARDS = 955
CHECK_SEND_GIFT = 956
SET_FRIEND_NICKNAME = 957
DELETE_GIFT_FROM_INVENTORY = 958
SAVE_SOCIAL_PLAYER_SETTINGS = 959
SHARE_EX_RAID_PASS = 960
CHECK_SHARE_EX_RAID_PASS = 961
DECLINE_SHARED_EX_RAID_PASS = 962
OPEN_TRADING = 970
UPDATE_TRADING = 971
CONFIRM_TRADING = 972
CANCEL_TRADING = 973
GET_TRADING = 974
GET_FITNESS_REWARDS = 980
GET_COMBAT_PLAYER_PROFILE = 990
GENERATE_COMBAT_CHALLENGE_ID = 991
CREATE_COMBAT_CHALLENGE = 992
OPEN_COMBAT_CHALLENGE = 993
GET_COMBAT_CHALLENGE = 994
ACCEPT_COMBAT_CHALLENGE = 995
DECLINE_COMBAT_CHALLENGE = 996
CANCEL_COMBAT_CHALLENGE = 997
SUBMIT_COMBAT_CHALLENGE_POKEMONS = 998
SAVE_COMBAT_PLAYER_PREFERENCES = 999
OPEN_COMBAT_SESSION = 1000
UPDATE_COMBAT = 1001
QUIT_COMBAT = 1002
GET_COMBAT_RESULTS = 1003
UNLOCK_SPECIAL_MOVE = 1004
GET_NPC_COMBAT_REWARDS = 1005
COMBAT_FRIEND_REQUEST = 1006
OPEN_NPC_COMBAT_SESSION = 1007
START_TUTORIAL_ACTION = 1008
GET_TUTORIAL_EGG_ACTION = 1009
SEND_PROBE = 1020
PROBE_DATA = 1021
COMBAT_DATA = 1022
COMBAT_CHALLENGE_DATA = 1023
CHECK_PHOTOBOMB = 1101
CONFIRM_PHOTOBOMB = 1102
GET_PHOTOBOMB = 1103
ENCOUNTER_PHOTOBOMB = 1104
GET_SIGNED_GMAP_URL_DEPRECATED = 1105
CHANGE_TEAM = 1106
GET_WEB_TOKEN = 1107
COMPLETE_SNAPSHOT_SESSION = 1110
START_INCIDENT = 1200
INVASION_COMPLETE_DIALOGUE = 1201
INVASION_OPEN_COMBAT_SESSION = 1202
INVASION_BATTLE_UPDATE = 1203
INVASION_ENCOUNTER = 1204
PURIFY_POKEMON = 1205
VS_SEEKER_START_MATCHMAKING = 1300
CANCEL_MATCHMAKING = 1301
GET_MATCHMAKING_STATUS = 1302
COMPLETE_VS_SEEKER_AND_RESTART_CHARGING = 1303
GET_VS_SEEKER_STATUS = 1304
COMPLETE_COMBAT_COMPETITIVE_SEASON_ACTION = 1305
CLAIM_VS_SEEKER_REWARDS = 1306
VS_SEEKER_REWARD_ENCOUNTER = 1307
ACTIVATE_VS_SEEKER = 1308
GET_BUDDY_MAP = 1350
GET_BUDDY_STATS = 1351
FEED_BUDDY = 1352
OPEN_BUDDY_GIFT = 1353
PET_BUDDY = 1354
GET_BUDDY_HISTORY = 1355
CREATE_BUDDY_MUTLIPLAYER_SESSION = 1456
JOIN_BUDDY_MULTIPLAYER_SESSION = 1457
LEAVE_BUDDY_MULTIPLAYER_SESSION = 1458
GET_TODAY_VIEW = 1501
REMOTE_GIFT_PING = 1503
SEND_RAID_INVITATION = 1504


DESCRIPTOR.enum_types_by_name['RequestType'] = _REQUESTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
