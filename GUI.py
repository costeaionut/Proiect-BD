from tkinter import *
import cx_Oracle as db

root = Tk()
root.title("Click For Food!")
root.geometry("500x500")

def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    list = root.place_slaves()
    for l in list:
        l.destroy()

def sterg_produs():
	conn = db.connect('Admin/pass@localhost:1521/DBPR')
	cursor = conn.cursor()
	cursor.execute('delete from produs where lower(nume) = ' + "lower('" + option_stergere.get() +"')" + "and magazin_id = (select magazin_id from magazin where email = " + "'" + current_sesion_shop + "'"  + ')')
	cursor.close()
	conn.commit()
	conn.close()
	shop_interface()

def sterg_produs_interfata():
	global option_stergere
	clear()
	root.geometry("300x250")

	selectare_produs = Label(root, text = "Introduceti produsul care sa fie sters")
	selectare_produs.grid(row = 0, column = 0, padx = 50)

	option_stergere = Entry(root, width = 25)
	option_stergere.grid(row = 1, column = 0)

	button_stergere = Button(root, text = "Stergere", command = sterg_produs)
	button_stergere.grid(row = 2, column = 0)

def sterg_meniu():
	conn = db.connect('Admin/pass@localhost:1521/DBPR')
	cursor = conn.cursor()
	cursor.execute('delete from meniu where lower(nume) = ' + "lower('" + option_stergere_meniu.get() +"')")
	cursor.close()
	conn.commit()
	conn.close()
	shop_interface()

def sterg_meniu_interfata():
	global option_stergere_meniu
	clear()
	root.geometry("300x250")

	selectare_produs = Label(root, text = "Introduceti meniul care sa fie sters")
	selectare_produs.grid(row = 0, column = 0, padx = 50)

	option_stergere_meniu = Entry(root, width = 25)
	option_stergere_meniu.grid(row = 1, column = 0)

	button_stergere = Button(root, text = "Stergere", command = sterg_meniu)
	button_stergere.grid(row = 2, column = 0)

def edit_produs():
	a = "'"
	conn = db.connect('Admin/pass@localhost:1521/DBPR')
	cursor = conn.cursor()
	cursor.execute('UPDATE Produs SET Nume =' + a + produs_name_edit.get() + a + ', Categorie = ' + a + tip_option_edit.get() + a + ', Pret = ' + produs_pret_edit.get() + ', Gramaj = ' +  produs_gramaj_edit.get() + ' WHERE Nume = ' + a + edit + a + 'and magazin_id = (select magazin_id from magazin where email = ' + a + current_sesion_shop + a + ')')
	cursor.close()
	conn.commit()
	conn.close()

def edit_produs_interfata_2():
    global edit
    edit = option_editare_produs.get()
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, categorie, pret, gramaj from produs where lower(nume) = ' + "lower('" + edit + "')")
    valori = cursor.fetchall()
    cursor.close()
    conn.close()
    global produs_name_edit, produs_pret_edit, tip_option_edit, produs_gramaj_edit

    produs_name_label = Label(root, text = "Nume produs")
    produs_name_label.grid(row = 0, column = 0)
    produs_name_edit = Entry(root, width = 25)
    produs_name_edit.grid(row = 0, column = 1)
    produs_name_edit.insert(END, valori[0][0])


    produs_pret_label = Label(root, text = "Pret produs")
    produs_pret_label.grid(row = 1, column = 0)
    produs_pret_edit = Entry(root, width = 25)
    produs_pret_edit.grid(row = 1, column = 1)
    produs_pret_edit.insert(END, valori[0][2])

    choices = {'-', 'Vegetarian', 'Vegan'}
    tip_option_edit = StringVar()
    tip_option_edit.set(valori[0][1])
    produs_tip_label = Label(root, text = "Categorie")
    tip_dropD = OptionMenu(root, tip_option_edit, *choices)
    produs_tip_label.grid(row = 4, column = 0)
    tip_dropD.grid(row = 4, column = 1, sticky = W)

    produs_gramaj_label = Label(root, text = "Gramaj")
    produs_gramaj_edit = Entry(root, width = 25)
    produs_gramaj_label.grid(row = 3, column = 0)
    produs_gramaj_edit.grid(row = 3, column = 1)
    produs_gramaj_edit.insert(END, valori[0][3])

    back_button = Button(root, text = "Inapoi", command = shop_interface)
    back_button.place(relx = 0.20, rely = 0.45)

    submit_button = Button(root, text = "Adauga produs", command = edit_produs)
    submit_button.place(relx = 0.38, rely = 0.45)

def edit_produs_interfata_1():
	global option_editare_produs
	clear()
	root.geometry("400x250")

	selectare_produs = Label(root, text = "Introduceti produsul care sa fie editat")
	selectare_produs.grid(row = 0, column = 0, padx = 50)

	option_editare_produs = Entry(root, width = 25)
	option_editare_produs.grid(row = 1, column = 0)

	button_editare = Button(root, text = "Editeaza", command = edit_produs_interfata_2)
	button_editare.grid(row = 2, column = 0)

def afis_magazine_nume():
    root.geometry("700x700")
    clear()
    root.geometry("700x350")
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select m.nume, m.adresa, m.telefon, m.email, v.nume, v.prenume from magazin m, vanzator v where m.VANZATOR_ID = v.VANZATOR_ID order by m.nume')
    magazine = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_magazin_label = Label(root, text = "Nume magazin")
    nume_magazin_label.grid(row = 0, column = 0, sticky = W)

    adresa_magazin_label = Label(root, text = "Adresa magazin")
    adresa_magazin_label.grid(row = 0, column = 1, sticky = W)

    telefon_magazin_label = Label(root, text = "Telefon magazin")
    telefon_magazin_label.grid(row = 0, column = 2, sticky = W)

    email_magazin_label = Label(root, text = "Email magazin")
    email_magazin_label.grid(row = 0, column = 3, sticky = W)

    nume_vanzator_label = Label(root, text = "Nume vanzator")
    nume_vanzator_label.grid(row = 0, column = 4, sticky = W)

    prenume_vanzator_label = Label(root, text = "Prenume vanzator")
    prenume_vanzator_label.grid(row = 0, column = 5, sticky = W)

    i = 1

    for m in magazine:
	    nume_magazin = Label(root, text = m[0])
	    nume_magazin.grid(row = i, column = 0, sticky = W)

	    adresa_magazin = Label(root, text = m[1])
	    adresa_magazin.grid(row = i, column = 1, sticky = W)

	    telefon_magazin = Label(root, text = m[2])
	    telefon_magazin.grid(row = i, column = 2, sticky = W)

	    email_magazin = Label(root, text = m[3])
	    email_magazin.grid(row = i, column = 3, sticky = W)

	    nume_vanzator = Label(root, text = m[4])
	    nume_vanzator.grid(row = i, column = 4, sticky = W)

	    prenume_vanzator = Label(root, text = m[5])
	    prenume_vanzator.grid(row = i, column = 5, sticky = W)
	    i = i + 1

    ordonare_nume = Button(root, text = "Ordonare dupa nume", command = afis_magazine_nume)
    ordonare_nume.grid(row = i + 2, column = 0, columnspan = 2, sticky = W)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 3, sticky = W)

def afis_magazine():
    root.geometry("700x700")
    clear()
    root.geometry("700x350")
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select m.nume, m.adresa, m.telefon, m.email, v.nume, v.prenume from magazin m, vanzator v where m.VANZATOR_ID = v.VANZATOR_ID')
    magazine = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_magazin_label = Label(root, text = "Nume magazin")
    nume_magazin_label.grid(row = 0, column = 0, sticky = W)

    adresa_magazin_label = Label(root, text = "Adresa magazin")
    adresa_magazin_label.grid(row = 0, column = 1, sticky = W)

    telefon_magazin_label = Label(root, text = "Telefon magazin")
    telefon_magazin_label.grid(row = 0, column = 2, sticky = W)

    email_magazin_label = Label(root, text = "Email magazin")
    email_magazin_label.grid(row = 0, column = 3, sticky = W)

    nume_vanzator_label = Label(root, text = "Nume vanzator")
    nume_vanzator_label.grid(row = 0, column = 4, sticky = W)

    prenume_vanzator_label = Label(root, text = "Prenume vanzator")
    prenume_vanzator_label.grid(row = 0, column = 5, sticky = W)

    i = 1

    for m in magazine:
	    nume_magazin = Label(root, text = m[0])
	    nume_magazin.grid(row = i, column = 0, sticky = W)

	    adresa_magazin = Label(root, text = m[1])
	    adresa_magazin.grid(row = i, column = 1, sticky = W)

	    telefon_magazin = Label(root, text = m[2])
	    telefon_magazin.grid(row = i, column = 2, sticky = W)

	    email_magazin = Label(root, text = m[3])
	    email_magazin.grid(row = i, column = 3, sticky = W)

	    nume_vanzator = Label(root, text = m[4])
	    nume_vanzator.grid(row = i, column = 4, sticky = W)

	    prenume_vanzator = Label(root, text = m[5])
	    prenume_vanzator.grid(row = i, column = 5, sticky = W)
	    i = i + 1

    ordonare_nume = Button(root, text = "Ordonare dupa nume", command = afis_magazine_nume)
    ordonare_nume.grid(row = i + 2, column = 0, columnspan = 2, sticky = W)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 3, sticky = W)

def sterg_client():
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('delete from client where mail =' + a + sterge_entry.get() + a)
    conn.commit()
    cursor.close()
    conn.close()
    afis_clienti()

def edit_client():
	a = "'"
	root.geometry("700x350")
	conn = db.connect('Admin/pass@localhost:1521/DBPR')
	cursor = conn.cursor()
	cursor.execute('UPDATE Client SET Nume = ' + a + client_nume_edit.get() + a + ',Prenume = ' + a + client_prenume_edit.get() + a + ', Adresa = ' + a + client_adresa_edit.get() + a + ', Telefon = ' + a + client_telefon_edit.get() + a + ', Mail = ' + a + client_mail_edit.get() + a + ' WHERE mail = ' + a + local + a)
	conn.commit()
	cursor.close()
	conn.close()
	admin_interface()

def edit_client_interface():
	global local, client_nume_edit, client_prenume_edit, client_adresa_edit, client_telefon_edit, client_mail_edit
	a = "'"
	root.geometry("700x350")
	conn = db.connect('Admin/pass@localhost:1521/DBPR')
	cursor = conn.cursor()
	cursor.execute('select nume, prenume, adresa, telefon, mail from client where mail = ' + a + sterge_entry.get() + a)
	valori = cursor.fetchall()
	cursor.close()
	conn.close()
    
	local = sterge_entry.get()

	clear()

	nume_label = Label(root, text = "Nume")
	nume_label.grid(row = 0, column = 0)
	client_nume_edit = Entry(root, width = 25)
	client_nume_edit.grid(row = 0, column = 1)
	client_nume_edit.insert(END, valori[0][0])

	prenume_label = Label(root, text = "Prenume")
	prenume_label.grid(row = 1, column = 0)
	client_prenume_edit = Entry(root, width = 25)
	client_prenume_edit.grid(row = 1, column = 1)
	client_prenume_edit.insert(END, valori[0][1])

	adresa_label = Label(root, text = "Adresa")
	adresa_label.grid(row = 2, column = 0)
	client_adresa_edit = Entry(root, width = 25)
	client_adresa_edit.grid(row = 2, column = 1)
	client_adresa_edit.insert(END, valori[0][2])

	telefon_label = Label(root, text = "Telefon")
	telefon_label.grid(row = 3, column = 0)
	client_telefon_edit = Entry(root, width = 25)
	client_telefon_edit.grid(row = 3, column = 1)
	client_telefon_edit.insert(END, valori[0][3])

	mail_label = Label(root, text = "Mail")
	mail_label.grid(row = 4, column = 0)
	client_mail_edit = Entry(root, width = 25)
	client_mail_edit.grid(row = 4, column = 1)
	client_mail_edit.insert(END, valori[0][4])

	edit_button = Button(root, text = "Editeaza", command = edit_client)
	edit_button.grid(row = 5, column = 1, sticky = W)

def afis_clienti_nume():
    global sterge_entry
    root.geometry("700x350")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, adresa, telefon, mail from client order by nume')
    clienti = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_label = Label(root, text = "Nume")
    nume_label.grid(row = 0, column = 0, sticky = W)

    prenume_label = Label(root, text = "Prenume")
    prenume_label.grid(row = 0, column = 1, sticky = W)

    adresa_label = Label(root, text = "Adresa")
    adresa_label.grid(row = 0, column = 2, sticky = W)

    telefon = Label(root, text = "Telefon")
    telefon.grid(row = 0, column = 3, sticky = W)

    mail = Label(root, text = "Email")
    mail.grid(row = 0, column = 4, sticky = W)

    i = 1

    for c in clienti:
    	nume_client = Label(root, text = c[0])
    	nume_client.grid(row = i, column = 0, sticky = W)

    	prenume_client = Label(root, text = c[1])
    	prenume_client.grid(row = i, column = 1, sticky = W)

    	adresa_client = Label(root, text = c[2])
    	adresa_client.grid(row = i, column = 2, sticky = W)

    	telefon_client = Label(root, text = c[3])
    	telefon_client.grid(row = i, column = 3, sticky = W)

    	mail_client = Label(root, text = c[4])
    	mail_client.grid(row = i, column = 4, sticky = W)
    	i = i + 1


    sterge_client = Label(root, text = "Mail")
    sterge_client.grid(row = i + 4, column = 0)

    sterge_entry = Entry(root, width = 25)
    sterge_entry.grid(row = i + 4, column = 1)

    sterge_button = Button(root, text = "Sterge", command = sterg_client)
    sterge_button.grid(row = i + 5, column = 0)

    editeaza_button = Button(root, text = "Editeaza", command = edit_client_interface)
    editeaza_button.grid(row = i + 5, column = 1)

    order_by_nume = Button(root, text = "Ordonare dupa nume", command = afis_clienti_nume)
    order_by_nume.grid(row = i + 2, column = 0, columnspan = 2)

    order_by_prenume = Button(root, text = "Ordonare dupa prenume", command = afis_clienti_prenume)
    order_by_prenume.grid(row = i + 3, column = 0, columnspan = 2)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 2)

def afis_clienti_prenume():
    global sterge_entry
    root.geometry("700x350")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, adresa, telefon, mail from client order by prenume')
    clienti = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_label = Label(root, text = "Nume")
    nume_label.grid(row = 0, column = 0, sticky = W)

    prenume_label = Label(root, text = "Prenume")
    prenume_label.grid(row = 0, column = 1, sticky = W)

    adresa_label = Label(root, text = "Adresa")
    adresa_label.grid(row = 0, column = 2, sticky = W)

    telefon = Label(root, text = "Telefon")
    telefon.grid(row = 0, column = 3, sticky = W)

    mail = Label(root, text = "Email")
    mail.grid(row = 0, column = 4, sticky = W)

    i = 1

    for c in clienti:
    	nume_client = Label(root, text = c[0])
    	nume_client.grid(row = i, column = 0, sticky = W)

    	prenume_client = Label(root, text = c[1])
    	prenume_client.grid(row = i, column = 1, sticky = W)

    	adresa_client = Label(root, text = c[2])
    	adresa_client.grid(row = i, column = 2, sticky = W)

    	telefon_client = Label(root, text = c[3])
    	telefon_client.grid(row = i, column = 3, sticky = W)

    	mail_client = Label(root, text = c[4])
    	mail_client.grid(row = i, column = 4, sticky = W)
    	i = i + 1


    sterge_client = Label(root, text = "Mail")
    sterge_client.grid(row = i + 4, column = 0)

    sterge_entry = Entry(root, width = 25)
    sterge_entry.grid(row = i + 4, column = 1)

    sterge_button = Button(root, text = "Sterge", command = sterg_client)
    sterge_button.grid(row = i + 5, column = 0)

    editeaza_button = Button(root, text = "Editeaza", command = edit_client_interface)
    editeaza_button.grid(row = i + 5, column = 1)


    order_by_nume = Button(root, text = "Ordonare dupa nume", command = afis_clienti_nume)
    order_by_nume.grid(row = i + 2, column = 0, columnspan = 2)

    order_by_prenume = Button(root, text = "Ordonare dupa prenume", command = afis_clienti_prenume)
    order_by_prenume.grid(row = i + 3, column = 0, columnspan = 2)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 2)

def afis_clienti():
    global sterge_entry
    root.geometry("700x350")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, adresa, telefon, mail from client')
    clienti = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_label = Label(root, text = "Nume")
    nume_label.grid(row = 0, column = 0, sticky = W)

    prenume_label = Label(root, text = "Prenume")
    prenume_label.grid(row = 0, column = 1, sticky = W)

    adresa_label = Label(root, text = "Adresa")
    adresa_label.grid(row = 0, column = 2, sticky = W)

    telefon = Label(root, text = "Telefon")
    telefon.grid(row = 0, column = 3, sticky = W)

    mail = Label(root, text = "Email")
    mail.grid(row = 0, column = 4, sticky = W)

    i = 1

    for c in clienti:
    	nume_client = Label(root, text = c[0])
    	nume_client.grid(row = i, column = 0, sticky = W)

    	prenume_client = Label(root, text = c[1])
    	prenume_client.grid(row = i, column = 1, sticky = W)

    	adresa_client = Label(root, text = c[2])
    	adresa_client.grid(row = i, column = 2, sticky = W)

    	telefon_client = Label(root, text = c[3])
    	telefon_client.grid(row = i, column = 3, sticky = W)

    	mail_client = Label(root, text = c[4])
    	mail_client.grid(row = i, column = 4, sticky = W)
    	i = i + 1


    sterge_client = Label(root, text = "Mail")
    sterge_client.grid(row = i + 4, column = 0)

    sterge_entry = Entry(root, width = 25)
    sterge_entry.grid(row = i + 4, column = 1)

    sterge_button = Button(root, text = "Sterge", command = sterg_client)
    sterge_button.grid(row = i + 5, column = 0)

    editeaza_button = Button(root, text = "Editeaza", command = edit_client_interface)
    editeaza_button.grid(row = i + 5, column = 1)

    order_by_nume = Button(root, text = "Ordonare dupa nume", command = afis_clienti_nume)
    order_by_nume.grid(row = i + 2, column = 0, columnspan = 2)

    order_by_prenume = Button(root, text = "Ordonare dupa prenume", command = afis_clienti_prenume)
    order_by_prenume.grid(row = i + 3, column = 0, columnspan = 2)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 2)

def afis_vanzatori_varsta():
    root.geometry("500x500")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, telefon, varsta from vanzator order by varsta')
    vanzatori = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_vanzator_label = Label(root, text = "Nume")
    nume_vanzator_label.grid(row = 0, column = 0)

    prenume_vanzator_label = Label(root, text = "Prenume")
    prenume_vanzator_label.grid(row = 0, column = 1)

    telefon_vanzator_label = Label(root, text = "Telefon")
    telefon_vanzator_label.grid(row = 0, column = 2)

    varsta_vanzator_label = Label(root, text = "Varsta")
    varsta_vanzator_label.grid(row = 0, column = 3)

    i = 1

    for v in vanzatori:
        nume_vanzator = Label(root, text = v[0])
        nume_vanzator.grid(row = i, column = 0)

        prenume_vanzator = Label(root, text = v[1])
        prenume_vanzator.grid(row = i, column = 1)

        telefon_vanzator = Label(root, text = v[2])
        telefon_vanzator.grid(row = i, column = 2)

        varsta_vanzator = Label(root, text = v[3])
        varsta_vanzator.grid(row = i, column = 3)

        i = i + 1


    ordonare_varsta = Button(root, text = "Ordonare dupa varsta", command = afis_vanzatori_varsta)
    ordonare_varsta.grid(row = i + 2, column = 0, sticky = W, rowspan = 2, columnspan = 2)
    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 2, sticky = W)

def afis_vanzatori():
    root.geometry("500x500")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, telefon, varsta from vanzator')
    vanzatori = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_vanzator_label = Label(root, text = "Nume")
    nume_vanzator_label.grid(row = 0, column = 0)

    prenume_vanzator_label = Label(root, text = "Prenume")
    prenume_vanzator_label.grid(row = 0, column = 1)

    telefon_vanzator_label = Label(root, text = "Telefon")
    telefon_vanzator_label.grid(row = 0, column = 2)

    varsta_vanzator_label = Label(root, text = "Varsta")
    varsta_vanzator_label.grid(row = 0, column = 3)

    i = 1

    for v in vanzatori:
        nume_vanzator = Label(root, text = v[0])
        nume_vanzator.grid(row = i, column = 0)

        prenume_vanzator = Label(root, text = v[1])
        prenume_vanzator.grid(row = i, column = 1)

        telefon_vanzator = Label(root, text = v[2])
        telefon_vanzator.grid(row = i, column = 2)

        varsta_vanzator = Label(root, text = v[3])
        varsta_vanzator.grid(row = i, column = 3)

        i = i + 1


    ordonare_varsta = Button(root, text = "Ordonare dupa varsta", command = afis_vanzatori_varsta)
    ordonare_varsta.grid(row = i + 2, column = 0, sticky = W)
    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 2, sticky = W, rowspan = 2, columnspan = 2)

def sterg_pl():
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('delete from persoana_livrari where email = ' + a + sterge_pl.get() + a)
    conn.commit()
    cursor.close()
    conn.close()
    afis_pers_livr()

def afis_pers_livr_pret():
    global sterge_pl
    root.geometry("900x600")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, varsta, telefon, email, pret_livrare from persoana_livrari order by pret_livrare')
    pl = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_pl_label = Label(root, text ="Nume")
    nume_pl_label.grid(row = 0, column = 0)

    prenume_pl_label = Label(root, text ="Preume")
    prenume_pl_label.grid(row = 0, column = 1)

    varsta_pl_label = Label(root, text ="Varsta")
    varsta_pl_label.grid(row = 0, column = 2)

    telefon_pl_label = Label(root, text ="Telefon")
    telefon_pl_label.grid(row = 0, column = 3)

    email_pl_label = Label(root, text ="Email")
    email_pl_label.grid(row = 0, column = 4)

    pl_pl_label = Label(root, text ="Pret livrare")
    pl_pl_label.grid(row = 0, column = 5)

    i = 1

    for p in pl:
        nume_pl = Label(root, text =p[0])
        nume_pl.grid(row = i, column = 0)

        prenume_pl = Label(root, text =p[1])
        prenume_pl.grid(row = i, column = 1)

        varsta_pl = Label(root, text =p[2])
        varsta_pl.grid(row = i, column = 2)

        telefon_pl = Label(root, text =p[3])
        telefon_pl.grid(row = i, column = 3)

        email_pl = Label(root, text =p[4])
        email_pl.grid(row = i, column = 4)

        pl_pl = Label(root, text =p[5])
        pl_pl.grid(row = i, column = 5)

        i = i + 1

    ordonare_pret = Button(root, text = "Ordonare dupa pret", command = afis_pers_livr_pret)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2)

    sterge_label = Label(root, text = "Email")
    sterge_label.grid(row = i + 3, column = 0, columnspan = 2, sticky = W)

    sterge_pl = Entry(root, width = 25)
    sterge_pl.grid(row = i + 3, column = 1, columnspan = 2, sticky = W)

    sterge_button = Button(root, text = "Sterge", command = sterg_pl)
    sterge_button.grid(row = i + 4, column = 0, columnspan = 2, sticky = W)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 4, sticky = W)

def afis_pers_livr():

    global sterge_pl
    root.geometry("900x600")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, varsta, telefon, email, pret_livrare from persoana_livrari')
    pl = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_pl_label = Label(root, text ="Nume")
    nume_pl_label.grid(row = 0, column = 0)

    prenume_pl_label = Label(root, text ="Preume")
    prenume_pl_label.grid(row = 0, column = 1)

    varsta_pl_label = Label(root, text ="Varsta")
    varsta_pl_label.grid(row = 0, column = 2)

    telefon_pl_label = Label(root, text ="Telefon")
    telefon_pl_label.grid(row = 0, column = 3)

    email_pl_label = Label(root, text ="Email")
    email_pl_label.grid(row = 0, column = 4)

    pl_pl_label = Label(root, text ="Pret livrare")
    pl_pl_label.grid(row = 0, column = 5)

    i = 1

    for p in pl:
        nume_pl = Label(root, text =p[0])
        nume_pl.grid(row = i, column = 0)

        prenume_pl = Label(root, text =p[1])
        prenume_pl.grid(row = i, column = 1)

        varsta_pl = Label(root, text =p[2])
        varsta_pl.grid(row = i, column = 2)

        telefon_pl = Label(root, text =p[3])
        telefon_pl.grid(row = i, column = 3)

        email_pl = Label(root, text =p[4])
        email_pl.grid(row = i, column = 4)

        pl_pl = Label(root, text =p[5])
        pl_pl.grid(row = i, column = 5)

        i = i + 1

    ordonare_pret = Button(root, text = "Ordonare dupa pret", command = afis_pers_livr_pret)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2)

    sterge_label = Label(root, text = "Email")
    sterge_label.grid(row = i + 3, column = 0, columnspan = 2, sticky = W)

    sterge_pl = Entry(root, width = 25)
    sterge_pl.grid(row = i + 3, column = 1, columnspan = 2, sticky = W)

    sterge_button = Button(root, text = "Sterge", command = sterg_pl)
    sterge_button.grid(row = i + 4, column = 0, columnspan = 2, sticky = W)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 4, sticky = W)

def afis_comenzi_nume():
    root.geometry("500x500")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select cl.nume, m.nume, co.nume_meniu, pl.nume, co.cost from client cl, comanda co, magazin m, persoana_livrari pl where cl.client_id = co.client_id and co.magazin_id = m.magazin_id and pl.pl_id = co.pl_id')
    comenzi = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_client_lable = Label(root, text = "Nume client")
    nume_client_lable.grid(row = 0, column = 0)

    nume_magazin_lable = Label(root, text = "Nume magazin")
    nume_magazin_lable.grid(row = 0, column = 1)
    
    nume_meniu_lable = Label(root, text = "Nume meniu")
    nume_meniu_lable.grid(row = 0, column = 2)

    nume_pl_lable = Label(root, text = "Nume persoana livrari")
    nume_pl_lable.grid(row = 0, column = 3)

    cost_lable = Label(root, text = "Cost meniu")
    cost_lable.grid(row = 0, column = 4)

    i = 1
    for co in comenzi:
    	nume_client_lable = Label(root, text = co[0])
    	nume_client_lable.grid(row = i, column = 0)

    	nume_magazin_lable = Label(root, text = co[1])
    	nume_magazin_lable.grid(row = i, column = 1)
    
    	nume_meniu_lable = Label(root, text = co[2])
    	nume_meniu_lable.grid(row = i, column = 2)

    	nume_pl_lable = Label(root, text = co[3])
    	nume_pl_lable.grid(row = i, column = 3)

    	cost_lable = Label(root, text = co[4])
    	cost_lable.grid(row = i, column = 4)

    	i = i + 1

    sortare_magazin = Button(root, text = "Sortare dupa magazin", command = afis_comenzi_nume)
    sortare_magazin.grid(row = i + 2, column = 0, columnspan = 2)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 1)

def afis_comenzi():
    root.geometry("500x500")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select cl.nume, m.nume, co.nume_meniu, pl.nume, co.cost from client cl, comanda co, magazin m, persoana_livrari pl where cl.client_id = co.client_id and co.magazin_id = m.magazin_id and pl.pl_id = co.pl_id')
    comenzi = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_client_lable = Label(root, text = "Nume client")
    nume_client_lable.grid(row = 0, column = 0)

    nume_magazin_lable = Label(root, text = "Nume magazin")
    nume_magazin_lable.grid(row = 0, column = 1)
    
    nume_meniu_lable = Label(root, text = "Nume meniu")
    nume_meniu_lable.grid(row = 0, column = 2)

    nume_pl_lable = Label(root, text = "Nume persoana livrari")
    nume_pl_lable.grid(row = 0, column = 3)

    cost_lable = Label(root, text = "Cost meniu")
    cost_lable.grid(row = 0, column = 4)

    i = 1
    for co in comenzi:
    	nume_client_lable = Label(root, text = co[0])
    	nume_client_lable.grid(row = i, column = 0)

    	nume_magazin_lable = Label(root, text = co[1])
    	nume_magazin_lable.grid(row = i, column = 1)
    
    	nume_meniu_lable = Label(root, text = co[2])
    	nume_meniu_lable.grid(row = i, column = 2)

    	nume_pl_lable = Label(root, text = co[3])
    	nume_pl_lable.grid(row = i, column = 3)

    	cost_lable = Label(root, text = co[4])
    	cost_lable.grid(row = i, column = 4)

    	i = i + 1

    sortare_magazin = Button(root, text = "Sortare dupa magazin", command = afis_comenzi_nume)
    sortare_magazin.grid(row = i + 2, column = 0, columnspan = 2)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 1)

def rezolv_d():
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select m.nume, sum(p.pret), max(m.pret) from meniu m join produs_meniu pm on(pm.meniu_id = m.meniu_id) join produs p on(p.produs_id = pm.produs_id) group by m.nume having (sum(p.pret) - max(m.pret)) > 5')
    meniuri = cursor.fetchall()
    cursor.close()
    conn.close()

    cerinta_label = Label(root, text = "Afiseaza toate meniurile la care este o diferenta mai mare de 5 lei intre achizitionare produselor individual sau la meniu: ")
    cerinta_label.grid(row = 0, column = 0, columnspan = 2)

    nume_label = Label(root, text = "Nume meniu")
    nume_label.grid(row = 1, column = 0)

    pretP_label = Label(root, text = "Pret suma produse")
    pretP_label.grid(row = 1, column = 1)

    pretM_label = Label(root, text = "Pret meniu")
    pretM_label.grid(row = 1, column = 2)

    i = 2

    for m in meniuri:
    	nume_meniu = Label(root, text = m[0])
    	nume_meniu.grid(row = i, column = 0)

    	pretP = Label(root, text = m[1])
    	pretP.grid(row = i, column = 1)

    	pretM = Label(root, text = m[2])
    	pretM.grid(row = i, column = 2)
    	i = i + 1

    button_back = Button(root, text = "Back", command = admin_interface)
    button_back.grid(row = i + 1, column = 1)

def rezolv_c():
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select co.nume_meniu, cl.nume, pl.nume, co.cost from comanda co join client cl on(co.client_id = cl.client_id) join persoana_livrari pl on(co.pl_id = pl.pl_id) where co.cost > 20 and pl.pret_livrare < 5')
    comenzi = cursor.fetchall()
    cursor.close()
    conn.close()

    cerinta_label = Label(root, text = "Sa se afiseze toate numele meniului, numele clientului, numele livratorului si costul meniului pentru comenzile mai mari de 20 de lei cu pretul transportului mai mic de 5 lei ")
    cerinta_label.grid(row = 0, column = 0, columnspan = 2)

    nume_label = Label(root, text = "Nume meniu")
    nume_label.grid(row = 1, column = 0)

    numeC_label = Label(root, text = "Nume client")
    numeC_label.grid(row = 1, column = 1)

    numePL_label = Label(root, text = "Nume livrator")
    numePL_label.grid(row = 1, column = 2)

    costM = Label(root, text = "Cost meniu")
    costM.grid(row = 1, column = 3)

    i = 2

    for c in comenzi:
    	nume_meniu = Label(root, text = c[0])
    	nume_meniu.grid(row = i, column = 0)

    	nume = Label(root, text = c[1])
    	nume.grid(row = i, column = 1)

    	numeP = Label(root, text = c[2])
    	numeP.grid(row = i, column = 2)

    	cost = Label(root, text = c[3])
    	cost.grid(row = i, column = 3)

    	i = i + 1

    button_back = Button(root, text = "Back", command = admin_interface)
    button_back.grid(row = i + 1, column = 1)

def afis_prod_pret():
    root.geometry("900x600")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, categorie, pret, gramaj, magazin_id from produs order by pret')
    pr = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_pl_label = Label(root, text ="Nume")
    nume_pl_label.grid(row = 0, column = 0)

    categorie_pl_label = Label(root, text ="Categorie")
    categorie_pl_label.grid(row = 0, column = 1)

    pret_pl_label = Label(root, text ="Pret")
    pret_pl_label.grid(row = 0, column = 2)

    gramaj_pl_label = Label(root, text ="Gramaj")
    gramaj_pl_label.grid(row = 0, column = 3)

    id_magazin_pl_label = Label(root, text ="magazin_id")
    id_magazin_pl_label.grid(row = 0, column = 4)

    i = 1

    for p in pr:
        nume_pl = Label(root, text =p[0])
        nume_pl.grid(row = i, column = 0)

        prenume_pl = Label(root, text =p[1])
        prenume_pl.grid(row = i, column = 1)

        varsta_pl = Label(root, text =p[2])
        varsta_pl.grid(row = i, column = 2)

        telefon_pl = Label(root, text =p[3])
        telefon_pl.grid(row = i, column = 3)

        email_pl = Label(root, text =p[4])
        email_pl.grid(row = i, column = 4)

        i = i + 1

    ordonare_pret = Button(root, text = "Ordonare dupa pret", command = afis_prod_pret)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 4, sticky = W)

def afis_prod():
    root.geometry("900x600")
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, categorie, pret, gramaj, magazin_id from produs')
    pr = cursor.fetchall()
    cursor.close()
    conn.close()

    nume_pl_label = Label(root, text ="Nume")
    nume_pl_label.grid(row = 0, column = 0)

    categorie_pl_label = Label(root, text ="Categorie")
    categorie_pl_label.grid(row = 0, column = 1)

    pret_pl_label = Label(root, text ="Pret")
    pret_pl_label.grid(row = 0, column = 2)

    gramaj_pl_label = Label(root, text ="Gramaj")
    gramaj_pl_label.grid(row = 0, column = 3)

    id_magazin_pl_label = Label(root, text ="id_magazin")
    id_magazin_pl_label.grid(row = 0, column = 4)

    i = 1

    for p in pr:
        nume_pl = Label(root, text =p[0])
        nume_pl.grid(row = i, column = 0)

        prenume_pl = Label(root, text =p[1])
        prenume_pl.grid(row = i, column = 1)

        varsta_pl = Label(root, text =p[2])
        varsta_pl.grid(row = i, column = 2)

        telefon_pl = Label(root, text =p[3])
        telefon_pl.grid(row = i, column = 3)

        email_pl = Label(root, text =p[4])
        email_pl.grid(row = i, column = 4)

        i = i + 1

    ordonare_pret = Button(root, text = "Ordonare dupa pret", command = afis_prod_pret)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2)

    back_button = Button(root, text = "Back", command = admin_interface)
    back_button.grid(row = i + 1, column = 4, sticky = W)

def admin_interface():
    root.geometry("250x200")
    clear()
    
    afisare_clienti = Button(root, text = "Clienti", command = afis_clienti)
    afisare_clienti.grid(row = 0, column = 0)

    afisare_vanzatori = Button(root, text = "Vanzator", command = afis_vanzatori)
    afisare_vanzatori.grid(row = 0, column = 1)

    afisare_persoana_livrare = Button(root, text = "Persoane Livrari", command = afis_pers_livr)
    afisare_persoana_livrare.grid(row = 0, column = 2)

    afisare_magainze = Button(root, text = "Magazine", command = afis_magazine)
    afisare_magainze.grid(row = 1, column = 0)

    afisare_comenzi = Button(root, text = "Comenzi", command = afis_comenzi)
    afisare_comenzi.grid(row = 1, column = 2)

    rezolvare_d = Button(root, text = "rezolvare d)", command = rezolv_d)
    rezolvare_d.grid(row = 2, column = 0)

    rezolvare_c = Button(root, text = "rezolvare c)", command = rezolv_c)
    rezolvare_c.grid(row = 2, column = 1)

    afisare_produs = Button(root, text = "Produse", command = afis_prod)
    afisare_produs.grid(row = 3, column = 0)

    back_button = Button(root, text = "Back", command = MainPage)
    back_button.grid(row = 1, column = 1)

def show_produse_price():
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    select_syntax = 'select Nume, Pret, Categorie from Produs where MAGAZIN_ID = (select MAGAZIN_ID from Magazin where Email = '
    cursor.execute(select_syntax + "'" + current_sesion_shop + "'"  + ') order by pret')
    produs = cursor.fetchall()
    titles_1 = Label(root, text = "Nume")
    titles_1.grid(row = 0, column = 0)
    titles_2 = Label(root, text = "Pret")
    titles_2.grid(row = 0, column = 1)
    titles_3 = Label(root, text = "Tip")
    titles_3.grid(row = 0, column = 2)
    i = 1
    for p in produs:
        i = i + 1
        produs_list_1 = Label(root, text = p[0])
        produs_list_1.grid(row = i, column = 0, sticky = W)
        produs_list_2 = Label(root, text = p[1])
        produs_list_2.grid(row = i, column = 1)
        produs_list_3 = Label(root, text = p[2])
        produs_list_3.grid(row = i, column = 2)

    ordonare_pret = Button(root, text = "Ordonare dupa pret", command = show_produse_price)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2, sticky = W)

    back_button = Button(root, text = "Back", command = shop_interface)
    back_button.grid(row = i + 100, column = 1)

def show_produse():
    clear()
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    select_syntax = 'select Nume, Pret, Categorie from Produs where MAGAZIN_ID = (select MAGAZIN_ID from Magazin where Email = '
    cursor.execute(select_syntax + "'" + current_sesion_shop + "'"  + ') order by PRODUS_ID')
    produs = cursor.fetchall()
    titles_1 = Label(root, text = "Nume")
    titles_1.grid(row = 0, column = 0)
    titles_2 = Label(root, text = "Pret")
    titles_2.grid(row = 0, column = 1)
    titles_3 = Label(root, text = "Tip")
    titles_3.grid(row = 0, column = 2)
    i = 1
    for p in produs:
        i = i + 1
        produs_list_1 = Label(root, text = p[0])
        produs_list_1.grid(row = i, column = 0, sticky = W)
        produs_list_2 = Label(root, text = p[1])
        produs_list_2.grid(row = i, column = 1)
        produs_list_3 = Label(root, text = p[2])
        produs_list_3.grid(row = i, column = 2)

    ordonare_pret = Button(root, text = "Ordonare dupa pret", command = show_produse_price)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2, sticky = W)

    back_button = Button(root, text = "Back", command = shop_interface)
    back_button.grid(row = i + 100, column = 1)

def create_produs():
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()

    insert_syntax_1 = 'INSERT INTO Produs VALUES((SELECT max(PRODUS_ID) + 1 FROM Produs), '
    insert_syntax_2 = '(SELECT MAGAZIN_ID FROM Magazin WHERE Email = '
    a = "'"
    c = ','
    cursor.execute(insert_syntax_1 + a + produs_name_entry.get() + a + c + a + tip_option.get() + a + c + produs_pret_entry.get() + c + produs_gramaj_entry.get() + c + insert_syntax_2 + a + current_sesion_shop + a + '))')
    cursor.close()
    conn.commit()
    conn.close()
    shop_interface()

def show_meniu_price():
    clear()
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()

    cursor.execute("select m.nume, p.nume, m.pret from produs p, meniu m, produs_meniu mp where p.produs_id = mp.produs_id and m.meniu_id = mp.meniu_id and p.magazin_id = (select magazin_id from magazin where email = " + a + current_sesion_shop + a + ")" + "order by m.pret" )
    meniuri = cursor.fetchall()
    cursor.close()
    conn.close()

    meniu_meniu_label = Label(root, text = "Nume meniu:")
    meniu_meniu_label.grid(row = 0, column = 0, sticky = W)

    produs_meniu_label = Label(root, text = "Nume produse:")
    produs_meniu_label.grid(row = 0, column = 1, sticky = W)

    pret_meniu_label = Label(root, text = "Pret meniu:")
    pret_meniu_label.grid(row = 0, column = 2, sticky = W)
    i = 1
    for m in meniuri:
    	j = 1
    	if j == i: 
    		meniu_nume_label = Label(root, text = m[0])
    		meniu_nume_label.grid(row = i, column = 0, sticky = W)
    		pret_label = Label(root, text = m[2])
    		pret_label.grid(row = i, column = 2, sticky = W)
    	for p in meniuri:
    		produs_nume_label = Label(root, text = p[1])
    		produs_nume_label.grid(row = j, column = 1, sticky = W)
    		j = j + 1
    	i = i + 1

    ordonare_pret = Button(root, text = "Ordonare dupa nume", command = show_meniu_price)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2, sticky = W)
    
    back_button = Button(root, text = "Back", command = shop_interface)
    back_button.grid(row = i + 1, column = 1)

def show_meniu():
    clear()
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()

    cursor.execute("select m.nume, p.nume, m.pret from produs p, meniu m, produs_meniu mp where p.produs_id = mp.produs_id and m.meniu_id = mp.meniu_id and p.magazin_id = (select magazin_id from magazin where email = " + a + current_sesion_shop + a + ")" )
    meniuri = cursor.fetchall()
    cursor.close()
    conn.close()

    meniu_meniu_label = Label(root, text = "Nume meniu:")
    meniu_meniu_label.grid(row = 0, column = 0, sticky = W)

    produs_meniu_label = Label(root, text = "Nume produse:")
    produs_meniu_label.grid(row = 0, column = 1, sticky = W)

    pret_meniu_label = Label(root, text = "Pret meniu:")
    pret_meniu_label.grid(row = 0, column = 2, sticky = W)
    i = 1
    for m in meniuri:
    	meniu_nume_label = Label(root, text = m[0])
    	meniu_nume_label.grid(row = i, column = 0, sticky = W)
    	pret_label = Label(root, text = m[2])
    	pret_label.grid(row = i, column = 2, sticky = W)
    	produs_nume_label = Label(root, text = m[1])
    	produs_nume_label.grid(row = i, column = 1, sticky = W)
    	i = i + 1

    ordonare_pret = Button(root, text = "Ordonare dupa nume", command = show_meniu_price)
    ordonare_pret.grid(row = i + 2, column = 0, columnspan = 2, sticky = W)

    back_button = Button(root, text = "Back", command = shop_interface)
    back_button.grid(row = i + 1, column = 1)

def create_produs_interface():

    clear()

    global produs_name_entry,produs_pret_entry, tip_option, produs_gramaj_entry

    produs_name_label = Label(root, text = "Nume produs")
    produs_name_label.grid(row = 0, column = 0)
    produs_name_entry = Entry(root, width = 25)
    produs_name_entry.grid(row = 0, column = 1)

    produs_pret_label = Label(root, text = "Pret produs")
    produs_pret_label.grid(row = 1, column = 0)
    produs_pret_entry = Entry(root, width = 25)
    produs_pret_entry.grid(row = 1, column = 1)

    choices = {'-', 'Vegetarian', 'Vegan'}
    tip_option = StringVar()
    tip_option.set('-')
    produs_tip_label = Label(root, text = "Categorie")
    tip_dropD = OptionMenu(root, tip_option, *choices)
    produs_tip_label.grid(row = 4, column = 0)
    tip_dropD.grid(row = 4, column = 1, sticky = W)

    produs_gramaj_label = Label(root, text = "Gramaj")
    produs_gramaj_entry = Entry(root, width = 25)
    produs_gramaj_label.grid(row = 3, column = 0)
    produs_gramaj_entry.grid(row = 3, column = 1)

    back_button = Button(root, text = "Inapoi", command = shop_interface)
    back_button.place(relx = 0.20, rely = 0.45)

    submit_button = Button(root, text = "Adauga produs", command = create_produs)
    submit_button.place(relx = 0.38, rely = 0.45)

def sterg_vanzator():
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('delete from vanzator where VANZATOR_ID = (select VANZATOR_ID from magazin where email = ' + a + current_sesion_shop + a + ')')
    cursor.close()
    conn.commit()
    conn.close()

def sterg_magazin():
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('delete from magazin where email = ' + a + current_sesion_shop + a )
    cursor.close()
    conn.commit()
    conn.close()
    MainPage()

def edit_vanzator():
    a="'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('UPDATE Vanzator SET Nume = ' + a + seller_l_name_edit.get() + a + ', Prenume = ' + a + seller_f_name_edit.get() + a + ', Telefon = ' + a + seller_telefon_edit.get() + a + ', Varsta =' + seller_varsta_edit.get() + 'WHERE Vanzator_id = (SELECT VANZATOR_ID FROM MAGAZIN WHERE Email = ' + a + current_sesion_shop + a + ')')
    cursor.close()
    conn.commit()
    conn.close()
    shop_interface()

def edit_vanzator_interface():
    clear()
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, prenume, telefon, varsta from vanzator where VANZATOR_ID = (select VANZATOR_ID from magazin where email = ' + a + current_sesion_shop + a + ')')
    valori = cursor.fetchall()
    cursor.close()
    conn.close()

    global seller_telefon_edit, seller_varsta_edit, seller_l_name_edit, seller_f_name_edit

    seller_l_name_label = Label(root, text = "Nume vanzator")
    seller_l_name_edit = Entry(root, width = 25)
    seller_l_name_label.grid(row = 1, column = 0)
    seller_l_name_edit.grid(row = 1, column = 1)
    seller_l_name_edit.insert(END, valori[0][0])

    seller_f_name_label = Label(root, text = "Prenume vanzator")
    seller_f_name_edit = Entry(root, width = 25)
    seller_f_name_label.grid(row = 2, column = 0)
    seller_f_name_edit.grid(row = 2, column = 1)
    seller_f_name_edit.insert(END, valori[0][1])

    seller_telefon_label = Label(root, text = "Telefon")
    seller_telefon_edit = Entry(root, width = 25)
    seller_telefon_label.grid(row = 3, column = 0)
    seller_telefon_edit.grid(row = 3, column = 1)
    seller_telefon_edit.insert(END, valori[0][2])

    seller_varsta_label = Label(root, text = "Varsta")
    seller_varsta_edit = Entry(root, width = 25)
    seller_varsta_label.grid(row = 4, column = 0)
    seller_varsta_edit.grid(row = 4, column = 1)
    seller_varsta_edit.insert(END, valori[0][3])

    shop_sign_button = Button(root, text = "Schimba", command = edit_vanzator)
    shop_sign_button.grid(row = 5, column = 1)

def edit_magazin():
    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('UPDATE Magazin SET Nume =' + a + shop_name_edit.get() + a + ', Telefon =' + a + shop_telefon_edit.get() + a + ', Adresa = ' + a + shop_adresa_edit.get() + a + ',Email = ' + a + shop_email_edit.get() + a + ',Parola = ' + a + shop_pass_edit.get() + a +  'WHERE email = ' + a + current_sesion_shop + a )
    conn.commit()
    cursor.close()
    conn.close()
    shop_interface()

def edit_magazin_interface():
    clear()

    a = "'"
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.execute('select nume, telefon, adresa, email, parola from magazin where email = ' + a + current_sesion_shop + a )
    valori = cursor.fetchall()
    cursor.close()
    conn.close()

    global shop_name_edit, shop_adresa_edit, shop_email_edit, shop_telefon_edit, shop_pass_edit

    shop_name_label = Label(root, text = "Nume Magazin")
    shop_name_edit = Entry(root, width = 25)
    shop_name_label.grid(row = 2, column = 0)
    shop_name_edit.grid(row = 2, column = 1)
    shop_name_edit.insert(END, valori[0][0])

    shop_telefon_label = Label(root, text = "Telefon")
    shop_telefon_edit = Entry(root, width = 25)
    shop_telefon_label.grid(row = 3, column = 0)
    shop_telefon_edit.grid(row = 3, column = 1)
    shop_telefon_edit.insert(END, valori[0][1])

    shop_adresa_label = Label(root, text = "Adresa")
    shop_adresa_edit = Entry(root, width = 25)
    shop_adresa_label.grid(row = 4, column = 0)
    shop_adresa_edit.grid(row = 4, column = 1)
    shop_adresa_edit.insert(END, valori[0][2])

    shop_email_label = Label(root, text = "Email")
    shop_email_edit = Entry(root, width = 25)
    shop_email_label.grid(row = 5, column = 0)
    shop_email_edit.grid(row = 5, column = 1)
    shop_email_edit.insert(END, valori[0][3])

    shop_pass_label = Label(root, text = "Parola")
    shop_pass_edit = Entry(root, width = 25)
    shop_pass_label.grid(row = 6, column = 0)
    shop_pass_edit.grid(row = 6, column = 1)
    shop_pass_edit.insert(END, valori[0][4])

    shop_next_button = Button(text = "Schimba", command = edit_magazin)
    shop_next_button.grid(row = 7, column = 1)

def shop_interface():
    clear()
    root.geometry("500x500")

    page_title = Label(root, text = "Shop_Interface")
    page_title.place(relx = 0.35, rely = 0)

    space = Label(root, text = " ")
    space.grid(row = 0, column = 0)

    create_produs_button = Button(root, text = "Adaugare produs", command = create_produs_interface)
    create_produs_button.grid(row = 1, column = 0, sticky = W)

    listare_produse_button = Button(root, text = "Vezi produse", command = show_produse)
    listare_produse_button.grid(row = 1, column = 1)

    show_meniu_button = Button(root, text = "Vezi meniuri", command = show_meniu)
    show_meniu_button.grid(row = 1, column = 2, sticky = W)

    stergere_produs = Button(root, text = "Sterge produs", command = sterg_produs_interfata)
    stergere_produs.grid(row = 2, column = 0, sticky = W)

    editeaza_produs = Button(root, text = "Editeaza produs", command = edit_produs_interfata_1)
    editeaza_produs.grid(row = 2, column = 1, sticky = W)

    sterge_meniu = Button(root, text = "Sterge meniu", command = sterg_meniu_interfata)
    sterge_meniu.grid(row = 2, column = 2, sticky = W)

    sterge_vanzator = Button(root, text = "Sterge vanzator", command = sterg_vanzator)
    sterge_vanzator.grid(row = 3, column = 0, sticky = W)

    sterge_magazin = Button(root, text = "Sterge magazin", command = sterg_magazin)
    sterge_magazin.grid(row = 3, column = 1, sticky = W)

    editare_vanzator = Button(root, text = "Editare vanzator", command = edit_vanzator_interface)
    editare_vanzator.grid(row = 3, column = 2, sticky = W)

    editare_magazin = Button(root, text = "Editare magazin", command = edit_magazin_interface)
    editare_magazin.grid(row = 4, column = 0, sticky = W)

    back_button = Button(root, text = "Back", command = MainPage)
    back_button.grid(row =4 , column = 1, sticky = W)

def login_shop():

    global current_sesion_shop

    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()

    a = "'"

    current_sesion_shop =  login_shop_email_entry.get()
    cursor.execute('SELECT Parola FROM Magazin WHERE Email = ' + a + current_sesion_shop + a)
    pass_verif = cursor.fetchone()
    cursor.close()
    conn.close()

    if  pass_verif[0] == login_shop_pass_entry.get():
        shop_interface()
    else:
        denied_label = Label(root, text = "Username sau Parola gresit")
        denied_label.grid(row = 4, column = 1)

def login_user():
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    cursor.close()
    conn.close()

def create_shop():
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    seller_insert_syntax = 'INSERT INTO Vanzator VALUES((SELECT max(VANZATOR_ID) + 1 FROM Vanzator), '
    shop_insert_syntax = 'INSERT INTO Magazin VALUES((SELECT max(MAGAZIN_ID) + 1 FROM Magazin), (SELECT max(VANZATOR_ID) FROM Vanzator),'
    c = ','
    a = "'"
    cursor.execute(seller_insert_syntax + a + seller_l_name_entry.get() + a + c + a + seller_f_name_entry.get() + a + c + a + seller_telefon_entry.get() + a + c + seller_varsta_entry.get() + ")")
    cursor.execute(shop_insert_syntax + a + entry1 + a + c + a + entry2 + a + c + a + entry3 + a + c + a + entry4 + a + c + a + entry5 + a + ")")
    cursor.close()
    conn.commit()
    conn.close()
    MainPage()

def create_username():
    conn = db.connect('Admin/pass@localhost:1521/DBPR')
    cursor = conn.cursor()
    insert_syntax = 'INSERT INTO Client VALUES((SELECT max(CLIENT_ID) + 1 FROM Client),'
    c = ', '
    a = "'"
    cursor.execute(insert_syntax + a + l_name_user_entry.get() + a + c + a + f_name_user_entry.get() + a + c + a + user_address_entry.get() + a + c + a + user_telefon_entry.get() + a + c + a + user_mail_entry.get() + a + c + a + user_password_entry.get()+ a + ')')
    cursor.close()
    conn.commit()
    conn.close()
    MainPage()

def shop_sign_page_2():

    global seller_l_name_entry, seller_f_name_entry, seller_varsta_entry, seller_telefon_entry
    global entry1, entry2, entry3, entry4, entry5

    entry1 = shop_name_entry.get()
    entry2 = shop_telefon_entry.get()
    entry3 = shop_adresa_entry.get()
    entry4 = shop_email_entry.get()
    entry5 = shop_pass_entry.get()

    clear()

    shop_page_title = Label(root, text = "Sign up")
    shop_page_title.grid(row = 0, column = 1)

    shop_page_subtitle = Label(root, text = "Detalii vanzator:")
    shop_page_subtitle.grid(row = 0, column = 1)

    seller_l_name_label = Label(root, text = "Nume vanzator")
    seller_l_name_entry = Entry(root, width = 25)
    seller_l_name_label.grid(row = 1, column = 0)
    seller_l_name_entry.grid(row = 1, column = 1)

    seller_f_name_label = Label(root, text = "Prenume vanzator")
    seller_f_name_entry = Entry(root, width = 25)
    seller_f_name_label.grid(row = 2, column = 0)
    seller_f_name_entry.grid(row = 2, column = 1)

    seller_telefon_label = Label(root, text = "Telefon")
    seller_telefon_entry = Entry(root, width = 25)
    seller_telefon_label.grid(row = 3, column = 0)
    seller_telefon_entry.grid(row = 3, column = 1)

    seller_varsta_label = Label(root, text = "Varsta")
    seller_varsta_entry = Entry(root, width = 25)
    seller_varsta_label.grid(row = 4, column = 0)
    seller_varsta_entry.grid(row = 4, column = 1)


    shop_sign_button = Button(root, text = "Sign Up", command = create_shop)
    shop_sign_button.place(relx = 0.45, rely = 0.38)

def shop_sign_page_1():
    clear()

    global shop_name_entry, shop_adresa_entry, shop_email_entry, shop_telefon_entry, shop_pass_entry

    root.geometry("350x350")

    shop_page_title = Label(root, text = "Sign up")
    shop_page_title.grid(row = 0, column = 1)

    shop_page_subtitle = Label(root, text = "Detalii magazin:")
    shop_page_subtitle.grid(row = 1, column = 0)

    shop_name_label = Label(root, text = "Nume Magazin")
    shop_name_entry = Entry(root, width = 25)
    shop_name_label.grid(row = 2, column = 0)
    shop_name_entry.grid(row = 2, column = 1)

    shop_telefon_label = Label(root, text = "Telefon")
    shop_telefon_entry = Entry(root, width = 25)
    shop_telefon_label.grid(row = 3, column = 0)
    shop_telefon_entry.grid(row = 3, column = 1)

    shop_adresa_label = Label(root, text = "Adresa")
    shop_adresa_entry = Entry(root, width = 25)
    shop_adresa_label.grid(row = 4, column = 0)
    shop_adresa_entry.grid(row = 4, column = 1)

    shop_email_label = Label(root, text = "Email")
    shop_email_entry = Entry(root, width = 25)
    shop_email_label.grid(row = 5, column = 0)
    shop_email_entry.grid(row = 5, column = 1)

    shop_pass_label = Label(root, text = "Parola")
    shop_pass_entry = Entry(root, width = 25)
    shop_pass_label.grid(row = 6, column = 0)
    shop_pass_entry.grid(row = 6, column = 1)

    shop_next_button = Button(text = "Next", command = shop_sign_page_2)
    shop_next_button.grid(row = 7, column = 1)

def user_sign_page():
    clear()
    root.geometry("300x250")
    global l_name_user_entry, f_name_user_entry, user_address_entry, user_telefon_entry, user_mail_entry, option, user_password_entry

    user_page_title = Label(root, text = "Sign up")
    user_page_title.grid(row = 0, column = 1)

    l_name_user_label = Label(root, text = "Nume")
    l_name_user_entry = Entry(root, width = 25)
    l_name_user_label.grid(row = 1, column = 0)
    l_name_user_entry.grid(row = 1, column = 1)

    f_name_user_label = Label(root, text = "Prenume")
    f_name_user_entry = Entry(root, width = 25)
    f_name_user_label.grid(row = 2, column = 0)
    f_name_user_entry.grid(row = 2, column = 1)

    user_password_label = Label(root, text = "Password")
    user_password_entry = Entry(root, width = 25)
    user_password_label.grid(row = 3, column = 0)
    user_password_entry.grid(row = 3, column = 1)

    user_address_label = Label(root, text = "Adresa")
    user_address_entry = Entry(root, width = 25)
    user_address_label.grid(row = 4, column = 0)
    user_address_entry.grid(row = 4, column = 1)

    user_telefon_label = Label(root, text = "Telefon")
    user_telefon_entry = Entry(root, width = 25)
    user_telefon_label.grid(row = 5, column = 0)
    user_telefon_entry.grid(row = 5, column = 1)

    user_mail_label = Label(root, text = "Mail")
    user_mail_entry = Entry(root, width = 25)
    user_mail_label.grid(row = 6, column = 0)
    user_mail_entry.grid(row = 6, column = 1)

    user_button = Button(text = "Sign up", command = create_username)
    user_button.grid(row = 8, column = 1)

def login_page_user():
    clear()

    global login_user_email_entry, login_user_pass_entry

    root.geometry("300x250")

    login_page_title = Label(root, text = "Logare")
    login_page_title.grid(row = 0, column = 1)

    login_user_email_label = Label(root, text = "Email")
    login_user_email_entry = Entry(root, width = 25)
    login_user_email_label.grid(row = 1, column = 0)
    login_user_email_entry.grid(row = 1, column = 1)

    login_user_pass_label = Label(root, text = "Parola")
    login_user_pass_entry = Entry(root, width = 25)
    login_user_pass_label.grid(row = 2, column = 0)
    login_user_pass_entry.grid(row = 2, column = 1)

    button = Button(text = "Login", command = login_user)
    button.grid(row = 3, column = 1)

def login_page_shop():
    clear()

    global login_shop_email_entry, login_shop_pass_entry

    root.geometry("300x250")

    login_page_title = Label(root, text = "Logare")
    login_page_title.grid(row = 0, column = 1)

    login_shop_email_label = Label(root, text = "Email")
    login_shop_email_entry = Entry(root, width = 25)
    login_shop_email_label.grid(row = 1, column = 0)
    login_shop_email_entry.grid(row = 1, column = 1)

    login_shop_pass_label = Label(root, text = "Parola")
    login_shop_pass_entry = Entry(root, width = 25)
    login_shop_pass_label.grid(row = 2, column = 0)
    login_shop_pass_entry.grid(row = 2, column = 1)

    button = Button(text = "Login", command = login_shop)
    button.grid(row = 3, column = 1)
    button_back = Button(text = "Back", command = MainPage)
    button_back.grid(row = 4, column = 1)

def MainPage():
    clear()

    root.geometry("300x250")

    login_button_shop = Button(root, text = "Login Shop", command = login_page_shop)
    login_button_shop.grid(row = 0, column = 0)

    login_button_user = Button(root, text = "Login User", command = login_page_user)
    login_button_user.grid(row = 1, column = 0)

    sign_button_user = Button(root, text = "Create User", command = user_sign_page)
    sign_button_user.grid(row = 2, column = 0, padx = 100)

    shop_button = Button(root, text = "Create Shop", command = shop_sign_page_1)
    shop_button.grid(row = 3, column = 0)

    admin_button = Button(root, text = "Admin Page", command = admin_interface)
    admin_button.grid(row = 4, column = 0)

MainPage()

root.mainloop()
