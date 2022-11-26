from loader import dp, bot
from aiogram.types import Message, ContentTypes

from pathlib import Path

# yuklangan fayllar tushadigan joyni mo'rsatamiz
download_path = Path().joinpath("downloads",)
download_path.mkdir(parents=True, exist_ok=True)


# for text
@dp.message_handler()
async def text_handler(message: Message):
	await message.answer("Siz matn yubordingiz!")

# for document
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
# @dp.message_handler(content_types="document")
async def doc_handler(message: Message):
	await message.document.download(destination=download_path)
	doc_id = message.document.file_id
	await message.reply("Siz fayl yubordingiz! \n"
		f"file_id = {doc_id}")


# for video
# @dp.message_handler(content_types=ContentTypes.VIDEO)
@dp.message_handler(content_types="video")
async def video_handler(message: Message):
	await message.video.download(destination=download_path)
	await message.reply("Siz vidoe yubordingiz! \n"
		f"file_id = {message.video.file_id}")


# for photo
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def photo_handler(message: Message):
	await message.photo[-1].download(destination=download_path)
	await message.reply("Siz rasm yubordingiz! \n"
		f"file_id = {message.photo[-1].file_id}")



# for audio
@dp.message_handler(content_types=ContentTypes.AUDIO)
async def audio_handler(message: Message):
	await message.audio.download(destination_dir=download_path)
	await message.reply("Siz audio yubordingiz! \n"
		f"file_id = {message.audio.file_id}")

