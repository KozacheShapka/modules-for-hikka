import os
from .. import loader, utils
from telethon import types
import string
import random
import eyed3


@loader.tds
class EAudioEditorMod(loader.Module):
    "Модуль для работы с аудио"
    strings = {"name": "Music Speed Changer (BETA)"}
    
    async def ratecmd(self, message):
        '''Изменяет скорость аудио с привязкой тона. 1.00 стандарт скорость'''
        letters = string.ascii_lowercase
        random_letters = ""
        for _ in range(10):
            random_letters += random.choice(letters)
        args = message.text.split(' ')[1:]
        reply = await message.get_reply_message()
        
        if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
            if args:
                performer = "Неизвестен"
                title = "Неизвестен"
                messages = await message.client.get_messages(reply.chat_id, ids=[reply.id])
                if messages:
                    message_with_audio = messages[0]
                    if message_with_audio.media and hasattr(message_with_audio.media, 'document'):
                        audio = message_with_audio.media.document
                        for attribute in audio.attributes:
                            if isinstance(attribute, types.DocumentAttributeAudio):
                                if attribute.performer:
                                    performer = attribute.performer
                                if attribute.title:
                                    title = attribute.title
                                duration = attribute.duration
                                break
            
                if performer or title:
                    file_name = f"{performer or title}_{random_letters}.mp3"
                else:
                    file_name = f"audio_{random_letters}.mp3"
                rate = float(args[0])
                await message.edit('[Music Speed Changer] Скачиваю...')
                await reply.download_media(file=file_name)
                await message.edit('[Music Speed Changer] Работаю...')
                if performer or title:
                    outputfile = f"{performer or title}_(рейт {rate})_{random_letters}.mp3"
                else:
                    outputfile = f"audio_(рейт {rate})_{random_letters}.mp3"
                if performer or title:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,asetrate=44100*{rate}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (рейт {rate})" "{outputfile}"')
                else:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,asetrate=44100*{rate}" -b:a 320k "{outputfile}"')
                fileinfo = f'{outputfile}'
                audiofile = eyed3.load(fileinfo)
                song_length_seconds = audiofile.info.time_secs
                duration = int(song_length_seconds)
                await message.edit('[Music Speed Changer] Отправляю...')
                await message.client.send_file(message.to_id, f'{outputfile}', voice_note=True, attributes=[types.DocumentAttributeAudio(duration=duration, performer=f'{performer}', title=f'{title} (рейт {rate})')])
                
                await message.delete()
                os.remove(f'{file_name}')
                os.remove(f'{outputfile}')
            else:
                await message.edit('Не указаны аргументы')
        else:
            await message.edit('Ответь на аудио!')

    async def basscmd(self, message):
        '''Добавляет басс к аудио. От 2 до 200'''
        letters = string.ascii_lowercase
        random_letters = ""
        for _ in range(10):
            random_letters += random.choice(letters)
        args = message.text.split(' ')[1:]
        reply = await message.get_reply_message()
        
        if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
            if args:
                performer = "Неизвестен"
                title = "Неизвестен"
                messages = await message.client.get_messages(reply.chat_id, ids=[reply.id])
                if messages:
                    message_with_audio = messages[0]
                    if message_with_audio.media and hasattr(message_with_audio.media, 'document'):
                        audio = message_with_audio.media.document
                        for attribute in audio.attributes:
                            if isinstance(attribute, types.DocumentAttributeAudio):
                                if attribute.performer:
                                    performer = attribute.performer
                                if attribute.title:
                                    title = attribute.title
                                duration = attribute.duration
                                break
            
                if performer or title:
                    file_name = f"{performer or title}_{random_letters}.mp3"
                else:
                    file_name = f"audio_{random_letters}.mp3"
                bass = int(args[0])
                await message.edit('[Music Speed Changer] Скачиваю...')
                await reply.download_media(file=file_name)
                await message.edit('[Music Speed Changer] Работаю...')
                if performer or title:
                    outputfile = f"{performer or title}_(Бас на +{bass}db)_{random_letters}.mp3"
                else:
                    outputfile = f"audio_(Бас на +{bass}db)_{random_letters}.mp3"
                if performer or title:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,bass=g={bass}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (Бас на +{bass}db)" "{outputfile}"')
                else:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,bass=g={bass}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (Бас на +{bass}db)" "{outputfile}')
                fileinfo = f'{outputfile}'
                audiofile = eyed3.load(fileinfo)
                song_length_seconds = audiofile.info.time_secs
                duration = int(song_length_seconds)
                await message.edit('[Music Speed Changer] Отправляю...')
                await message.client.send_file(message.to_id, f'{outputfile}', voice_note=True, attributes=[types.DocumentAttributeAudio(duration=duration, performer=f'{performer}', title=f'{title} (Бас на +{bass}db)')])
                
                await message.delete()
                os.remove(f'{file_name}')
                os.remove(f'{outputfile}')
            else:
                await message.edit('Не указаны аргументы')
        else:
            await message.edit('Ответь на аудио!')
    
    async def volcmd(self, message):
        '''Изменяет громкость аудио. 1.0 - Стандартная громкость'''
        letters = string.ascii_lowercase
        random_letters = ""
        for _ in range(10):
            random_letters += random.choice(letters)
        args = message.text.split(' ')[1:]
        reply = await message.get_reply_message()
        
        if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
            if args:
                performer = "Неизвестен"
                title = "Неизвестен"
                messages = await message.client.get_messages(reply.chat_id, ids=[reply.id])
                if messages:
                    message_with_audio = messages[0]
                    if message_with_audio.media and hasattr(message_with_audio.media, 'document'):
                        audio = message_with_audio.media.document
                        for attribute in audio.attributes:
                            if isinstance(attribute, types.DocumentAttributeAudio):
                                if attribute.performer:
                                    performer = attribute.performer
                                if attribute.title:
                                    title = attribute.title
                                duration = attribute.duration
                                break
            
                if performer or title:
                    file_name = f"{performer or title}_{random_letters}.mp3"
                else:
                    file_name = f"audio_{random_letters}.mp3"
                vol = float(args[0])
                await message.edit('[Music Speed Changer] Скачиваю...')
                await reply.download_media(file=file_name)
                await message.edit('[Music Speed Changer] Работаю...')
                if performer or title:
                    outputfile = f"{performer or title}_(Громкость {vol})_{random_letters}.mp3"
                else:
                    outputfile = f"audio_(Громкость {vol})_{random_letters}.mp3"
                if performer or title:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,volume={vol}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (Громкость {vol})" "{outputfile}"')
                else:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,volume={vol}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (Громкость {vol})" "{outputfile}"')
                fileinfo = f'{outputfile}'
                audiofile = eyed3.load(fileinfo)
                song_length_seconds = audiofile.info.time_secs
                duration = int(song_length_seconds)
                await message.edit('[Music Speed Changer] Отправляю...')
                await message.client.send_file(message.to_id, f'{outputfile}', voice_note=True, attributes=[types.DocumentAttributeAudio(duration=duration, performer=f'{performer}', title=f'{title} (Громкость {vol})')])
                
                await message.delete()
                os.remove(f'{file_name}')
                os.remove(f'{outputfile}')
            else:
                await message.edit('Не указаны аргументы')
        else:
            await message.edit('Ответь на аудио!')

    async def pitchcmd(self, message):
        '''Изменяет тон аудио. 1.0 стандарт'''
        letters = string.ascii_lowercase
        random_letters = ""
        for _ in range(10):
            random_letters += random.choice(letters)
        args = message.text.split(' ')[1:]
        reply = await message.get_reply_message()
        
        if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
            if args:
                performer = "Неизвестен"
                title = "Неизвестен"
                messages = await message.client.get_messages(reply.chat_id, ids=[reply.id])
                if messages:
                    message_with_audio = messages[0]
                    if message_with_audio.media and hasattr(message_with_audio.media, 'document'):
                        audio = message_with_audio.media.document
                        for attribute in audio.attributes:
                            if isinstance(attribute, types.DocumentAttributeAudio):
                                if attribute.performer:
                                    performer = attribute.performer
                                if attribute.title:
                                    title = attribute.title
                                duration = attribute.duration
                                break
            
                if performer or title:
                    file_name = f"{performer or title}_{random_letters}.mp3"
                else:
                    file_name = f"audio_{random_letters}.mp3"
                pitch = float(args[0])
                await message.edit('[Music Speed Changer] Скачиваю...')
                await reply.download_media(file=file_name)
                await message.edit('[Music Speed Changer] Работаю...')
                if performer or title:
                    outputfile = f"{performer or title}_(Тон {pitch})_{random_letters}.mp3"
                else:
                    outputfile = f"audio_(Тон {pitch})_{random_letters}.mp3"
                if performer or title:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,rubberband=pitch={pitch}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (тон {pitch})" "{outputfile}"')
                else:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,rubberband=pitch={pitch}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (тон {pitch})" "{outputfile}"')
                fileinfo = f'{outputfile}'
                audiofile = eyed3.load(fileinfo)
                song_length_seconds = audiofile.info.time_secs
                duration = int(song_length_seconds)
                await message.edit('[Music Speed Changer] Отправляю...')
                await message.client.send_file(message.to_id, f'{outputfile}', voice_note=True, attributes=[types.DocumentAttributeAudio(duration=duration, performer=f'{performer}', title=f'{title} (тон {pitch})')])
                
                await message.delete()
                os.remove(f'{file_name}')
                os.remove(f'{outputfile}')
            else:
                await message.edit('Не указаны аргументы')
        else:
            await message.edit('Ответь на аудио!')

    async def speedcmd(self, message):
        '''Изменяет скорость аудио. 1.0 стандартная скорость'''
        letters = string.ascii_lowercase
        random_letters = ""
        for _ in range(10):
            random_letters += random.choice(letters)
        args = message.text.split(' ')[1:]
        reply = await message.get_reply_message()
        
        if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
            if args:
                performer = "Неизвестен"
                title = "Неизвестен"
                messages = await message.client.get_messages(reply.chat_id, ids=[reply.id])
                if messages:
                    message_with_audio = messages[0]
                    if message_with_audio.media and hasattr(message_with_audio.media, 'document'):
                        audio = message_with_audio.media.document
                        for attribute in audio.attributes:
                            if isinstance(attribute, types.DocumentAttributeAudio):
                                if attribute.performer:
                                    performer = attribute.performer
                                if attribute.title:
                                    title = attribute.title
                                duration = attribute.duration
                                break
            
                if performer or title:
                    file_name = f"{performer or title}_{random_letters}.mp3"
                else:
                    file_name = f"audio_{random_letters}.mp3"
                speed = float(args[0])
                await message.edit('[Music Speed Changer] Скачиваю...')
                await reply.download_media(file=file_name)
                await message.edit('[Music Speed Changer] Работаю...')
                if performer or title:
                    outputfile = f"{performer or title}_(Скорость {speed})_{random_letters}.mp3"
                else:
                    outputfile = f"audio_(Скорость {speed})_{random_letters}.mp3"
                if performer or title:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,atempo={speed}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (скорость {speed})" "{outputfile}"')
                else:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,atempo={speed}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (скорость {speed})" "{outputfile}"')
                fileinfo = f'{outputfile}'
                audiofile = eyed3.load(fileinfo)
                song_length_seconds = audiofile.info.time_secs
                duration = int(song_length_seconds)
                await message.edit('[Music Speed Changer] Отправляю...')
                await message.client.send_file(message.to_id, f'{outputfile}', voice_note=True, attributes=[types.DocumentAttributeAudio(duration=duration, performer=f'{performer}', title=f'{title} (cкорость {speed})')])
                await message.delete()
                os.remove(f'{file_name}')
                os.remove(f'{outputfile}')
            else:
                await message.edit('Не указаны аргументы')
        else:
            await message.edit('Ответь на аудио!')

    async def compresscmd(self, message):
        '''Используется для уровнирования громкости звука, снижения разницы между самыми тихими и самыми громкими частями  1.0 стандартная скорость'''
        letters = string.ascii_lowercase
        random_letters = ""
        for _ in range(10):
            random_letters += random.choice(letters)
        args = message.text.split(' ')[1:]
        reply = await message.get_reply_message()
        
        if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
            if args:
                performer = "Неизвестен"
                title = "Неизвестен"
                messages = await message.client.get_messages(reply.chat_id, ids=[reply.id])
                if messages:
                    message_with_audio = messages[0]
                    if message_with_audio.media and hasattr(message_with_audio.media, 'document'):
                        audio = message_with_audio.media.document
                        for attribute in audio.attributes:
                            if isinstance(attribute, types.DocumentAttributeAudio):
                                if attribute.performer:
                                    performer = attribute.performer
                                if attribute.title:
                                    title = attribute.title
                                duration = attribute.duration
                                break
            
                if performer or title:
                    file_name = f"{performer or title}_{random_letters}.mp3"
                else:
                    file_name = f"audio_{random_letters}.mp3"
                threshold = float(args[0])
                ratio = int(args[1])
                attack = int(args[2])
                release = int(args[3])
                await message.edit('[Music Speed Changer] Скачиваю...')
                await reply.download_media(file=file_name)
                await message.edit('[Music Speed Changer] Работаю...')
                if performer or title:
                    outputfile = f"{performer or title}_(+компрессор)_{random_letters}.mp3"
                else:
                    outputfile = f"audio_(+компрессор)_{random_letters}.mp3"
                if performer or title:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,acompressor=threshold={threshold}:ratio={ratio}:attack={attack}:release={release}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (+compressor)" "{outputfile}"')
                else:
                    os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,acompressor=threshold={threshold}:ratio={ratio}:attack={attack}:release={release}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (+compressor)" "{outputfile}"')
                fileinfo = f'{outputfile}'
                audiofile = eyed3.load(fileinfo)
                song_length_seconds = audiofile.info.time_secs
                duration = int(song_length_seconds)
                await message.edit('[Music Speed Changer] Отправляю...')
                await message.client.send_file(message.to_id, f'{outputfile}', voice_note=True, attributes=[types.DocumentAttributeAudio(duration=duration, performer=f'{performer}', title=f'{title} (+compressor)')])
                await message.delete()
                os.remove(f'{file_name}')
                os.remove(f'{outputfile}')
            else:
                await message.edit('Не указаны аргументы')
        else:
            await message.edit('Ответь на аудио!')

    async def effectcmd(self, message):
        '''Пакет эффектов.'''
        letters = string.ascii_lowercase
        random_letters = ""
        for _ in range(10):
            random_letters += random.choice(letters)
        args = message.text.split(' ')[1:]
        reply = await message.get_reply_message()
        
        if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
            if args:
                args = message.text.split(' ')[1:]
                performer = "Неизвестен"
                title = "Неизвестен"
                messages = await message.client.get_messages(reply.chat_id, ids=[reply.id])
                if messages:
                    message_with_audio = messages[0]
                    if message_with_audio.media and hasattr(message_with_audio.media, 'document'):
                        audio = message_with_audio.media.document
                        for attribute in audio.attributes:
                            if isinstance(attribute, types.DocumentAttributeAudio):
                                if attribute.performer:
                                    performer = attribute.performer
                                if attribute.title:
                                    title = attribute.title
                                    duration = attribute.duration
                                break
            
                if args[0] == 'nc' or 'nightcore':
                    if performer or title:
                        file_name = f"{performer or title}_{random_letters}.mp3"
                    else:
                        file_name = f"audio_{random_letters}.mp3"
                    rate = float(args[0])
                    await message.edit('[Music Speed Changer] Скачиваю...')
                    await reply.download_media(file=file_name)
                    await message.edit('[Music Speed Changer] Работаю...')
                    if performer or title:
                        outputfile = f"{performer or title}_(рейт {rate})_{random_letters}.mp3"
                    else:
                        outputfile = f"audio_(рейт {rate})_{random_letters}.mp3"
                    if performer or title:
                        os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,asetrate=44100*{rate}" -b:a 320k -metadata artist="{performer}" -metadata title="{title} (рейт {rate})" "{outputfile}"')
                    else:
                        os.system(f'ffmpeg -i "{file_name}" -filter:a "aresample=44100,asetrate=44100*{rate}" -b:a 320k "{outputfile}"')
                    fileinfo = f'{outputfile}'
                    audiofile = eyed3.load(fileinfo)
                    song_length_seconds = audiofile.info.time_secs
                    duration = int(song_length_seconds)
                    await message.edit('[Music Speed Changer] Отправляю...')
                    await message.client.send_file(message.to_id, f'{outputfile}', voice_note=True, attributes=[types.DocumentAttributeAudio(duration=duration, performer=f'{performer}', title=f'{title} (рейт {rate})')])
                
                    await message.delete()
                    os.remove(f'{file_name}')
                    os.remove(f'{outputfile}')





    async def mscversioncmd(self, message):
        '''Информация о модуле'''
        await message.edit('🎵Music Speed Changer \n\n🎵BETA 2 \n\nℹ️Модуль для работы и обработки аудио. Используйте под ваши нужды. \n\n♥️2023 - Anonymous Economy Team')