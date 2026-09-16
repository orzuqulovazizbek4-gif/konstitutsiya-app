import streamlit as st

# ==========================================
# 1. SAHIFA VA DIZAYN SOZLAMALARI
# ==========================================
st.set_page_config(
    page_title="O‘zbekiston Konstitutsiyasi: PhD Tahlil Markazi (1-18 moddalar)",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; font-weight: 800; color: #1e3a8a; text-align: center; margin-bottom: 5px; }
    .sub-header { font-size: 1.1rem; text-align: center; color: #475569; margin-bottom: 25px; font-style: italic; }
    .chapter-badge { display: inline-block; padding: 6px 16px; background: #1e40af; color: white; border-radius: 20px; font-weight: bold; margin-bottom: 15px; font-size: 0.95rem; }
    .article-box { background: #f8fafc; border-left: 6px solid #2563eb; padding: 20px; border-radius: 6px; font-size: 1.05rem; line-height: 1.6; color: #0f172a; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .card-box { background: #ffffff; border: 1px solid #e2e8f0; padding: 18px; border-radius: 8px; margin-top: 10px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
    .scholar-title { color: #1e3a8a; font-size: 1.15rem; font-weight: 700; border-bottom: 2px solid #3b82f6; padding-bottom: 4px; display: inline-block; margin-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. MUKAMMAL DOKTRINAL MA'LUMOTLAR BAZASI
# ==========================================
ARTICLES_DB = {
    # --- I BOB. DAVLAT SUVERENITETI ---
    1: {
        "chapter": "I BOB. DAVLAT SUVERENITETI",
        "title": "1-modda. Davlat shakli va atributlari",
        "text": "Oʻzbekiston — boshqaruvning respublika shakliga ega boʻlgan suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlat.\nDavlatning “Oʻzbekiston Respublikasi” va “Oʻzbekiston” degan nomlari bir maʼnoni anglatadi.",
        "basis": [
            "1991-yil 31-avgustdagi «O‘zbekiston Respublikasining Davlat mustaqilligi asoslari to‘g‘risida»gi Konstitutsiyaviy Qonun (O‘RQ-336-XII)",
            "1990-yil 20-iyundagi «Mustaqillik deklaratsiyasi»",
            "2023-yil 30-apreldagi Referendumda qabul qilingan Konstitutsiyaviy Qonun"
        ],
        "analysis": "Ushbu norma konstitutsiyaviy tuzumning tamal ustuni (*Materia Constitutionis*) hamda davlatning konstitutsiyaviy identifikatsiyasini belgilovchi *Eternity Clause* (o‘zgarmas norma) hisoblanadi. U davlatning 5 ta poydevor sifatini: Suverenitet (mustaqillik), Demokratiya (xalq hokimiyati), Huquqiy davlat (*Rechtsstaat*), Ijtimoiy davlat (*Sozialstaat*) va Dunyoviylik (*Secular State*) prinsiplarini yuridik sintez qiladi.",
        "scholars": [
            {"name": "Xans Kelsen (Hans Kelsen)", "theory": "Grundnorm (Asosiy Norma)", "desc": "Kelsenga ko‘ra, 1-modda milliy huquqiy piramidaning cho‘qqisida turuvchi va barcha quyi normativ hujjatlarning legitimligini ta'minlovchi oliy gipotezadir."},
            {"name": "Jan Boden (Jean Bodin)", "theory": "Suverenitetning Mutlaqligi Doktrinasi", "desc": "Boden ta'limotidagi suverenitet — davlatning ichki hududda mutlaq ustunligi va xalqaro munosabatlarda mustaqilligining konstitutsiyaviy ifodasidir."}
        ]
    },
    2: {
        "chapter": "I BOB. DAVLAT SUVERENITETI",
        "title": "2-modda. Davlatning xizmatkorlik funksiyasi va mas'uliyati",
        "text": "Davlat xalq irodasini ifoda etib, uning manfaatlariga xizmat qiladi. Davlat organlari va mansabdor shaxslar jamiyat va fuqarolar oldida masʼuldirlar.",
        "basis": [
            "«Davlat hokimiyati va boshqaruvi organlari faoliyatining ochiqligi to‘g‘risida»gi O‘RQ-369-son Qonun",
            "«Jamoatchilik nazorati to‘g‘risida»gi O‘RQ-474-son Qonun",
            "«Jismoniy va yuridik shaxslarning murojaatlari to‘g‘risida»gi O‘RQ-445-son Qonun"
        ],
        "analysis": "Modda davlat apparatini *Leviatan* (bostirib turuvchi kuch) modelidan *Service State* (xizmat ko‘rsatuvchi servis davlat) modeliga o‘tkazadi. Davlat va fuqaro o‘rtasidagi munosabat subordinatsiyadan fidutsiar (ishonchli mas'uliyat) munosabatiga aylanadi.",
        "scholars": [
            {"name": "Jon Lokk (John Locke)", "theory": "Hokimiyatning Fidutsiar Tabiati (Political Trust)", "desc": "Lokk fikricha, xalq davlatga hokimiyatni muayyan shartlar bilan topshiradi. Mas'uliyat yo‘qolgan joyda davlatning legitimligi tugaydi."},
            {"name": "Leon Dugi (Léon Duguit)", "theory": "Service Public (Ommaviy Xizmat) Doktrinasi", "desc": "Dugi ta'kidlaganidek, davlat — bu hokimiyat yurituvchi kuch emas, balki jamiyat ehtiyojlari uchun ommaviy xizmatlarni tashkillashtiruvchi muassasadir."}
        ]
    },
    3: {
        "chapter": "I BOB. DAVLAT SUVERENITETI",
        "title": "3-modda. Hududiy yaxlitlik va davlat mustaqilligi",
        "text": "Oʻzbekiston Respublikasi oʻzining milliy-davlat va maʼmuriy-hududiy tuzilishini, davlat hokimiyati organlarining tizimini belgilaydi, ichki va tashqi siyosatini amalga oshiradi.\nOʻzbekistonning davlat chegarasi va hududi daxlsiz va boʻlinmasdir.",
        "basis": [
            "«O‘zbekiston Respublikasining Davlat chegarasi to‘g‘risida»gi O‘RQ-868-son Qonun (yangi tahriri)",
            "«O‘zbekiston Respublikasining ma’muriy-hududiy tuzilishi to‘g‘risida»gi O‘RQ-627-son Qonun"
        ],
        "analysis": "Hududiy yaxlitlik va bo‘linmaslik (*Territorial Integrity*) davlatning fazoviy yurisdiksiyasini belgilaydi. 'Daxlsiz' degani tashqi tajovuzdan, 'bo‘linmas' degani esa ichki separatizmdan yuridik himoyani anglatadi.",
        "scholars": [
            {"name": "Georg Yellinek (Georg Jellinek)", "theory": "Davlatning Uch Elementi Doktrinasi (Drei-Elemente-Lehre)", "desc": "Yellinek bo‘yicha davlat mavjud bo‘lishi uchun Hudud (Staatsgebiet), Xalq (Staatsvolk) va Hokimiyat (Staatsgewalt) shart. 3-modda ushbu birinchi elementni kafolatlaydi."},
            {"name": "Pol Foshil (Paul Fauchille)", "theory": "Eksklyuziv Hududiy Yurisdiksiya", "desc": "Foshil ta'limotiga ko‘ra, davlat hududi ustida faqat shu davlatning o‘zigina mutlaq suveren huquqlarni amalga oshirishga haqlidir."}
        ]
    },
    4: {
        "chapter": "I BOB. DAVLAT SUVERENITETI",
        "title": "4-modda. Davlat tili va bag'rikenglik",
        "text": "Oʻzbekiston Respublikasining davlat tili oʻzbek tilidir.\nOʻzbekiston Respublikasi oʻz hududida istiqomat qiluvchi millat va elatlarning tillari, urf-odatlari va anʼanalari hurmat qilinishini taʼminlaydi, ularning rivojlanishi uchun sharoit yaratadi.",
        "basis": [
            "«Davlat tili haqida»gi O‘RQ-547-I-son Qonun (yangi tahriri)",
            "Xalqaro milliy ozchiliklar huquqlarini himoya qilish to'g'risidagi konvensiyalar"
        ],
        "analysis": "Modda bir vaqtning o‘zida lingvistik suverenitetni (integratsion til) hamda pluralistik multikulturalizm (etnik va lingvistik bag‘rikenglik) prinsiplarini o‘zida uyg‘unlashtiradi.",
        "scholars": [
            {"name": "Yohann Gotfrid fon Gerder (J.G. Herder)", "theory": "Til — Millat Ruhi (Volksgeist)", "desc": "Gerder nazariyasiga ko‘ra, davlat tili millatning kollektiv ongi va madaniyatining bosh uzviy elementi hisoblanadi."},
            {"name": "Vil Kimlika (Will Kymlicka)", "theory": "Multikultural Fuqarolik (Multicultural Citizenship)", "desc": "Kimlika davlat tilini mustahkamlash bilan birga kamchilikni tashkil etuvchi etnoslar huquqlarini kafolatlash barqarorlik omili ekanligini isbotlagan."}
        ]
    },
    5: {
        "chapter": "I BOB. DAVLAT SUVERENITETI",
        "title": "5-modda. Davlat ramzlari",
        "text": "Oʻzbekiston Respublikasi qonun bilan tasdiqlanadigan oʻz davlat ramzlari — bayrogʻi, gerbi va madhiyasiga ega.\nDavlat ramzlari davlat himoyasidadir.",
        "basis": [
            "«O‘zbekiston Respublikasining Davlat bayrog‘i to‘g‘risida»gi O‘RQ-407-XII-son Qonun",
            "«O‘zbekiston Respublikasining Davlat gerbi to‘g‘risida»gi O‘RQ-615-XII-son Qonun",
            "«O‘zbekiston Respublikasining Davlat madhiyasi to‘g‘risida»gi O‘RQ-768-XII-son Qonun"
        ],
        "analysis": "Davlat ramzlari — suverenitet va identiklikning rasmiy siyosiy-semiotik timsollaridir. Ularni davlat himoyasiga olish – konstitutsiyaviy tuzum va milliy g‘ururni huquqiy muhofaza qilish demakdir.",
        "scholars": [
            {"name": "Ernst Kantorovich (Ernst Kantorowicz)", "theory": "Siyosiy Semiotika va Sakral Identiklik", "desc": "Kantorovich ta'kidlaganidek, abstrakt davlat mexanizmi ramzlar orqali fuqarolar ongida moddiy va psixologik shaklga kiradi."},
            {"name": "Marrey Edelman (Murray Edelman)", "theory": "Siyosiy Timsollar va Mobilizatsiya", "desc": "Edelman ta'limotida davlat ramzlari jamiyatni umumiy qadriyatlar va g‘oyalar atrofida jipslashtiruvchi ramziy vositadir."}
        ]
    },
    6: {
        "chapter": "I BOB. DAVLAT SUVERENITETI",
        "title": "6-modda. Poytaxt maqomi",
        "text": "Oʻzbekiston Respublikasining poytaxti — Toshkent shahri.",
        "basis": [
            "«O‘zbekiston Respublikasi poytaxtining maqomi to‘g‘risida»gi O‘RQ-922-I-son Qonun"
        ],
        "analysis": "Poytaxt — davlat konstitutsiyaviy organlari joylashgan siyosiy, ma'muriy va huquqiy markaz (*Locus of Power*). Bu norma poytaxt maqomini oliy yuridik darajada qat'iylashtiradi.",
        "scholars": [
            {"name": "Maks Veber (Max Weber)", "theory": "Legal-Ratsional Hukmronlik Markazi", "desc": "Veber sotsiologiyasida poytaxt — markaziy byurokratiya va davlat boshqaruv institutlari jamlangan asosiy jug‘rofiy-huquqiy makondir."},
            {"name": "Xalford Makkinder (Sir Halford Mackinder)", "theory": "Geosiyosiy Markaz (Heartland) Doktrinasi", "desc": "Makkinder bo‘yicha poytaxt shunchaki shahar emas, u butun davlat hududini boshqaruvchi va vertikal nazorat qiluvchi markaziy tugundir."}
        ]
    },

    # --- II BOB. XALQ HOKIMIYATCHILIGI ---
    7: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "7-modda. Xalq suvereniteti va hokimiyat uzurpatsiyasi taqiqi",
        "text": "Xalq davlat hokimiyatining birdan-bir manbaidir.\nOʻzbekiston Respublikasida davlat hokimiyati xalq manfaatlarini koʻzlab va Oʻzbekiston Respublikasi Konstitutsiyasi hamda uning asosida qabul qilingan qonunlar vakolat bergan organlar tomonidangina amalga oshiriladi.\nKonstitutsiyada nazarda tutilmagan tartibda davlat hokimiyati vakolatlarini oʻzlashtirish, hokimiyat organlari faoliyatini toʻxtatib qoʻyish yoki tugatish, hokimiyatning yangi va muvoziy tarkiblarini tuzish Konstitutsiyaga xilof hisoblanadi va qonunga binoan javobgarlikka tortishga asos boʻladi.",
        "basis": [
            "O‘zbekiston Respublikasining Saylov kodeksi (O‘RQ-544-son)",
            "O‘zbekiston Respublikasining Jinoyat kodeksi (159-modda - Konstitutsiyaviy tuzumga tajovuz qilish)",
            "«O‘zbekiston Respublikasining Referendumi to‘g‘risida»gi O‘RQ-265-I-son Qonun"
        ],
        "analysis": "Xalq suvereniteti (*Popular Sovereignty*) prinsipi. Davlat idoralari o‘zicha mutlaq emas, ular xalq bergan mandanggina vakolat oladi. Har qanday parallel (muvoziy) hokimiyat tuzish yoki hokimiyatni uzurpatsiya qilish eng og‘ir konstitutsiyaviy jinoyat hisoblanadi.",
        "scholars": [
            {"name": "Karl Shmitt (Carl Schmitt)", "theory": "Pouvoir Constituant (Ta'sis etuvchi hokimiyat)", "desc": "Shmittga ko‘ra, xalq yagona ta'sis etuvchi hokimiyat sohibidir. Davlat institutlari faqat xalq irodasi bergan doiradagina (Pouvoir constitué) faoliyat yuritadi."},
            {"name": "Jan-Jak Russo (Jean-Jacques Rousseau)", "theory": "Bo‘linmas Xalq Suvereniteti", "desc": "Russo ta'kidlaganidek, suverenitet xalqqa tegishli bo‘lib, uni o‘zlashtirgan yoki uzurpatsiya qilgan har qanday tuzilma nolegitimdir."}
        ]
    },
    8: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "8-modda. O'zbekiston xalqi tushunchasi",
        "text": "Oʻzbekiston xalqini millatidan qatʼi nazar, Oʻzbekiston Respublikasining fuqarolari tashkil etadi.",
        "basis": [
            "«O‘zbekiston Respublikasining fuqaroligi to‘g‘risida»gi O‘RQ-610-son Qonun (yangi tahriri)"
        ],
        "analysis": "Siyosiy-fuqarolik millati (*Civic Nation*) doktrinasi. Norma etnik millatchilikni rad etib, fuqarolik huquqiy rishtasini jamiyatni birlashtiruvchi yagona konstitutsiyaviy mezon deb belgilaydi.",
        "scholars": [
            {"name": "Yurgen Habermas (Jürgen Habermas)", "theory": "Konstitutsiyaviy Vatanparvarlik (Verfassungspatriotismus)", "desc": "Habermas fikricha, zamonaviy jamiyatni etnik kelib chiqish emas, balki Konstitutsiya va umumiy fuqarolik huquqlariga bo‘lgan sadoqat birlashtiradi."},
            {"name": "Ernest Renan (Ernest Renan)", "theory": "Fuqarolik Jamiyati va Millat Erki", "desc": "Renanning mashhur 'Millat — bu har kungi referendum' tezisi 8-moddadagi fuqarolarning jamoaviy va teng irodasi bilan mos tushadi."}
        ]
    },
    9: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "9-modda. Bevosita demokratiya va referendum",
        "text": "Jamiyat va davlat hayotining eng muhim masalalari xalq muhokamasiga taqdim etiladi, umumxalq ovoziga — referendumga qoʻyiladi.\nOʻzbekiston Respublikasida referendum oʻtkazish tartibi qonun bilan belgilanadi.",
        "basis": [
            "«O‘zbekiston Respublikasining Referendumi to‘g‘risida»gi O‘RQ-265-I-son Qonun",
            "«Qonun loyihalarining muhokamasi to‘g‘risida»gi O‘RQ-76-son Qonun"
        ],
        "analysis": "To‘g‘ridan-to‘g‘ri (plebissitar) demokratiya instituti. Xalq vakillik organlarisiz, muhim masalalarni bevosita ovoz berish orqali hal qilish imkoniyatiga ega bo‘ladi.",
        "scholars": [
            {"name": "Aleksis de Tokvil (Alexis de Tocqueville)", "theory": "Ishtirokchi Demokratiya", "desc": "Tokvil ta'kidlaganidek, xalqning bevosita qarorlar qabul qilishda ishtirok etishi davlat tiraniyasining oldini oluvchi eng kuchli qalqondir."},
            {"name": "Arend Layphart (Arend Lijphart)", "theory": "Konsensus Demokratiyasi", "desc": "Layphart referendum va jamoatchilik muhokamalarini jamiyatda keng konsensus va ijtimoiy kelishuv yaratish vositasi deb baholaydi."}
        ]
    },
    10: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "10-modda. Eksklyuziv vakillik mandati",
        "text": "Oʻzbekiston xalqi nomidan faqat u saylagan Oʻzbekiston Respublikasi Oliy Majlisi va Prezidenti ish olib borishi mumkin.\nJamiyatning biron-bir qismi, siyosiy partiya, jamoat birlashmasi, ijtimoiy harakat yoki alohida shaxs Oʻzbekiston xalqi nomidan ish olib borishga haqli emas.",
        "basis": [
            "O‘zbekiston Respublikasining Saylov kodeksi",
            "«O‘zbekiston Respublikasi Oliy Majlisi Qonunchilik palatasi to‘g‘risida»gi Konstitutsiyaviy Qonun",
            "«O‘zbekiston Respublikasi Prezidenti faoliyatining asosiy kafolatlari to‘g‘risida»gi Qonun"
        ],
        "analysis": "Ushbu norma vakillik mandatining monopoliya huquqini belgilaydi. Noyuridik guruhlar yoki alohida partiyalarning 'biz xalq nomidan gapirayapmiz' degan monopolistik da'volarini qat'iyan taqiqlaydi.",
        "scholars": [
            {"name": "Edmund Berk (Edmund Burke)", "theory": "Vakillikning Ishonchli (Trustee) Modeli", "desc": "Berk qarashlariga ko‘ra, saylangan vakillar umummillat mandatiga ega bo‘ladi va faqat ular butun millat nomidan qaror qabul qilishga legitim huquqqa ega."},
            {"name": "Yozef Shumpeter (Joseph Schumpeter)", "theory": "Elitar-Vakillik Demokratiyasi Model", "desc": "Shumpeter demokratiyani saylovlar orqali xalqdan vakolat olgan elitaning qonuniy boshqaruvi sifatida ta'riflaydi."}
        ]
    },
    11: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "11-modda. Hokimiyatlar bo'linishi prinsipi",
        "text": "Oʻzbekiston Respublikasi davlat hokimiyatining tizimi — hokimiyatning qonun chiqaruvchi, ijro etuvchi va sud hokimiyatiga boʻlinishi prinsipiga asoslanadi.",
        "basis": [
            "«O‘zbekiston Respublikasi Oliy Majlisi to‘g‘risida»gi Konstitutsiyaviy Qonunlar",
            "«O‘zbekiston Respublikasi Vazirlar Mahkamasi to‘g‘risida»gi O‘RQ-591-son Qonun",
            "«Sudlar to‘g‘risida»gi O‘RQ-703-son Qonun (yangi tahriri)"
        ],
        "analysis": "Tiyib turish va muvozanatlash (*Checks and Balances*) tizimi. Mutlaq hokimiyat konsentratsiyasining oldini olish uchun hokimiyat funksiyalari uchta mustaqil tarmoqqa bo‘linadi.",
        "scholars": [
            {"name": "Sharl Lui de Monteskyo (Montesquieu)", "theory": "Hokimiyatlar Bo'linishi (Trias Politica)", "desc": "Monteskyoning 'Qonunlar ruhi haqida' asariga ko‘ra, inson erkinligi ta'minlanishi uchun qonun chiqaruvchi, ijro va sud hokimiyati alohida qo‘llarda bo‘lishi shart."},
            {"name": "Djayms Madison (James Madison)", "theory": "Tiyib Turish va Muvozanatlash Tizimi", "desc": "Federalist No. 51 yozuvchisi Madison ta'kidlaganidek, 'Ambitsiya ambitsiyaga qarshi turishi kerak' — har bir tarmoq boshqasini tiyib turishi shart."}
        ]
    },
    12: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "12-modda. Siyosiy va mafkuraviy plyuralizm",
        "text": "Oʻzbekiston Respublikasida ijtimoiy hayot siyosiy institutlar, mafkuralar va fikrlarning xilma-xilligi asosida rivojlanadi.\nHech qaysi mafkura davlat mafkurasi sifatida oʻrnatilishi mumkin emas.",
        "basis": [
            "«Siyosiy partiyalar to‘g‘risida»gi O‘RQ-337-I-son Qonun",
            "«Nodavlat nodijorat tashkilotlari to‘g‘risida»gi O‘RQ-763-I-son Qonun",
            "«Vijdon erkinligi va diniy tashkilotlar to‘g‘risida»gi O‘RQ-698-son Qonun"
        ],
        "analysis": "Totalitarizm va avtoritarizmga qarshi konstitutsiyaviy kafolat. Davlat muayyan bir g‘oyani monopoliyaga ololmaydi, jamiyat ochiq g‘oyalar va partiyalar raqobati asosida rivojlanadi.",
        "scholars": [
            {"name": "Karl Popper (Karl Popper)", "theory": "Ochiq Jamiyat (The Open Society)", "desc": "Popper fikricha, yagona davlat mafkurasi o o‘rnatilgan jamiyatlar yopiq (totalitar) hisoblanadi. Rivojlanish faqat fikrlar xilma-xilligi mavjud joyda bo‘ladi."},
            {"name": "Isayya Berlin (Isaiah Berlin)", "theory": "Qadriyatlar Plyuralizmi (Pluralism of Values)", "desc": "Berlin jamiyatda turlicha qarashlar va mafkuralar mavjudligini inson erkinligining tabiiy ko‘rinishi va ajralmas huquqi deb bilgan."}
        ]
    },
    13: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "13-modda. Inson qadri va ajralmas huquqlari",
        "text": "Oʻzbekiston Respublikasida demokratiya umuminsoniy prinsiplarga asoslanadi, ularga koʻra inson, uning hayoti, erkinligi, shaʼni, qadr-qimmati va boshqa ajralmas huquqlari oliy qadriyat hisoblanadi.\nDemokratik huquq va erkinliklar Konstitutsiya va qonunlar bilan himoya qilinadi.",
        "basis": [
            "1948-yilgi Inson huquqlari umumjahon deklaratsiyasi",
            "Inson huquqlari bo‘yicha Milliy strategiya (O‘zbekiston Respublikasi Prezidentining Farmoni)",
            "«Inson huquqlari bo‘yicha Vakil (Ombudsman) to‘g‘risida»gi O‘RQ"
        ],
        "analysis": "Huquqiy Antropotsentrizm va Inson Qadri (*Human Dignity*) prinsipi. Davlat va jamiyat inson uchun mavjuddir, inson davlat maqsadlariga erishish vositasi emas.",
        "scholars": [
            {"name": "Immanuil Kant (Immanuel Kant)", "theory": "Kategorik Imperativ va Inson Qadri", "desc": "Kant ta'limotida inson hech qachon boshqa narsalarga erishish uchun 'vosita' bo‘lishi mumkin emas; insonning o‘zi mutlaq 'maqsad' va oliy qadriyatdir."},
            {"name": "Ronald Dvorkin (Ronald Dworkin)", "theory": "Huquqlarni Jiddiy Qabul Qilish (Taking Rights Seriously)", "desc": "Dvorkin bo‘yicha inson huquqlari davlat va ko‘pchilikning irodasidan ustun turuvchi 'kozir' (trump) hisoblanadi."}
        ]
    },
    14: {
        "chapter": "II BOB. XALQ HOKIMIYATCHILIGI",
        "title": "14-modda. Davlat faoliyatining tamal prinsiplari",
        "text": "Davlat oʻz faoliyatini inson farovonligini va jamiyatning barqaror rivojlanishini taʼminlash maqsadida qonuniylik, ijtimoiy adolat va birdamlik prinsiplari asosida amalga oshiradi.",
        "basis": [
            "«Aholi bandligi to‘g‘risida»gi O‘RQ-642-son Qonun",
            "«Ijtimoiy xizmatlar to‘g‘risida»gi O‘RQ-415-son Qonun",
            "Kambag‘allikni qisqartirish va ijtimoiy himoyaga oid normativ hujjatlar"
        ],
        "analysis": "Davlatning maqsadli majburiyatlari (*Staatszielbestimmungen*). Davlat faoliyati faqat ma'muriy boshqaruv emas, balki ijtimoiy adolat, birdamlik (*Solidarity*) va inson farovonligiga yo‘naltirilgan bo‘lishi shart.",
        "scholars": [
            {"name": "Jon Roulz (John Rawls)", "theory": "Adolat Nazariyasi va Farqlash Prinsipi", "desc": "Roulz bo‘yicha adolatli davlat jamiyatdagi eng muhtoj va zaif qatlamlar farovonligini oshirishni o‘z zimmasiga olgan davlatdir."},
            {"name": "Amartya Sen (Amartya Sen)", "theory": "Salohiyatlar Yondashuvi (Capabilities Approach)", "desc": "Nobel mukofoti sovrindori Sen davlat rivojlanishini inson imkoniyatlari va salohiyatini kengaytirish bilan o‘lchaydi."}
        ]
    },

    # --- III BOB. KONSTITUTSIYA VA QONUNNING USTUNLIGI ---
    15: {
        "chapter": "III BOB. KONSTITUTSIYA VA QONUNNING USTUNLIGI",
        "title": "15-modda. Konstitutsiya va qonun ustunligi, to'g'ridan-to'g'ri amal qilish",
        "text": "Oʻzbekiston Respublikasida Oʻzbekiston Respublikasi Konstitutsiyasi va qonunlarining ustunligi soʻzsiz tan olinadi.\nOʻzbekiston Respublikasi Konstitutsiyasi mamlakatning butun hududida oliy yuridik kuchga ega, toʻgʻridan-toʻgʻri amal qiladi va yagona huquqiy makonning asosini tashkil etadi. Alohida hududlarda Oʻzbekiston Respublikasining Konstitutsiyaviy Qonuni bilan yagona huquqiy makon doirasida maxsus huquqiy rejim oʻrnatilishi mumkin.\nOʻzbekiston Respublikasining xalqaro shartnomalari xalqaro huquqning umumeʼtirof etilgan prinsip va normalari bilan bir qatorda Oʻzbekiston Respublikasi huquqiy tizimining tarkibiy qismidir. Agar Oʻzbekiston Respublikasining xalqaro shartnomasida Oʻzbekiston Respublikasining qonunida nazarda tutilganidan boshqacha qoidalar belgilangan boʻlsa, Oʻzbekiston Respublikasining xalqaro shartnomasi qoidalari qoʻllaniladi.\nDavlat va uning organlari, boshqa tashkilotlar, mansabdor shaxslar, fuqarolik jamiyati institutlari hamda fuqarolar Konstitutsiya va qonunlarga muvofiq ish yuritadilar.",
        "basis": [
            "«O‘zbekiston Respublikasining Konstitutsiyaviy sudi to‘g‘risida»gi O‘RQ-688-son Konstitutsiyaviy Qonun",
            "«Normativ-huquqiy hujjatlar to‘g‘risida»gi O‘RQ-682-son Qonun",
            "«O‘zbekiston Respublikasining xalqaro shartnomalari to‘g‘risida»gi O‘RQ-525-son Qonun"
        ],
        "analysis": "Konstitutsionierarxiya va *Direct Effect* (To‘g‘ridan-to‘g‘ri amal qilish) prinsipi. Konstitutsiya sudlarda to‘g‘ridan-to‘g‘ri qo‘llaniladigan hujjatdir. Xalqaro shartnomalarning milliy huquqqa integratsiyasi va qonunlar oldidagi ustunligi (monizm/primat) kafolatlanadi.",
        "scholars": [
            {"name": "Xans Kelsen (Hans Kelsen)", "theory": "Normalar Piramidasi (Stufenbau der Rechtsordnung)", "desc": "Kelsen yuridik tizimni ierarxik piramida deb ataydi: Konstitutsiya eng tepada turadi, quyi normalar unga zid bo‘lsa o‘z kuchini yo‘qotadi."},
            {"name": "X.L.A. Hart (H.L.A. Hart)", "theory": "Tan Olish Qoidasi (Rule of Recognition)", "desc": "Hart fikricha, Konstitutsiya huquqiy tizimdagi barcha boshqa qoidalarning haqiqiyligi va kuchini belgilab beruvchi eng oliy mezondir."}
        ]
    },
    16: {
        "chapter": "III BOB. KONSTITUTSIYA VA QONUNNING USTUNLIGI",
        "title": "16-modda. Konstitutsiya yaxlitligi va talqin qilish taqiqlari",
        "text": "Ushbu Konstitutsiyaning birorta qoidasi Oʻzbekiston Respublikasining huquq va manfaatlariga, ushbu Konstitutsiyaning birinchi boʻlimida nazarda tutilgan asosiy prinsip va normalarga zarar yetkazadigan tarzda talqin etilishi mumkin emas.\nOʻzbekiston Respublikasining qonunlari va boshqa normativ-huquqiy hujjatlari Oʻzbekiston Respublikasining Konstitutsiyasi asosida va uni ijro etish yuzasidan qabul qilinadi. Birorta qonun yoki boshqa normativ-huquqiy hujjat Konstitutsiyaning prinsip va normalariga zid boʻlishi mumkin emas.",
        "basis": [
            "«O‘zbekiston Respublikasining Konstitutsiyaviy sudi to‘g‘risida»gi Konstitutsiyaviy Qonun",
            "«Normativ-huquqiy hujjatlar to‘g‘risida»gi O‘RQ-682-son Qonun"
        ],
        "analysis": "Konstitutsiyaviy yaxlitlik va *In dubio pro libertate* (Inson va davlat manfaatlariga zarar yetkazmaslik) talqin prinsipi. Konstitutsiyaning biror normasini suiiste'mol qilib, uning tamal prinsiplariga zarar yetkazish taqiqlanadi.",
        "scholars": [
            {"name": "Aharon Barak (Aharon Barak)", "theory": "Purposive Interpretation (Maqsadli Talqin)", "desc": "Isroil Oliy sudi sobiq raisi Barak ta'kidlaganidek, Konstitutsiya o‘z qadriyat va prinsiplariga zid kelmaydigan, uning umumiy ruhini saqlagan holda talqin qilinishi shart."},
            {"name": "Antonin Skaliya (Antonin Scalia)", "theory": "Konstitutsiyaviy Tekstualizm", "desc": "Skaliya konstitutsiyaviy normalarni buzib yoki noto‘g‘ri kengaytirib talqin qilish konstitutsiyaviy tartibotni barbod etishini isbotlagan."}
        ]
    },

    # --- IV BOB. TASHQI SIYOSAT ---
    17: {
        "chapter": "IV BOB. TASHQI SIYOSAT",
        "title": "17-modda. Tashqi siyosatning xalqaro-huquqiy prinsiplari",
        "text": "Oʻzbekiston Respublikasi xalqaro munosabatlarning toʻla huquqli subyektidir.\nOʻzbekistonning tashqi siyosati davlatlarning suveren tengligi, kuch ishlatmaslik yoki kuch bilan tahdid qilmaslik, chegaralarning buzilmasligi, davlatlarning hududiy yaxlitligi, nizolarni tinch yoʻl bilan hal etish, boshqa davlatlarning ichki ishlariga aralashmaslik prinsiplariga hamda xalqaro huquqning umumeʼtirof etilgan boshqa prinsip va normalariga asoslanadi.",
        "basis": [
            "Birlashgan Millatlar Tashkilotining Nizomi (1945-yil)",
            "1975-yilgi Xelsinki Yakuniy Hujjati",
            "«O‘zbekiston Respublikasining Tashqi siyosiy faoliyati konsepsiyasini tasdiqlash to‘g‘risida»gi O‘RQ"
        ],
        "analysis": "Tashqi siyosatning konstitutsionalizatsiyasi. Xalqaro huquqning 7 ta asosiy prinsipini milliy Konstitutsiyaga singdirish orqali davlat o‘zining tinchliksevar va mas'uliyatli xalqaro subyekt ekanligini muhrlaydi.",
        "scholars": [
            {"name": "Gyugo Grotsiy (Hugo Grotius)", "theory": "Xalqaro Huquq Prinsipialligi (De Jure Belli ac Pacis)", "desc": "Xalqaro huquq otasi Grotsiy davlatlararo munosabatlar kuchga emas, qat'iy huquqiy norma va tinch kelishuvlarga asoslanishi shartligini ko‘rsatgan."},
            {"name": "Hedli Bull (Hedley Bull)", "theory": "Anarxik Jamiyat va Xalqaro Tartib", "desc": "Bull ta'limotida suveren tenglik va aralashmaslik prinsiplari global xaosning oldini oluvchi xalqaro tartib ustunlaridir."}
        ]
    },
    18: {
        "chapter": "IV BOB. TASHQI SIYOSAT",
        "title": "18-modda. Xalqaro hamkorlik va ittifoqlar tuzish huquqi",
        "text": "Oʻzbekiston Respublikasi davlatlar va xalqaro tashkilotlar bilan ikki va koʻp tomonlama munosabatlarni har taraflama rivojlantirishga qaratilgan tinchliksevar tashqi siyosatni amalga oshiradi.\nOʻzbekiston Respublikasi davlatning, xalqning oliy manfaatlaridan, uning farovonligi va xavfsizligidan kelib chiqqan holda ittifoqlar tuzishi, hamdoʻstliklarga va boshqa davlatlararo tuzilmalarga kirishi hamda ulardan chiqishi mumkin.",
        "basis": [
            "«O‘zbekiston Respublikasining xalqaro shartnomalari to‘g‘risida»gi O‘RQ-525-son Qonun",
            "Xalqaro tashkilotlar va ittifoqlarga a'zolik to'g'risidagi maxsus ratifikatsiya qonunlari"
        ],
        "analysis": "Suveren Pragmatizm va Integratsiya Huquqi. Davlat o‘z milliy xavfsizligi va farovonligidan kelib chiqib xalqaro blroklarga kirish yoki chiqish erkinligiga ega (bloklarga qo‘shilmaslik/qo‘shilish suveren huquqi).",
        "scholars": [
            {"name": "Robert Kioheyn (Robert Keohane)", "theory": "Neoliberal Institutsionalizm", "desc": "Kioheyn ko‘ra, zamonaviy davlatlar xavfsizlik va taraqqiyotga yakkalanish orqali emas, balki xalqaro tashkilotlar va ko‘p tomonlama hamkorlik orqali erishadi."},
            {"name": "Immanuil Kant (Immanuel Kant)", "theory": "Abadiy Tinchlik (Perpetual Peace)", "desc": "Kantning Abadiy tinchlik risolasiga ko‘ra, davlatlarning tinchliksevar ittifoqlari (Foedus Pacificum) global urushlarning oldini oluvchi yagona kafolatdir."}
        ]
    }
}

# ==========================================
# 3. INTERFEYS VA LOGIKA (UI)
# ==========================================

st.markdown('<div class="main-header">O‘ZBEKISTON RESPUBLIKASI KONSTITUTSIYASI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">I - IV Boblar (1–18 Moddalar): Aniq Normativ Asoslar va PhD Darajasidagi Akademik Tahlil</div>', unsafe_allow_html=True)

# Sidebar (Yon panel)
st.sidebar.markdown("### 📌 Navigatsiya")

# Boblar filtri
chapters = [
    "Barchasi",
    "I BOB. DAVLAT SUVERENITETI",
    "II BOB. XALQ HOKIMIYATCHILIGI",
    "III BOB. KONSTITUTSIYA VA QONUNNING USTUNLIGI",
    "IV BOB. TASHQI SIYOSAT"
]

selected_chapter = st.sidebar.selectbox("Konstitutsiya bobini tanlang:", chapters)

# Filterlangan moddalar ro'yxati
if selected_chapter == "Barchasi":
    filtered_articles = list(ARTICLES_DB.keys())
else:
    filtered_articles = [k for k, v in ARTICLES_DB.items() if v["chapter"] == selected_chapter]

selected_art_num = st.sidebar.selectbox(
    "Tahlil qilinadigan moddani tanlang:",
    filtered_articles,
    format_func=lambda x: f"{x}-modda"
)

st.sidebar.markdown("---")
st.sidebar.success("""
**Platfoma xususiyatlari:**
- Rasmiy va aniq modda matnlari
- Bevosita tayanch O‘RQ va qonunlar
- Chuqur doktrinal tahlil
- Xalqaro huquqiy nazariyalar va olimlar
""")

# Tanlangan modda ma'lumotlari
art_data = ARTICLES_DB[selected_art_num]

# Bob nomi va Modda Sarlavhasi
st.markdown(f'<div class="chapter-badge">{art_data["chapter"]}</div>', unsafe_allow_html=True)
st.subheader(f"📜 {art_data['title']}")

# Rasmiy Modda Matni
st.markdown(f"""
<div class="article-box">
    <b>Rasmiy Konstitutsiyaviy Norma Matni:</b><br><br>
    <i>{art_data['text'].replace(chr(10), '<br>')}</i>
</div>
""", unsafe_allow_html=True)

# Tahlil Vkladkalari (Tabs)
tab1, tab2, tab3 = st.tabs([
    "⚖️ Tayanch Qonunlar (O‘RQ)", 
    "🔬 PhD Doktrinal Tahlil", 
    "🎓 Nazariyalar va Olimlar"
])

with tab1:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown("#### Ushbu modda uchun normativ-huquqiy poydevor bo'lgan hujjatlar:")
    for b in art_data["basis"]:
        st.markdown(f"- 📄 **{b}**")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown("#### Konseptual Akademik Tahlil (PhD level):")
    st.write(art_data["analysis"])
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("#### Xalqaro Huquqshunoslar va Nazariy Ildizlar:")
    for scholar in art_data["scholars"]:
        name = scholar["name"]
        theory = scholar["theory"]
        desc = scholar["desc"]
        
        card_html = (
            f'<div class="card-box">'
            f'<div class="scholar-title">👨‍🏫 {name}</div>'
            f'<p style="margin-bottom: 5px;"><b>Asosiy Nazariya:</b> <i>{theory}</i></p>'
            f'<p style="color: #334155;"><b>Modda bilan bog‘liqligi:</b> {desc}</p>'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)
