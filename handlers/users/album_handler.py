from loader import dp, bot
from aiogram.types import InputFile, Message, MediaGroup
from aiogram.dispatcher.filters import Command

from keyboards.inline.buy_car import car_keys

from loader import dp, bot

@dp.message_handler(Command("car"))
async def send_car(message: Message):

	file_id = 'AgACAgIAAxkBAAP3Y2-A21BFVHrRgQaQ9F5VdZCzh-gAAta9MRt4kYBLsBXS0XgsLb8BAAMCAAN4AAMrBA'
	
	text = "<b>BMW A3</b> aftamobili\n"
	text += "Narxi - 23.000 $\n"
	text += "Mashinani quyidagi do'konlardan harid qilishingiz mumkin:\n"
	text += "👉 GTA\n👉 Auto Salon\n👉 Mustang\n👉 Auto Planeta"
	
	await message.reply_photo(file_id, caption=text, reply_markup=car_keys)
	

@dp.message_handler(Command("album"))
async def send_album(message: Message):
	album = MediaGroup()
	
	car1 = "AgACAgIAAxkBAAP3Y2-A21BFVHrRgQaQ9F5VdZCzh-gAAta9MRt4kYBLsBXS0XgsLb8BAAMCAAN4AAMrBA"
	car2 = InputFile(path_or_bytesio='C:/Users/COMPUTERS/Pictures/car.jpg')
	car3 = "https://i.playground.ru/i/pix/1447307/image.jpg"


	video1 = "BAACAgIAAxkBAAPJY29rYdaJxxMzBS2Ru_2Lphwubq8AAjInAAJ4kXhLehA_IQJNnCMrBA"

	album.attach_photo(photo=car1)
	album.attach_photo(photo=car2)
	album.attach_photo(photo=car3)
	album.attach_video(video=video1, caption="Bizning Albom")
	
	await message.reply_media_group(media=album)



@dp.message_handler(Command("doc"))
async def send_doc(message: Message):

	doc_album = MediaGroup()

	doc1 = "BQACAgIAAxkBAAPbY29sweOqd7J39LwsWClP_ez1i04AAj8nAAJ4kXhLdKCbQFczlasrBA"
	doc2 = "BQACAgIAAxkBAAPbY29sweOqd7J39LwsWClP_ez1i04AAj8nAAJ4kXhLdKCbQFczlasrBA"

	doc_album.attach_document(document=doc1,)
	doc_album.attach_document(document=doc2, caption="Bizning Hujjatlar")

	await message.reply_media_group(media=doc_album)

