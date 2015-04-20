import pygtk
pygtk.require('2.0')
import gtk
import os
# -------------------------

class TextViewExample:

    def close_application(self, widget):
        gtk.main_quit()

    def __init__(self,wid):
        wind4 = gtk.Window(gtk.WINDOW_TOPLEVEL)
       
        wind4.set_title("R N S Institue Of Technology")
        wind4.set_border_width(5)
        wind4.set_size_request(400, 400)
        wind4.set_resizable(True)  

        box1 = gtk.VBox(False, 0)
        wind4.add(box1)
        box1.show()


        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        textbuffer = textview.get_buffer()
       
        sw.add(textview)
        sw.show()
        textview.show()

        box2.pack_start(sw)
        
        infile = open(wid, "r")

        if infile:
            string = infile.read()
            infile.close()
            textbuffer.set_text(string)

        wind4.show()

def main3():
    gtk.main()

    return 0
#--------------------------


def label_box(parent,label_text):
	box1 = gtk.HBox(False, 0)
	label = gtk.Label(label_text)
	label.set_justify(gtk.JUSTIFY_CENTER)
	box1.pack_start(label, True, False, 50)
	label.show()
	return box1

class gui:
	def mod_dest(self,widget,widget1):
		widget1.destroy()
	
	def del_dest(self,widget,widget1):
		widget1.destroy()

	def search_call(self,widget,entry_txt):
		etry_search=entry_txt.get_text()
		print "Search for %s \n" %etry_search
		os.system("./a.out -s %s > searched.txt" % etry_search)
		
		fobj=open("searched.txt","r")
		for i in range(0,6):
			string2=fobj.readline()	
		if(string2=="Not Found"):
			#self.l7.set_text(string2)
			title="R N S Institute of Technology"
			message="<b>Search Not found.</b>\n<i>Enter your search keyword properly</i>\n<i><b>Note:</b></i>\nDon't Enter the<b> Date of Birth</b>\nas your search."
			dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_ERROR,
                               buttons=gtk.BUTTONS_OK)
			dialog.set_markup("<b>%s</b>" % title)
			dialog.format_secondary_markup(message)
			dialog.run()
			dialog.destroy()
			
		
		else:
			TextViewExample("searched.txt")
			main3()
		
		fobj.close()


	def list_call(self,widget):

		os.system("./a.out -l > list.txt")
		TextViewExample("list.txt")
		main3()
		
       
	def mod_call_final(self,widget,usn_mod,name,usn,dob,add):
		name1 = name.get_text()
		usn1  =	usn.get_text()
		dob1  = dob.get_text()
		add1  = add.get_text()
		
		command="./a.out -m %s %s %s %s %s > modified.txt" %(usn_mod,name1,usn1,dob1,add1)
		os.system(command)
		#fobj=open("modified.txt","r")
		#string1=fobj.readline()
		#self.l5.set_text(string1)
		#fobj.close()

		fobj=open("modified.txt","r")
		for i in range(0,1):
			string2=fobj.readline()	
		if(string2=="Requested USN Not found"):
			#self.l7.set_text(string2)
			title="R N S Institute of Technology"
			message="<b>Requested USN Not found.</b>\nNote:\nEnter the USN properly in the \n<b><i>previous window,</i></b>\nto Modify the Record. "
			dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_ERROR,
                               buttons=gtk.BUTTONS_OK)
			dialog.set_markup("<b>%s</b>" % title)
			dialog.format_secondary_markup(message)
			dialog.run()
			dialog.destroy()
		else:
			title="R N S Institute of Technology"
			message="<b><i>Requested Record is updated successfully.</i></b><i>Thank you!!..</i>"
			dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_INFO,
                               buttons=gtk.BUTTONS_OK)
			dialog.set_markup("<b>%s</b>" % title)
			dialog.format_secondary_markup(message)
			dialog.run()
			dialog.destroy()
		fobj.close()
	


	def add_call(self,widget,name,usn,dob,add):
		name1 = name.get_text()
		usn1  =	usn.get_text()
		dob1  = dob.get_text()
		add1  = add.get_text()

		command="./a.out -a %s %s %s %s > added.txt" %(name1,usn1,dob1,add1)
		os.system(command)
		#self.l6.set_text("Added successfully...")

		title="R N S Institute of Technology"
		message="<i>Thank you!!</i>\n\n<b><i>Your Recorded is Added successfully.</i></b>"
		dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_INFO,
                               buttons=gtk.BUTTONS_OK)
		dialog.set_markup("<b>%s</b>" % title)
		dialog.format_secondary_markup(message)
		dialog.run()
		dialog.destroy()

		#TextViewExample("added.txt")
		#main3()


	def del_call(self,widget,usn):
		usn_del = usn.get_text()
		print "USN to be Deleted %s \n" % usn_del
		
		os.system("./a.out -d " + usn_del + " >deleted.txt ")
		fobj=open("deleted.txt","r")
		for i in range(0,1):
			string2=fobj.readline()	
		if(string2=="Enter the correct USN"):
			#self.l7.set_text(string2)
			title="R N S Institute of Technology"
			message="<b>Requested USN Not found.</b>\nNote:\nEnter the USN properly\nto delete the Record."
			dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_ERROR,
                               buttons=gtk.BUTTONS_OK)
			dialog.set_markup("<b>%s</b>" % title)
			dialog.format_secondary_markup(message)
			dialog.run()
			dialog.destroy()
		else:
			title="R N S Institute of Technology"
			message="<b><i>Requested Record is Deleted successfully.</i></b>"
			dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_INFO,
                               buttons=gtk.BUTTONS_OK)
			dialog.set_markup("<b>%s</b>" % title)
			dialog.format_secondary_markup(message)
			dialog.run()
			dialog.destroy()
		fobj.close()
	
		#TextViewExample("deleted.txt")
		#main3()


		
	def mod_call1(self,widget,usn):
		usn_mod = usn.get_text()
		print "USN to be modified %s \n" % usn_mod
		wind=gtk.Window()
		wind.set_position(gtk.WIN_POS_CENTER)
		wind.set_size_request(375,275)
		wind.set_title("Modify Record")
		wind.set_border_width(20)

	        table = gtk.Table(27, 27, False)
		wind.add(table)
		
		#l12=gtk.Label("Enter Details to Modify:")
		#l13=gtk.Label("-------------------------")

		l1=gtk.Label("Name")
		
		l1.set_justify(gtk.JUSTIFY_LEFT)
		l1.show()
		etry_search = gtk.Entry()
		
		etry_search.show()
		
		l2=gtk.Label("USN")
		
		l2.set_justify(gtk.JUSTIFY_LEFT)
		l2.show()
		
		etry_search2 = gtk.Entry()
		
		etry_search2.show()
		
		l3=gtk.Label("Date Of Birth")
		
		l3.set_justify(gtk.JUSTIFY_LEFT)		
		l3.show()
		etry_search3 = gtk.Entry()
		
		etry_search3.show()
		
		l4=gtk.Label("Address")
		
		l4.set_justify(gtk.JUSTIFY_LEFT)		
		l4.show()
		self.l5 = gtk.Label()
		self.l5.show()
		etry_search4 = gtk.Entry()
				
		etry_search4.show()
		
		button1 = gtk.Button()
		
		button1.connect("clicked", self.mod_call_final,usn_mod,etry_search,etry_search2,etry_search3,etry_search4)
		button1.connect("clicked", self.mod_dest,wind)
		box1=label_box(wind,"Modify")
		button1.add(box1)
		
		button1.show()

		button2=gtk.Button()
		button2.connect("clicked", self.mod_dest,wind)
		box1=label_box(wind,"Exit")
		button2.add(box1)
	
		button2.show()

		

		#table.attach(l12,2,5,0,2)
		#table.attach(l13,2,5,3,5)
		table.attach(l1,1,2,5,7)
		table.attach(etry_search,3,5,5,7)
		table.attach(l2,1,2,9,11)
		table.attach(etry_search2,3,5,9,11)
		table.attach(l3,1,2,13,15)
		table.attach(etry_search3,3,5,13,15)
		table.attach(l4,1,2,17,19)
		table.attach(etry_search4,3,5,17,19)
		table.attach(button2,1,2,21,23)
		table.attach(button1,3,5,21,23)
		table.attach(self.l5,3,5,25,27)
		table.show()

		wind.show_all()


	def search(self, widget, data=None):
		
		wind=gtk.Window()
		wind.set_position(gtk.WIN_POS_CENTER)
		#wind.set_size_request(300,200)
		wind.set_title("Search Record")
		wind.set_border_width(20)
		vbox=gtk.VBox(False,0)
		wind.add(vbox)
		
		

		hbox=gtk.HBox(False,0)
		l1=gtk.Label("Name/USN/Place")
		hbox.pack_start(l1,False,False,0)
		l1.set_justify(gtk.JUSTIFY_LEFT)
		l1.show()
		etry_search = gtk.Entry()
		hbox.pack_start(etry_search,True,False,0)
		etry_search.show()
		vbox.add(hbox)

		hbox.show()
		#self.l7 = gtk.Label()
	
		#self.l7.show()
		textabc="Note:Don't Enter the Date of Birth"
		l14=gtk.Label("%s" % textabc)
		vbox.pack_start(l14,False,False,0)
		l14.show()

		button1 = gtk.Button()
		button1.connect("clicked", self.search_call,etry_search)
		button1.connect("clicked", self.mod_dest,wind)
		box1=label_box(wind,"Search")
		#button1.connect("clicked", self.mod_dest,wind)
		button1.add(box1)
		
		vbox.pack_start(button1,0,10,15)
		#vbox.pack_start(self.l7,0,0,5)
		box1.show()
		button1.show()
		
		vbox.show()
		wind.show()
		
	def add(self, widget, data=None):
		wind=gtk.Window()
		wind.set_position(gtk.WIN_POS_CENTER)

		wind.set_size_request(375,325)
		wind.set_border_width(100)
		wind.set_title("Add Record")
		wind.set_border_width(50)

	        table = gtk.Table(27, 27, False)
		wind.add(table)


		#l12=gtk.Label("Enter your Deatails:")
		#l13=gtk.Label("-------------------------")
	
		l1=gtk.Label("Name")
		
		l1.set_justify(gtk.JUSTIFY_LEFT)
		l1.show()
		etry_search = gtk.Entry()
		
		etry_search.show()
	
		l2=gtk.Label("USN")
	
		l2.set_justify(gtk.JUSTIFY_LEFT)
		l2.show()
	
		etry_search2 = gtk.Entry()
		
		etry_search2.show()
		
		l3=gtk.Label("Date Of Birth")
		
		l3.set_justify(gtk.JUSTIFY_LEFT)		
		l3.show()
		etry_search3 = gtk.Entry()
		
		etry_search3.show()
		
		l4=gtk.Label("Address")
		
		l4.set_justify(gtk.JUSTIFY_LEFT)		
		l4.show()
		self.l6 = gtk.Label()
		self.l6.show()
		etry_search4 = gtk.Entry()
				
		etry_search4.show()

		button1 = gtk.Button()
		
		button1.connect("clicked", self.add_call, etry_search,etry_search2,etry_search3,etry_search4)
		button1.connect("clicked", self.del_dest,wind)
		box1=label_box(wind,"Add")
		button1.add(box1)
	
		button1.show()
		#vbox.show()

		button2=gtk.Button()
		button2.connect("clicked", self.mod_dest,wind)
		box1=label_box(wind,"Exit")
		button2.add(box1)
	
		button2.show()


		#table.attach(l12,2,5,0,2)
		#table.attach(l13,2,5,3,5)
		table.attach(l1,1,2,5,7)
		table.attach(etry_search,3,5,5,7)
		table.attach(l2,1,2,9,11)
		table.attach(etry_search2,3,5,9,11)
		table.attach(l3,1,2,13,15)
		table.attach(etry_search3,3,5,13,15)
		table.attach(l4,1,2,17,19)
		table.attach(etry_search4,3,5,17,19)
		table.attach(button2,1,2,21,23)
		table.attach(button1,3,5,21,23)

		table.attach(self.l6,3,5,26,27)


		table.show()
		wind.show_all()
		
	def delete(self, widget, data=None):
		wind=gtk.Window()
		wind.set_position(gtk.WIN_POS_CENTER)
		wind.set_size_request(300,200)
		wind.set_border_width(150)
		wind.set_title("Delete Record")
		wind.set_border_width(20)
		vbox=gtk.VBox(False,0)
		wind.add(vbox)
		hbox=gtk.HBox(False,0)

		l14=gtk.Label("Record Will be Deleted from Database")
		vbox.pack_start(l14,False,False,0)
		l14.show()

		l15=gtk.Label("------------------------------------")
		vbox.pack_start(l15,False,False,0)
		l15.show()

		

		l1=gtk.Label("Enter the USN")
		hbox.pack_start(l1,False,False,5)
		l1.show()
		etry_search = gtk.Entry()
		hbox.pack_start(etry_search,False,False,5)
		vbox.pack_start(etry_search,False,False,0)

		#etry_search.set_border_width(50)
		etry_search.show()
		vbox.add(hbox)
		hbox.show()
		self.l8 = gtk.Label()
		
		self.l8.show()
		button1 = gtk.Button()
		button1.connect("clicked", self.del_call, etry_search)
		button1.connect("clicked", self.mod_dest,wind)
		box1=label_box(wind,"Delete")
		button1.add(box1)
		vbox.pack_start(button1,False,True,0)
		vbox.pack_start(self.l8,0,0,5)
		box1.show()
		vbox.show()
		button1.show()
		wind.show()
	def mod1(self,widget,data=None):
		wind=gtk.Window()
		wind.set_position(gtk.WIN_POS_CENTER)
		wind.set_size_request(300,150)
		wind.set_title("Modify Record")
		wind.set_border_width(20)
		vbox=gtk.VBox(False,0)
		wind.add(vbox)
		hbox=gtk.HBox(False,0)

		l14=gtk.Label("Record Will be modified in Database")
		vbox.pack_start(l14,False,False,0)
		l14.show()

		l15=gtk.Label("------------------------------------")
		vbox.pack_start(l15,False,False,0)
		l15.show()

		l1=gtk.Label("Enter the USN")
		hbox.pack_start(l1,False,False,5)
		l1.show()
		etry_search = gtk.Entry()
		hbox.pack_start(etry_search,False,False,5)
		etry_search.show()
		vbox.add(hbox)
		hbox.show()
		button1 = gtk.Button()
		button1.connect("clicked", self.mod_call1, etry_search)
		button1.connect("clicked", self.mod_dest,wind)
		box1=label_box(wind,"Modify")
		
		button1.add(box1)
		vbox.pack_start(button1,False,False,0)
		box1.show()
		button1.show()
		vbox.show()
		wind.show()
	
	def thk(self, widget,wind):
		title="R N S Institute of Technology"
		message="Keep your records safe with us\n(Maintaining Database)\n \n<i>Thank you! for sparing your precious\n time with us.</i>\n\n\n<i>By Code Commandos.</i>"
		dialog = gtk.MessageDialog(wind,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_INFO,
                               buttons=gtk.BUTTONS_OK)
		dialog.set_markup("<b>%s</b>" % title)
		dialog.format_secondary_markup(message)
		dialog.run()
		dialog.destroy()


	def about(self, widget, wind):
		title="R N S Institute of Technology"
		message="Keep your records safe with us.\n(Maintaining Student Database)\n\n<i>Authors :\nRakesh Shetty,\n Sagar M Ayi and \n Ramesh Sidaray Mudalagi</i>"
		dialog = gtk.MessageDialog(wind,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_INFO,
                               buttons=gtk.BUTTONS_OK)
		dialog.set_markup("<b>%s</b>" % title)
		dialog.format_secondary_markup(message)
		dialog.run()
		dialog.destroy()

	def info(self, widget, wind):
		title="R N S Institute of Technology"
		message="Keep your records safe with us\n(Maintaining Database)\n \n<i>Authors : \n\nRakesh Shetty,\n Sagar M Ayi and \n Ramesh Sidaray Mudalagi</i>"
		dialog = gtk.MessageDialog(wind,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_INFO,
                               buttons=gtk.BUTTONS_OK)
		dialog.set_markup("<b>%s</b>" % title)
		dialog.format_secondary_markup(message)
		dialog.run()
		dialog.destroy()
	
		

	def __init__(self):
	 	
	 	window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Menu")
		window.set_border_width(50)
		window.set_size_request(250,450)
		window.connect("destroy", lambda wid: gtk.main_quit())
                window.connect("delete_event", lambda w,e: gtk.main_quit())
                window.set_position(gtk.WIN_POS_CENTER)
                vbox=gtk.VBox(False,0)
		window.add(vbox)
		vbox.show()

		l10=gtk.Label("Student Database")
		vbox.pack_start(l10,False,False,10)
		l10.show()

		l11=gtk.Label("--------------------------")
		vbox.pack_start(l11,False,False,0)
		l11.show()
		
		

		#creating about button
		button6 = gtk.Button()
		button6.connect("clicked", self.about, window)
		box6=label_box(window,"About app..")
		button6.add(box6)
		vbox.pack_start(button6,False,False,8)
		box6.show()
		button6.show()


		#creating add button
		button2 = gtk.Button()
		button2.connect("clicked", self.add, "Add record")
		box2=label_box(window,"Add record")
		button2.add(box2)
		vbox.pack_start(button2,False,False,8)
		box2.show()
		button2.show()

                
	    #creating search button
		button1 = gtk.Button()
		button1.connect("clicked", self.search, "Search record")
		box1=label_box(window,"Search record")
		button1.add(box1)
		vbox.pack_start(button1,False,False,8)
		box1.show()
		
		button1.show()
		
		
		#creating delete button
		button3 = gtk.Button()
		button3.connect("clicked", self.delete, "Delete record")
		box3=label_box(window,"Delete record")
		#button3.connect("clicked", self.mod_dest,window)
		button3.add(box3)
		vbox.pack_start(button3,False,False,8)
		box3.show()
		button3.show()
		#creating modify button
		button4 = gtk.Button()
		button4.connect("clicked", self.mod1, "Modify record")
		box4=label_box(window,"Modify record")
		button4.add(box4)
		vbox.pack_start(button4,False,False,8)
		box4.show()
		button4.show()
		
		#creating list button
		button5 = gtk.Button()
		button5.connect("clicked", self.list_call)
		box5=label_box(window,"List record")
		button5.add(box5)
		vbox.pack_start(button5,False,False,8)
		box5.show()
		button5.show()

		#creating thank button
		button10 = gtk.Button()
		#button10.connect("clicked", self.thk, window)
		box10=label_box(window,"Thank You!!")
		button10.connect("clicked", self.thk, window)
		button10.connect("clicked", self.del_dest,window)
		button10.add(box10)
		vbox.pack_start(button10,False,False,8)
		box10.show()
		button10.show()
		
		
		window.show()

def main():
    gtk.main()
   	
    return 0

if __name__ == "__main__":
    gui()
    main()

