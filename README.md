Auer Máté (VJ7SKP)
A projektem egy konditerem bérlet nyilvántartó alkamazás amit a konditerem recepciósa kezel, ezért egy login felülettel nyílik meg az alkalmazás. A felhasználónév: admin, jelszó: admin.

Az alábbi Python modulokat használtam:

tkinter: Ez a Python beépített GUI könyvtára, amely lehetővé teszi grafikus felhasználói felületek létrehozását. Az alábbi elemeket használtad a tkinter könyvtárból:
Tk, Label, Entry, Button, OptionMenu, Menu és Frame: Ezek az elemek a felhasználói felület különböző részeit hozzák létre, például szövegmezőket, gombokat és menüket.
messagebox: Párbeszédablakok megjelenítésére használtad, például hibajelzésekhez vagy sikerüzenetekhez.
filedialog: Ez a modul párbeszédablakokat biztosít fájlok kiválasztásához mentéshez és betöltéshez.
ttk.Treeview: Táblázatos megjelenítésre használtad, ahol a felhasználói adatokat jeleníted meg.
datetime: A datetime modul az időpontokkal és dátumokkal kapcsolatos műveletek végrehajtására szolgál.

datetime: Ez az osztály lehetővé teszi az aktuális dátum és idő lekérését, valamint dátumformátumok kezelését.
timedelta: Időbeli különbségek kiszámítására használtad, például a bérletek lejárati dátumának beállításakor.

AM_modul (Saját modul): Az AM_modul az általad létrehozott egyedi Python modul, amely az alkalmazásban használt adatkezelő osztályokat és függvényeket tartalmazza:

User_AM: Ez az osztály reprezentálja a felhasználókat, a bérletek típusát, kezdő- és lejárati dátumát. Ezen felül tartalmazza a is_membership_active és get_user_data metódusokat.
save_data és load_data: Ezek a funkciók biztosítják az adatok mentését és betöltését fájlba.
refresh_table: Ez a függvény frissíti a Treeview táblázatot a GUI-ban, amikor új adatot adnak hozzá.

Osztály:

User_AM

Ez az osztály egy felhasználót reprezentál, tartalmazza a felhasználó nevét, a bérlet típusát, a kezdési és lejárati dátumot. Az osztályban két fontos metódust definiáltál:
is_membership_active(): Ellenőrzi, hogy a felhasználó bérlete aktív-e a mai napon.
get_user_data(): Egy szótárban adja vissza a felhasználó adatait, beleértve a nevet, bérlet típusát, kezdési és lejárati dátumokat szöveges formában.
