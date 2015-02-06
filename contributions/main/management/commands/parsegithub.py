from django.core.management.base import BaseCommand, CommandError
from main.models import Project, Student, Contribution

from bs4 import BeautifulSoup
from selenium import webdriver

class Command(BaseCommand):
    # https://docs.djangoproject.com/en/1.7/howto/custom-management-commands/

    def handle(self, *args, **options):
        browser = webdriver.Firefox()
        for project in Project.objects.all():

            # api access is blocked to contributors page unless you have access to push to repo
            browser.get(project.github)

            soup = BeautifulSoup(browser.page_source)

            cards = soup.find_all('li', {'class': 'capped-card'})

            for li in cards:
                # get user info
                user = {
                    'github_username': li.find('a', {'class': 'aname'}).text
                }

                if user['github_username'] == 'gitter-badger':
                    continue

                student = Student.objects.get_or_create(**user)[0]

                # get user contributions
                commit_meta = li.find('span', {'class': 'cmeta'})

                contribution = {
                    'project': project,
                    'student': student,
                    'commits': int(li.find('a', {'class': 'cmt'}).text.replace(',','').split()[0]),
                    'lines_added': int(commit_meta.find('span', {'class': 'a'}).text.replace(',','').split()[0]),
                    'lines_deleted': int(commit_meta.find('span', {'class': 'd'}).text.replace(',','').split()[0])
                }

                Contribution.objects.update_or_create(**contribution)

        browser.quit()