import streamlit as st
from back import SistemaCadastroMembros

MEMBROS_FILE = 'membros.csv'
ADVERTENCIAS_FILE = 'alocacao.csv'

sistema = SistemaCadastroMembros(MEMBROS_FILE, ADVERTENCIAS_FILE)

def cadastrar_membro():
    nome = st.text_input('Nome')
    setor = st.text_input('Senioridade')
    cargo = st.text_input('Cargo')
    pontos = st.number_input('Horas Cumpridas', value=0)
    if st.button('Cadastrar'):
        try:
            sistema.cadastrar_membro(nome, setor, cargo, pontos)
            st.success('Membro cadastrado com sucesso!')
        except ValueError as e:
            st.error(str(e))

def cadastrar_alocacao():
    nome_membro = st.text_input('Nome do membro')
    pontos = st.number_input('Horas', value=0)
    motivo = st.text_input('Alocação')
    if st.button('Cadastrar'):
        try:
            sistema.cadastrar_advertencia(nome_membro, pontos, motivo)
            st.success('Alocação cadastrada com sucesso!')
        except ValueError as e:
            st.error(str(e))

def buscar_membro():
    nome = st.text_input('Nome')
    if st.button('Buscar'):
        try:
            membro = sistema.buscar_membro_por_nome(nome)
            st.write(f'Nome: {membro.nome}')
            st.write(f'Senioridade: {membro.setor}')
            st.write(f'Cargo: {membro.cargo}')
            st.write(f'Horarios: {membro.pontos}')
        except ValueError as e:
            st.error(str(e))

def buscar_advertencias():
    nome = st.text_input('Nome')
    if st.button('Buscar'):
        try:
            advertencias = sistema.buscar_advertencias_por_nome(nome)
            for adv in advertencias:
                st.write(str(adv))
        except ValueError as e:
            st.error(str(e))

def main():
    st.title('Cadastro de Membros e Sistema de Advertências')
    opcoes = ['Cadastrar Membro', 'Cadastrar Advertência', 'Buscar Membro', 'Buscar Advertências']
    escolha = st.sidebar.selectbox('Escolha uma opção', opcoes)
    if escolha == 'Cadastrar Membro':
        cadastrar_membro()
    elif escolha == 'Cadastrar Advertência':
        cadastrar_alocacao()
    elif escolha == 'Buscar Membro':
        buscar_membro()
    elif escolha == 'Buscar Advertências':
        buscar_advertencias()

if __name__ == '__main__':
    main()
