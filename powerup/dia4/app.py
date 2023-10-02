import flet as ft 
from flet import (
    Page,
    colors
)

if __name__ == "__main__":

    def main(pagina: Page):
        pagina.bgcolor = colors.BLUE_GREY_200
    # def de definir, ou seja vai definir uma função pro python, mesma coisa do function do js
    # pagina é um parametro
        texto = ft.Text('Zap Do Yuki')

        chat = ft.Column()

        nome_usuario = ft.TextField(label='Seu nome:')

        def enviar_msg_tunel(mensagem):
            tipo = mensagem['tipo']
            if tipo == 'mensagem':
                texto_msg = mensagem['texto']
                usuario_msg = mensagem['usuario']
                chat.controls.append(ft.Text(f"{usuario_msg}: {texto_msg}", color='black'))
            else:
                usuario_msg = mensagem['usuario']
                chat.controls.append(ft.Text(f"{usuario_msg} entrou no chat", color='black', size=12, italic=True))
            pagina.update()


        pagina.pubsub.subscribe(enviar_msg_tunel)

        def enviar_msg(evento):
            pagina.pubsub.send_all({'texto': campo_mensagem.value, 'usuario': nome_usuario.value,
                                    'tipo': 'mensagem'})
            campo_mensagem.value = ''
            pagina.update()

        campo_mensagem =ft.TextField(label='Digite uma mensagem', on_submit=enviar_msg)
        bota_enviar_msg = ft.ElevatedButton('Enviar', on_click=enviar_msg)

        def entrar_popup(evento):
            pagina.pubsub.send_all({'usuario': nome_usuario.value, 'tipo': 'entrada'})
            pagina.add(chat)
            popup.open = False
            pagina.remove(botao_iniar)
            pagina.remove(texto)
            pagina.add(ft.Row(
                [campo_mensagem, bota_enviar_msg]
            ))
            pagina.update()
            

        popup = ft.AlertDialog(
            open=False,
            modal=True,
            title=ft.Text('Bem vindo ao chat do Yuki'),
            content=nome_usuario,
            actions=[ft.ElevatedButton('Entrar', on_click=entrar_popup)]
        )

        def entrar_chat(evento):
            pagina.dialog = popup
            popup.open = True
            pagina.update()

        botao_iniar = ft.ElevatedButton('Iniciar Chat', on_click=entrar_chat)

        pagina.add(texto)
        pagina.add(botao_iniar)
        
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

    #Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.1.8
    #isso vai rodar o site