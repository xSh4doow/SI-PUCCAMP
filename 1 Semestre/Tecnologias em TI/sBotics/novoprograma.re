tarefa parar
{
	TravarMotor("r", verdadeiro)
	TravarMotor("l", verdadeiro)
}
	
tarefa esquerda com numero velocidade 
{
	TravarMotor("r", falso)
	TravarMotor("l", falso)
	Motor("l",0 - velocidade/2)
	Motor("r",0 + velocidade)
}

tarefa direita com numero velocidade 
{
	TravarMotor("r", falso)
	TravarMotor("l", falso)
	Motor("r",0 - velocidade/2)
	Motor("l",0 + velocidade)
}

tarefa frente com numero velocidade 
{
	TravarMotor("r", falso)
	TravarMotor("l", falso)
	Motor("r", velocidade)
	Motor("l", velocidade)
}

inicio

LigarLuz("led",0, 255, 0)
	AbrirConsole()
	enquanto (verdadeiro) farei 
{
		se (Colorido("rc") e Colorido("lc")) entao 
{
			frente(100)
			Escrever("Seguindo em frente")
}
		senao se (Colorido("lc")) entao 
{
			Escrever("Virando à direita")
			direita(400)
}
		senao se (Colorido("rc")) entao 
{
			Escrever("Virando à esquerda")
			esquerda(400)
}
		se (Cor("rc")=="Vermelho" e Cor("lc")=="Vermelho") entao
{
			parar()
			DesligarLuz("led")
			Escrever("Fim da linha")
			Interromper()
}
}

fim