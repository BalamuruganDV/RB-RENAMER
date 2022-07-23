# (c) @AbirHasan2005

import os
import time
import asyncio
from typing import Optional


async def take_screen_shot(video_file, output_directory, ttl) -> Optional[str]:
    """
    𝚃𝚊𝚔𝚎 𝚂𝚌𝚛𝚎𝚎𝚗𝚜𝚑𝚘𝚝 𝚏𝚛𝚘𝚖 𝚅𝚒𝚍𝚎𝚘.

    𝚂𝚘𝚞𝚛𝚌𝚎: https://stackoverflow.com/a/13891070/4723940

    :𝚙𝚊𝚛𝚊𝚖 𝚟𝚒𝚍𝚎𝚘_𝚏𝚒𝚕𝚎: 𝙿𝚊𝚜𝚜 𝚅𝚒𝚍𝚎𝚘 𝙵𝚒𝚕𝚎 𝙿𝚊𝚝𝚑.
    :𝚙𝚊𝚛𝚊𝚖 𝚘𝚞𝚝𝚙𝚞𝚝_𝚍𝚒𝚛𝚎𝚌𝚝𝚘𝚛𝚢: 𝙿𝚊𝚜𝚜 𝚘𝚞𝚝𝚙𝚞𝚝 𝚏𝚘𝚕𝚍𝚎𝚛 𝚙𝚊𝚝𝚑 𝚏𝚘𝚛 𝚜𝚌𝚛𝚎𝚎𝚗𝚜𝚑𝚘𝚝. 𝙸𝚏 𝚏𝚘𝚕𝚍𝚎𝚛𝚜 𝚗𝚘𝚝 𝚎𝚡𝚒𝚜𝚝𝚜, 𝚝𝚑𝚒𝚜 𝚠𝚒𝚕𝚕 𝚌𝚛𝚎𝚊𝚝𝚎 𝚏𝚘𝚕𝚍𝚎𝚛𝚜.
    :𝚙𝚊𝚛𝚊𝚖 𝚝𝚝𝚕: 𝚃𝚒𝚖𝚎!

    :𝚛𝚎𝚝𝚞𝚛𝚗: 𝚃𝚑𝚒𝚜 𝚠𝚒𝚕𝚕 𝚛𝚎𝚝𝚞𝚛𝚗 𝚜𝚌𝚛𝚎𝚎𝚗𝚜𝚑𝚘𝚝 𝚒𝚖𝚊𝚐𝚎 𝚙𝚊𝚝𝚑.
    """

    output_dir = f'{output_directory}/{time.time()}/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_filepath = output_dir + "thumbnail.jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        output_filepath
    ]
    # width = "90"
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    return output_filepath if os.path.lexists(output_filepath) else None
