_proc:
	mov ah, 00h ;subfuncao de video
	mov al, 01h ; modo de video 40x 25 16cores
	int 10h ;interrupção de video

	mov ah , 0eh ; subfuncao para escrever na tela

	mov al, 'O' ; coloca 'o 'no byte menos significativo 
				;do registrador AX , que tem 16bits (2byte)
	int 10h   ; escrever na tela

	mov al,'l'
	int 10h

	mov al,'a'
	int 10h 

	mov al,' '
	int 10h

	mov al,'M'
	int 10h

	mov al,'u'
	int 10h

	mov al,'n'
	int 10h

		mov al,'d'
	int 10h

	mov al,'o'
	int 10h

	mov al,'!'
	int 10h

	call _proc ; chamar procedimento

	