from django.core.management.base import BaseCommand
from courses.models import About


class Command(BaseCommand):
    help = "Seed para cadastrar registro na tabela about"

    def handle(self, *args, **kwargs):
        description = "Aqui vai um testes de frases para fazero teste. <p> um teste de paragrafo </p>"

        about = [
            {
                'name': 'Estrtura Fisica e Ambientes Gerais',
                'description':'<p>A pradox automation &eacute; lider em python e Dijango.&nbsp;</p>' ,
            },
            
            
        ]
        
        # Iterar sobre  a lista de sobre a empresa 
        for about_data in about:
            About.objects.update_or_create(
                name=about_data['name'],  # critério de busca
                defaults=about_data,      # valores para criar/atualizar
            )

        self.stdout.write(self.style.SUCCESS('sobre empresa adicionado com sucesso!'))
