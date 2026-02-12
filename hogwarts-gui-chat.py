#!/usr/bin/env python3
from html_sanitizer import Sanitizer
from nicegui import ui
from lib.tool import HogwartsSpellTools
from lib.utils import PromptUtils, OllamaUtils

# get available functions
functions = HogwartsSpellTools.available_functions()

def chat(user_prompt: str):
    return OllamaUtils.chat(user_prompt=user_prompt,
                            system_prompt=PromptUtils.get_system_prompt(),
                            tools=functions)

def add_hogwarts_theme():
    """Add Harry Potter/Hogwarts themed CSS to the page"""
    ui.add_head_html('''
    <style>
        /* Google Fonts for authentic Harry Potter aesthetic
           Using CDN for simplicity; consider self-hosting for production */
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Spectral:wght@300;400;600&display=swap');
        
        /* Main body styling with magical background */
        body {
            background: linear-gradient(135deg, #1a0e0e 0%, #2d1b1b 50%, #1a0e0e 100%) !important;
            background-attachment: fixed !important;
            font-family: 'Spectral', serif !important;
        }
        
        /* Add subtle stars/sparkles effect */
        body::before {
            content: '' !important;
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100% !important;
            height: 100% !important;
            background-image: 
                radial-gradient(2px 2px at 20% 30%, rgba(255, 215, 0, 0.3), transparent),
                radial-gradient(2px 2px at 60% 70%, rgba(255, 215, 0, 0.2), transparent),
                radial-gradient(1px 1px at 50% 50%, rgba(255, 215, 0, 0.3), transparent),
                radial-gradient(1px 1px at 80% 10%, rgba(255, 215, 0, 0.2), transparent),
                radial-gradient(2px 2px at 90% 60%, rgba(255, 215, 0, 0.3), transparent),
                radial-gradient(1px 1px at 33% 80%, rgba(255, 215, 0, 0.2), transparent) !important;
            background-size: 200% 200% !important;
            background-position: 0% 0% !important;
            pointer-events: none !important;
            z-index: 0 !important;
        }
        
        /* Hogwarts house colors */
        :root {
            --gryffindor-gold: #D3A625;
            --dark-gold: #B8860B;
            --bright-gold: #FFD700;
            --gryffindor-red: #740001;
            --dark-red: #5A0001;
            --hover-red: #8B0001;
            --ravenclaw-blue: #0E1A40;
            --magic-purple: #4A148C;
            --parchment: #F4E8D0;
            --dark-wood: #2C1810;
        }
        
        /* Main container styling */
        .nicegui-content {
            position: relative !important;
            z-index: 1 !important;
        }
        
        /* Chat message containers */
        .q-message {
            margin: 1rem 0 !important;
        }
        
        /* Sent messages (user) - styled as magical scrolls */
        .q-message-sent .q-message-text {
            background: linear-gradient(135deg, var(--gryffindor-gold) 0%, var(--dark-gold) 100%) !important;
            color: var(--dark-wood) !important;
            border: 2px solid var(--gryffindor-red) !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 15px rgba(211, 166, 37, 0.4), inset 0 1px 3px rgba(255, 255, 255, 0.3) !important;
            padding: 12px 18px !important;
            font-family: 'Spectral', serif !important;
            font-weight: 600 !important;
            position: relative !important;
        }
        
        .q-message-sent .q-message-text::before {
            content: '✨' !important;
            position: absolute !important;
            left: -25px !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            font-size: 1.2rem !important;
        }
        
        /* Received messages (bot) - styled as aged parchment */
        .q-message-received .q-message-text {
            background: linear-gradient(to bottom, #F4E8D0 0%, #E8DCC0 100%) !important;
            color: #2C1810 !important;
            border: 2px solid var(--gryffindor-gold) !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 15px rgba(44, 24, 16, 0.3), inset 0 1px 3px rgba(139, 90, 43, 0.2) !important;
            padding: 12px 18px !important;
            font-family: 'Spectral', serif !important;
            position: relative !important;
        }
        
        .q-message-received .q-message-text::before {
            content: '🪄' !important;
            position: absolute !important;
            right: -25px !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            font-size: 1.2rem !important;
        }
        
        /* Message name labels */
        .q-message-name {
            font-family: 'Cinzel', serif !important;
            font-weight: 700 !important;
            color: var(--gryffindor-gold) !important;
            text-shadow: 0 0 10px rgba(211, 166, 37, 0.5) !important;
            font-size: 0.9rem !important;
            letter-spacing: 1px !important;
        }
        
        /* Footer styling - magical dark theme */
        .q-footer {
            background: linear-gradient(to bottom, rgba(26, 14, 14, 0.95), rgba(45, 27, 27, 0.95)) !important;
            border-top: 2px solid var(--gryffindor-gold) !important;
            box-shadow: 0 -4px 20px rgba(211, 166, 37, 0.2) !important;
            backdrop-filter: blur(10px) !important;
        }
        
        /* Input field - enchanted scroll style */
        .q-field {
            background: rgba(244, 232, 208, 0.95) !important;
            border-radius: 25px !important;
            border: 2px solid var(--gryffindor-gold) !important;
            box-shadow: 0 2px 10px rgba(211, 166, 37, 0.3), inset 0 1px 2px rgba(139, 90, 43, 0.1) !important;
        }
        
        .q-field__control {
            color: var(--dark-wood) !important;
            font-family: 'Spectral', serif !important;
        }
        
        .q-field__control::before,
        .q-field__control::after {
            border: none !important;
        }
        
        .q-field__native {
            color: var(--dark-wood) !important;
            font-weight: 500 !important;
        }
        
        .q-field__label {
            color: rgba(44, 24, 16, 0.6) !important;
            font-family: 'Cinzel', serif !important;
        }
        
        /* Send button - magical appearance */
        .q-btn {
            background: linear-gradient(135deg, var(--gryffindor-red) 0%, var(--dark-red) 100%) !important;
            color: var(--gryffindor-gold) !important;
            border: 2px solid var(--gryffindor-gold) !important;
            border-radius: 25px !important;
            font-family: 'Cinzel', serif !important;
            font-weight: 700 !important;
            letter-spacing: 1px !important;
            text-transform: uppercase !important;
            box-shadow: 0 4px 15px rgba(116, 0, 1, 0.4), inset 0 1px 2px rgba(211, 166, 37, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        
        .q-btn:hover {
            background: linear-gradient(135deg, var(--hover-red) 0%, var(--gryffindor-red) 100%) !important;
            box-shadow: 0 6px 20px rgba(116, 0, 1, 0.6), inset 0 1px 2px rgba(211, 166, 37, 0.5) !important;
            transform: translateY(-2px) !important;
        }
        
        /* Spinner - golden magical loading */
        .q-spinner {
            color: var(--gryffindor-gold) !important;
        }
        
        /* Footer text styling */
        .q-footer .q-markdown {
            font-family: 'Cinzel', serif !important;
        }
        
        .q-footer .q-markdown p {
            color: var(--gryffindor-gold) !important;
            text-shadow: 0 0 10px rgba(211, 166, 37, 0.5) !important;
        }
        
        .q-footer .q-markdown a {
            color: var(--gryffindor-gold) !important;
            text-decoration: none !important;
            font-weight: 700 !important;
            transition: all 0.3s ease !important;
        }
        
        .q-footer .q-markdown a:hover {
            color: var(--bright-gold) !important;
            text-shadow: 0 0 15px rgba(255, 215, 0, 0.8) !important;
        }
        
        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 10px !important;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(26, 14, 14, 0.5) !important;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, var(--gryffindor-gold) 0%, var(--gryffindor-red) 100%) !important;
            border-radius: 5px !important;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, var(--bright-gold) 0%, var(--hover-red) 100%) !important;
        }
        
        /* Add subtle glow animation to gold elements */
        @keyframes goldenGlow {
            0%, 100% {
                filter: drop-shadow(0 0 3px rgba(211, 166, 37, 0.5));
            }
            50% {
                filter: drop-shadow(0 0 8px rgba(211, 166, 37, 0.8));
            }
        }
        
        .q-message-name,
        .q-btn {
            animation: goldenGlow 3s ease-in-out infinite !important;
        }
    </style>
    ''')

def root():
    # Apply Hogwarts theme
    add_hogwarts_theme()
    
    # Add Hogwarts header
    with ui.header().classes('bg-transparent'):
        ui.html('''
            <div style="text-align: center; padding: 1rem;">
                <h1 style="
                    font-family: 'Cinzel', serif;
                    font-size: 2.5rem;
                    color: var(--gryffindor-gold);
                    text-shadow: 0 0 20px rgba(211, 166, 37, 0.6), 0 0 40px rgba(116, 0, 1, 0.3);
                    margin: 0;
                    letter-spacing: 3px;
                ">🏰 Hogwarts Spell Chatbot 🪄</h1>
                <p style="
                    font-family: 'Spectral', serif;
                    color: #F4E8D0;
                    font-size: 1rem;
                    margin-top: 0.5rem;
                    font-style: italic;
                ">Seek magical wisdom from the Hogwarts Expert</p>
            </div>
        ''')

    async def send() -> None:
        question = text.value
        text.value = ''
        with message_container:
            ui.chat_message(text=question, name='You', sent=True)
            response_message = ui.chat_message(name='Hogwarts Expert', sent=False)
            spinner = ui.spinner(type='dots', size='lg', color='primary')

        await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')
        response = ''
        for chunk in chat(question):
            response += chunk['message']['content']
            with response_message.clear():
                ui.html(response, sanitize=Sanitizer().sanitize)
                await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')
        message_container.remove(spinner)

    message_container = ui.column().classes('w-full max-w-2xl mx-auto flex-grow items-stretch')

    with (ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6')):
        with ui.row().classes('w-full no-wrap items-center'):
            placeholder = 'Message'
            text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3').classes('w-full self-center').on('keydown.enter', send)
            button = ui.button(text="Send", color="primary", on_click=send).props('rounded outlined input-class=mx-3').classes('self-center')

        ui.markdown('Made with 🔥 by [carmelolg](https://carmelolg.github.io)') \
            .classes('text-xs self-center mr-12 m-[-1em] text-primary') \
            .classes('[&_a]:text-inherit [&_a]:no-underline [&_a]:font-medium')


ui.run(root, title='Hogwarts Spell Chatbot', favicon='🪄', show_welcome_message=True, reconnect_timeout=6000)
