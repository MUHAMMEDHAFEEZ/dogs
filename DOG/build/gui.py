
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3

qty=0
qty1=0
qty2=0
qty3=0
qty4=0
qty5=0
qty6=0
qty7=0
qty8=0


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\DOG\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


def itemplus():
    global qty
    qty+=1
    my_label.config(text = qty)

def item1plus():
    global qty1
    qty1+=1
    my_label1.config(text = qty1)

def item2plus():
    global qty2
    qty2+=1
    my_label2.config(text = qty2)

def item3plus():
    global qty3
    qty3+=1
    my_label3.config(text = qty3)

def item4plus():
    global qty4
    qty4+=1
    my_label4.config(text = qty4)

def item5plus():
    global qty5
    qty5+=1
    my_label5.config(text = qty5)

def item6plus():
    global qty6
    qty6+=1
    my_label6.config(text = qty6)

def item7plus():
    global qty7
    qty7+=1
    my_label7.config(text = qty7)

def item8plus():
    global qty8
    qty8+=1
    my_label8.config(text = qty8)
    
#item mins
def itemmins():
    global qty
    if(qty>0):
         qty-=1
    my_label.config(text = qty)
    
def item1mins():
    global qty1
    if(qty1>0):
         qty1-=1
    my_label1.config(text = qty1)

def item2mins():
    global qty2
    if(qty2>0):
         qty2-=1
    my_label2.config(text = qty2)

def item3mins():
    global qty3
    if(qty3>0):
         qty3-=1
    my_label3.config(text = qty3)

def item4mins():
    global qty4
    if(qty4>0):
         qty4-=1
    my_label4.config(text = qty4)

    
def item5mins():
    global qty5
    if(qty5>0):
         qty5-=1
    my_label5.config(text = qty5)

def item6mins():
    global qty6
    if(qty6>0):
         qty6-=1
    my_label6.config(text = qty6)

def item7mins():
    global qty7
    if(qty7>0):
         qty7-=1
    my_label7.config(text = qty7)

def item8mins():
    global qty8
    if(qty8>0):
         qty8-=1
    my_label8.config(text = qty8)


#LaBL
my_label= Label(window,text = qty ,font="BOLD 30")
my_label.place(x=157,
    y=293,
    width=45,
    height=45)    
    
my_label1= Label(window,text = qty1 ,font="BOLD 30")
my_label1.place(x=522,
    y=293,
    width=45,
    height=45)    
    
my_label2= Label(window,text = qty2 ,font="BOLD 30")
my_label2.place(x=887,
    y=293,
    width=45,
    height=45)  

my_label3= Label(window,text = qty3 ,font="BOLD 30")
my_label3.place(x=161,
    y=623,
    width=45,
    height=45)  

   
my_label4= Label(window,text = qty4 ,font="BOLD 30")
my_label4.place(x=522,
    y=623,
    width=45,
    height=45)  

my_label5= Label(window,text = qty5 ,font="BOLD 30")
my_label5.place(x=879,
    y=623,
    width=45,
    height=45)  

my_label6= Label(window,text = qty6,font="BOLD 30")
my_label6.place(x=157,
    y=955,
    width=45,
    height=45)  

my_label7= Label(window,text = qty7,font="BOLD 30")
my_label7.place(x=524,
    y=955,
    width=45,
    height=45)  

my_label8= Label(window,text = qty8,font="BOLD 30")
my_label8.place(x=879,
    y=952,
    width=45,
    height=45)      

#new_invice
invoice_list = []
def new_invoice():
    tree.delete(*tree.get_children())
    
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = "mohammed hafeez"
    phone = "666-666"
    subtotal = sum(item[3] for item in invoice_list) 
    salestax = 0.1
    total = subtotal*(1-salestax)
    
    doc.render({"name":name, 
            "phone":phone,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "salestax":str(salestax*100)+"%",
            "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
   
    new_invoice()    

def enter_data(qt,descz,pricez,totalz):
    
    # Create Table
    conn = sqlite3.connect('data.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS dogs 
            (qt INT, descz TEXT, pricez FLOAT, totalz FLOAT )
    '''
    conn.execute(table_create_query)
    
    # Insert Data
    data_insert_query = '''INSERT INTO dogs (qt, descz, pricez, 
    totalz) VALUES 
    (?, ?, ?,?)'''
    data_insert_tuple = (qt,
                          descz, pricez, totalz)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
 

#add item
def add_item():
    global qty
    if(qty>0):
         desc = "فيلادلفيا"
         price = 10
         line_total= qty*price
         invoice_item = [qty, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty,desc,price,line_total)
         invoice_list.append(invoice_item)
    
def add_item1():
    global qty1
    if(qty1>0):
         desc = "شيتاكي ساكي ماكي"
         price = 10
         line_total= qty*price
         invoice_item = [qty1, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty1,desc,price,line_total)
         invoice_list.append(invoice_item)
    
def add_item2():
    global qty2
    if(qty2>0):
         desc = "فيلادلفيا مع الجمبري"
         price = 15
         line_total= qty2*price
         invoice_item = [qty2, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty2,desc,price,line_total)
         invoice_list.append(invoice_item)
    
def add_item3():
    global qty3
    if(qty3>0):
         desc = "فيلادلفيا عجينة البانكيك السائلة"
         price = 12
         line_total= qty3*price
         invoice_item = [qty3, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty3,desc,price,line_total)
         invoice_list.append(invoice_item)
    
def add_item4():
    global qty4
    if(qty4>0):
         desc = "سكن ماكي"
         price = 10
         line_total= qty4*price
         invoice_item = [qty4, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty4,desc,price,line_total)
         invoice_list.append(invoice_item)
    
def add_item5():
    global qty5
    if(qty5>0):
         desc = "سينسي"
         price = 13
         line_total= qty5*price
         invoice_item = [qty5, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty5,desc,price,line_total)
         invoice_list.append(invoice_item)
    
def add_item6():
    global qty6
    if(qty6>0):
         desc = "تاماجويا"
         price = 12
         line_total= qty6*price
         invoice_item = [qty6, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty6,desc,price,line_total)
         invoice_list.append(invoice_item)
    


def add_item7():
    global qty7
    if(qty7>0):
         desc = "رنجه"
         price = 80
         line_total= qty7*price
         invoice_item = [qty7, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty7,desc,price,line_total)
         invoice_list.append(invoice_item)
    
def add_item8():
    global qty8
    if(qty8>0):
         desc = "سيزر"
         price = 13
         line_total= qty8*price
         invoice_item = [qty8, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty8,desc,price,line_total)
         invoice_list.append(invoice_item)
 


#making a tree
columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text="Total")
tree.place(x=1079,
    y=38,
    width=342,
    height=800)



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemmins(),
    relief="flat"
)
button_1.place(
    x=229.0,
    y=293.0,
    width=45.0,
    height=45.0
)
button_1_new = Button(
    text="NEW",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: new_invoice()
)
button_1_new.place(
    x=1079.0,
    y=852.0,
    width=133.0,
    height=111.0
)

button_1_gen = Button(
    text="GEN",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_invoice(),
    relief="flat"
)
button_1_gen.place(
    x=1283.0,
    y=852.0,
    width=133.0,
    height=111.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3mins(),
    relief="flat"
)
button_2.place(
    x=229.0,
    y=626.0,
    width=45.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6mins(),
    relief="flat"
)
button_3.place(
    x=229.0,
    y=955.0,
    width=45.0,
    height=45.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7mins(),
    relief="flat"
)
button_4.place(
    x=592.0,
    y=955.0,
    width=45.0,
    height=45.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8mins(),
    relief="flat"
)
button_5.place(
    x=948.0,
    y=955.0,
    width=45.0,
    height=45.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=591.0,
    y=623.0,
    width=45.0,
    height=45.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4mins(),
    relief="flat"
)
button_7.place(
    x=591.0,
    y=623.0,
    width=45.0,
    height=45.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8mins(),
    relief="flat"
)
button_8.place(
    x=591.0,
    y=293.0,
    width=45.0,
    height=45.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2mins(),
    relief="flat"
)
button_9.place(
    x=943.0,
    y=296.0,
    width=45.0,
    height=45.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5mins(),
    relief="flat"
)
button_10.place(
    x=948.0,
    y=623.0,
    width=45.0,
    height=45.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemplus(),
    relief="flat"
)
button_11.place(
    x=94.0,
    y=293.0,
    width=45.0,
    height=45.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3plus(),
    relief="flat"
)
button_12.place(
    x=94.0,
    y=623.0,
    width=45.0,
    height=45.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6plus(),
    relief="flat"
)
button_13.place(
    x=89.0,
    y=955.0,
    width=45.0,
    height=45.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=457.0,
    y=955.0,
    width=45.0,
    height=45.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=457.0,
    y=955.0,
    width=45.0,
    height=45.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7plus(),
    relief="flat"
)
button_16.place(
    x=457.0,
    y=955.0,
    width=45.0,
    height=45.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8plus(),
    relief="flat"
)
button_17.place(
    x=811.0,
    y=952.0,
    width=45.0,
    height=45.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4plus(),
    relief="flat"
)
button_18.place(
    x=457.0,
    y=623.0,
    width=45.0,
    height=45.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=457.0,
    y=293.0,
    width=45.0,
    height=45.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item1plus(),
    relief="flat"
)
button_20.place(
    x=457.0,
    y=293.0,
    width=45.0,
    height=45.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2plus(),
    relief="flat"
)
button_21.place(
    x=811.0,
    y=293.0,
    width=45.0,
    height=45.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5plus(),
    relief="flat"
)
button_22.place(
    x=811.0,
    y=623.0,
    width=45.0,
    height=45.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item(),
    relief="flat"
)
button_23.place(
    x=30.0,
    y=24.0,
    width=300.0,
    height=250.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item3(),
    relief="flat"
)
button_24.place(
    x=30.0,
    y=354.0,
    width=300.0,
    height=250.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item1(),
    relief="flat"
)
button_25.place(
    x=395.0,
    y=24.0,
    width=300.0,
    height=250.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item4(),
    relief="flat"
)
button_26.place(
    x=395.0,
    y=354.0,
    width=300.0,
    height=250.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item5(),
    relief="flat"
)
button_27.place(
    x=760.0,
    y=354.0,
    width=300.0,
    height=250.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item8(),
    relief="flat"
)
button_28.place(
    x=760.0,
    y=684.0,
    width=300.0,
    height=250.0
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item7(),
    relief="flat"
)
button_29.place(
    x=395.0,
    y=684.0,
    width=300.0,
    height=250.0
)

button_image_30 = PhotoImage(
    file=relative_to_assets("button_30.png"))
button_30 = Button(
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item6(),
    relief="flat"
)
button_30.place(
    x=30.0,
    y=684.0,
    width=300.0,
    height=250.0
)

button_image_31 = PhotoImage(
    file=relative_to_assets("button_31.png"))
button_31 = Button(
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item2(),
    relief="flat"
)
button_31.place(
    x=760.0,
    y=24.0,
    width=300.0,
    height=250.0
)
window.resizable(False, False)
window.mainloop()
