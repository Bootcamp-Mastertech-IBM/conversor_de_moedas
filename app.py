from audioop import getsample
from tkinter import Tk, ttk
from tkinter import *
import requests
import json
import string

####################### cores ############################

cor0= "#c0c0c0" #cinza#
cor1= "#333333" #preta#
cor2= "#38576b" #azul#
cor4= "#ffffff"
######################## janela ##############################

janela = Tk()
janela.geometry('300x360')
janela.title('Converso de Moedas')
janela.configure(bg=cor0)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

########################### divisao da janela #############################

Frame_cima = Frame(janela, width=300, height=60, padx=0,pady=0, bg=cor0, relief='flat')
Frame_cima.grid(row=0,column=0, columnspan=2)

Frame_baixo = Frame(janela, width=300, height=260, padx=0,pady=5, bg=cor0, relief='flat')
Frame_baixo.grid(row=1,column=0, sticky=NSEW)

####################################### FUNCAO CONVERTER #########################################
def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrada = valor.get()



    
    url = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
    dados = json.loads(url.text)
    cambio= dados['rates'][moeda_para]

    resultado = float(valor_entrada) * float(cambio)

    if moeda_para == 'USD':
        simbolo = '$'
    elif moeda_para == 'AOA':
        simbolo = 'Kz'
    elif moeda_para == 'INR':
        simbolo = '₹'
    elif moeda_para == 'EUR':
        simbolo = '€'
    else:
        simbolo = 'R$'
        
        

    moeda_equivalente = simbolo + "{:.2f}".format(resultado)
    app_resultado["text"] = moeda_equivalente
    

        

########################## configurando frame de cima ############################
Frame_cima = Label(janela, text='Conversor de Moedas', relief='solid', anchor='center', font=('Arial 16 bold'), bg=cor2, fg=cor1, width=23, height=2)
Frame_cima.place(x=0, y=0)

app_resultado = Label(Frame_baixo, relief='solid',  anchor='center', font=('Ivy 15 bold'), bg=cor4,fg=cor1, width=15, height=2)
app_resultado.place(x=50, y=10)

moeda = ['AOA', 'BRL', 'EUR', 'INR', 'USD']

janela = Label(Frame_baixo, text='De', relief='flat', anchor= 's', font=('Arial 9 bold'), bg=cor0,fg=cor1, width=8, height=1, justify='left')
janela.place(x=60, y=90)
combo_de = ttk.Combobox(Frame_baixo, height=200, width=8, font=('Ivy 12 bold'))
combo_de.place(x=50, y=120)
combo_de['value'] = (moeda)


janela = Label(Frame_baixo, text='Para', relief='flat', anchor= 's', font=('Arial 9 bold'), bg=cor0,fg=cor1, width=8, height=1, justify='left')
janela.place(x=170, y=90)
combo_para = ttk.Combobox(Frame_baixo, height=200, width=8, font=('Ivy 12 bold'))
combo_para.place(x=160, y=120)
combo_para['value'] = (moeda)

valor = Entry(Frame_baixo, width=23, justify='center', font=('Ivy 12 bold'), relief='solid')
valor.place(x=50, y=155)

botao = Button(Frame_baixo, command=converter, text='converter', width=19, padx=5, height=1, bg=cor2, fg=cor1, font=('Ivy 12 bold'), relief='flat', overrelief=RIDGE)
botao.place(x=49, y=183)

def limpar():
    combo_de.delete(0, END)
    combo_para.delete(0, END)
    valor.delete(0, END)
    app_resultado["text"] = ''

 
botao_limpar = Button(Frame_baixo, text='limpar', command=limpar, width=15, padx=10, bg=cor2, fg=cor1, relief='raised', highlightthickness=0, bd=0, font=('Ivy 10 bold'))
botao_limpar.place(x=85, y=225)


janela.mainloop()