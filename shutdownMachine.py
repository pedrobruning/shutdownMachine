from tkinter import *
import os
import subprocess
import webbrowser

inicial = Tk()
inicial.title("Passo a Passo")
def callback():
    webbrowser.open_new("https://discord.gg/7UJDgBG")

def opcao():
	telaOpcao = Tk()
	telaOpcao.title("Escolha")
	telaOpcao.geometry("300x150")
	inicial.destroy()
	def desligar():
		telaOpcao.destroy()
		root = Tk()
		root.title("ShutdownMachine")
		#The app makes a .bat file to execute after, I tried to use os.system but it seems to not accept more than 3 commands
		#This was the way that I found to make the app run. 
		#I expect to solve this in a near future
		def execute():
			with open('desligar.bat', 'w') as file:
				file.write('shutdown -s -t 15 -c "Desligando em 15 segundos" -m \\' + '\\' + e.get())
			subprocess.call([r'desligar.bat'])
		def abort():
			with open('abortShutdown.bat', 'w') as file:
				file.write('shutdown -a -m \\' + '\\' + e.get())
			subprocess.call([r'abortShutdown.bat'])                    
		def close():
			root.destroy()
		#This Labels between Buttons and Entry are for spaces. I know that's not the best way to do this but now I'm out of time
		w = Label(root, text="Digite o nome do computador na rede\n")
		w.grid(column=0, row=0)
		e = Entry(root)
		e.grid(column=0, row=1)
		z = Label(root, text="")
		z.grid(column=0, row=2)
		button1 = Button(root, text="Executar Desligamento", command=execute)
		button1.grid(column=0,row=3)
		x = Label(root, text="")
		x.grid(column=0, row=4)
		button6 = Button(root, text="Cancelar Desligamento", command=abort)
		button6.grid(column=0, row=5)
		y = Label(root, text="")
		y.grid(column=0, row=6)
		button4 = Button(root, text="Fechar", command=close)
		button4.grid(column=0, row=7)
		root.mainloop()
	def reiniciar():
		telaOpcao.destroy()
		root = Tk()
		root.title("ShutdownMachine")
		#The app makes a .bat file to execute after, I tried to use os.system but it seems to not accept more than 3 commands
		#This was the way that I found to make the app run. 
		#I expect to solve this in a near future
		def execute():
			with open('reiniciar.bat', 'w') as file:
				file.write('shutdown -r -t 15 -c "Reiniciando em 15 segundos" -m \\' + '\\' + e.get())
			subprocess.call([r'reiniciar.bat'])
		def abort():
			with open('abortRestart.bat', 'w') as file:
				file.write('shutdown -a -m \\' + '\\' + e.get())
			subprocess.call([r'abortRestart.bat'])                    
		def close():
			root.destroy()
		w = Label(root, text="Digite o nome do computador na rede\n")
		w.grid(column=0, row=0)
		e = Entry(root)
		e.grid(column=0, row=1)
		z = Label(root, text="")
		z.grid(column=0, row=2)
		button1 = Button(root, text="Executar Reinicialização", command=execute)
		button1.grid(column=0,row=3)
		x = Label(root, text="")
		x.grid(column=0, row=4)
		button6 = Button(root, text="Cancelar Reinicialização", command=abort)
		button6.grid(column=0, row=5)
		y = Label(root, text="")
		y.grid(column=0, row=6)
		button4 = Button(root, text="Fechar", command=close)
		button4.grid(column=0, row=7)
		root.mainloop()
	choice = Label(telaOpcao, text="Escolha Uma Opção")
	choice.pack()
	x = Label(telaOpcao, text="")
	x.pack()
	botaoDesligar = Button(telaOpcao, text="Desligamento", command=desligar)
	botaoDesligar.pack()
	w = Label(telaOpcao, text="")
	w.pack()
	botaoReiniciar = Button(telaOpcao, text="Reinicializar", command=reiniciar)
	botaoReiniciar.pack()
	telaOpcao.mainloop()
rules = Label(inicial, text="Como utilizar:\n 1° - Escolha uma opção\n 2° - Digite o nome da máquina na rede(Caso deixe em branco o computador a ser desligado será o seu)\n3° - Execute a função desejada\n(Lembrando que demora por padrão 15 segundos para desligar/reiniciar)\nExiste um botao de cancelar desligamento/reinicialização\nUse-o com sabedoria.",font=("Arial", 12))
rules.pack()
warning = Label(inicial, text="Não me responsabilizo por quaisquer danos causados com esse programa.\nEsse programa foi feito unicamente para fins didaticos", font=("Arial", 12), fg="red")
warning.pack()
credits = Label(inicial, text="App feito por PhboHe4rt", font=("Comic Sans MS",10), fg="Green")
credits.pack()
buttonHe4rt = Button(inicial, text="Clique aqui para acessar o discord da He4rt", command=callback)
buttonHe4rt.pack()
button4 = Button(inicial, text="Entendi", command=opcao)
button4.pack()
inicial.mainloop()
