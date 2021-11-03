

import logging
from typing import Literal

from aiogram import  Bot, Dispatcher, executor, types
from aiogram.types import message, reply_keyboard
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from aiogram.utils import markdown

TOKENn = '1867858470:AAHAn7TTFmv8nh33B6J5F1gqJLXTKlj9uiU'
logging.basicConfig(level=logging.INFO)
from markups import i,  v
from aiogram.utils.markdown import hide_link
bot = Bot(token=TOKENn)
dp = Dispatcher(bot)
CHANNEL_ID = '@b148uz'
import markups as nav

cd = ' <b>📜 Surani tanlang</b>  \n  \n <b>1.</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ) \n <b>2.</b> Al-Baqara (سُورَةُ البَقَرَةِ) \n <b>3.</b> Aal-i-Imraan (سُورَةُ آلِ عِمۡرَانَ) \n <b>4.</b> An-Nisaa (سُورَةُ النِّسَاءِ) \n <b>5.</b> Al-Maaida (سُورَةُ المَائـِدَةِ) \n <b>6.</b> Al-An\'aam (سُورَةُ الأَنۡعَامِ) \n <b>7.</b> Al-A\'raaf (سُورَةُ الأَعۡرَافِ) \n <b>8.</b> Al-Anfaal (سُورَةُ الأَنفَالِ) \n <b>9.</b> At-Tawba (سُورَةُ التَّوۡبَةِ) \n <b>10.</b> Yunus (سُورَةُ يُونُسَ) \n <b>11.</b> Hud (سُورَةُ هُودٍ) \n <b>12.</b> Yusuf (سُورَةُ يُوسُفَ) \n <b>13.</b> Ar-Ra\'d (سُورَةُ الرَّعۡدِ) \n <b>14.</b> Ibrahim (سُورَةُ إِبۡرَاهِيمَ) \n <b>15.</b> Al-Hijr (سُورَةُ الحِجۡرِ) \n <b>16.</b> An-Nahl (سُورَةُ النَّحۡلِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'
cd2 = ' <b>📜 Surani tanlang</b>  \n  \n <b>17.</b> Al-Israa (سُورَةُ الإِسۡرَاءِ) \n <b>18.</b> Al-Kahf (سُورَةُ الكَهۡفِ) \n <b>19.</b> Maryam (سُورَةُ مَرۡيَمَ) \n <b>20.</b> Taa-Haa (سُورَةُ طه) \n <b>21.</b> Al-Anbiyaa (سُورَةُ الأَنبِيَاءِ) \n <b>22.</b> Al-Hajj (سُورَةُ الحَجِّ) \n <b>23.</b> Al-Muminoon (سُورَةُ المُؤۡمِنُونَ) \n <b>24.</b> An-Noor (سُورَةُ النُّورِ) \n <b>25.</b> Al-Furqaan (سُورَةُ الفُرۡقَانِ) \n <b>26.</b> Ash-Shu\'araa (سُورَةُ الشُّعَرَاءِ) \n <b>27.</b> An-Naml (سُورَةُ النَّمۡلِ) \n <b>28.</b> Al-Qasas (سُورَةُ القَصَصِ) \n <b>29.</b> Al-Ankaboot (سُورَةُ العَنكَبُوتِ) \n <b>30.</b> Ar-Room (سُورَةُ الرُّومِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'  
cd3 = ' <b>📜 Surani tanlang</b>  \n \n <b>31.</b> Luqman (سُورَةُ لُقۡمَانَ) \n <b>32.</b> As-Sajda (سُورَةُ السَّجۡدَةِ) \n <b>33.</b> Al-Ahzaab (سُورَةُ الأَحۡزَابِ) \n <b>34.</b> Saba (سُورَةُ سَبَإٍ) \n <b>35.</b> Faatir (سُورَةُ فَاطِرٍ) \n <b>36.</b> Yaseen (سُورَةُ يسٓ) \n <b>37.</b> As-Saaffaat (سُورَةُ الصَّافَّاتِ) \n <b>38.</b> Saad (سُورَةُ صٓ) \n <b>39.</b> Az-Zumar (سُورَةُ الزُّمَرِ) \n <b>40.</b> Ghafir (سُورَةُ غَافِرٍ) \n <b>41.</b> Fussilat (سُورَةُ فُصِّلَتۡ) \n <b>42.</b> Ash-Shura (سُورَةُ الشُّورَىٰ) \n <b>43.</b> Az-Zukhruf (سُورَةُ الزُّخۡرُفِ) \n <b>44.</b> Ad-Dukhaan (سُورَةُ الدُّخَانِ) \n <b>45.</b> Al-Jaathiya (سُورَةُ الجَاثِيَةِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'
cd4 = ' <b>📜 Surani tanlang</b>  \n \n <b>46.</b> Al-Ahqaf (سُورَةُ الأَحۡقَافِ) \n <b>47.</b> Muhammad (سُورَةُ مُحَمَّدٍ) \n <b>48.</b> Al-Fath (سُورَةُ الفَتۡحِ) \n <b>49.</b> Al-Hujuraat (سُورَةُ الحُجُرَاتِ) \n <b>50.</b> Qaaf (سُورَةُ قٓ) \n <b>51.</b> Adh-Dhaariyat (سُورَةُ الذَّارِيَاتِ) \n <b>52.</b> At-Tur (سُورَةُ الطُّورِ) \n <b>53.</b> An-Najm (سُورَةُ النَّجۡمِ) \n <b>54.</b> Al-Qamar (سُورَةُ القَمَرِ) \n <b>55.</b> Ar-Rahmaan (سُورَةُ الرَّحۡمَٰن) \n <b>56.</b> Al-Waaqia (سُورَةُ الوَاقِعَةِ) \n <b>57.</b> Al-Hadid (سُورَةُ الحَدِيدِ) \n <b>58.</b> Al-Mujaadila (سُورَةُ المُجَادلَةِ) \n <b>59.</b> Al-Hashr (سُورَةُ الحَشۡرِ) \n <b>60.</b> Al-Mumtahana (سُورَةُ المُمۡتَحنَةِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'
cd5 = ' <b>📜 Surani tanlang</b>  \n \n <b>61.</b> As-Saff (سُورَةُ الصَّفِّ) \n <b>62.</b> Al-Jumu\'a (سُورَةُ الجُمُعَةِ) \n <b>63.</b> Al-Munaafiqoon (سُورَةُ المُنَافِقُونَ) \n <b>64.</b> At-Taghaabun (سُورَةُ التَّغَابُنِ) \n <b>65.</b> At-Talaaq (سُورَةُ الطَّلَاقِ) \n <b>66.</b> At-Tahrim (سُورَةُ التَّحۡرِيمِ) \n <b>67.</b> Al-Mulk (سُورَةُ المُلۡكِ) \n <b>68.</b> Al-Qalam (سُورَةُ القَلَمِ) \n <b>69.</b> Al-Haaqqa (سُورَةُ الحَاقَّةِ) \n <b>70.</b> Al-Ma\'aarij (سُورَةُ المَعَارِجِ) \n <b>71.</b> Nooh (سُورَةُ نُوحٍ) \n <b>72.</b> Al-Jinn (سُورَةُ الجِنِّ) \n <b>73.</b> Al-Muzzammil (سُورَةُ المُزَّمِّلِ) \n <b>74.</b> Al-Muddaththir (سُورَةُ المُدَّثِّرِ) \n <b>75.</b> Al-Qiyaama (سُورَةُ القِيَامَةِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'
cd6 = ' <b>📜 Surani tanlang</b>  \n \n <b>76.</b> Al-Insaan (سُورَةُ الإِنسَانِ) \n <b>77.</b> Al-Mursalaat (سُورَةُ المُرۡسَلَاتِ) \n <b>78.</b> An-Naba (سُورَةُ النَّبَإِ) \n <b>79.</b> An-Naazi\'aat (سُورَةُ النَّازِعَاتِ) \n <b>80.</b> Abasa (سُورَةُ عَبَسَ) \n <b>81.</b> At-Takwir (سُورَةُ التَّكۡوِيرِ) \n <b>82.</b> Al-Infitaar (سُورَةُ الانفِطَارِ) \n <b>83.</b> Al-Mutaffifin (سُورَةُ المُطَفِّفِينَ) \n <b>84.</b> Al-Inshiqaaq (سُورَةُ الانشِقَاقِ) \n <b>85.</b> Al-Burooj (سُورَةُ البُرُوجِ) \n <b>86.</b> At-Taariq (سُورَةُ الطَّارِقِ) \n <b>87.</b> Al-A\'laa (سُورَةُ الأَعۡلَىٰ) \n <b>88.</b> Al-Ghaashiya (سُورَةُ الغَاشِيَةِ) \n <b>89.</b> Al-Fajr (سُورَةُ الفَجۡرِ) \n <b>90.</b> Al-Balad (سُورَةُ البَلَدِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'
cd7 = ' <b>📜 Surani tanlang</b>  \n \n <b>91.</b> Ash-Shams (سُورَةُ الشَّمۡسِ) \n <b>92.</b> Al-Lail (سُورَةُ اللَّيۡلِ) \n <b>93.</b> Ad-Dhuhaa (سُورَةُ الضُّحَىٰ) \n <b>94.</b> Ash-Sharh (سُورَةُ الشَّرۡحِ) \n <b>95.</b> At-Tin (سُورَةُ التِّينِ) \n <b>96.</b> Al-Alaq (سُورَةُ العَلَقِ) \n <b>97.</b> Al-Qadr (سُورَةُ القَدۡرِ) \n <b>98.</b> Al-Bayyina (سُورَةُ البَيِّنَةِ) \n <b>99.</b> Az-Zalzala (سُورَةُ الزَّلۡزَلَةِ) \n <b>100.</b> Al-Aadiyaat (سُورَةُ العَادِيَاتِ) \n <b>101.</b> Al-Qaari\'a (سُورَةُ القَارِعَةِ) \n <b>102.</b> At-Takaathur (سُورَةُ التَّكَاثُرِ) \n <b>103.</b> Al-Asr (سُورَةُ العَصۡرِ) \n <b>104.</b> Al-Humaza (سُورَةُ الهُمَزَةِ) \n <b>105.</b> Al-Fil (سُورَةُ الفِيلِ) \n <b>106.</b> Quraish (سُورَةُ قُرَيۡشٍ) \n <b>107.</b> Al-Maa\'un (سُورَةُ المَاعُونِ) \n <b>108.</b> Al-Kawthar (سُورَةُ الكَوۡثَرِ) \n <b>109.</b> Al-Kaafiroon (سُورَةُ الكَافِرُونَ) \n <b>110.</b> An-Nasr (سُورَةُ النَّصۡرِ) \n <b>111.</b> Al-Masad (سُورَةُ المَسَدِ) \n <b>112.</b> Al-Ikhlaas (سُورَةُ الإِخۡلَاصِ) \n <b>113.</b> Al-Falaq (سُورَةُ الفَلَقِ) \n <b>114.</b> An-Naas (سُورَةُ النَّاسِ) \n \n  <b>Hamma Audiolar uchun 📻</b>'
orqaga = '📜 Suralar ro\'yxatiga qaytish uchun orqagani bosing'



import requests
import json

# url = "https://dailyprayer.abdulrcs.repl.co/api/toshkent"
# response = requests.get(url)
# data = response.json()
# print(data['city'])
# print(data['date'])
# for prayer in data["today"]:
#   print(prayer + ": " + data["today"][prayer])  


















def check_sub_channel(chat_member):
    
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
           if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
               await bot.send_message(message.from_user.id, 'salom ishladi' , reply_markup=nav.checksubmenu)
           else:
               await bot.send_message(message.from_user.id, 'ishlamadi', reply_markup=nav.checksubmenu)



@dp.callback_query_handler(text="subchanneldone")
async def subchanell(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id,'azo buldi', reply_markup=nav.sainmenu)
    else:
        await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)




@dp.message_handler()
async def botmeseg(message: types.Message):
  
    if message.chat.type == 'private':
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

   
           if message.text == 'Quron Tinglang':
              await bot.send_message(message.from_user.id, 'Quron tinglang 🤲', reply_markup=nav.qori)
           elif message.text == 'boshqa':
               await bot.send_message(message.from_user.id, 'boshqa', reply_markup=nav.othermenu, )
           elif message.text == 'info':
               await bot.send_message(message.from_user.id, 'salomlar bulsin', reply_markup=nav.mainMenu )
     
        else:
            await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)


@dp.callback_query_handler(text="btnqori")
async def random(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
     
            await bot.delete_message(message.from_user.id,  message.message.message_id)
            await bot.send_message(message.from_user.id , " <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML' ,reply_markup=nav.qorila)
    
    else:
            await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)



@dp.callback_query_handler(text="btnqori2")
async def random(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
     
            await bot.delete_message(message.from_user.id,  message.message.message_id)
            await bot.send_message(message.from_user.id , " <b>•______________________________________•ㅤ </b> \n  \n  <b>1.</b>  \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML' ,reply_markup=nav.qorila2)
    
    else:
            await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)



 
@dp.callback_query_handler(text="qoriasosiy")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)

@dp.callback_query_handler(text="Keyingi")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________• </b> \n  \n <b>16.</b> Saad Al-Ghamdi (سعد الغامدي) \n <b>17.</b> Khalid Abdulkafi (خالد عبدالكافي) \n <b>18. </b>Tawfeeq As-Sayegh (توفيق الصايغ) \n <b>19.</b> Adel Ryyan (عادل ريان) \n <b>20.</b> Zakaria Hamamah (زكريا حمامة) \n <b>21.</b> Slaah Bukhatir (القارئ صلاح بو خاطر) \n <b>22.</b> Abdelbari Al-Toubayti (عبدالبارئ الثبيتي) \n <b>23.</b> Abdulaziz Az-Zahrani (عبدالعزيز الزهراني) \n <b>24.</b> Abdullah Al-Burimi (عبدالله البريمي) \n <b>25.</b> Abdullah Al-Mattrod (عبدالله المطرود) \n <b>26.</b> Abdullah Al-Johany (عبدالله عواد الجهني) \n <b>27.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>28.</b> Abdulmohsin Al-Harthy (عبدالمحسن الحارثي) \n <b>29.</b> Abdulmohsin Al-Askar (عبدالمحسن العسكر) \n <b>30.</b> Salah Alhashim (صلاح الهاشم)",parse_mode='HTML' , reply_markup=nav.qorila2)
 

  
@dp.callback_query_handler(text="Keyingi2")
async def sura(message: types.Message):

            await message.message.edit_text(f"<b>•______________________________________•ㅤ </b> \n \n <b>31.</b> Salah Alhashim (صلاح الهاشم) \n <b>32.</b> Alhusayni Al-Azazi (الحسيني العزازي) \n <b>33.</b> Khalid Al-Jileel (خالد الجليل)\n <b>34.</b> Fawaz Alkabi (فواز الكعبي) \n <b>35.</b> Salah Albudair (صلاح البدير) \n <b>36.</b> Fahad Al-Kandari (فهد الكندري) \n <b>37.</b> Fares Abbad (فارس عباد) \n <b>38.</b> Nabil Al Rifay (نبيل الرفاعي) \n <b>39.</b> Walid Al-Dulaimi (وليد الدليمي) \n <b>40.</b> Yasser Al-Dosari (ياسر الدوسري) \n <b>41.</b> Yasser Al-Qurashi (ياسر القرشي) \n <b>42.</b> Yahya Hawwa (يحيى حوا) \n <b>43.</b> Yousef Alshoaey (يوسف الشويعي) \n <b>44.</b> Majed Al-Enezi (ماجد العنزي) \n <b>45.</b> Rachid Belalya (رشيد بلعالية)",parse_mode='HTML' , reply_markup=nav.qorila3)
 
 
@dp.callback_query_handler(text="Keyingi3")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>46.</b> Alzain Mohammad Ahmad (الزين محمد أحمد) \n <b>47.</b> Al-Qaria Yassen (القارئ ياسين) \n <b>48.</b> Rachid Belalya (رشيد بلعالية) \n <b>49.</b> Rasheed Ifrad (رشيد إفراد) \n <b>50.</b> Hamad Al Daghriri (حمد الدغريري) \n <b>51.</b> Lafi Al-Oni (لافي العوني) \n <b>52.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>53.</b> Abdullah Al-Kandari (عبدالله الكندري) \n <b>54.</b> Saber Abdulhakm (صابر عبدالحكم) \n <b>55.</b> Ahmed Amer (أحمد عامر) \n <b>56.</b> Malik shaibat Alhamed (مالك شيبة الحمد) \n <b>57.</b> Abdulmajeed Al-Arkani (عبدالمجيد الأركاني) \n <b>58.</b> Mustafa Ismail (مصطفى إسماعيل) \n <b>59.</b> Ahmad Shaheen (أحمد خليل شاهين) \n <b>60.</b> Omar Al-Qazabri' (عمر القزابري)",parse_mode='HTML' , reply_markup=nav.qorila4)
 

@dp.callback_query_handler(text="Keyingi4")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>61.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>62.</b> Saad Almqren (سعد المقرن) \n <b>63.</b> Omar Al-Qazabri\' (عمر القزابري) \n <b>64.</b> Akram Alalaqmi (أكرم العلاقمي) \n <b>65.</b> Abdulrahman Al-Majed (عبدالرحمن الماجد) \n <b>66.</b> Emad Hafez (عماد زهير حافظ) \n <b>67.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>68.</b> Salah Alhashim (صلاح الهاشم) \n <b>69.</b> Yasser Al-Faylakawi (ياسر الفيلكاوي) \n <b>70.</b> Khalid Algamdi (خالد الغامدي) \n <b>71.</b> Ali Hajjaj Alsouasi (علي حجاج السويسي) \n <b>72.</b> Ramadan Shakoor (رمضان شكور) \n <b>73.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>74.</b> Nasser Almajed (ناصر الماجد) \n <b>75.</b> Muftah Alsaltany (مفتاح السلطني)  ",parse_mode='HTML' , reply_markup=nav.qorila5)
 

@dp.callback_query_handler(text="Keyingi5")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>76.</b> Ahmad Deban (أحمد ديبان)  \n <b>77.</b> Khalid Al-Shoraimy (خالد الشريمي) \n <b>78.</b> Ustaz Zamri (استاذ زامري) \n <b>79.</b> Haitham Aldukhain (هيثم الدخين) \n <b>80.</b>  Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>81.</b>  Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>82.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>83.</b> Ibrahim Al-Jebreen (ابراهيم الجبرين) \n <b>84.</b>  Shaban Al-Sayiaad (شعبان الصياد) \n <b>85.</b> Waleed Alnaehi (وليد النائحي) \n <b>86.</b> Mohammad Al-Airawy (محمد الأيراوي) \n <b>87.</b> Mohammad Refat (محمد رفعت) \n <b>88.</b> Mohammed Al-Barrak (محمد البراك) \n <b>89.</b> Abdullah Al-Mousa (عبدالله الموسى) \n <b>90.</b> Muftah Alsaltany (مفتاح السلطني)",parse_mode='HTML' , reply_markup=nav.qorila6)
 

@dp.callback_query_handler(text="Keyingi6")
async def sura(message: types.Message):
       
        await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>91.</b> Ahmad Deban (أحمد ديبان) \n <b>92.</b> Rogayah Sulong (رقية سولونق) \n <b>93.</b> Abdulmohsin Al-Obaikan (عبدالمحسن العبيكان) \n <b>94.</b> Rami Aldeais (رامي الدعيس) \n <b>95.</b> Wasel Almethen (واصل المذن) \n <b>96.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>97.</b> Salah Alhashim (صلاح الهاشم) \n <b>98.</b> Ibrahim Aldosari (ابراهيم الدوسري) \n <b>99.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>100.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>101.</b> Abdul Aziz Al-Ahmad (عبدالعزيز الأحمد) \n <b>102.</b> Ibrahim Al-Akdar (إبراهيم الأخضر) \n <b>103.</b> Saleh Alsahood (صالح الصاهود) \n <b>104.</b> Yasser Al-Mazroyee (ياسر المزروعي) \n <b>105.</b> Ali Jaber (علي جابر)",parse_mode='HTML' , reply_markup=nav.qorila7)
 


@dp.callback_query_handler(text="Keyingi7")
async def sura2(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>106.</b> Mohammed Al-Muhasny (محمد المحيسني) \n <b>107.</b> Saidin Abdulrahman (سيدين عبدالرحمن) \n <b>108.</b> Nasser Alosfor (ناصر العصفور) \n <b>109.</b> Abdulrahman Aloosi (عبدالرحمن العوسي) \n <b>110.</b> Mushaf Ibrahim Al-Asiri (مصحف ابراهيم العسيري) \n <b>111.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>112.</b> Bader Alturki (بدر التركي) \n <b>113.</b> Hitham Aljadani (هيثم الجدعاني) \n <b>114.</b> Ibrahim Aljormy (ابراهيم الجرمي) \n <b>115.</b> Sami Al-Dosari (سامي الدوسري) \n <b>116.</b> Jamal Addeen Alzailaie (جمال الدين الزيلعي) \n <b>117.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله) \n <b>118.</b> Salah Musali (صلاح مصلي) \n<b>119.</b> Muftah Alsaltany (مفتاح السلطني) \n<b>120.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n",parse_mode='HTML' , reply_markup=nav.qorila8)
  

@dp.callback_query_handler(text="Keyingi8")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>121.</b> Ahmad Al Nufais (أحمد النفيس) \n <b>122.</b> Salman Alotaibi (سلمان العتيبي) \n <b>123.</b> Abdullah Albuajan (عبدالله البعيجان) \n <b>124.</b> Shaik Abu Bakr Al Shatri (أبوبكر الشاطري) \n <b>125.</b> Abdullah Khayyat (عبدالله خياط) \n <b>126.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>127.</b> Maher Shakhashero (ماهر شخاشيرو) \n <b>128.</b> Younes Souilass (يونس اسويلص) \n <b>129.</b> Mohammad AlMonshed (محمد المنشد) \n <b>130.</b> Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>131.</b> Rodziah Abdulrahman (رضية عبدالرحمن) \n <b>132.</b> Ahmad Alhuthaifi (أحمد الحذيفي) \n <b>133.</b> Mustafa Al-Lahoni (مصطفى اللاهوني) \n <b>134.</b> Mohammad Albukheet (محمد البخيت) \n <b>135.</b> Youssef Edghouch (يوسف الدغوش) \n",parse_mode='HTML' , reply_markup=nav.qorila9)
  

@dp.callback_query_handler(text="Keyingi9")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>136.</b> Muamar (From Indonesia) (معمر الأندونيسي) \n <b>137.</b> Abdullah Kamel (عبدالله كامل) \n <b>138.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>139.</b> Islam Sobhi (إسلام صبحي) \n <b>140.</b> Ali Alhuthaifi (علي الحذيفي) \n <b>141.</b> Ahmad Al-Hawashi (أحمد الحواشي) \n <b>142.</b> Abdullah Qaulan (عبدالله غيلان) \n <b>143.</b> Adel Al-Khalbany (عادل الكلباني) \n <b>144.</b> Hussain Alshaik (حسين آل الشيخ) \n <b>145.</b> Mahmoud Khalil Al-Hussary (محمود خليل ا لحصري) \n <b>146.</b> Hatem Fareed Alwaer (حاتم فريد الواعر) \n <b>147.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>148.</b> Yousef Bin Noah Ahmad (يوسف بن نوح أحمد) \n <b>149.</b> Neamah Al-Hassan (نعمة الحسان) \n <b>150.</b> Bandar Balilah (بندر بليله) \n",parse_mode='HTML' , reply_markup=nav.qorila10)
  

@dp.callback_query_handler(text="Keyingi10")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>151.</b> Akhil Abdulhayy Rawa (أخيل عبدالحي روا) \n <b>152.</b> Ali Alhuthaifi' (علي الحذيفي)  \n <b>153.</b> Wadeea Al-Yamani (وديع اليمني) \n <b>154.</b> Khalid Almohana (خالد المهنا) \n <b>155.</b> Muhammad Abu Sneyna (محمد أبوسنينة )\n <b>156.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>157.</b> Abdulaziz Alasiri (عبدالعزيز العسيري) \n <b>158.</b> Fahad Al-Otaibi (فهد العتيبي) \n <b>159.</b> Ahmad Al-Ajmy - Rewayat Hafs A'n Assem (أحمد بن علي العجمي - رواية حفص عن عاصم) \n <b>160.</b> Abdulmohsen Al-Qasim (عبدالمحسن القاسم) \n <b>161.</b> Jamaan Alosaimi (جمعان العصيمي) \n <b>162.</b> Khaled Al-Qahtani (خالد القحطاني) \n <b>163.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>164.</b> Saud Al-Shuraim (سعود الشريم) \n <b>165.</b> Ibrahem Assadan (ابراهيم السعدان) \n",parse_mode='HTML' , reply_markup=nav.qorila11)

@dp.callback_query_handler(text="Keyingi11")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>166.</b> Mohammed Al-Lohaidan (محمد اللحيدان) \n <b>167.</b> Mohammad Khalil Al-Qari (محمد خليل القارئ) \n <b>168.</b> Nasser Al obaid (ناصر العبيد) \n <b>169.</b> Akasha Kameni  (عكاشة كميني)\n <b>170.</b> Hazza Al-Balushi (هزاع البلوشي) \n <b>171.</b> Abdulbari Mohammad (عبدالبارئ محمد) \n <b>172.</b> Mohammed Jibreel (محمد جبريل) \n <b>173.</b> Majed Al-Zamil (ماجد الزامل) \n <b>174.</b> Peshawa Qadr Al-Kurdi (بيشه وا قادر الكردي) \n <b>175.</b> Abdullah Fahmi (عبدالله فهمي) \n <b>176.</b> Ahmad Saud - Rewayat Hafs A'n Assem (أحمد سعود - رواية حفص عن عاصم) \n <b>177.</b> Abdulhadi Kanakeri (عبدالهادي أحمد كناكري) \n <b>178.</b> Mohammed Hafas Ali (محمد حفص علي) \n <b>179.</b> Khalid Al-Wehabi (خالد الوهيبي) \n <b>180.</b> Muhammed Khairul Anuar (محمد خير النور) \n ",parse_mode='HTML' , reply_markup=nav.qorila12)

@dp.callback_query_handler(text="Keyingi12")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>181.</b> Saleh Al-Habdan - Rewayat Hafs A\'n Assem (صالح الهبدان - رواية حفص عن عاصم) \n <b>182.</b> Othman Al-Ansary (عثمان الأنصاري) \n <b>183.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله)  \n <b>184.</b> Mansour Al-Salemi (منصور السالمي)  \n <b>185.</b> Sapinah Mamat (سابينة مامات)  \n <b>186.</b> Khalid Alsharekh (خالد الشارخ)  \n <b>187.</b> Alashri Omran (العشري عمران)  \n <b>188.</b> Muftah Alsaltany (مفتاح السلطني)  \n <b>189.</b> Mousa Bilal (موسى بلال)  \n <b>190.</b> Saleh Al-Talib (صالح آل طالب)  \n <b>191.</b> Wishear Hayder Arbili (وشيار حيدر اربيلي)  \n <b>192.</b> Ahmad Nauina (أحمد نعينع)  \n <b>193.</b> Ali Abo-Hashim - Rewayat Hafs A\'n Assem (علي أبو هاشم - رواية حفص عن عاصم)  \n <b>194.</b> Alfateh Alzubair (الفاتح محمد الزبير)  \n <b>195.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد)  \n ",parse_mode='HTML' , reply_markup=nav.qorila13)
  

@dp.callback_query_handler(text="Keyingi13")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>196.</b> Tareq Abdulgani daawob' (طارق عبدالغني دعوب)   \n <b>197.</b> Mohammad Al-Tablaway (محمد الطبلاوي)   \n <b>198.</b> Abdullah Al-Khalaf (عبدالله الخلف)   \n <b>199.</b> Yasser Salamah (ياسر سلامة)  \n <b>200.</b> Rachid Belalya (رشيد بلعالية)  \n <b>201.</b> Mohammed Osman Khan (محمد عثمان خان)  \n <b>202.</b> Mustafa raad Alazawy (مصطفى رعد العزاوي)  \n <b>203.</b> Abdulrasheed Soufi (عبدالرشيد صوفي)  \n <b>204.</b> Addokali Mohammad Alalim' (الدوكالي محمد العالم)  \n <b>205.</b> Mohammad Rashad Alshareef (محمد رشاد الشريف)  \n <b>206.</b> Muhammad Al-Hafiz (محمد الحافظ)  \n <b>207.</b> Abdulbari Mohammad (عبدالبارئ محمد)  \n <b>208.</b> Omar Al Darweez (عمر الدريويز)  \n <b>209.</b> Ahmad Saber (أحمد صابر) \n <b>210.</b> Hani Arrifai (هاني الرفاعي)  \n ",parse_mode='HTML' , reply_markup=nav.qorila14)


@dp.callback_query_handler(text="Keyingi14")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>211.</b> Abdulghani Abdullah (عبدالغني عبدالله) \n <b>212.</b> Aloyoon Al-Koshi (العيون الكوشي) \n <b>213.</b> Tawfeeq As-Sayegh (توفيق الصايغ) \n <b>214.</b> Jamal Shaker Abdullah (جمال شاكر عبدالله) \n <b>215.</b> Khalid Al-Jileel (خالد الجليل) \n <b>216.</b> Khalid Abdulkafi (خالد عبدالكافي) \n <b>217.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>218.</b> Dawood Hamza (داود حمزة) \n <b>219.</b> Rasheed Ifrad (رشيد إفراد) \n <b>220.</b> Alhusayni Al-Azazi (الحسيني العزازي) \n <b>221.</b> Zakaria Hamamah (زكريا حمامة) \n",parse_mode='HTML' , reply_markup=nav.qorila15)
  
   
     

   
  
@dp.callback_query_handler(text="btnsura")
async def sura(message: types.Message):
       
       await message.message.edit_text(f" <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n{cd} " , reply_markup=nav.allsuralarMaherAlMeaqli, parse_mode='html')
     
@dp.callback_query_handler(text=f"sura{1}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       bn = markdown.hide_link('https://t.me/b148uz/42')
       await bot.send_message(message.from_user.id, f"{bn} \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1, disable_web_page_preview=False)

@dp.callback_query_handler(text=f"sura{2}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/43'>ㅤ</a> \n <b>Nomi:</b>  Al-Baqara (سُورَةُ البَقَرَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 2:00:00 \n <b>Oyatlar soni:</b> 286 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)

@dp.callback_query_handler(text=f"sura{3}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/44'>ㅤ</a> \n <b>Nomi:</b>  Aal-i-Imraan (سُورَةُ آلِ عِمۡرَانَ) \n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:09:26 \n <b>Oyatlar soni:</b> 200 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)

@dp.callback_query_handler(text=f"sura{4}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/45'>ㅤ</a> \n <b>Nomi:</b> An-Nisaa (سُورَةُ النِّسَاءِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:04:37 \n <b>Oyatlar soni:</b> 176 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)



@dp.callback_query_handler(text=f"sura{5}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/46'>ㅤ</a> \n <b>Nomi:</b>  Al-Maaida (سُورَةُ المَائـِدَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 51:27 \n <b>Oyatlar soni:</b> 120 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)

@dp.callback_query_handler(text=f"sura{6}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/47'>ㅤ</a> \n <b>Nomi:</b> Al-An'aam (سُورَةُ الأَنۡعَامِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b>  50:15 \n <b>Oyatlar soni:</b> 165 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{7}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/48'>ㅤ</a> \n <b>Nomi:</b> Al-A'raaf (سُورَةُ الأَعۡرَافِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b>  58:41 \n <b>Oyatlar soni:</b> 206 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1) 
@dp.callback_query_handler(text=f"sura{8}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/49'>ㅤ</a> \n <b>Nomi:</b> Al-Anfaal (سُورَةُ الأَنفَالِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 21:49 \n <b>Oyatlar soni:</b> 75 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{9}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/50'>ㅤ</a> \n <b>Nomi:</b> At-Tawba (سُورَةُ التَّوۡبَةِ\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 43:12 \n <b>Oyatlar soni:</b> 129 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{10}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/51'>ㅤ</a> \n <b>Nomi:</b> Yunus (سُورَةُ يُونُسَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 30:40 \n <b>Oyatlar soni:</b> 109 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{11}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/52'>ㅤ</a> \n <b>Nomi:</b> Hud (سُورَةُ هُودٍ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 32:59 \n <b>Oyatlar soni:</b> 123 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{12}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/53'>ㅤ</a> \n <b>Nomi:</b> Yusuf (سُورَةُ يُوسُفَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 29:59 \n <b>Oyatlar soni:</b> 111 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{13}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/54'>ㅤ</a> \n <b>Nomi:</b>  Ar-Ra'd (سُورَةُ الرَّعۡدِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 14:09 \n <b>Oyatlar soni:</b> 43 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{14}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/55'>ㅤ</a> \n <b>Nomi:</b> Ibrahim (سُورَةُ إِبۡرَاهِيمَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 13:34 \n <b>Oyatlar soni:</b> 52 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text=f"sura{15}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/56'>ㅤ</a> \n <b>Nomi:</b> Al-Hijr (سُورَةُ الحِجۡرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 10:55 \n <b>Oyatlar soni:</b> 99 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
@dp.callback_query_handler(text="MaherAlMeaqlisuralarhammasi1")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       for b in range (42,56):
            await bot.send_message(message.from_user.id,f"<a href='https://t.me/b148uz/{b}'>ㅤ</a>",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
     






















@dp.callback_query_handler(text="MaherAlMeaqlisuralarhammasi7")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       for n in range (135,160):
            await bot.send_message(message.from_user.id,f"<a href='https://t.me/b148uz/{n}'>ㅤ</a>",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)
    

@dp.callback_query_handler(text="MaherAlMeaqlisuralarhammasi6")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       for n in range (119,135):
            await bot.send_message(message.from_user.id,f"<a href='https://t.me/b148uz/{n}'>ㅤ</a>",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)
    

@dp.callback_query_handler(text="MaherAlMeaqlisuralarhammasi5")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       for n in range (105,131):
            await bot.send_message(message.from_user.id,f"<a href='https://t.me/b148uz/{n}'>ㅤ</a>",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)
    
@dp.callback_query_handler(text="MaherAlMeaqlisuralarhammasi4")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       for n in range (89,104):
            await bot.send_message(message.from_user.id,f"<a href='https://t.me/b148uz/{n}'>ㅤ</a>",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli4reply)
    
@dp.callback_query_handler(text="MaherAlMeaqlisuralarhammasi3")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       for n in range (75,91):
            await bot.send_message(message.from_user.id,f"<a href='https://t.me/b148uz/{n}'>ㅤ</a>",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralarhammasi2")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
   
       list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
       for v in list2:
              print(v)
       #59 74
       for n in range (1,5):
           if n == list2.index(v):
                   await bot.send_message(message.from_user.id,f"<a href='https://t.me/b148uz/{n}'>ㅤ</a>",parse_mode='HTML' )
       else:
                  await bot.send_message(message.from_user.id , f'{list2}')
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2reply)
    
@dp.callback_query_handler(text="keyingiMaherAlMeaqli2")
async def sura(message: types.Message):
       
       await message.message.edit_text( f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd2}",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli2)
   
@dp.callback_query_handler(text="keyingiMaherAlMeaqli4")
async def sura(message: types.Message):
       
       await message.message.edit_text( f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd4}",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli4)
  
#_________________________________________________________________________________________________________

@dp.callback_query_handler(text=f"sura2{16}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/59'>ㅤ</a> \n <b>Nomi:</b> An-Nahl (سُورَةُ النَّحۡلِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 33:38 \n <b>Oyatlar soni:</b> 128 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)

@dp.callback_query_handler(text=f"sura2{17}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/60'>ㅤ</a> \n <b>Nomi:</b> Al-Israa (سُورَةُ الإِسۡرَاءِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 26:01 \n <b>Oyatlar soni:</b> 111 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)

@dp.callback_query_handler(text=f"sura2{18}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/61'>ㅤ</a> \n <b>Nomi:</b> Al-Kahf (سُورَةُ الكَهۡفِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 23:13 \n <b>Oyatlar soni:</b> 110 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)

@dp.callback_query_handler(text=f"sura2{19}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/62'>ㅤ</a> \n <b>Nomi:</b> Maryam (سُورَةُ مَرۡيَمَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 17:40 \n <b>Oyatlar soni:</b> 98 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)



@dp.callback_query_handler(text=f"sura2{20}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/63'>ㅤ</a> \n <b>Nomi:</b>  Taa-Haa (سُورَةُ طه)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 23:49 \n <b>Oyatlar soni:</b> 135 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)

@dp.callback_query_handler(text=f"sura2{21}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/64'>ㅤ</a> \n <b>Nomi:</b> Al-Anbiyaa (سُورَةُ الأَنبِيَاءِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 20:18 \n <b>Oyatlar soni:</b> 112 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{22}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/65'>ㅤ</a> \n <b>Nomi:</b> Al-Hajj (سُورَةُ الحَجِّ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b>  22:20 \n <b>Oyatlar soni:</b> 78 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2) 
@dp.callback_query_handler(text=f"sura2{23}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/66'>ㅤ</a> \n <b>Nomi:</b>  Al-Muminoon (سُورَةُ المُؤۡمِنُونَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 18:24 \n <b>Oyatlar soni:</b> 118 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{24}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/67'>ㅤ</a> \n <b>Nomi:</b> An-Noor (سُورَةُ النُّورِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 25:30 \n <b>Oyatlar soni:</b> 64 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{25}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/68'>ㅤ</a> \n <b>Nomi:</b> Al-Furqaan (سُورَةُ الفُرۡقَانِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 15:50 \n <b>Oyatlar soni:</b> 77 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{26}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/69'>ㅤ</a> \n <b>Nomi:</b> Ash-Shu'araa (سُورَةُ الشُّعَرَاءِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 24:26 \n <b>Oyatlar soni:</b> 227 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{27}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/70'>ㅤ</a> \n <b>Nomi:</b> An-Naml (سُورَةُ النَّمۡلِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 20:12 \n <b>Oyatlar soni:</b> 93 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{28}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/71'>ㅤ</a> \n <b>Nomi:</b> Al-Qasas (سُورَةُ القَصَصِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 25:33 \n <b>Oyatlar soni:</b> 88 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{29}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/72'>ㅤ</a> \n <b>Nomi:</b> Al-Ankaboot (سُورَةُ العَنكَبُوتِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 15:45 \n <b>Oyatlar soni:</b> 69 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)
@dp.callback_query_handler(text=f"sura2{30}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/73'>ㅤ</a> \n <b>Nomi:</b> Ar-Room (سُورَةُ الرُّومِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 13:59 \n <b>Oyatlar soni:</b> 60 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' )
       await bot.send_message(message.from_user.id,"📜 Suralar ro'yxatiga qaytish uchun orqagani bosing",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli2)

#_________________________________________________________________________________________________________________________


@dp.callback_query_handler(text="keyingiMaherAlMeaqli3")
async def sura(message: types.Message):
       
       await message.message.edit_text( f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n{cd3}",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli3)




   
@dp.callback_query_handler(text=f"sura3{31}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/74'>ㅤ</a> \n <b>Nomi:</b> Luqman (سُورَةُ لُقۡمَانَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 8:45\n <b>Oyatlar soni:</b> 34 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)


@dp.callback_query_handler(text=f"sura3{32}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/75'>ㅤ</a> \n <b>Nomi:</b> As-Sajda (سُورَةُ السَّجۡدَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:20 \n <b>Oyatlar soni:</b> 30 \n <b>Nozil bo\'lgan yeri: Meccan</b> ",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)


@dp.callback_query_handler(text=f"sura3{33}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/76'>ㅤ</a> \n <b>Nomi:</b> Al-Ahzaab (سُورَةُ الأَحۡزَابِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b>  22:13 \n <b>Oyatlar soni:</b> 73 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)



@dp.callback_query_handler(text=f"sura3{34}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/77'>ㅤ</a> \n <b>Nomi:</b>  Saba (سُورَةُ سَبَإٍ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 14:47 \n <b>Oyatlar soni:</b> 54 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)


m = 'Meccan'
m2 = 'Madina'

@dp.callback_query_handler(text=f"sura3{35}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/78'>ㅤ</a> \n <b>Nomi:</b> Faatir (سُورَةُ فَاطِرٍ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 13:22 \n <b>Oyatlar soni:</b> 45 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{36}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/79'>ㅤ</a> \n <b>Nomi:</b> Yaseen (سُورَةُ يسٓ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b>  11:37\n <b>Oyatlar soni:</b>  83\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{38}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/80'>ㅤ</a> \n <b>Nomi:</b> Saad (سُورَةُ صٓ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 12:30\n <b>Oyatlar soni:</b> 88 \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{37}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/81'>ㅤ</a> \n <b>Nomi:</b> As-Saaffaat (سُورَةُ الصَّافَّاتِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b>  15:32\n <b>Oyatlar soni:</b> 182 \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{39}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/82'>ㅤ</a> \n <b>Nomi:</b> Az-Zumar (سُورَةُ الزُّمَرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 18:44 \n <b>Oyatlar soni:</b> 75 \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{40}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/83'>ㅤ</a> \n <b>Nomi:</b> Ghafir (سُورَةُ غَافِرٍ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 20:13\n <b>Oyatlar soni:</b> 85 \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{41}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/84'>ㅤ</a> \n <b>Nomi:</b> Fussilat (سُورَةُ فُصِّلَتۡ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 14:21 \n <b>Oyatlar soni:</b> 54 \n <b>Nozil bo\'lgan yeri: {m}</b> ",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{42}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/85'>ㅤ</a> \n <b>Nomi:</b> Ash-Shura (سُورَةُ الشُّورَىٰ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 14:28 \n <b>Oyatlar soni:</b> 53 \n <b>Nozil bo\'lgan yeri: {m}</b> ",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{43}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/86'>ㅤ</a> \n <b>Nomi:</b> Az-Zukhruf (سُورَةُ الزُّخۡرُفِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 15:52 \n <b>Oyatlar soni:</b> 89 \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{44}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/87'>ㅤ</a> \n <b>Nomi:</b>  Ad-Dukhaan (سُورَةُ الدُّخَانِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:37 \n <b>Oyatlar soni:</b> 59 \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




@dp.callback_query_handler(text=f"sura3{45}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/88'>ㅤ</a> \n <b>Nomi:</b> Al-Jaathiya (سُورَةُ الجَاثِيَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 9:11 \n <b>Oyatlar soni:</b> 37\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli3reply)




#_______________________________________________________________________________________________________________________


@dp.callback_query_handler(text=f"sura4{46}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/89'>ㅤ</a> \n <b>Nomi:</b> Al-Ahqaf (سُورَةُ الأَحۡقَافِ) \n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 11:03\n <b>Oyatlar soni:</b> 35 \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)





@dp.callback_query_handler(text=f"sura4{47}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/90'>ㅤ</a> \n <b>Nomi:</b>  Muhammad (سُورَةُ مُحَمَّدٍ) \n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 9:50\n <b>Oyatlar soni:</b> 38\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{48}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/91'>ㅤ</a> \n <b>Nomi:</b>  Al-Fath (سُورَةُ الفَتۡحِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 9:21\n <b>Oyatlar soni:</b> 29\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{49}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/92'>ㅤ</a> \n <b>Nomi:</b>  Al-Hujuraat (سُورَةُ الحُجُرَاتِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:11\n <b>Oyatlar soni:</b> 18\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{50}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/93'>ㅤ</a> \n <b>Nomi:</b> Qaaf (سُورَةُ قٓ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:22\n <b>Oyatlar soni:</b> 45\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{51}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/94'>ㅤ</a> \n <b>Nomi:</b> Adh-Dhaariyat (سُورَةُ الذَّارِيَاتِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:24\n <b>Oyatlar soni:</b> 60\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{52}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/95'>ㅤ</a> \n <b>Nomi:</b> At-Tur (سُورَةُ الطُّورِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 5:41\n <b>Oyatlar soni:</b> 49\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{53}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/96'>ㅤ</a> \n <b>Nomi:</b> An-Najm (سُورَةُ النَّجۡمِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:00\n <b>Oyatlar soni:</b> 62\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{54}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/97'>ㅤ</a> \n <b>Nomi:</b> Al-Qamar (سُورَةُ القَمَرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:04\n <b>Oyatlar soni:</b> 55\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{55}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/98'>ㅤ</a> \n <b>Nomi:</b>  Ar-Rahmaan (سُورَةُ الرَّحۡمَٰن)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 7:20\n <b>Oyatlar soni:</b> 78\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)






@dp.callback_query_handler(text=f"sura4{56}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/99'>ㅤ</a> \n <b>Nomi:</b>  Al-Waaqia (سُورَةُ الوَاقِعَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 8:04\n <b>Oyatlar soni:</b> 96\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)




@dp.callback_query_handler(text=f"sura4{57}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/100'>ㅤ</a> \n <b>Nomi:</b> Al-Hadid (سُورَةُ الحَدِيدِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 9:59\n <b>Oyatlar soni:</b> 29\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)





@dp.callback_query_handler(text=f"sura4{58}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/101'>ㅤ</a> \n <b>Nomi:</b> Al-Mujaadila (سُورَةُ المُجَادلَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 8:24\n <b>Oyatlar soni:</b> 22\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)



@dp.callback_query_handler(text=f"sura4{59}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/102'>ㅤ</a> \n <b>Nomi:</b> Al-Hashr (سُورَةُ الحَشۡرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 8:52\n <b>Oyatlar soni:</b> 24\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)



@dp.callback_query_handler(text=f"sura4{60}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
              
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/103'>ㅤ</a> \n <b>Nomi:</b> Al-Mumtahana (سُورَةُ المُمۡتَحنَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 6:26\n <b>Oyatlar soni:</b> 13\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli5reply)

#__________________________________________________________________________________________________________________
@dp.callback_query_handler(text=f"sura5{61}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/104'>ㅤ</a> \n <b>Nomi:</b> As-Saff (سُورَةُ الصَّفِّ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 4:11\n <b>Oyatlar soni:</b> 14\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{62}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/105'>ㅤ</a> \n <b>Nomi:</b> Al-Jumu'a (سُورَةُ الجُمُعَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:01\n <b>Oyatlar soni:</b> 11\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{63}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/106'>ㅤ</a> \n <b>Nomi:</b> Al-Munaafiqoon (سُورَةُ المُنَافِقُونَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:31\n <b>Oyatlar soni:</b> 11\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{64}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/107'>ㅤ</a> \n <b>Nomi:</b> At-Taghaabun (سُورَةُ التَّغَابُنِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 4:54\n <b>Oyatlar soni:</b> 18\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{65}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/108'>ㅤ</a> \n <b>Nomi:</b> At-Talaaq (سُورَةُ الطَّلَاقِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 5:00\n <b>Oyatlar soni:</b> 12\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{66}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/109'>ㅤ</a> \n <b>Nomi:</b> At-Tahrim (سُورَةُ التَّحۡرِيمِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 4:36\n <b>Oyatlar soni:</b> 12\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{67}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/110'>ㅤ</a> \n <b>Nomi:</b> Al-Mulk (سُورَةُ المُلۡكِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 5:26\n <b>Oyatlar soni:</b> 30\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{68}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/111'>ㅤ</a> \n <b>Nomi:</b> Al-Qalam (سُورَةُ القَلَمِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 5:30\n <b>Oyatlar soni:</b> 52\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{69}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/112'>ㅤ</a> \n <b>Nomi:</b> Al-Haaqqa (سُورَةُ الحَاقَّةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 5:04\n <b>Oyatlar soni:</b> 52\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{70}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/113'>ㅤ</a> \n <b>Nomi:</b> Al-Ma'aarij (سُورَةُ المَعَارِجِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 4:11\n <b>Oyatlar soni:</b> 44\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{71}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/114'>ㅤ</a> \n <b>Nomi:</b>  Nooh (سُورَةُ نُوحٍ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:57\n <b>Oyatlar soni:</b> 28\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{72}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/115'>ㅤ</a> \n <b>Nomi:</b> Al-Jinn (سُورَةُ الجِنِّ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 4:42\n <b>Oyatlar soni:</b> 28\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{73}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/116'>ㅤ</a> \n <b>Nomi:</b> Al-Muzzammil (سُورَةُ المُزَّمِّلِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:35\n <b>Oyatlar soni:</b> 20\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{74}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/117'>ㅤ</a> \n <b>Nomi:</b> \n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> \n <b>Oyatlar soni:</b> \n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

@dp.callback_query_handler(text=f"sura5{75}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/118'>ㅤ</a> \n <b>Nomi:</b> Al-Qiyaama (سُورَةُ القِيَامَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 2:56\n <b>Oyatlar soni:</b> 40\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli6reply)

#_____________________________________________________________________________________________________________________________________________________________________#

@dp.callback_query_handler(text=f"sura6{76}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/119'>ㅤ</a> \n <b>Nomi:</b> Al-Insaan (سُورَةُ الإِنسَانِ) \n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 4:58\n <b>Oyatlar soni:</b> 31\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)


@dp.callback_query_handler(text=f"sura6{77}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/120'>ㅤ</a> \n <b>Nomi:</b>  Al-Mursalaat (سُورَةُ المُرۡسَلَاتِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:30\n <b>Oyatlar soni:</b> 50\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)


@dp.callback_query_handler(text=f"sura6{78}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/121'>ㅤ</a> \n <b>Nomi:</b> An-Naba (سُورَةُ النَّبَإِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:35\n <b>Oyatlar soni:</b> 40\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{79}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/122'>ㅤ</a> \n <b>Nomi:</b>  An-Naazi'aat (سُورَةُ النَّازِعَاتِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:15\n <b>Oyatlar soni:</b> 46\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{80}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/123'>ㅤ</a> \n <b>Nomi:</b>  Abasa (سُورَةُ عَبَسَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 2:50\n <b>Oyatlar soni:</b> 42\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{81}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/124'>ㅤ</a> \n <b>Nomi:</b> At-Takwir (سُورَةُ التَّكۡوِيرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:54\n <b>Oyatlar soni:</b> 29\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{82}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/125'>ㅤ</a> \n <b>Nomi:</b> Al-Infitaar (سُورَةُ الانفِطَارِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:29\n <b>Oyatlar soni:</b> 19\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{83}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/126'>ㅤ</a> \n <b>Nomi:</b> Al-Mutaffifin (سُورَةُ المُطَفِّفِينَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 3:11\n <b>Oyatlar soni:</b> 36\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{84}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/127'>ㅤ</a> \n <b>Nomi:</b> Al-Inshiqaaq (سُورَةُ الانشِقَاقِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:55\n <b>Oyatlar soni:</b> 25\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{85}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/128'>ㅤ</a> \n <b>Nomi:</b> Al-Burooj (سُورَةُ البُرُوجِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:57\n <b>Oyatlar soni:</b> 22\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)

@dp.callback_query_handler(text=f"sura6{86}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/129'>ㅤ</a> \n <b>Nomi:</b> At-Taariq (سُورَةُ الطَّارِقِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:08\n <b>Oyatlar soni:</b> 17\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)


@dp.callback_query_handler(text=f"sura6{87}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/130'>ㅤ</a> \n <b>Nomi:</b> Al-A'laa (سُورَةُ الأَعۡلَىٰ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:20\n <b>Oyatlar soni:</b> 19\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)




@dp.callback_query_handler(text=f"sura6{88}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/131'>ㅤ</a> \n <b>Nomi:</b> Al-Ghaashiya (سُورَةُ الغَاشِيَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:39\n <b>Oyatlar soni:</b> 26\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)




@dp.callback_query_handler(text=f"sura6{89}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/132'>ㅤ</a> \n <b>Nomi:</b> Al-Fajr (سُورَةُ الفَجۡرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 2:35\n <b>Oyatlar soni:</b> 30\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)




@dp.callback_query_handler(text=f"sura6{90}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/133'>ㅤ</a> \n <b>Nomi:</b> Al-Balad (سُورَةُ البَلَدِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:33\n <b>Oyatlar soni:</b> 20\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli7reply)



#____________________________________________________________________________________________________________________________________________________________________________________________#



@dp.callback_query_handler(text=f"sura7{91}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/134'>ㅤ</a> \n <b>Nomi:</b> Ash-Shams (سُورَةُ الشَّمۡسِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:03\n <b>Oyatlar soni:</b> 15\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)



@dp.callback_query_handler(text=f"sura7{92}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/135'>ㅤ</a> \n <b>Nomi:</b> Al-Lail (سُورَةُ اللَّيۡلِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:24\n <b>Oyatlar soni:</b> 21\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{93}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/136'>ㅤ</a> \n <b>Nomi:</b> Ad-Dhuhaa (سُورَةُ الضُّحَىٰ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:49\n <b>Oyatlar soni:</b> 11\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{94}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/137'>ㅤ</a> \n <b>Nomi:</b> Ash-Sharh (سُورَةُ الشَّرۡحِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:31\n <b>Oyatlar soni:</b> 8\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{95}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/138'>ㅤ</a> \n <b>Nomi:</b> At-Tin (سُورَةُ التِّينِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:41\n <b>Oyatlar soni:</b> 8\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{96}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/139'>ㅤ</a> \n <b>Nomi:</b> Al-Alaq (سُورَةُ العَلَقِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:15\n <b>Oyatlar soni:</b> 19\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{97}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/140'>ㅤ</a> \n <b>Nomi:</b> Al-Qadr (سُورَةُ القَدۡرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:33\n <b>Oyatlar soni:</b> 5\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{98}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/141'>ㅤ</a> \n <b>Nomi:</b> Al-Bayyina (سُورَةُ البَيِّنَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 1:37\n <b>Oyatlar soni:</b> 8\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{99}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/142'>ㅤ</a> \n <b>Nomi:</b> Az-Zalzala (سُورَةُ الزَّلۡزَلَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:46\n <b>Oyatlar soni:</b> 8\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)



@dp.callback_query_handler(text=f"sura7{100}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/143'>ㅤ</a> \n <b>Nomi:</b> Al-Aadiyaat (سُورَةُ العَادِيَاتِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:48\n <b>Oyatlar soni:</b> 11\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{101}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/144'>ㅤ</a> \n <b>Nomi:</b> Al-Qaari'a (سُورَةُ القَارِعَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:45\n <b>Oyatlar soni:</b> 11\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{102}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/145'>ㅤ</a> \n <b>Nomi:</b> At-Takaathur (سُورَةُ التَّكَاثُرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:35\n <b>Oyatlar soni:</b> 8\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{103}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/146'>ㅤ</a> \n <b>Nomi:</b> Al-Asr (سُورَةُ العَصۡرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:21\n <b>Oyatlar soni:</b> 3\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{104}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/147'>ㅤ</a> \n <b>Nomi:</b> Al-Humaza (سُورَةُ الهُمَزَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:43\n <b>Oyatlar soni:</b> 9\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{105}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/148'>ㅤ</a> \n <b>Nomi:</b> Al-Fil (سُورَةُ الفِيلِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:31\n <b>Oyatlar soni:</b> 5\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{106}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/149'>ㅤ</a> \n <b>Nomi:</b> Quraish (سُورَةُ قُرَيۡشٍ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:26\n <b>Oyatlar soni:</b> 4\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{107}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/150'>ㅤ</a> \n <b>Nomi:</b> Al-Maa'un (سُورَةُ المَاعُونِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:33\n <b>Oyatlar soni:</b> 7\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{108}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/151'>ㅤ</a> \n <b>Nomi:</b> Al-Kawthar (سُورَةُ الكَوۡثَرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:19\n <b>Oyatlar soni:</b> 3\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{109}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/152'>ㅤ</a> \n <b>Nomi:</b> Al-Kaafiroon (سُورَةُ الكَافِرُونَ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:34\n <b>Oyatlar soni:</b> 6\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)


@dp.callback_query_handler(text=f"sura7{110}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/153'>ㅤ</a> \n <b>Nomi:</b> An-Nasr (سُورَةُ النَّصۡرِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:25\n <b>Oyatlar soni:</b> 3\n <b>Nozil bo\'lgan yeri:</b> {m2}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)


@dp.callback_query_handler(text=f"sura7{111}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/154'>ㅤ</a> \n <b>Nomi:</b> Al-Masad (سُورَةُ المَسَدِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:32\n <b>Oyatlar soni:</b> 5\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{112}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/155'>ㅤ</a> \n <b>Nomi:</b> Al-Ikhlaas (سُورَةُ الإِخۡلَاصِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:17\n <b>Oyatlar soni:</b> 4\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{113}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/156'>ㅤ</a> \n <b>Nomi:</b> Al-Falaq (سُورَةُ الفَلَقِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:25\n <b>Oyatlar soni:</b> 5\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)

@dp.callback_query_handler(text=f"sura7{114}")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
                     
       await bot.send_message(message.from_user.id, f"<a href='https://t.me/b148uz/157'>ㅤ</a> \n <b>Nomi:</b> An-Naas (سُورَةُ النَّاسِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:30\n <b>Oyatlar soni:</b> 6\n <b>Nozil bo\'lgan yeri:</b> {m}",parse_mode='HTML')
       await bot.send_message(message.from_user.id,f"{orqaga}",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli8reply)


@dp.callback_query_handler(text="keyingiMaherAlMeaqli5")
async def sura(message: types.Message):
       
       await message.message.edit_text( f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n{cd5}",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli5)





@dp.callback_query_handler(text="keyingiMaherAlMeaqli6")
async def sura(message: types.Message):
       
       await message.message.edit_text( f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd6}",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli6)
  



@dp.callback_query_handler(text="keyingiMaherAlMeaqli7")
async def sura(message: types.Message):
       
       await message.message.edit_text( f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd7}",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli7)
  









@dp.callback_query_handler(text="Keyingi13")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>196.</b> Tareq Abdulgani daawob' (طارق عبدالغني دعوب)   \n <b>197.</b> Mohammad Al-Tablaway (محمد الطبلاوي)   \n <b>198.</b> Abdullah Al-Khalaf (عبدالله الخلف)   \n <b>199.</b> Yasser Salamah (ياسر سلامة)  \n <b>200.</b> Rachid Belalya (رشيد بلعالية)  \n <b>201.</b> Mohammed Osman Khan (محمد عثمان خان)  \n <b>202.</b> Mustafa raad Alazawy (مصطفى رعد العزاوي)  \n <b>203.</b> Abdulrasheed Soufi (عبدالرشيد صوفي)  \n <b>204.</b> Addokali Mohammad Alalim' (الدوكالي محمد العالم)  \n <b>205.</b> Mohammad Rashad Alshareef (محمد رشاد الشريف)  \n <b>206.</b> Muhammad Al-Hafiz (محمد الحافظ)  \n <b>207.</b> Abdulbari Mohammad (عبدالبارئ محمد)  \n <b>208.</b> Omar Al Darweez (عمر الدريويز)  \n <b>209.</b> Ahmad Saber (أحمد صابر) \n <b>210.</b> Hani Arrifai (هاني الرفاعي)  \n ",parse_mode='HTML' , reply_markup=nav.qorila14)

#shu yerdan 17 boshlanadi 



@dp.callback_query_handler(text="ortgaMaherAlMeaqli")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await message.message.edit_text(f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli)

@dp.callback_query_handler(text="ortgaMaherAlMeaqli3")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await message.message.edit_text(f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd2} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli2)

@dp.callback_query_handler(text="ortgaMaherAlMeaqli4")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await message.message.edit_text(f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd3} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli3)

@dp.callback_query_handler(text="ortgaMaherAlMeaqli5")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await message.message.edit_text(f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd4} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli4)

@dp.callback_query_handler(text="ortgaMaherAlMeaqli6")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await message.message.edit_text(f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd5} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli5)
        

@dp.callback_query_handler(text="ortgaMaherAlMeaqli7")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await message.message.edit_text(f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd6} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli6)


@dp.callback_query_handler(text="ortgaMaherAlMeaqli8")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await message.message.edit_text(f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n {cd7} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli7)
                

@dp.callback_query_handler(text="ortgaMaherAlMeaqlimenu")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي)",parse_mode='HTML' , reply_markup=nav.oyatsura)
  












  
@dp.callback_query_handler(text="btn1")
async def sura(query: types.CallbackQuery):
       await bot.delete_message(query.from_user.id,  query.message.message_id)
       await query.message.answer(f"<i> <b>Tanlangan qori :</b> </i> Maher Al Meaqli (ماهر المعيقلي)",parse_mode="html",reply_markup=nav.oyatsura)

  




























 
@dp.callback_query_handler(text="obshiyortga")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)




@dp.callback_query_handler(text="ortga")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id , "Qorilarni tanglang 🤲",parse_mode='HTML' , reply_markup=nav.qori)

 
@dp.callback_query_handler(text="ortga2")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)

 
@dp.callback_query_handler(text="ortga2a")
async def sura(message: types.Message):
       
      await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)


 
@dp.callback_query_handler(text="ortga22a")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________• </b> \n  \n <b>16.</b> Saad Al-Ghamdi (سعد الغامدي) \n <b>17.</b> Khalid Abdulkafi (خالد عبدالكافي) \n <b>18. </b>Tawfeeq As-Sayegh (توفيق الصايغ) \n <b>19.</b> Adel Ryyan (عادل ريان) \n <b>20.</b> Zakaria Hamamah (زكريا حمامة) \n <b>21.</b> Slaah Bukhatir (القارئ صلاح بو خاطر) \n <b>22.</b> Abdelbari Al-Toubayti (عبدالبارئ الثبيتي) \n <b>23.</b> Abdulaziz Az-Zahrani (عبدالعزيز الزهراني) \n <b>24.</b> Abdullah Al-Burimi (عبدالله البريمي) \n <b>25.</b> Abdullah Al-Mattrod (عبدالله المطرود) \n <b>26.</b> Abdullah Al-Johany (عبدالله عواد الجهني) \n <b>27.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>28.</b> Abdulmohsin Al-Harthy (عبدالمحسن الحارثي) \n <b>29.</b> Abdulmohsin Al-Askar (عبدالمحسن العسكر) \n <b>30.</b> Salah Alhashim (صلاح الهاشم)",parse_mode='HTML' , reply_markup=nav.qorila2 )




@dp.callback_query_handler(text="ortga3")
async def sura(message: types.Message):
       
      await message.message.edit_text(" <b>•______________________________________•  </b> \n \n <b>31.</b> Salah Alhashim (صلاح الهاشم) \n <b>32.</b> Alhusayni Al-Azazi (الحسيني العزازي) \n <b>33.</b> Khalid Al-Jileel (خالد الجليل)\n <b>34.</b> Fawaz Alkabi (فواز الكعبي) \n <b>35.</b> Salah Albudair (صلاح البدير) \n <b>36.</b> Fahad Al-Kandari (فهد الكندري) \n <b>37.</b> Fares Abbad (فارس عباد) \n <b>38.</b> Nabil Al Rifay (نبيل الرفاعي) \n <b>39.</b> Walid Al-Dulaimi (وليد الدليمي) \n <b>40.</b> Yasser Al-Dosari (ياسر الدوسري) \n <b>41.</b> Yasser Al-Qurashi (ياسر القرشي) \n <b>42.</b> Yahya Hawwa (يحيى حوا) \n <b>43.</b> Yousef Alshoaey (يوسف الشويعي) \n <b>44.</b> Majed Al-Enezi (ماجد العنزي) \n <b>45.</b> Rachid Belalya (رشيد بلعالية)" , parse_mode='HTML', reply_markup=nav.qorila3)



@dp.callback_query_handler(text="ortga4")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>46.</b> Alzain Mohammad Ahmad (الزين محمد أحمد) \n <b>47.</b> Al-Qaria Yassen (القارئ ياسين) \n <b>48.</b> Rachid Belalya (رشيد بلعالية) \n <b>49.</b> Rasheed Ifrad (رشيد إفراد) \n <b>50.</b> Hamad Al Daghriri (حمد الدغريري) \n <b>51.</b> Lafi Al-Oni (لافي العوني) \n <b>52.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>53.</b> Abdullah Al-Kandari (عبدالله الكندري) \n <b>54.</b> Saber Abdulhakm (صابر عبدالحكم) \n <b>55.</b> Ahmed Amer (أحمد عامر) \n <b>56.</b> Malik shaibat Alhamed (مالك شيبة الحمد) \n <b>57.</b> Abdulmajeed Al-Arkani (عبدالمجيد الأركاني) \n <b>58.</b> Mustafa Ismail (مصطفى إسماعيل) \n <b>59.</b> Ahmad Shaheen (أحمد خليل شاهين) \n <b>60.</b> Omar Al-Qazabri' (عمر القزابري)",parse_mode='HTML' , reply_markup=nav.qorila4)

@dp.callback_query_handler(text="ortga5")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>61.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>62.</b> Saad Almqren (سعد المقرن) \n <b>63.</b> Omar Al-Qazabri\' (عمر القزابري) \n <b>64.</b> Akram Alalaqmi (أكرم العلاقمي) \n <b>65.</b> Abdulrahman Al-Majed (عبدالرحمن الماجد) \n <b>66.</b> Emad Hafez (عماد زهير حافظ) \n <b>67.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>68.</b> Salah Alhashim (صلاح الهاشم) \n <b>69.</b> Yasser Al-Faylakawi (ياسر الفيلكاوي) \n <b>70.</b> Khalid Algamdi (خالد الغامدي) \n <b>71.</b> Ali Hajjaj Alsouasi (علي حجاج السويسي) \n <b>72.</b> Ramadan Shakoor (رمضان شكور) \n <b>73.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>74.</b> Nasser Almajed (ناصر الماجد) \n <b>75.</b> Muftah Alsaltany (مفتاح السلطني)  ",parse_mode='HTML' , reply_markup=nav.qorila5)



@dp.callback_query_handler(text="ortga6")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>76.</b> Ahmad Deban (أحمد ديبان)  \n <b>77.</b> Khalid Al-Shoraimy (خالد الشريمي) \n <b>78.</b> Ustaz Zamri (استاذ زامري) \n <b>79.</b> Haitham Aldukhain (هيثم الدخين) \n <b>80.</b>  Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>81.</b>  Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>82.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>83.</b> Ibrahim Al-Jebreen (ابراهيم الجبرين) \n <b>84.</b>  Shaban Al-Sayiaad (شعبان الصياد) \n <b>85.</b> Waleed Alnaehi (وليد النائحي) \n <b>86.</b> Mohammad Al-Airawy (محمد الأيراوي) \n <b>87.</b> Mohammad Refat (محمد رفعت) \n <b>88.</b> Mohammed Al-Barrak (محمد البراك) \n <b>89.</b> Abdullah Al-Mousa (عبدالله الموسى) \n <b>90.</b> Muftah Alsaltany (مفتاح السلطني)",parse_mode='HTML' , reply_markup=nav.qorila6)




@dp.callback_query_handler(text="ortga7")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>91.</b> Ahmad Deban (أحمد ديبان) \n <b>92.</b> Rogayah Sulong (رقية سولونق) \n <b>93.</b> Abdulmohsin Al-Obaikan (عبدالمحسن العبيكان) \n <b>94.</b> Rami Aldeais (رامي الدعيس) \n <b>95.</b> Wasel Almethen (واصل المذن) \n <b>96.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>97.</b> Salah Alhashim (صلاح الهاشم) \n <b>98.</b> Ibrahim Aldosari (ابراهيم الدوسري) \n <b>99.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>100.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>101.</b> Abdul Aziz Al-Ahmad (عبدالعزيز الأحمد) \n <b>102.</b> Ibrahim Al-Akdar (إبراهيم الأخضر) \n <b>103.</b> Saleh Alsahood (صالح الصاهود) \n <b>104.</b> Yasser Al-Mazroyee (ياسر المزروعي) \n <b>105.</b> Ali Jaber (علي جابر)",parse_mode='HTML' , reply_markup=nav.qorila7)




@dp.callback_query_handler(text="ortga8")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>106.</b> Mohammed Al-Muhasny (محمد المحيسني) \n <b>107.</b> Saidin Abdulrahman (سيدين عبدالرحمن) \n <b>108.</b> Nasser Alosfor (ناصر العصفور) \n <b>109.</b> Abdulrahman Aloosi (عبدالرحمن العوسي) \n <b>110.</b> Mushaf Ibrahim Al-Asiri (مصحف ابراهيم العسيري) \n <b>111.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>112.</b> Bader Alturki (بدر التركي) \n <b>113.</b> Hitham Aljadani (هيثم الجدعاني) \n <b>114.</b> Ibrahim Aljormy (ابراهيم الجرمي) \n <b>115.</b> Sami Al-Dosari (سامي الدوسري) \n <b>116.</b> Jamal Addeen Alzailaie (جمال الدين الزيلعي) \n <b>117.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله) \n <b>118.</b> Salah Musali (صلاح مصلي) \n<b>119.</b> Muftah Alsaltany (مفتاح السلطني) \n<b>120.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n ",parse_mode='HTML' , reply_markup=nav.qorila8)




@dp.callback_query_handler(text="ortga9")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>121.</b> Ahmad Al Nufais (أحمد النفيس) \n <b>122.</b> Salman Alotaibi (سلمان العتيبي) \n <b>123.</b> Abdullah Albuajan (عبدالله البعيجان) \n <b>124.</b> Shaik Abu Bakr Al Shatri (أبوبكر الشاطري) \n <b>125.</b> Abdullah Khayyat (عبدالله خياط) \n <b>126.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>127.</b> Maher Shakhashero (ماهر شخاشيرو) \n <b>128.</b> Younes Souilass (يونس اسويلص) \n <b>129.</b> Mohammad AlMonshed (محمد المنشد) \n <b>130.</b> Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>131.</b> Rodziah Abdulrahman (رضية عبدالرحمن) \n <b>132.</b> Ahmad Alhuthaifi (أحمد الحذيفي) \n <b>133.</b> Mustafa Al-Lahoni (مصطفى اللاهوني) \n <b>134.</b> Mohammad Albukheet (محمد البخيت) \n <b>135.</b> Youssef Edghouch (يوسف الدغوش) \n",parse_mode='HTML' , reply_markup=nav.qorila9)



@dp.callback_query_handler(text="ortga10")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>136.</b> Muamar (From Indonesia) (معمر الأندونيسي) \n <b>137.</b> Abdullah Kamel (عبدالله كامل) \n <b>138.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>139.</b> Islam Sobhi (إسلام صبحي) \n <b>140.</b> Ali Alhuthaifi (علي الحذيفي) \n <b>141.</b> Ahmad Al-Hawashi (أحمد الحواشي) \n <b>142.</b> Abdullah Qaulan (عبدالله غيلان) \n <b>143.</b> Adel Al-Khalbany (عادل الكلباني) \n <b>144.</b> Hussain Alshaik (حسين آل الشيخ) \n <b>145.</b> Mahmoud Khalil Al-Hussary (محمود خليل ا لحصري) \n <b>146.</b> Hatem Fareed Alwaer (حاتم فريد الواعر) \n <b>147.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>148.</b> Yousef Bin Noah Ahmad (يوسف بن نوح أحمد) \n <b>149.</b> Neamah Al-Hassan (نعمة الحسان) \n <b>150.</b> Bandar Balilah (بندر بليله) \n",parse_mode='HTML' , reply_markup=nav.qorila10)


@dp.callback_query_handler(text="ortga11")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>151.</b> Akhil Abdulhayy Rawa (أخيل عبدالحي روا) \n <b>152.</b> Ali Alhuthaifi' (علي الحذيفي)  \n <b>153.</b> Wadeea Al-Yamani (وديع اليمني) \n <b>154.</b> Khalid Almohana (خالد المهنا) \n <b>155.</b> Muhammad Abu Sneyna (محمد أبوسنينة ) \n <b>156.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>157.</b> Abdulaziz Alasiri (عبدالعزيز العسيري) \n <b>158.</b> Fahad Al-Otaibi (فهد العتيبي) \n <b>159.</b> Ahmad Al-Ajmy - Rewayat Hafs A'n Assem (أحمد بن علي العجمي - رواية حفص عن عاصم) \n <b>160.</b> Abdulmohsen Al-Qasim (عبدالمحسن القاسم) \n <b>161.</b> Jamaan Alosaimi (جمعان العصيمي) \n <b>162.</b> Khaled Al-Qahtani (خالد القحطاني) \n <b>163.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>164.</b> Saud Al-Shuraim (سعود الشريم) \n <b>165.</b> Ibrahem Assadan (ابراهيم السعدان) \n",parse_mode='HTML' , reply_markup=nav.qorila11)





@dp.callback_query_handler(text="ortga12")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>166.</b> Mohammed Al-Lohaidan (محمد اللحيدان) \n <b>167.</b> Mohammad Khalil Al-Qari (محمد خليل القارئ) \n <b>168.</b> Nasser Al obaid (ناصر العبيد) \n <b>169.</b> Akasha Kameni  (عكاشة كميني) \n <b>170.</b> Hazza Al-Balushi (هزاع البلوشي) \n <b>171.</b> Abdulbari Mohammad (عبدالبارئ محمد) \n <b>172.</b> Mohammed Jibreel (محمد جبريل) \n <b>173.</b> Majed Al-Zamil (ماجد الزامل) \n <b>174.</b> Peshawa Qadr Al-Kurdi (بيشه وا قادر الكردي) \n <b>175.</b> Abdullah Fahmi (عبدالله فهمي) \n <b>176.</b> Ahmad Saud - Rewayat Hafs A'n Assem (أحمد سعود - رواية حفص عن عاصم) \n <b>177.</b> Abdulhadi Kanakeri (عبدالهادي أحمد كناكري) \n <b>178.</b> Mohammed Hafas Ali (محمد حفص علي) \n <b>179.</b> Khalid Al-Wehabi (خالد الوهيبي) \n <b>180.</b> Muhammed Khairul Anuar (محمد خير النور) \n",parse_mode='HTML' , reply_markup=nav.qorila12)



@dp.callback_query_handler(text="ortga13")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>181.</b> Saleh Al-Habdan - Rewayat Hafs A\'n Assem (صالح الهبدان - رواية حفص عن عاصم) \n <b>182.</b> Othman Al-Ansary (عثمان الأنصاري) \n <b>183.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله)  \n <b>184.</b> Mansour Al-Salemi (منصور السالمي)  \n <b>185.</b> Sapinah Mamat (سابينة مامات)  \n <b>186.</b> Khalid Alsharekh (خالد الشارخ)  \n <b>187.</b> Alashri Omran (العشري عمران)  \n <b>188.</b> Muftah Alsaltany (مفتاح السلطني)  \n <b>189.</b> Mousa Bilal (موسى بلال)  \n <b>190.</b> Saleh Al-Talib (صالح آل طالب)  \n <b>191.</b> Wishear Hayder Arbili (وشيار حيدر اربيلي)  \n <b>192.</b> Ahmad Nauina (أحمد نعينع)  \n <b>193.</b> Ali Abo-Hashim - Rewayat Hafs A\'n Assem (علي أبو هاشم - رواية حفص عن عاصم)  \n <b>194.</b> Alfateh Alzubair (الفاتح محمد الزبير)  \n <b>195.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد)  \n",parse_mode='HTML' , reply_markup=nav.qorila13)


@dp.callback_query_handler(text="ortga14")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n \n <b>196.</b> Tareq Abdulgani daawob' (طارق عبدالغني دعوب)   \n <b>197.</b> Mohammad Al-Tablaway (محمد الطبلاوي)   \n <b>198.</b> Abdullah Al-Khalaf (عبدالله الخلف)   \n <b>199.</b> Yasser Salamah (ياسر سلامة)  \n <b>200.</b> Rachid Belalya (رشيد بلعالية)  \n <b>201.</b> Mohammed Osman Khan (محمد عثمان خان)  \n <b>202.</b> Mustafa raad Alazawy (مصطفى رعد العزاوي)  \n <b>203.</b> Abdulrasheed Soufi (عبدالرشيد صوفي)  \n <b>204.</b> Addokali Mohammad Alalim' (الدوكالي محمد العالم)  \n <b>205.</b> Mohammad Rashad Alshareef (محمد رشاد الشريف)  \n <b>206.</b> Muhammad Al-Hafiz (محمد الحافظ)  \n <b>207.</b> Abdulbari Mohammad (عبدالبارئ محمد)  \n <b>208.</b> Omar Al Darweez (عمر الدريويز)  \n <b>209.</b> Ahmad Saber (أحمد صابر) \n <b>210.</b> Hani Arrifai (هاني الرفاعي)  \n ",parse_mode='HTML' , reply_markup=nav.qorila14)




import sys

sys.setrecursionlimit(10000)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)       
      


         