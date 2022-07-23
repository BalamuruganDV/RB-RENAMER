# (c) @AbirHasan2005

from pyrogram.types import Message


def get_media_file_name(message: Message):
    """
    𝙿𝚊𝚜𝚜 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚋𝚓𝚎𝚌𝚝 𝚘𝚏 𝚊𝚞𝚍𝚒𝚘 𝚘𝚛 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝 𝚘𝚛 𝚜𝚝𝚒𝚌𝚔𝚎𝚛 𝚘𝚛 𝚟𝚒𝚍𝚎𝚘 𝚘𝚛 𝚊𝚗𝚒𝚖𝚊𝚝𝚒𝚘𝚗 𝚝𝚘 𝚐𝚎𝚝 𝚏𝚒𝚕𝚎_𝚗𝚊𝚖𝚎.
    """

    media = message.audio or \
            message.document or \
            message.sticker or \
            message.video or \
            message.animation

    if media and media.file_name:
        return media.file_name
    else:
        return None


def get_media_file_size(message: Message):
    """
    𝙿𝚊𝚜𝚜 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚋𝚓𝚎𝚌𝚝 𝚘𝚏 𝚊𝚞𝚍𝚒𝚘 𝚘𝚛 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝 𝚘𝚛 𝚙𝚑𝚘𝚝𝚘 𝚘𝚛 𝚜𝚝𝚒𝚌𝚔𝚎𝚛 𝚘𝚛 𝚟𝚒𝚍𝚎𝚘 𝚘𝚛 𝚊𝚗𝚒𝚖𝚊𝚝𝚒𝚘𝚗 𝚘𝚛 𝚟𝚘𝚒𝚌𝚎 𝚘𝚛 𝚟𝚒𝚍𝚎𝚘_𝚗𝚘𝚝𝚎 𝚝𝚘 𝚐𝚎𝚝 𝚏𝚒𝚕𝚎_𝚜𝚒𝚣𝚎.
    """

    media = message.audio or \
            message.document or \
            message.photo or \
            message.sticker or \
            message.video or \
            message.animation or \
            message.voice or \
            message.video_note

    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_mime_type(message: Message):
    """
    𝙿𝚊𝚜𝚜 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚋𝚓𝚎𝚌𝚝 𝚘𝚏 𝚊𝚞𝚍𝚒𝚘 𝚘𝚛 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝 𝚘𝚛 𝚟𝚒𝚍𝚎𝚘 𝚝𝚘 𝚐𝚎𝚝 𝚖𝚒𝚖𝚎_𝚝𝚢𝚙𝚎
    """

    media = message.audio or \
            message.document or \
            message.video
    
    if media and media.mime_type:
        return media.mime_type
    else:
        return None


def get_media_file_id(message: Message):
    """
    𝙿𝚊𝚜𝚜 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚋𝚓𝚎𝚌𝚝 𝚘𝚏 𝚊𝚞𝚍𝚒𝚘 𝚘𝚛 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝 𝚘𝚛 𝚙𝚑𝚘𝚝𝚘 𝚘𝚛 𝚜𝚝𝚒𝚌𝚔𝚎𝚛 𝚘𝚛 𝚟𝚒𝚍𝚎𝚘 𝚘𝚛 𝚊𝚗𝚒𝚖𝚊𝚝𝚒𝚘𝚗 𝚘𝚛 𝚟𝚘𝚒𝚌𝚎 𝚘𝚛 𝚟𝚒𝚍𝚎𝚘_𝚗𝚘𝚝𝚎 𝚝𝚘 𝚐𝚎𝚝 𝚏𝚒𝚕𝚎_𝚒𝚍.
    """

    media = message.audio or \
            message.document or \
            message.photo or \
            message.sticker or \
            message.video or \
            message.animation or \
            message.voice or \
            message.video_note

    if media and media.file_id:
        return media.file_id
    else:
        return None


def get_file_type(message: Message):
    if message.document:
        return "document"
    if message.video:
        return "video"
    if message.audio:
        return "audio"


def get_file_attr(message: Message):

    """
    Combine audio or video or document
    """

    media = message.audio or \
            message.video or \
            message.document

    return media


def get_thumb_file_id(message: Message):
    media = message.audio or \
            message.video or \
            message.document
    if media and media.thumbs:
        return media.thumbs[0].file_id
    else:
        return None
