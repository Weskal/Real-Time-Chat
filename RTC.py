
# Importar o flet

import flet as ft
from datetime import datetime

# Função para rodar o aplicativo

def main(pagina):
    
    titulo = ft.Text("Hashzap")
    
    # websocket = tunel de comunicação entre dois usuários
    
    def msg_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(msg_tunel)
    
    def enviar_msg(evento):
        nome_usuario = label_nome_usuario.value
        nowtime = datetime.now()
        time = nowtime.strftime("%H:%M:%S")
        mensagem = f'{nome_usuario} : {campo_enviar_msg.value} [Submited in {time}]'
        pagina.pubsub.send_all(mensagem) # enviar no tunel a mensagem para todos que estão concectados
       
        # limpar a caixa de msg
        campo_enviar_msg.value = ""
        pagina.update()
        
    
    campo_enviar_msg = ft.TextField(on_submit=enviar_msg)
    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar_msg)
    linha_enviar = ft.Row([campo_enviar_msg, btn_enviar])
    
    chat = ft.Column()
    
    def entrar_chat(evento):
        popup.open= False
        pagina.remove(titulo)
        pagina.remove(botao)
        
        pagina.add(linha_enviar)
        pagina.add(chat)
        
        pagina.add(campo_enviar_msg)
        pagina.add(btn_enviar)
        
        mensagem = f'{label_nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()
    
    # criar o popup
    titulo_popup = ft.Text("Bem-vindo ao Hashzap!")
    label_nome_usuario = ft.TextField(label="Digite o seu nome ")
    btn_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=label_nome_usuario, actions=[btn_popup]) # titulo do popup, conteudo do popup, qtd de botões que tem o popup
    
    def abrir_popup(event):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
    pagina.add(titulo)
    pagina.add(botao)
    
        

ft.app(main, view=ft.AppView.WEB_BROWSER)