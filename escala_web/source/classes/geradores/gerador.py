import subprocess
from jinja2 import Template
from classes.escala import Escala
from classes.conversores.conversor import Conversor
from classes.modelos.cabecalho import Cabecalho
from classes.modelos.tabela import Tabela
from classes.modelos.memoria import Memoria
from classes.modelos.atividades import Atividades

class Gerador:
    @staticmethod
    def gerar_escala(escala: Escala) -> None:
        conversor = Conversor()
        Gerador._gerar_escala_(escala, conversor)

    @staticmethod
    def _gerar_cabecalho_(cabecalho: Cabecalho):
        with open("latex/escala/templates/cabecalho.tex", "r", encoding="utf-8") as f:
            cabecalho_template = Template(f.read())
    
        cabecalho_dados = cabecalho.render()
        rendered_cabecalho = cabecalho_template.render(cabecalho_dados)
    
        with open("latex/escala/cabecalho.tex", "w", encoding="utf-8") as f:
            f.write(rendered_cabecalho)
    
    @staticmethod
    def _gerar_tabela_(tabela: Tabela):
        with open("latex/escala/templates/tabela.tex", "r", encoding="utf-8") as f:
            tabela_template = Template(f.read())
        
        tabela_dados = tabela.render()
        rendered_tabela = tabela_template.render(tabela_dados)
        
        with open("latex/escala/tabela.tex", "w", encoding="utf-8") as f:
            f.write(rendered_tabela)

    @staticmethod
    def _gerar_memoria_(memoria: Memoria):
        with open("latex/escala/templates/memoria.tex", "r", encoding="utf-8") as f:
            memoria_template = Template(f.read())
        
        memoria_dados = memoria.render()
        rendered_memoria = memoria_template.render(memoria_dados)
        
        with open("latex/escala/memoria.tex", "w", encoding="utf-8") as f:
            f.write(rendered_memoria)
    
    @staticmethod
    def _gerar_atividades_(atividades: Atividades):
        with open("latex/escala/templates/atividades.tex", "r", encoding="utf-8") as f:
            atividades_template = Template(f.read())
        
        atividades_dados = atividades.render()
        rendered_atividades = atividades_template.render(atividades_dados)
        
        with open("latex/escala/atividades.tex", "w", encoding="utf-8") as f:
            f.write(rendered_atividades)
    
    @staticmethod
    def _gerar_escala_(escala: Escala, conversor: Conversor):
        cabecalho = conversor.converter_escala_para_cabecalho(escala)
        tabela = conversor.converter_calendario_para_tabela(escala.calendario)
        memoria = conversor.converter_escala_para_memoria(escala)
        atividades = conversor.converter_escala_para_atividades(escala)

        Gerador._gerar_cabecalho_(cabecalho)
        Gerador._gerar_tabela_(tabela)
        Gerador._gerar_memoria_(memoria)
        Gerador._gerar_atividades_(atividades)

        with open("latex/escala.tex", "r", encoding="utf-8") as f:
            template = Template(f.read())
        
        rendered_tex = template.render()

        with open("latex/main.tex", "w", encoding="utf-8") as f:
            f.write(rendered_tex)
        subprocess.run([
            "pdflatex",
            "-output-directory=latex",
            "latex/main.tex"
        ])
