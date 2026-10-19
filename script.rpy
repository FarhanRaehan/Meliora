# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
transform masuk_kanan_kiri :
    xalign 1.5 yalign 1.0
    easein 1.0 xalign 0.2
transform masuk_kiri_kanan :
    xalign 1.0 yalign 1.5
    easein 1.0 xalign 0.2

default f_papan = False
default f_pulpen = False
default f_gudang = False
default f_kantin = False
default f_perpus = False 
default f_buku_catatan = False
default f_payung = False
default f_revisi = False
default f_buku = False 
default f_minuman = False
default f_lomba = False
default f_teka  = False
default f_strategi = False
default f_pohon = False

default D4_P1 = ""

default seri_dicek = False


init python:
    if persistent.episode_unlocked is None:
        persistent.episode_unlocked = 1

    def hitung_ending():
        skor = sorted(
            [("isy", store.ISY), ("rhe", store.RHE), ("ghe", store.GHE)],
            key=lambda x: x[1],
            reverse=True
        )
        top = skor[0][1]
        diff = top - skor[1][1]
        tied = [nama for nama, s in skor if s == top]

        if top < 8:
            jenis = "bad"
        elif top >= 20 and diff >= 3:
            jenis = "true"
        elif top >= 14 and diff >= 2:
            jenis = "good"
        else:
            jenis = "normal"

        return jenis, skor[0][0], tied

default ISY = 0
default RHE = 0
default GHE = 0

define n = Character(" ")
define al = Character("Altan")
define isy = Character("Daisy")
define rhe = Character("Kak Fira")
define ghe = Character("nayla")
define pa = Character("Pak Anwar")
# The game starts here.

label start:
    jump episode_1

label episode_1:
    ": Pukul 06.15. Matahari belum terlalu tinggi, tapi gerbang SMA Malaka sudah dipenuhi murid baru. Di
    leherku tergantung papan nama dari kardus, lengkap dengan tali rafia merah yang sudah mulai kusut."
    "Hari ini adalah hari pertama Masa Pengenalan Lingkungan Sekolah, 
    atau yang biasa disebut MPLS."

    scene bg pager
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    show altan bingung at masuk_kiri_kanan with dissolve
    al " (batin) Oke. Empat hari. Gua cuma perlu bertahan empat hari."
    hide altan bingung with fade

    show daisy kaget at masuk_kanan_kiri with fade
    isy " Aduh! Maaf, maaf!"
    hide daisy kaget
    show daisy malu
    isy " Eh, kamu bawa gunting, nggak? Atau lakban?"
    isy " Atau, ya ampun, kamu tahu cara bikin papan nama dari kardus yang nggak kelihatan kayak bekas
    kardus mi instan?"
    hide daisy malu
    show daisy kecewa with dissolve
    isy " Aku Daisy. Papan namaku ketinggalan di meja belajar. Padahal semalam udah kutaruh di tas. Kayaknya."

label choices1:
    isy " Aku Daisy. Papan namaku ketinggalan di meja belajar. Padahal semalam udah kutaruh di tas. Kayaknya."
    hide daisy kecewa
    menu:

        "Sini, aku bantu buatkan. Aku bawa spidol cadangan.":
            jump choices1_a

        "Kamu bisa minta kardus dan tali ke panitia di meja registrasi.":
            jump choices1_b

        "(Pura-pura tidak mendengar dan jalan masuk.)" :
            jump choices1_c
        
label choices1_a:
        $ISY += 2 
        $f_papan = True
        show altan bantu
        al "Nih, tulis nama lengkap dulu, terus panggilannya dibesarin."
        hide altan bantu
        show daisy bingung
        isy "(menulis dengan lidah menjulur) Dai... sy... Anna. Panggilan: Daisy. Kelas: X-3. Cita-cita..."
        hide daisy bingung
        show altan bingung
        al " Itu nggak perlu."
        hide altan bingung
        show daisy senang
        isy "Hehe kebiasaan. Makasih ya! Beneran, kamu penyelamatku! Nama kamu siapa?"
        hide daisy senang
        show altan bingung
        al " Altan."
        hide altan bingung
        show daisy bingung
        isy " Altan, Altan, oke. Aku hafal! Kelas berapa?"
        hide daisy bingung
        with fade
        n " Ternyata kami satu kelas. X-3."
        jump choices1_common

label choices1_b: 
        $ISY +=0
        $RHE +=1
        show altan senang
        al " Kamu bisa minta kardus dan tali ke panitia di meja registrasi."
        hide altan senang

        show daisy bingung
        isy " Oh iya, panitia! Makasih ya, Altan!"
        hide daisy bingung
        show daisy salting
        isy "Eh, aku tahu namamu dari papan nama kamu, bukan stalking lho! humphh"
        hide daisy salting
        n "Ia berlari kecil sambil melambai. Di meja registrasi, aku sekilas melihat seorang kakak OSIS yang sedang mengatur antrean dengan sigap."
        n " Tak lama kemudian, kakak kelas berkacamata itu menghentikan Daisy
dan menegurnya soal antrean."
        jump choices1_common

label choices1_c:
        $ISY -=1
        n " Daisy terdiam, lalu bergumam sendiri."
        n "Dari kejauhan, aku mendengarnya bertanya pada orang lain"
        n "Ada yang punya kardus cadangan, nggak?"
        n "Nada suaranya masih ceria, tapi ada yang terasa dipaksakan."
        jump choices1_common

        
label choices1_common:

        scene bg lapangan
        with fade 

        n  "Bel berbunyi... 
        Panitia meniup peluit dan seluruh murid baru digiring ke lapangan upacara. Barisan
        dirapikan satu per satu, sepatu diperiksa, dan papan nama dicek."
        n "Di barisan sebelah, seorang gadis berambut hitam panjang sibuk mengaduk-aduk tasnya. Wajahnya
        pucat."

        show ghefira bingung
        ghe "(berbisik) Pulpenku..."


label choices2:
    ghe "(berbisik) Pulpenku..."
    hide ghefira

    menu:
        "(Menyodorkan pulpen cadangan)":
            jump choices2_a

        "(Pura-pura tidak lihat)":
            jump choices2_b

label choices2_a:
    $ GHE += 2
    $ f_pulpen = True
    show ghefira salting
    ghe "...Terima kasih. Aku Ghefira. Nanti kukembalikan."
    hide ghefira salting

    show altan senang
    al "Santai aja. Aku masih punya satu lagi."
    jump choices2_common


label choices2_b:
    $ f_pulpen = False
    n "Ghefira akhirnya meminjam pulpen dari anak lain dengan wajah canggung."
    jump choices2_common

        
label choices2_common:
        hide altan senang
        n " Upacara pembukaan MPLS berlangsung khidmat. Pak Anwar, sang kepala sekolah, berpidato
            tentang semangat Malaka: Maju, Amanah, Lugas, Aktif, Kreatif, Akur."
        show altan kecewa
        show altan kecewa
        al " Panas banget. Kakiku mulai kesemutan."
        hide altan kecewa
        show rhea marah
        rhe "Kamu"
        rhe "Yang barusan bergerak saat sikap sempurna. Maju ke depan"
        hide rhea marah
        n " Seorang kakak kelas dengan name tag RHEA (OSIS) berdiri dengan tangan bersedekap. Tatapannya tajam, tapi ada kelelahan samar di matanya."

label choices3:
        n " Seorang kakak kelas dengan name tag RHEA (OSIS) berdiri dengan tangan bersedekap. Tatapannya tajam, tapi ada kelelahan samar di matanya."
        

        menu:

            "Maju tegas dan minta maaf dengan jelas.":
                    jump choices3_a

            "Mencoba mencairkan dengan bercanda":
                    jump choices3_b
            
            "Diam, menunduk, menerima teguran." :
                    jump choices3_c

label choices3_a:
        $RHE +=2 
        show altan 
        al " Maaf, Ka. Saya tidak fokus. Tidak akan terulang"
        hide altan

        show kak rhea
        rhe " (sedikit terkejut) Hm. Setidaknya kamu tidak beralasan."
        jump choices3_common


label choices3_b:

        show altan
        al " Maaf Ka, kakiku kesemutan, mungkin gara-gara semangat Malaka terlalu membara."
        hide altan

        n " Beberapa murid terkekeh. Daisy di barisan belakang tertawa lepas. Ka Rhea menyipitkan mata"
        jump choices3_common

label choices3_c:

        show kak rhea
        rhe " Kamu tidak bicara? Baik. Kembali ke barisan."
        hide kak rhea
        jump choices3_common

        
label choices3_common:
        hide kak rhea
        scene bg koridor
        with fade
        n " Bel istirahat. Murid-murid berhamburan keluar barisan. Kakiku masih pegal dan tenggorokanku kering"
        n "Di depan ada tiga arah: kantin yang ramai dan beraroma gorengan, perpustakaan yang tenang
        dengan pintu setengah terbuka, dan gudang olahraga tempat beberapa panitia terlihat kerepotan menggotong kardus."
        
        al "( Aku punya waktu lima belas menit. Cukup untuk satu tempat saja.)"

label choices4:
        al "( Aku punya waktu lima belas menit. Cukup untuk satu tempat saja.)"

        
        menu:

            "Ke Kantin":
                    jump choices4_a

            "Ke Perpustakaan":
                    jump choices4_b
            
            " Ke gudang, membantu panitia." :
                    jump choices4_c

label choices4_a:
        scene bg kantin
        with fade
        $ISY +=2
        $f_kantin = True 
        show daisy senang
        isy "  Altan! Sini sini!"
        isy "Aku udah pesenin bakso, eh tunggu, kamu alergi sesuatu, nggak?"
        hide daisy senang

        show altan bantu
        al " Nggak ada. Makasih."
        hide altan bantu

        show daisy malu
        isy "Yes! Eh, aku mau
cerita. Dulu di SMP aku sering banget lupa bawa barang. Pernah lupa bawa sepatu, sampai pulang pakai sandal jepit
teman. Hehe. Tapi di sini aku mau berubah. Mau jadi anak yang rapi."
        hide daisy malu

        n " Ia tertawa, tapi jarinya mengetuk-ngetuk
meja dengan gelisah."

        show altan senang
        al " Kamu nggak harus berubah drastis. Mulai dari hal kecil aja."
        hide altan senang

        show daisy salting
        isy "(terdiam sebentar, lalu
tersenyum tulus) Iya juga ya."
        hide daisy salting

        jump choices4_common

label choices4_b:
    $GHE += 2
    $f_perpus = True

    n "Aroma kertas lama menyambutku. Di pojok dekat jendela, Ghefira duduk dengan buku ..."

    ghe "...kamu, yang tadi pagi disebelahku ya"

    if f_pulpen == True:
        al "Iya. Pulpenmu masih awet?"
    else:
        al "Oh, kamu yang tadi pagi di barisan sebelah, kan?"

    ghe "(menutup buku catatannya sedikit) Aku... menulis. Cuma iseng. Jangan dibaca ya"

    al "Tenang. Aku bukan tipe yang suka ngintip."

    n "Untuk pertama kalinya, sudut bibir Ghefira terangkat sedikit."
    jump choices3_common

label choices4_c:
        $RHE +=2
        $f_gudang = True
        show kak rhea
        rhe " Kamu? Yang tadi ditegur? Ngapain di sini?"
        hide kak rhea

        al " Kakak kelihatan kerepotan. Boleh saya bantu angkat kardusnya?"

        rhe "(menatap curiga, lalu menghela napas) Baiklah. Tapi jangan sampai ada yang jatuh."

        n "Kami mengangkat kardus berisi peralatan MPLS satu per satu. Sesekali Ka Rhea menyeka dahi, napasnya tersengal."

        rhe "(pelan) Panitia kurang orang. Semua bergantung sama beberapa gelintir anggota"

        al ": Kakak pasti capek"

        rhe " ...Jangan sok tahu. (tapi nadanya tidak setajam tadi)"
        jump choices4_common

        
label choices4_common:
        scene bg pager
        with fade
        n "Hari pertama selesai. Murid-murid berhamburan keluar gerbang, suara motor dan obrolan bercampur jadi satu."
        n "Di antara keramaian, aku melihat tiga sosok yang entah kenapa menarik perhatianku: Daisy yang melambai-lambai, Ka Rhea yang masih merapikan barisan, dan Ghefira yang berjalan sendirian sambil memeluk buku catatannya"


label choices5:
        n "Siapa yang kamu hampiri?"

        menu:

            " Daisy yang sedang melambai ceria.":
                    jump choices5_a

            "Ka Rhea yang sedang merapikan barisan.":
                    jump choices5_b
            
            " Ghefira yang menjatuhkan buku catatannya." :
                    jump choices5_c

label choices5_a:
        $ISY +=1 
        show daisy senang
        isy "Altan! Besok jangan lupa bawa spidol yaaa!"
        hide daisy senang
        show daisy malu
        isy "Ehh, itu aku yang harus bawa. Hehee"
        hide daisy malu
        jump choices5_common

label choices5_b:
        $RHE +=1
        al "Ka, makasih untuk hari ini. Maaf soal tadi pagi."

        rhe "(tertegun) Besok datang tepat waktu. Itu saja."
        jump choices5_common

label choices5_c:
        $GHE +=1
        $f_buku_catatan = True
        al "(memungut) Ini punyamu."

        ghe " ...Terima kasih. (pelan) Besok, bisa duduk di dekatku?"
        jump choices5_common

        
label choices5_common:
        scene bg aula
        with fade
        n " Hari kedua. Hari ini panitia membagi murid baru ke dalam kelompok untuk membuat yel-yel dan mengikuti lomba antar kelompok."

        rhe "(membaca daftar) Kelompok 7, anggota: Altan, Daisy Anna, dan Ghefira. Pembimbing, saya."

        n "Ketiga gadis itu, dan aku, di satu kelompok. Seolah semesta sedang bercanda"

label cek_tertinggi:
    if ISY > RHE and ISY > GHE:
        show daisy senang
        n "Daisy melambai heboh saat melihat Altan di kelompoknya."
        hide daisy senang

    elif RHE > ISY and RHE > GHE:
        show rhea
        n "Ka Rhea sempat melirik Altan dan berkata pelan,"
        rhe "Kamu lagi. Awas ya."
        hide rhea

    elif GHE > ISY and GHE > RHE:
        show ghefira
        n "Ghefira langsung duduk di kursi kosong sebelah Altan tanpa bicara."
        hide ghefira

    else:
        n "Ketiganya bersikap sopan, tapi menjaga jarak."

    n " Ka Rhea menjelaskan tugas pertama: kelompok harus memilih satu ketua yel-yel, satu penulis lirik, dan satu
koreografer. Semua mata menoleh padaku, seakan aku yang paling tahu."


label choices6:
        

        menu:

            "Mengusulkan Daisy sebagai ketua yel-yel (semangatnya cocok)":
                    jump choices6_a

            "Mengusulkan Ghefira sebagai penulis lirik (ia suka menulis)":
                    jump choices6_b
            
            "Meminta arahan Ka Rhea soal pembagian yang efisien." :
                    jump choices6_c

label choices6_a:
        $ISY +=2
        show daisy senang
        isy "Serius?! Aku? Oke! Aku bakal bikin yel-yel yang paling heboh!"
        hide daisy senang
        jump choices6_common

label choices6_b:
        $GHE +=2
        show ghefira
        ghe "(menunduk, memerah) ...Aku... bisa coba"
        hide ghefira
        jump choices6_common

label choices6_c:
        $RHE +=2
        show rhea
        rhe "Pertanyaan bagus. Setidaknya kamu mikir sebelum bertindak"
        hide rhea
        jump choices6_common

        
label choices6_common:
        n "Latihan yel-yel dimulai. Lirik buatan Ghefira ternyata bagus. Diksinya puitis, ritmenya enak. Daisy
sampai bertepuk tangan sendiri saat membacanya."
        n "Tapi saat Ghefira membacakannya di depan kelompok, suaranya hampir tak terdengar. Ka Rhea:
Suaranya tidak sampai. Lirik sebagus apa pun tidak berguna kalau penontonnya tidak dengar. Ulangi. Ghefira:
(gemetar) Maaf..."

label choices7:
        n "Siapa yang kamu hampiri?"

        menu:

            ". Membela Ghefira dengan sopan":
                    jump choices7_a

            "Setuju dengan Ka Rhea dan bantu merevisi":
                    jump choices7_b
            
            ". Mencairkan suasana dengan lelucon." :
                    jump choices7_c

label choices7_a:
        $GHE +=2
        show altan
        al "Ka, liriknya sudah bagus. Mungkin kita bantu dia pelan-pelan, bukan ditekan."
        hide altan
        n "Ghefira
menatap Altan dengan mata berkaca-kaca. Ka Rhea tidak tersinggung, tapi diam sejenak."
        jump choices7_common

label choices7_b:
        $RHE +=2
        $f_revisi = True
        show altan
        al ":Kakak benar. Gimana kalau kita ubah bagian refrennya jadi lebih pendek
dan tegas?"
        hide altan
        show rhea
        rhe "(mengangguk) Nah, itu baru solusi."
        hide rhea
        jump choices7_common

label choices7_c:
        $ISY +=1
        $RHE +=1
        show altan
        al ": Bagaimana kalau Daisy yang teriak, Ghefira yang nulis, dan Ka Rhea yang jadi wasit?"
        hide altan
        show daisy
        isy "Hahaha! Setuju!"
        hide daisy
        show rhea
        rhe "(menatap dingin) Ini bukan waktunya bercanda."
        hide rhea
        jump choices7_common

        
label choices7_common:

        n "Latihan berlanjut sampai siang. Langit yang tadinya cerah perlahan berubah kelabu, dan angin
membawa bau tanah basah."
        n "Lalu hujan deras turun mendadak. Murid-murid berlarian mencari tempat berteduh. Panitia
mengumumkan latihan ditunda dan semua diminta kembali ke dalam gedung. Narasi: Di tengah kekacauan, aku melihat
Daisy berdiri kebingungan tanpa payung, Ghefira berteduh sendirian di koridor perpustakaan, dan Ka Rhea sibuk
memindahkan perlengkapan yang mulai basah."

label choices8:
        

        menu:

            "Berbagi payung dengan Daisy yang lupa bawa payung (tentu saja).":
                    jump choices8_a

            "Menemani Ghefira yang berteduh di koridor perpustakaan.":
                    jump choices8_b
            
            "Membantu Ka Rhea memindahkan perlengkapan ke aula." :
                    jump choices8_c

label choices8_a:
        $ISY +=2
        $f_payung = True 
        show daisy senang
        isy "Aduh, aku memang nggak bisa dipercaya soal payung. Tapi kamu bisa
dipercaya, kan?"
        hide daisy senang
        show altan
        al "semoga"
        hide altan
        show daisy
        isy "(tertawa, lalu tiba-tiba pelan) Altan, kamu nggak risih kan, aku cerewet begini?"
        hide daisy
        jump choices8_common

label choices8_b:
        $GHE +=2
        show ghefira
        ghe "...Aku suka hujan. Lebih tenang daripada orang banyak"
        hide ghefira
        show altan
        al "Aku juga"
        show altan
        show ghefira
        ghe ": (menatap
hujan) Kalau di panggung nanti aku... aku takut"
        hide ghefira
        jump choices8_common

label choices8_c:
        $RHE +=2
        show rhea
        rhe "Kamu kenapa nggak berteduh seperti yang lain?"
        hide rhea
        show altan
        al "Kakak sendirian"
        hide altan
        show rhea
        rhe "(terdiam, lalu pelan) ...Terima kasih."
        hide rhea
        jump choices8_common

        
label choices8_common:
        n "Hujan reda menjelang sore. Halaman sekolah dipenuhi genangan yang memantulkan langit jingga. Murid-murid mulai pulang satu per satu."
        n "Sebelum pulang, aku melihat tiga hal kecil. Daisy menggigit kuku sambil menatap ponselnya,
tampak gugup soal besok. Ghefira bergumam bahwa ia ingin membaca ulang novel favoritnya, tapi bukunya tertinggal di
rumah. Ka Rhea masih berkeliling beres-beres sendirian"

label choices9:
        

        menu:

            "Mengirim pesan semangat ke Daisy yang tampak gugup soal besok":
                    jump choices9_a

            "Meminjamkan buku ke Ghefira yang ingin membaca novel favoritnya.":
                    jump choices9_b
            
            "Membelikan minuman untuk Ka Rhea yang masih lembur beres-beres." :
                    jump choices9_c

label choices9_a:
        $ISY +=1
        show daisy senang
        isy "Makasih Altan. Besok kita pasti bisa!"
        hide daisy senang
        jump choices9_common

label choices9_b:
        $GHE +=1
        $f_buku = True
        show ghefira
        ghe "Ku jaga Baik-Baik, Janji."
        hide ghefira
        jump choices9_common

label choices9_c:
        $RHE +=1
        $f_minuman = True
        show rhea
        rhe "Untuk saya? ...Terima kasih. Jangan bilang siapa-siapa."
        hide rhea
        jump choices9_common

        
label choices9_common:
        n "Hari ketiga. Langit bersih, tanah masih sedikit basah. Hari ini seluruh kelompok bertanding di lomba
tiga pos. Hasilnya menentukan urutan tampil di malam penutupan besok. Ka Rhea: (membaca papan skor) Pos Lari
Estafet, Pos Teka-teki, dan Pos Strategi Logistik. Satu anggota kelompok memimpin tiap pos. Pembimbing hanya boleh
mengawasi."
        
label cek_tertinggi2:
    if ISY > RHE and ISY > GHE:
        show daisy senang
        n "Daisy sudah menunggu di garis start dan melambaikan bendera kelompok ke arah Altan."
        hide daisy senang

    elif RHE > ISY and RHE > GHE:
        show rhea
        n "Ka Rhea menyerahkan lembar aturan lomba langsung ke tangan Altan. Ka Rhea menyerahkan lembar aturan lomba langsung ke tangan Altan. (Baca. Jangansampai salah.)"

        rhe "Baca. Jangan sampai salah."
        hide rhea

    elif GHE > ISY and GHE > RHE:
        show ghefira
        n "Ghefira berdiri di dekat Altan dengan buku catatan terbuka, lalu bertanya pelan,"
        ghe "Kamu ambil pos yang mana?"
        hide ghefira
    else:
        n "Ketiganya menyambut Altan dengan sopan, lalu kembali sibuk dengan urusan zzmasing-masing."
        
        n "Altan hanya bisa mendampingi satu pos dengan serius. Dua pos lainnya akan berjalan tanpa dia."

label choices10:
        

        menu:

            "Mengusulkan Daisy sebagai ketua yel-yel (semangatnya cocok)":
                    jump choices10_a

            "Mengusulkan Ghefira sebagai penulis lirik (ia suka menulis)":
                    jump choices10_b
            
            "Meminta arahan Ka Rhea soal pembagian yang efisien." :
                    jump choices10_c

label choices10_a:
        $ISY +=2
        $f_lomba = True
        show daisy senang
        isy "Altan, kalau aku jatuh, jangan ketawa ya. Eh, boleh ketawa. Tapi pelan-pelan."
        hide daisy senang
        n "Daisy terpeleset di tikungan basah. Ia bangkit dengan lutut berlumpur, tertawa, dan tetap berlari sampai
selesai."
        show daisy malu
        isy "(terengah, menatap lututnya) Aku nggak lupa tongkatnya, lho. Ini rekor pribadi."
        hide daisy malu
        jump choices10_common

label choices10_b:
        $GHE +=2
        $ f_teka = True
        show ghefira
        ghe "(pelan) Kalau soalnya tentang kata, aku bisa. Tapi aku nggak sanggup
mengumumkan jawabannya."
        hide ghefira
        show altan
        al "Kamu yang menyusun jawabannya. Aku yang mengucapkan. Setuju"
        hide altan
        n "Ghefira menulis jawaban dengan cepat. Untuk pertama kalinya, ia tersenyum karena merasa dibutuhkan."
        jump choices10_common

label choices10_c:
        $RHE +=2
        $f_strategi = True
        show rhea
        rhe "Pembimbing tidak boleh ikut. Tapi... kamu boleh bertanya."
        hide rhea
        n "Altan menyusun daftar perlengkapan di samping Ka Rhea. Sesekali ia menyodorkan botol air tanpa diminta"
        show rhea
        rhe "(tanpa menoleh) Jangan terlalu perhatian. Nanti aku terbiasa."
        hide rhea
        jump choices10_common

        
label choices10_common:
        scene bg halaman sekolah
        n "Siang hari, lomba jeda sebentar. Panitia membagikan kertas kecil berwarna untuk kegiatan Pohon
Harapan: setiap murid menulis satu harapan untuk tiga tahun ke depan, lalu menggantungnya di dahan."
        n "Altan sudah menulis harapannya sendiri. Sambil menunggu tintanya kering, ia melihat tiga orang
yang masih belum selesai menulis. "
        n "Daisy yang mengetuk-ngetukkan pulpen ke dagu, Ghefira yang menutupi kertasnya
dengan lengan, dan Ka Rhea yang menatap dahan tanpa menulis apa pun"

label choices11:
        n "Siapa yang kamu tanya soal harapannya?"

        menu:

            "Daisy":
                    jump choices11_a

            "Ghefira":
                    jump choices11_b
            
            "Kak Rhea" :
                    jump choices11_c

label choices11_a:
        $ISY +=2
        $f_pohon = True
        show daisy senang
        isy "Harapanku? Dulu aku bakal nulis (nggak lupa bawa apa-apa). Tapi
sekarang... aku mau punya teman yang beneran ngerti aku."
        hide daisy senang
        al ": Kamu sudah punya satu."
        show daisy salting
        isy "Apasii alayyy"
        hide daisy salting
        jump choices11_common

label choices11_b:
        $GHE +=2
        $f_pohon = True
        show ghefira
        ghe "Aku mau berani membacakan tulisanku... sampai ada yang
mendengarkan."
        hide ghefira
        show altan
        al "Aku sudah mendengarkan"
        hide altan
        show ghefira
        ghe "(menunduk, nyaris tak terdengar) Aku tahu. Itu... alasannya
aku menulisnya"
        hide ghefira
        jump choices11_common

label choices11_c:
        $RHE +=2
        $f_pohon = True
        show rhea
        rhe "Harapanku sederhana. Ada penerus OSIS yang bisa kuandalkan. Dan
sekali saja tidur delapan jam"
        hide rhea
        show altan
        al "Yang kedua bisa kubantu."
        hide altan
        show rhea
        rhe "(menahan senyum) Jangan terlalu percaya diri,
anak baru."
        hide rhea
        jump choices11_common

        
label choices11_common:

        n "Sore hari, hasil lomba diumumkan. Kelompok 7 meraih posisi kedua. Bukan juara, tapi cukup untuk
tampil di urutan akhir besok malam."
        n "Namun suasana kelompok tidak sepenuhnya riang. Daisy terkena teguran karena salah mengoper
tongkat, Ghefira menghindari kontak mata, dan Ka Rhea hanya diam sambil mencatat sesuatu di bukunya."

label choices12:

        menu:

            "Mengajak Daisy tertawa lagi dan menyalahkan tikungan basah sebagai tersangka utama.":
                    jump choices12_a

            "Duduk di dekat Ghefira dan mengatakan jawaban teka-tekinya tadi sebenarnya hebat.":
                    jump choices12_b
            
            "Menghampiri Ka Rhea dan menanyakan apa yang sedang ia tulis" :
                    jump choices12_c

label choices12_a:
        $ISY +=1
        show daisy senang
        isy "Betul! Tikungan itu licik! Aku akan menuntutnya di pengadilan MPLS!"
        hide daisy senang
        jump choices12_common

label choices12_b:
        $GHE +=1
        show ghefira
        ghe "...Kamu memperhatikan?"
        hide ghefira
        show altan
        al ": Aku mencatatnya dalam hati"
        hide altan
        jump choices12_common

label choices12_c:
        $RHE +=1
        show rhea
        rhe "(menutup buku sedikit) Daftar kesalahan kelompok kita."
        hide rhea
        show altan
        al "Boleh aku tambahkan daftar hal yang berjalan baik?"
        hide altan
        show rhea
        rhe "(diam, lalu menyodorkan pena) ...Silakan."
        hide rhea
        jump choices12_common

        
label choices12_common:
        n "Menjelang pulang, ketiganya tampak berbeda dari biasanya. Daisy berbicara dengan suara yang
mulai serak karena terlalu banyak bersorak. Ghefira menggenggam kertas liriknya erat-erat sampai kusut di ujungnya."
        n "Ka Rhea berdiri agak jauh, menyembunyikan kantung matanya dengan tangan. Besok adalah hari
penampilan, dan aku punya firasat buruk bahwa ketiga masalah ini akan meledak bersamaan."

label choices13:

        menu:

            "Mengingatkan Daisy agar minum air hangat dan tidak berteriak lagi malam ini.":
                    jump choices13_a

            "Mengatakan pada Ghefira bahwa ia tidak harus sempurna, cukup selesai.":
                    jump choices13_b
            
            "Menyuruh Ka Rhea pulang lebih awal dan berjanji ikut menyiapkan sisanya" :
                    jump choices13_c

label choices13_a:
        $ISY +=1
        show daisy senang
        isy "Siapp wahai dokter Altann, janji besok bakal hemat suaraa."
        hide daisy senang
        show altan
        al "good girl."
        hide altan
        jump choices13_common

label choices13_b:
        $GHE +=1
        show ghefira
        ghe "...Akan ku coba, besok. Janjii."
        hide ghefira
        jump choices13_common

label choices13_c:
        $RHE +=1
        show rhea
        rhe "Kamu ini keras kepala. (pelan) But, Thanks ya Altan."
        hide rhea
        jump choices13_common

        
label choices13_common:
        n "Hari terakhir MPLS. Aula sudah dipenuhi murid, orang tua, dan guru. Lampu panggung menyala,
dan suara pembawa acara menggema dari pengeras suara."
        n "Pagi ini, tiga masalah muncul bersamaan."
        n "Daisy kehilangan suaranya karena kebanyakan berteriak kemarin.
        Ghefira gemetar dan bersembunyi di belakang panggung, tidak sanggup naik.
        Ka Rhea tampak pucat dan hampir pingsan karena kurang tidur"
        n "Waktuku hanya cukup untuk menolong satu orang dengan benar"

label choices14:
        n "Siapa yang kamu tolong?"

        menu:

            "Menolong Daisy.":
                    jump choices14_a

            "Menolong Ghefira.":
                    jump choices14_b
            
            "Menolong Kak Rhea." :
                    jump choices14_c

label choices14_a:
        $ISY +=3
        n "Altan membawa air hangat madu dan menenangkan Daisy"
        show daisy senang
        isy "(berbisik serak) Aku takut ngecewain semua orang."
        hide daisy senang
        show altan
        al "Kamu nggak harus tampil sempurna. Aku di sini."
        hide altan
label cek_khusus:
    if f_papan:
        $ ISY += 1
    if f_payung:
        $ ISY += 1
    if f_lomba:
        $ ISY += 1

    if f_papan or f_payung or f_lomba:
        n "Ada sesuatu yang terasa familiar di antara mereka, seperti kenangan yang tiba-tiba kembali."
        al "Eh, ini mengingatkanku pada waktu itu..."

        jump choices14_common

label choices14_b:
        $ GHE += 3
        n "Altan duduk di samping Ghefira di balik tirai."
        ghe "Aku nggak bisa..."
        al "Kamu menulis lirik yang indah. Mereka cuma perlu mendengar sebagian kecilnya."
label cek_khusus2:
    if f_perpus:
        $ GHE += 1
    if f_buku :
        $ GHE += 1
    if f_teka:
        $ GHE += 1

    if f_perpus or f_buku or f_teka:
        n "Ghefira terdiam sejenak, lalu menggenggam tangan Altan."
        jump choices14_common

label choices14_c:
        $RHE += 3
        n "Altan memaksa Ka Rhea duduk dan membawakan air"
        rhe "Aku nggak boleh ambruk. Mereka semua bergantung padaku."
        al "Kakak juga manusia."
label cek_khusus3:
    if f_gudang:
        $ RHE += 1
    if f_minuman:
        $ RHE += 1
    if f_strategi:
        $ RHE += 1

    if f_gudeng or f_minuman or f_strategi:
        n "Ka Rhea menangis pelan"
        jump choices14_common

        
label choices14_common:

        n "Giliran Kelompok 7 tampil. Hasil dari pilihan pagi tadi akan menentukan jalannya penampilan."

label cerita2:
    if D4_P1 == "A":
        jump cerita2_a
    elif D4_P1 == "B":
        jump cerita2_b
    else:
        jump cerita2_c


# ===== CABANG A: menolong Daisy =====
label cerita2_a:
    show daisy
    n "Daisy tampil dengan suara serak tapi penuh tekad. Penonton tertawa dan bertepuk tangan."
    n "Ghefira menyelesaikan bagian lirik dengan suara pelan, dan Ka Rhea memberi aba-aba dari bawah panggung."

    menu:
        "Berdiri tegap di samping Daisy dan menyalurkan semangat.":
            jump d4_p2_a1

        "Mengambil alih bagian sorak agar Daisy beristirahat.":
            jump d4_p2_a2

label d4_p2_a1:
    $ ISY += 2
    n "Daisy menoleh ke arah Altan, menarik napas, dan menyelesaikan refren dengan suara serak yang lantang."
    n "Tepuk tangan penonton pecah."
    jump cerita2_common

label d4_p2_a2:
    $ ISY += 1
    $ RHE += 1
    n "Altan menyambar bagian sorak dan Daisy tersenyum lega sambil mengatur napas."
    n "Dari bawah panggung, Ka Rhea mengangguk kecil, tanda ia menghargai langkah itu."
    jump cerita2_common


# ===== CABANG B: menolong Ghefira =====
label cerita2_b:
    show ghefira
    n "Ghefira naik panggung dengan tangan gemetar. Saat ia mulai membaca lirik, suaranya perlahan makin jelas."
    n "Penonton hening, lalu bertepuk tangan."

    menu:
        "Mengangguk memberi semangat dari sisi panggung.":
            jump d4_p2_b1

        "Maju dan menyahut bagian refren bersamanya.":
            jump d4_p2_b2

label d4_p2_b1:
    $ GHE += 2
    n "Ghefira mencari wajah Altan di sisi panggung. Setelah Altan mengangguk, bahunya turun, dan bait terakhir keluar dengan jelas."
    jump cerita2_common

label d4_p2_b2:
    $ GHE += 1
    $ ISY += 1
    n "Altan menyahut refren bersama Ghefira."
    n "Dari barisan penonton, Daisy melambai-lambai dengan wajah haru dan ikut menggerakkan bibirnya mengikuti lirik."
    jump cerita2_common


# ===== CABANG C: menolong Ka Rhea =====
label cerita2_c:
    show rhea
    n "Ka Rhea, meski pucat, memimpin barisan dari bawah panggung dengan wibawa."
    n "Yel-yel berjalan lancar. Murid-murid yang lain kagum pada kepemimpinannya."
    hide rhea

    menu:
        "Berdiri di samping Ka Rhea, menopangnya diam-diam.":
            jump d4_p2_c1

        "Menyampaikan ke Daisy dan Ghefira agar lebih mandiri dan percaya diri.":
            jump d4_p2_c2

label d4_p2_c1:
    $ RHE += 2
    n "Altan berdiri di sisi Ka Rhea tanpa bicara. Tangan Ka Rhea yang gemetar perlahan tenang, dan aba-abanya tetap tegas sampai akhir."
    jump cerita2_common

label d4_p2_c2:
    $ RHE += 1
    $ GHE += 1
    n "Daisy dan Ghefira mengangguk mantap setelah mendengar kata-kata Altan, lalu menyelesaikan bagian mereka sendiri."
    n "Ka Rhea menatap mereka dengan mata terkejut dan lega."
    jump cerita2_common


# ===== TITIK TEMU =====
label cerita2_common:

label d4_p3:
    n "Penutupan MPLS ditandai dengan api unggun. Murid-murid berkumpul melingkar, berbagi cerita, dan menyalakan lilin kecil satu per satu."

    n "Aku berdiri sebentar mencari tempat duduk. Daisy melambai dari sisi kiri lingkaran, Ghefira duduk menyendiri di sisi kanan sambil memeluk buku catatannya, dan Ka Rhea berdiri di dekat tumpukan kayu dengan tatapan jauh."
    n "Di tengah lingkaran, ada satu ruang kosong yang cukup untuk kami berempat."

label d4_p3_menu:
    menu:
        "Dengan siapa kamu duduk?"

        "Duduk di samping Daisy." if ISY >= 11:
            jump d4_p3_a

        "Duduk di samping Daisy. (terkunci)" if ISY < 11:
            jump d4_p3_terkunci

        "Duduk di samping Ghefira." if GHE >= 11:
            jump d4_p3_b

        "Duduk di samping Ghefira. (terkunci)" if GHE < 11:
            jump d4_p3_terkunci

        "Duduk di samping Ka Rhea." if RHE >= 11:
            jump d4_p3_c

        "Duduk di samping Ka Rhea. (terkunci)" if RHE < 11:
            jump d4_p3_terkunci

        "Duduk bersama semuanya.":
            jump d4_p3_d


label d4_p3_terkunci:
    n "Sepertinya kita belum cukup dekat untuk ini."
    jump d4_p3_menu


label d4_p3_a:
    $ ISY += 2
    isy "Altan, kamu tahu nggak? Empat hari ini aku ngerasa jadi versi diriku yang lebih baik."
    al "Kamu nggak berubah. Cuma lebih berani."
    jump d4_p3_common

label d4_p3_b:
    $ GHE += 2
    n "(Ghefira menyerahkan lipatan kertas.)"
    ghe "Ini... lirik yang nggak kuberikan ke siapa pun. Untukmu."
    jump d4_p3_common

label d4_p3_c:
    $ RHE += 2
    rhe "Aku nggak biasa begini. Tapi... kamu orang pertama yang bilang aku boleh capek."
    jump d4_p3_common

label d4_p3_d:
    $ ISY += 1
    $ RHE += 1
    $ GHE += 1
    n "Suasana hangat dan penuh tawa. Tapi tidak ada momen spesial dengan siapa pun."
    jump d4_p3_common


label d4_p3_common:

label cek_ending:
    n "Api unggun mulai padam. Satu per satu murid berpamitan, dan suara tawa perlahan menjauh dari halaman."
    n "Aku berjalan ke gerbang sambil memikirkan empat hari yang baru saja lewat. Dari awal hingga akhir, ada tiga orang yang mengubah caraku memandang sekolah ini."

label cek_ending_hitung:
    $ jenis, juara, tied = hitung_ending()

    # Pilihan D4-P4 hanya muncul sekali, kalau ada seri di puncak
    if len(tied) >= 2 and not seri_dicek and jenis != "bad":
        $ seri_dicek = True
        jump d4_p4

    jump ending_tentukan


label d4_p4:
    menu:
        "Siapa yang ingin kamu antar pulang malam ini?"

        "Daisy" if "isy" in tied:
            $ DAI += 1
            jump cek_ending_hitung

        "Ka Rhea" if "rhe" in tied:
            $ RHE += 1
            jump cek_ending_hitung

        "Ghefira" if "ghe" in tied:
            $ GHE += 1
            jump cek_ending_hitung


label ending_tentukan:
    if jenis == "true":
        if juara == "isy":
            jump true_ending_isy
        elif juara == "rhe":
            jump true_ending_rhe
        else:
            jump true_ending_ghe

    elif jenis == "good":
        if juara == "isy":
            jump good_ending_isy
        elif juara == "rhe":
            jump good_ending_rhe
        else:
            jump good_ending_ghe

    elif jenis == "normal":
        jump normal_ending

    else:
        jump bad_ending

# ===== TRUE ENDING: ISY (DAISY) =====
label true_ending_isy:
    scene bg pager
    show daisy malu
    isy "Altan! Aku punya sesuatu!"
    n "Ia menyodorkan papan nama kardus yang sudah ia laminasi dengan rapi. Di baliknya tertulis: \"Terima kasih sudah jadi teman pertamaku di Malaka.\""
    show daisy salting
    isy "Aku lupa bawa banyak hal selama empat hari ini. Tapi satu hal yang nggak bakal pernah kulupa, kamu."
    hide daisy salting
    al "Aku juga nggak akan lupa."
    n "Empat hari MPLS usai. Tapi tiga tahun SMA baru dimulai."
    centered "{size=+10}Ceria Tak Pernah Lupa{/size}"
    hide daisy
    return

# ===== GOOD ENDING: ISY (DAISY) =====
label good_ending_isy:
    show daisy
    isy "Besok kita sebangku lagi, ya?"
    al "Kalau kamu nggak lupa bawa tas."
    isy "Hahaha! Janji, nggak lupa!"
    n "Kami tertawa bersama di bawah lampu gerbang. Masih ada banyak hal yang belum kami ketahui, tapi aku yakin kami akan menemukannya pelan-pelan."
    centered "{size=+10}Awal yang Menyenangkan{/size}"
    hide daisy
    jump episode_1_complete

# ===== TRUE ENDING: KA RHEA =====
label true_ending_rhe:
    # scene bg gerbang_sekolah
    show rhea
    rhe "Kamu belum pulang?"
    al "Nunggu Kakak."
    rhe "(menghela napas, tersenyum tipis) Selama ini aku selalu berdiri paling depan. Nggak ada yang pernah menunggu aku di belakang."
    al "Mulai sekarang ada."
    n "Ia menatapku lama, lalu menyerahkan kotak kecil berisi pin OSIS. \"Jangan hilang.\""
    rhe "Aku nggak janji bisa jadi kakak yang lembut. Tapi aku janji akan selalu ada."
    centered "{size=+10}Di Balik Wibawa{/size}"
    hide rhea
    jump episode_1_complete

# ===== GOOD ENDING: KA RHEA =====
label good_ending_rhe:
    show rhea
    rhe "Besok kamu masuk kelas biasa. Jangan telat."
    al "Siap, Ka."
    rhe "Dan... kalau ada apa-apa, kamu boleh cari aku di ruang OSIS."
    n "Itu mungkin hal paling hangat yang pernah ia ucapkan."
    centered "{size=+10}Senior yang Mengawasi{/size}"
    hide rhea
    jump episode_1_complete

# ===== TRUE ENDING: GHEFIRA =====
label true_ending_ghe:
    # scene bg taman_belakang
    show ghefira
    ghe "Altan... aku punya kumpulan tulisan. Maukah kamu jadi pembaca pertamaku?"
    n "Ia menyerahkan buku catatan yang selama empat hari ini selalu ia peluk. Di halaman pertama tertulis: \"Untuk orang yang mendengarkan tanpa menyela.\""
    ghe "Aku nggak pandai bicara. Tapi di sini... aku bisa bilang semuanya."
    al "Aku akan baca semuanya, sampai halaman terakhir."
    n "Untuk pertama kalinya, Ghefira tertawa lepas."
    centered "{size=+10}Halaman yang Tak Pernah Kosong{/size}"
    hide ghefira
    jump episode_1_complete

# ===== GOOD ENDING: GHEFIRA =====
label good_ending_ghe:
    show ghefira
    ghe "Besok... boleh duduk bareng lagi di perpustakaan?"
    al "Boleh banget."
    ghe "(tersenyum kecil) Terima kasih sudah menunggu aku siap."
    centered "{size=+10}Kata yang Tertunda{/size}"
    hide ghefira
    jump episode_1_complete

# ===== NORMAL ENDING: PERSAHABATAN =====
label normal_ending:
    n "Aku punya tiga teman baru, dan tak satu pun di antaranya yang kupilih secara khusus. Tapi mungkin itu tidak apa-apa. Tiga tahun masih panjang."
    "Daisy, Ghefira, Ka Rhea" "(bersama) Sampai ketemu besok, Altan!"
    centered "{size=+10}Awal Cerita yang Panjang{/size}"
    jump episode_1_complete

# ===== BAD ENDING: SENDIRI =====
label bad_ending:
    n "Hari terakhir MPLS usai. Aku berjalan pulang sendirian. Tak ada yang melambai, tak ada yang menunggu."
    al "(Mungkin aku terlalu sibuk bertahan sampai lupa membuka diri.)"
    n "Tapi tiga tahun masih panjang. Masih ada kesempatan."
    centered "{size=+10}Empat Hari yang Terlewat{/size}"
    jump episode_1_complete

label episode_1_complete:

    # Simpan poin dari Episode 1.
    $ persistent.isy_points = ISY
    $ persistent.rhe_points = RHE
    $ persistent.ghe_points = GHE

    # Buka Episode 2.
    $ persistent.episode_unlocked = max(
        persistent.episode_unlocked or 1, 2
    )
    $ renpy.save_persistent()

    "Episode 1: MPLS telah selesai."
    "Poin pilihanmu telah disimpan."

    return

# =========================================
# EPISODE 2 - SETELAH MPLS
# =========================================

label episode_2:

    $ ISY = getattr(persistent, "isy_points", 0)
    $ RHE = getattr(persistent, "rhe_points", 0)
    $ GHE = getattr(persistent, "ghe_points", 0)

    # Lanjutkan cerita Episode 2 di bawah ini.

    scene bg halaman sekolah
    with fade

    "Beberapa hari setelah kegiatan MPLS berakhir..."

    al "Akhirnya kegiatan MPLS selesai juga."
    al "Tapi rasanya, ini justru awal dari sesuatu yang baru."

    "Altan mulai terbiasa dengan suasana SMA Malaka."
    "Ia juga mulai menyadari bahwa ada beberapa orang yang membuat hari-harinya terasa berbeda."

    menu:
        "Apa yang akan Altan lakukan hari ini?"

        "Mencari Daisy":
            $ ISY += 1
            jump episode_2_daisy

        "Menemui Ka Rhea":
            $ RHE += 1
            jump episode_2_rhea

        "Mengunjungi Ghefira":
            $ GHE += 1
            jump episode_2_ghefira


label episode_2_daisy:

    scene bg koridor
    with dissolve

    show daisy senang

    al "Daisy, sedang apa?"

    isy "Eh, Altan! Tumben kamu yang mencari aku."

    "Daisy tersenyum lebar, membuat Altan sedikit salah tingkah."

    al "Memangnya aku nggak boleh mencari kamu?"

    isy "Boleh, dong. Malah aku senang."

    jump episode_2_selesai


label episode_2_rhea:

    scene bg lapangan
    with dissolve

    show rhea

    al "Kak Rhea, ada yang bisa saya bantu?"

    rhe "Kamu sudah tidak perlu memanggilku hanya untuk urusan MPLS, Altan."

    al "Kalau begitu, boleh saya menyapa Kakak tanpa alasan khusus?"

    "Ka Rhea terdiam sebentar, lalu tersenyum tipis."

    rhe "Boleh. Asal jangan mengganggu kegiatanmu sendiri."

    jump episode_2_selesai


label episode_2_ghefira:

    scene bg koridor
    with dissolve

    show ghefira

    al "Ghefira, mau ke mana?"

    ghe "Aku mau mencari buku di perpustakaan."

    al "Kalau begitu, boleh aku menemanimu?"

    ghe "Boleh. Kalau kamu memang tidak keberatan."

    "Altan berjalan bersama Ghefira, menikmati percakapan kecil yang terasa nyaman."

    jump episode_2_selesai


label episode_2_selesai:

    scene bg halaman sekolah
    with fade

    "Hari itu berakhir dengan pengalaman baru bagi Altan."
    "Namun, ia belum menyadari bahwa pilihan-pilihannya akan menentukan kisah berikutnya."

    $ persistent.episode_unlocked = max(
        persistent.episode_unlocked or 1, 3
    )
    $ renpy.save_persistent()

    "Episode 2 selesai."

    # Simpan poin terbaru untuk Episode 3.
    $ persistent.isy_points = ISY
    $ persistent.rhe_points = RHE
    $ persistent.ghe_points = GHE

    $ persistent.episode_unlocked = max(
        persistent.episode_unlocked or 1, 3
    )
    $ renpy.save_persistent()

    "Episode 2 selesai."

    return

label episode_3:

    # Muat poin terakhir dari Episode 1 dan Episode 2.
    $ ISY = getattr(persistent, "isy_points", 0)
    $ RHE = getattr(persistent, "rhe_points", 0)
    $ GHE = getattr(persistent, "ghe_points", 0)

    "Saatnya Altan menentukan langkah berikutnya."

    if ISY >= RHE and ISY >= GHE:
        jump episode_3_daisy

    elif RHE >= ISY and RHE >= GHE:
        jump episode_3_rhea

    else:
        jump episode_3_ghefira


label episode_3_daisy:

    "Rute Daisy terbuka."
    "Altan mulai semakin dekat dengan Daisy."

    # Tambahkan cerita PDKT Daisy di sini.
    return


label episode_3_rhea:

    "Rute Ka Rhea terbuka."
    "Altan mulai melihat sisi lain dari Ka Rhea."

    # Tambahkan cerita PDKT Ka Rhea di sini.
    return


label episode_3_ghefira:

    "Rute Ghefira terbuka."
    "Altan mulai memahami Ghefira lebih dalam."

    # Tambahkan cerita PDKT Ghefira di sini.
    return