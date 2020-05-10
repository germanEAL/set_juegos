import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

archivo='jugadores.txt'
dicc={}
with open(archivo,'w')as f:
	json.dump(dicc,f)  #utilizo json para que pueda manejarme de manera mas facil con el txt

def guardar_datos(archivo,nombre,juego):
	with open(archivo,'r') as f:
		 dicc=json.load(f)
		 if nombre in dicc.keys():
			 dicc[nombre]+=[juego] #guardo los datos en un diccionario donde las keys son los jugadores y contienen una lista de los juegos que fue jugando
		 else:
			 lista=[]
			 lista.append(juego)
			 dicc.setdefault(nombre,lista)
	with open(archivo,'w') as f:
		 json.dump(dicc,f)
		 sg.Popup(dicc)




def main(args):
	sg.theme('DarkBrown4')

	opciones=['Ahorcado','TA-TE-TI','Otello']

	layout=[[sg.Text('ingrese su nombre:')], 
	        [sg.Input(key='nombre')],
		    [sg.Text('elija el juego que quiera jugar')],
			[sg.Listbox(opciones,size=(20,10),key='opcion')],
			[sg.Button('jugar'),sg.Button('dejar de jugar')]]	
		
	window=sg.Window('juegos',layout)
    
	while True:
		event,values=window.read()
		if event == 'dejar de jugar':
			 break
		if event == 'jugar':
			nombre=values['nombre']
			juego=values['opcion']
			print(juego)
			if juego[0] =='Ahorcado':
				hangman.main()
			elif juego[0] == 'TA-TE-TI':
				tictactoeModificado.main()
			elif juego[0] == 'Otello':
				reversegam.main()
			guardar_datos(archivo,nombre,juego[0])	 
	window.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
