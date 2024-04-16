HELP_1 = """<b><u>YÖNETİCİ KOMUTLARI:</b></u>

Sadece komutların başına <b>c</b> ekleyin ve bunları kanalda kullanın.


/dur : Şu anda çalan yayını duraklatır.

/devam : Duraklatılmış yayını devam ettirir.

/atla : Şu anda çalan yayını atlar ve sıradaki parçayı çalmaya başlar.

/bitir veya /durdur : Sırayı temizler ve şu anda çalan yayını sonlandırır.

/çalar : Etkileşimli bir çalar paneli alır.

/sıra : Sıradaki parçaların listesini gösterir.
"""

HELP_2 = """
<b><u>YETKİLİ KULLANICILAR:</b></u>

Yetkili kullanıcılar, sohbet ortamında yönetici yetkisine sahip olmadan bot üzerinde yönetici yetkilerini kullanabilirler.

/izinli [kullanıcı adı/kullanıcı_ID] : Bir kullanıcıyı botun izinli listesine ekler.
/izinli_degil [kullanıcı adı/kullanıcı_ID] : Bir kullanıcıyı izinli listesinden kaldırır.
/izinliler : Grubun izinli kullanıcılarının listesini gösterir.
"""

HELP_3 = """
<u><b>YAYIN YAPMA ÖZELLİĞİ</b></u> [SADECE SUDO YETKİLİLERİ İÇİN]:

/broadcast [MESAJ veya BİR MESAJA CEVAP] : Botun sunucu sohbetlerine bir mesaj yayınlamasını sağlar.

<u>YAYIN MODLARI:</u>
<b>-sabit</b> : Yayınladığınız mesajları sunucu sohbetlerinde sabitleyerek ön plana çıkarır.
<b>-sabit_yüksek_ses</b> : Yayınladığınız mesajları sunucu sohbetlerinde sabitleyerek ön plana çıkarır ve üyelere bildirim gönderir.
<b>-kullanıcı</b> : Botunuzu başlatan kullanıcılara mesajı yayınlar.
<b>-asistan</b> : Mesajı botun asistan hesabından yayınlar.
<b>-bot_yok</b> : Mesajın yayınlanmasını zorunlu hale getirir.

<b>ÖRNEK:</b> <code>/broadcast -kullanıcı -asistan -sabit YAYIN TESTİ</code>
"""

HELP_4 = """<u><b>SOHBET KARA LİSTESİ ÖZELLİĞİ</b></u> [YALNIZCA SUDO YETKİLİLERİ İÇİN]

Kıymetli botumuzu kullanarak çöp sohbetlerin kullanımını kısıtlayın.

/blacklistchat [sohbet kimliği] : Bot kullanarak sohbeti kara listeye alın.
/whitelistchat [sohbet kimliği] : Kara listeye alınmış sohbeti beyaz listeye alın.
/blacklistedchat : Kara listeye alınmış sohbetlerin listesini gösterir.

"""

HELP_5 = """
<u><b>KULLANICI ENGELLEME:</b></u> [YALNIZCA SUDO YETKİLİLERİ İÇİN]

Kara listelenen kullanıcıları engellemeye başlar, böylece bot komutlarını kullanamazlar.

/block [kullanıcı adı veya bir kullanıcıya cevap] : Kullanıcıyı botumuzdan engeller.
/unblock [kullanıcı adı veya bir kullanıcıya cevap] : Engellenen kullanıcıların engelini kaldırır.
/blockedusers : Engellenen kullanıcıların listesini gösterir.

"""

HELP_6 = """
<u><b>KANAL OYNATMA KOMUTLARI:</b></u>

Kanalda ses/video yayını yapabilirsiniz.

/cplay : Kanalın video sohbetinde istenen ses izlemini başlatır.
/cvplay : Kanalın video sohbetinde istenen video izlemini başlatır.
/cplayforce veya /cvplayforce : Devam eden yayını durdurur ve istenen izlemeyi başlatır.

/channelplay [sohbet kullanıcı adı veya kimliği] veya [devre dışı] : Kanalı bir gruba bağlar ve grup tarafından gönderilen komutlarla izleme yapmaya başlar.

"""

HELP_7 = """
<u><b>GLOBAL BAN ÖZELLİĞİ</b></u> [YALNIZCA SUDO YETKİLİLERİ İÇİN]:

/gban [kullanıcı adı veya bir kullanıcıya cevap] : Kullanıcıyı tüm sunucu sohbetlerinden global olarak yasaklar ve bot kullanımını kara listeler.
/ungban [kullanıcı adı veya bir kullanıcıya cevap] : Global olarak yasaklanan kullanıcının yasağını kaldırır.
/gbannedusers : Global olarak yasaklanan kullanıcıların listesini gösterir.

"""

HELP_8 = """
<b><u>LOOP STREAM:</b></u>

<b>Oynatılan yayını döngüye alır.</b>

/loop [etkinleştir/devre dışı] : Yayını döngüye alır veya döngüyü kaldırır.
/loop [1, 2, 3, ...] : Belirtilen değeri döngüye alır.

"""

HELP_9 = """
<u><b>BAKIM MODU</b></u> [YALNIZCA SUDO YETKİLİLERİ İÇİN]:

/logs : Botun günlüklerini alır.

/logger [etkinleştir/devre dışı] : Botun etkinliklerini günlüğe kaydetmeye başlar.
/maintenance [etkinleştir/devre dışı] : Botun bakım modunu etkinleştirir veya devre dışı bırakır.

"""

HELP_10 = """
<b><u>PİNG & STATS:</b></u>

/start : Müzik botunu başlatır.
/help : Komutları açıklamalı yardım menüsü alır.

/ping : Botun ping'ini ve sistem istatistiklerini gösterir.

/stats : Botun genel istatistiklerini gösterir.

"""

HELP_11 = """
<u><b>OYNATMA KOMUTLARI:</b></u>

<v> : Video oynatma anlamına gelir.
<force> : Zorla oynatma anlamına gelir.

/oynat veya /voynat : İstenilen ses izlemesini video sohbetinde başlatır.
/playforce veya /vplayforce : Devam eden yayını durdurur ve istenen izlemeyi başlatır.

"""

HELP_12 = """
<b><u>KARIŞTIRMA KUYRUSU:</b></u>

/karistir : Kuyruğu karıştırır.
/sira : Karıştırılmış kuyruğu gösterir.

"""

HELP_13 = """
<b><u>YAYINI İLERİ SARMAYA İLİŞKİN KOMUTLAR:</b></u>

/ilerisar [saniye cinsinden süre] : Yayını belirtilen süreye sarmak için.
/gerisar [saniye cinsinden süre] : Yayını belirtilen süre kadar geri sarar.

"""

HELP_14 = """
<b><u>ŞARKI İNDİRME</b></u>

/indir [şarkı adı/yt URL] : YouTube'dan herhangi bir şarkıyı MP3 veya MP4 formatında indirir.
"""

HELP_15 = """
<b><u>HIZ KOMUTLARI :</b></u>

Oynatma hızını kontrol edebilirsiniz. [Yalnızca yöneticiler]

/speed veya /playback : Ses oynatma hızını grup içinde ayarlar.
/cspeed veya /cplayback : Ses oynatma hızını kanalda ayarlar.
"""
