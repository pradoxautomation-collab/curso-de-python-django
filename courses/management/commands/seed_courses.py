# BaseCommand: Classe base para criar comandos personalizados no Django.
from django.core.management.base import BaseCommand
# Course: Importar o modelo Course da aplicação courses.
from courses.models import Course

class Command(BaseCommand):
    help = 'Seed para cadastrar registro na tabela courses'

    def handle(self, *args, **kwargs):

        description = "<p>Lorem ipsum dolor sit amet...</p>" # (Mantive o texto original)

        # Criar a lista de cursos com os dados a serem cadastrados
        courses = [
            {
                'name': 'Curso de Python',
                'original_price': 497.43,
                'discounted_price': 347.61,
                'slug': 'curso-de-python',
                'description': description,
            },
            {
                'name': 'Curso de Django',
                'original_price': 597.43,
                'discounted_price': 447.61,
                'slug': 'curso-de-django',
                'description': description,
            },
            {
                'name': 'Curso de Python e Django',
                'original_price': 997.43,
                'discounted_price': 847.61,
                'slug': 'curso-de-python-e-django',
                'description': description,
            }
        ]

        # Iterar sobre a lista de cursos
        for course_data in courses:
            # 1. Pegamos o valor de 'name' do dicionário para usar na busca
            nome_curso = course_data['name']
            
            # 2. Criamos uma cópia dos dados para o 'defaults' 
            # e removemos a chave 'name' para o Django não tentar gravá-la em uma coluna inexistente
            dados_para_salvar = course_data.copy()
            del dados_para_salvar['name']

            # 3. Criar ou Atualizar
            # Se o seu Model no Django usa 'name', usamos name=nome_curso
            # Se o seu DBeaver mostra 'title', as migrations vão resolver isso no próximo passo.
            Course.objects.update_or_create(
                name=nome_curso, 
                defaults=dados_para_salvar
            )

        self.stdout.write(self.style.SUCCESS('Cursos adicionados com sucesso!'))