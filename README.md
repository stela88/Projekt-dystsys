Projekt se sastoji o 5 mikroservisa. 
Prvi, pod nazivom M0.py uzima podatke iz file-a 'file-000000000040.json' koji su:
reponame, te filename koji su nam kasnije potrebni za spremanje u bazu.
Nakon spajanja s bazom podatke (username, ghlink, filename) spremamo u nju.
Spremljeno je 10000 podataka od kojih uzimamo do 100 i šaljemo na drugi servis.
Drugi servis, pod nazivom M1.py, prima podatke te ih prosljeđuje na treći i četvrti mikroservis.
Treći servis, WT.py, nakon šro je zaprimio podatke sa drugog servisa, provjerava ih i iz njih izvlači samo one koji su potrebni.
podaci koji su potrebni su samo oni čiji username počinje slovom w ili W. Nakon što je uzeo podatke, sprema ih u listu te šalje petom sevisu.
Četvrti servis, radi sve isto kao i treći osim što on u listu sprema username sa početnim slovom d ili D, te također šalje 5. servisu.
Peti servis, M3.py nakon što je zaprimio podatke sa 3. i 4. servisa, spaja ih i sprema u listu.
Zatim provjerava nalazi li se u listi više od 10 elemenata, ako da, asinkrono svaki pojedini elemen sprema u novi file.

Pokretanje:
Potrebno je pokrenuti sve mikroservise.
Pokreće ih se u terminalu, naredbom python (ime file-a).py
Nakon što su svi pokrenuti u Postmanu se šalje get zahtjev prvoga servisa, njegovog porta i same rute koja je tamo definirana.
